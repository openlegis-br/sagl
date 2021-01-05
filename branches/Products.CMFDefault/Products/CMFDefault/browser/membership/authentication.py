##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Authentication browser views.
"""
try:
   from urllib import quote #py2
   from urllib import urlencode #py2
except ImportError:
   from urllib.parse import quote, urlencode #py3

from Acquisition import aq_inner
from Acquisition import aq_parent
from DateTime import DateTime
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zExceptions import Forbidden
from zExceptions import Redirect
from zope.component import getUtility
from zope.component import queryUtility
from zope.formlib import form
from zope.formlib.widgets import TextWidget
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.publisher.browser import BrowserView
from zope.schema import Bool
from zope.schema import Choice
from zope.schema import Password
from zope.schema import TextLine
from zope.schema import URI
from zope.schema.interfaces import ISource

from Products.CMFCore.CookieCrumbler import ATTEMPT_LOGIN
from Products.CMFCore.CookieCrumbler import ATTEMPT_NONE
from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import ICookieCrumbler
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import IRegistrationTool
from Products.CMFCore.interfaces import ISkinsTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.utils import ViewBase
from Products.CMFDefault.formlib.form import EditFormBase
from Products.CMFDefault.utils import Message as _


def _expireAuthCookie(view):
    cctool = queryUtility(ICookieCrumbler)
    if cctool is not None:
        method = cctool.getCookieMethod('expireAuthCookie',
                                        cctool.defaultExpireAuthCookie)
        method(view.request.response, cctool.auth_cookie)
    else:
        view.request.response.expireCookie('__ac', path='/')


class UnauthorizedView(BrowserView):

    """Exception view for Unauthorized.
    """

    forbidden_template = ViewPageTemplateFile('forbidden.pt')

    def __call__(self):
        self.exception = aq_inner(self.context)
        self.context = aq_parent(self)

        atool = queryUtility(IActionsTool)
        if atool is None:
            # re-raise the unhandled exception
            raise self.exception

        try:
            target = atool.getActionInfo('user/login')['url']
            if not target.startswith('/'):
                # May happen in unit tests
                target = '/%s' % target
        except ValueError:
            # re-raise the unhandled exception
            raise self.exception

        req = self.request
        if (not req['REQUEST_METHOD'] in ('HEAD', 'GET', 'PUT', 'POST')
            or 'WEBDAV_SOURCE_PORT' in req.environ):
            # re-raise the unhandled exception
            raise self.exception

        attempt = getattr(req, '_cookie_auth', ATTEMPT_NONE)
        if attempt not in (ATTEMPT_NONE, ATTEMPT_LOGIN):
            # An authenticated user was denied access to something.
            raise Forbidden(self.forbidden_template())

        _expireAuthCookie(self)
        came_from = req.get('came_from', None)
        if came_from is None:
            came_from = req.get('ACTUAL_URL')
            query = req.get('QUERY_STRING')
            if query:
                # Include the query string in came_from
                if not query.startswith('?'):
                    query = '?' + query
                came_from = came_from + query
        url = '%s?came_from=%s' % (target, quote(came_from))
        raise Redirect(url)

@implementer(ISource)
class NameSource(object):


    def __contains__(self, value):
        mtool = getUtility(IMembershipTool)
        if mtool.getMemberById(value):
            return True
        candidates = mtool.searchMembers('email', value)
        for candidate in candidates:
            if candidate['email'].lower() == value.lower():
                return True
        return False

available_names = NameSource()


class ILoginSchema(Interface):

    """Schema for login form.
    """

    came_from = URI(
        required=False)

    name = TextLine(
        title=_(u'Member ID'),
        description=_(u'Case sensitive'))

    password = Password(
        title=_(u'Password'),
        description=_(u'Case sensitive'))

    persistent = Bool(
        title=_(u'Remember my ID.'),
        description=_(u'Saves your member ID in a cookie.'),
        default=True)


class IMailPasswordSchema(Interface):

    """Schema for mail password form.
    """

    name = Choice(
        title=_(u'Member ID'),
        description=_(u'Member ID or email address'),
        source=available_names)


class LoginFormView(EditFormBase):

    """Form view for ILoginSchema.
    """

    template = ViewPageTemplateFile('login.pt')
    label = _(u'Log in')
    prefix = ''

    form_fields = form.FormFields(ILoginSchema)

    actions = form.Actions(
        form.Action(
            name='login',
            label=_(u'Login'),
            validator='handle_login_validate',
            success='handle_login_success',
            failure='handle_failure'))

    def setUpWidgets(self, ignore_request=False):
        cctool = queryUtility(ICookieCrumbler)
        if cctool is not None:
            ac_name_id = cctool.name_cookie
            ac_password_id = cctool.pw_cookie
            ac_persistent_id = cctool.persist_cookie
        else:
            ac_name_id = '__ac_name'
            ac_password_id = '__ac_password'
            ac_persistent_id = '__ac_persistent'
        ac_name = self.request.get(ac_name_id)
        if ac_name is not None:
            self.request.form['name'] = ac_name
            self.request.form[ac_name_id] = ac_name
        ac_persistent = self.request.get(ac_persistent_id)
        if ac_persistent is not None:
            self.request.form['persistent'] = ac_persistent
        ac_persistent_used = self.request.get("%s.used" % ac_persistent_id)
        if ac_persistent_used is not None:
            self.request.form['persistent.used'] = ac_persistent_used
        super(LoginFormView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['came_from'].hide = True
        self.widgets['name'].name = ac_name_id
        self.widgets['password'].name = ac_password_id
        self.widgets['persistent'].name = ac_persistent_id

    def handle_login_validate(self, action, data):
        mtool = getUtility(IMembershipTool)
        if mtool.isAnonymousUser():
            _expireAuthCookie(self)
            return (_(u'Login failure'),)
        return None

    def handle_login_success(self, action, data):
        return self._setRedirect('portal_actions', 'user/logged_in',
                                 'came_from')


class LoggedInView(ViewBase):

    """Post login methods"""

    # helpers

    def _set_skin_cookie(self):
        stool = queryUtility(ISkinsTool)
        if stool is not None and stool.updateSkinCookie():
            skinname = self.context.getSkinNameFromRequest(self.request)
            self.context.changeSkin(skinname, self.request)

    def _first_login(self, member):
        """First time login, reset password"""
        atool = getUtility(IActionsTool)
        now = DateTime()
        member.setProperties(last_login_time='1999/01/01', login_time=now)
        target = atool.getActionInfo('user/change_password')['url']
        self.request.response.redirect(target)
        return ''

    # interface

    def __call__(self):
        self._set_skin_cookie()
        mtool = getUtility(IMembershipTool)
        mtool.createMemberArea()
        member = mtool.getAuthenticatedMember()
        last_login = member.getProperty('login_time')
        never_logged_in = str(last_login).startswith('2000/01/01')
        ptool = getUtility(IPropertiesTool)
        if never_logged_in and ptool.getProperty('validate_email'):
            return self._first_login(member)
        now = DateTime()
        member.setProperties(last_login_time=last_login, login_time=now)
        came_from = self.request.get('came_from', None)
        if came_from:
            self.request.response.redirect(came_from)
            return ''
        return self.index()


class MailPasswordFormView(EditFormBase):

    """Form view for IMailPasswordSchema.
    """

    template = ViewPageTemplateFile('mail_password.pt')
    label = _(u"Don't panic!")
    description = _(u"Just enter your member ID below, click 'Send', and "
                    u"your password will be mailed to you if you gave a "
                    u"valid email address when you signed on.")

    form_fields = form.FormFields(IMailPasswordSchema)
    form_fields['name'].custom_widget = TextWidget

    actions = form.Actions(
        form.Action(
            name='send',
            label=_(u'Send'),
            success='handle_send_success',
            failure='handle_failure'))

    def setUpWidgets(self, ignore_request=False):
        cctool = queryUtility(ICookieCrumbler)
        if cctool is not None:
            ac_name_id = cctool.name_cookie
        else:
            ac_name_id = '__ac_name'
        ac_name = self.request.get(ac_name_id)
        if ac_name and not ('%s.name' % self.prefix) in self.request:
            self.request.form['%s.name' % self.prefix] = ac_name
        super(MailPasswordFormView,
              self).setUpWidgets(ignore_request=ignore_request)

    def handle_send_success(self, action, data):
        mtool = getUtility(IMembershipTool)
        if not mtool.getMemberById(data['name']):
            candidates = mtool.searchMembers('email', data['name'])
            for candidate in candidates:
                if candidate['email'].lower() == data['name'].lower():
                    data['name'] = candidate['username']
                    break
        rtool = getUtility(IRegistrationTool)
        rtool.mailPassword(data['name'], self.request)
        self.status = _(u'Your password has been mailed to you.')
        return self._setRedirect('portal_actions', 'user/login')

    @property
    @memoize
    def admin_email(self):
        ptool = getUtility(IPropertiesTool)
        return ptool.getProperty('email_from_address')


class LogoutView(ViewBase):

    """Log the user out"""

    # helpers

    def _logout(self):
        """Log the user out"""
        _expireAuthCookie(self)

    def _clear_skin_cookie(self):
        """Remove skin cookie"""
        stool = queryUtility(ISkinsTool)
        if stool is not None:
            stool.clearSkinCookie()

    # interface

    def __call__(self):
        """Clear cookies and return the template"""
        if 'portal_status_message' in self.request:
            return self.index()
        if self.logged_in():
            self._clear_skin_cookie()
            self._logout()
            status = "?" + urlencode({'portal_status_message':
                                      _(u'You have been logged out.')})
            self.request.response.redirect(self._getViewURL() + status)
            return ''

    @memoize
    def logged_in(self):
        """Check whether the user is (still logged in)"""
        mtool = getUtility(IMembershipTool)
        return not mtool.isAnonymousUser()
