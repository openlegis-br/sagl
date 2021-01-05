#############################################################################
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
"""Join form.
"""

import transaction
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.component import queryUtility
from zope.formlib import form
from zope.interface import Interface
from zope.interface import Invalid
from zope.interface import invariant
from zope.schema import ASCIILine
from zope.schema import Bool
from zope.schema import Password

from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import ICookieCrumbler
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import IRegistrationTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.formlib.form import EditFormBase
from Products.CMFDefault.formlib.schema import EmailLine
from Products.CMFDefault.permissions import ManageUsers
from Products.CMFDefault.utils import Message as _


class IJoinSchema(Interface):

    """Schema for join form.
    """

    member_id = ASCIILine(
        title=_(u"Member ID"))

    email = EmailLine(
        title=_(u"Email Address"))

    password = Password(
        title=_(u"Password"),
        min_length=5)

    confirmation = Password(
        title=_(u"Password (confirm)"),
        min_length=5)

    send_password = Bool(
        title=_(u"Mail Password?"),
        description=_(u"Check this box to have the password mailed."))

    @invariant
    def check_passwords_match(schema):
        """Password and confirmation must match"""
        if schema.password != schema.confirmation:
            raise Invalid(_(u"Your password and confirmation did not match. "
                            u"Please try again."))


class JoinFormView(EditFormBase):

    template = ViewPageTemplateFile("join.pt")

    actions = form.Actions(
        form.Action(
            name='register',
            label=_(u'Register'),
            validator='handle_register_validate',
            success='handle_register_success',
            failure='handle_failure'),
        form.Action(
            name='cancel',
            label=_(u'Cancel'),
            validator='handle_cancel_validate',
            success='handle_cancel_success'))

    @property
    def form_fields(self):
        form_fields = form.FormFields(IJoinSchema)
        if self.validate_email:
            form_fields = form_fields.select('member_id', 'email')
        return form_fields

    @property
    @memoize
    def validate_email(self):
        ptool = getUtility(IPropertiesTool)
        return ptool.getProperty('validate_email')

    @property
    @memoize
    def isAnon(self):
        mtool = getUtility(IMembershipTool)
        return mtool.isAnonymousUser()

    @property
    @memoize
    def isManager(self):
        mtool = getUtility(IMembershipTool)
        return mtool.checkPermission(ManageUsers, mtool)

    @property
    @memoize
    def isOrdinaryMember(self):
        return not (self.isManager or self.isAnon)

    @property
    def label(self):
        if self.isManager:
            return _(u'Register a New Member')
        else:
            return _(u'Become a Member')

    def personalize(self):
        atool = getUtility(IActionsTool)
        return atool.getActionInfo("user/preferences")['url']

    def handle_register_validate(self, action, data):
        errors = self.validate(action, data)
        if errors:
            return errors
        rtool = getUtility(IRegistrationTool)
        if self.validate_email:
            data['password'] = rtool.generatePassword()
        else:
            result = rtool.testPasswordValidity(data['password'],
                                                data['confirmation'])
            if result is not None:
                errors.append(result)
        if not rtool.isMemberIdAllowed(data['member_id']):
            errors.append(_(u"The login name you selected is already in use "
                            u"or is not valid. Please choose another."))
        return errors

    def _add_member(self, data):
        member_id = data['member_id']
        password = data['password'].encode(self._getDefaultCharset())
        rtool = getUtility(IRegistrationTool)
        rtool.addMember(id=member_id, password=password,
                        properties={'username': member_id,
                                    'email': data['email']})

    def _notify_member(self, data):
        if not (self.validate_email or data['send_password']):
            return False
        rtool = getUtility(IRegistrationTool)
        try:
            rtool.registeredNotify(data['member_id'], REQUEST=self.request)
        except IOError:
            return False
        return True

    def handle_register_success(self, action, data):
        """Register user and inform they have been registered"""
#        try:
#            self._add_member(data)
#        except ValueError, errmsg:
#            transaction.abort()
#            self.form_reset = False
#            self.status = errmsg
#            return self.handle_failure(action, data, ())

        if self.isManager:
            if self._notify_member(data):
                self.status = _(u'Member registered and notified.')
            else:
                self.status = _(u'Member registered.')
            return self._setRedirect('portal_actions',
                                     'global/members_register',
                                     keys='b_start')
        if self._notify_member(data):
            self.status = _(u'You will receive an email shortly containing '
                            u'your password and instructions on how to '
                            u'activate your membership.')
        else:
            self.status = _(u'You have been registered as a member.')
        try:
            cctool = queryUtility(ICookieCrumbler)
            ac_name_id = cctool.name_cookie
        except AttributeError:
            ac_name_id = '__ac_name'
        self.request.form[ac_name_id] = data['member_id']
        return self._setRedirect('portal_actions', 'user/login',
                                 keys=ac_name_id)

    def handle_cancel_success(self, action, data):
        return self._setRedirect('portal_actions', 'global/manage_members',
                                 keys='b_start')
