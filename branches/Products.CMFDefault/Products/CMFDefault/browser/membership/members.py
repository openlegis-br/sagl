##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Forms for managing members.
"""

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.formlib import form
from zope.interface import Interface
from zope.schema import Date
from zope.schema import TextLine

from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.widgets.batch import BatchFormMixin
from Products.CMFDefault.browser.widgets.batch import BatchViewBase
from Products.CMFDefault.browser.widgets.batch import IBatchForm
from Products.CMFDefault.formlib.form import EditFormBase
from Products.CMFDefault.permissions import ManageUsers
from Products.CMFDefault.utils import Message as _


class IMemberItem(Interface):

    """Schema for portal members """

    name = TextLine(
        title=u"Name",
        required=False,
        readonly=True
        )

    email = TextLine(
        title=_(u"Email Address"),
        required=False,
        readonly=True
        )

    last_login = Date(
        title=_(u"Last Login"),
        required=False,
        readonly=True
        )


class MemberProxy(object):

    """Utility class wrapping a member for display purposes"""

    def __init__(self, member, mtool, charset):
        member_id = member.getId()
        last_login = member.getProperty('login_time')
        never_logged_in = str(last_login).startswith('2000/01/01')
        self.login_time = never_logged_in and '---' or last_login.Date()
        self.name = member_id
        self.fullname = member.getProperty('fullname').decode(charset)
        self.home = mtool.getHomeUrl(member_id, verifyPermission=0)
        self.email = member.getProperty('email')


class Manage(BatchFormMixin, EditFormBase):

    _NEXT_PLURAL_MESSAGE = _(u'Next ${count} members')
    _NEXT_SINGULAR_MESSAGE = _(u'Next member')
    _PREV_PLURAL_MESSAGE = _(u'Previous ${count} members')
    _PREV_SINGULAR_MESSAGE = _(u'Previous member')

    template = ViewPageTemplateFile("members.pt")
    delete_template = ViewPageTemplateFile("members_delete.pt")
    form_fields = form.FormFields()
    hidden_fields = form.FormFields(IBatchForm)

    manage_actions = form.Actions(
        form.Action(
            name='new',
            label=_(u'New...'),
            success='handle_add',
            failure='handle_failure'),
        form.Action(
            name='select',
            label=_(u'Delete...'),
            condition='members_exist',
            success='handle_select_for_deletion',
            failure='handle_failure',
            validator=('validate_items')))

    delete_actions = form.Actions(
        form.Action(
            name='delete',
            label=_(u'Delete'),
            success='handle_delete',
            failure='handle_failure'),
        form.Action(
            name='cancel',
            label=_(u'Cancel')))

    actions = manage_actions + delete_actions
    label = _(u'Manage Members')

    @property
    def description(self):
        if not self.members_exist():
            return _(u'Currently there are no members registered.')
        return u''

    @memoize
    def _get_items(self):
        mtool = getUtility(IMembershipTool)
        return mtool.listMembers()

    @memoize
    def members_exist(self, action=None):
        return len(self._getBatchObj()) > 0

    @memoize
    def _get_ids(self):
        """Identify objects that have been selected"""
        ids = self.request.form.get('form.select_ids', [])
        if isinstance(ids, basestring):
            ids = [ids]
        return [ str(id) for id in ids ]

    @memoize
    def listBatchItems(self):
        """Create content field objects only for batched items
        """
        mtool = getUtility(IMembershipTool)
        charset = self._getDefaultCharset()
        members = []
        for item in self._getBatchObj():
            members.append(MemberProxy(item, mtool, charset))
        return tuple(members)

    @memoize
    def listSelectedItems(self):
        ids = self._get_ids()
        members = [ m for m in self.listBatchItems() if m.name in ids ]
        return tuple(members)

    def setUpWidgets(self, ignore_request=False):
        """Create widgets for the members"""
        super(Manage, self).setUpWidgets(ignore_request)
        self.widgets = self.hidden_widgets

    def validate_items(self, action=None, data=None):
        """Check whether any items have been selected for
        the requested action."""
        errors = self.validate(action, data)
        if errors:
            return errors
        if self._get_ids() == []:
            errors.append(_(u"Please select one or more members first."))
        return errors

    def handle_add(self, action, data):
        """Redirect to the join form where managers can add users"""
        return self._setRedirect('portal_actions', 'global/members_register')

    def handle_select_for_deletion(self, action, data):
        """Identify members to be deleted and redirect to confirmation
        template"""
        return self.delete_template()

    def handle_delete(self, action, data):
        """Delete selected members"""
        mtool = getUtility(IMembershipTool)
        mtool.deleteMembers(self._get_ids())
        self.status = _(u"Selected members deleted.")
        self._setRedirect('portal_actions', "global/manage_members",
                          '{0}.b_start'.format(self.prefix))


class Roster(BatchViewBase):

    @property
    @memoize
    def mtool(self):
        return getUtility(IMembershipTool)

    @memoize
    def isUserManager(self):
        return self.mtool.checkPermission(ManageUsers,
                                          self.mtool.getMembersFolder())

    @memoize
    def _get_items(self):
        return self.mtool.getRoster()

    def listBatchItems(self):
        members = []
        for member in self._getBatchObj():
            member_home = self.mtool.getHomeUrl(member['id'],
                                                verifyPermission=1)
            member_listed = member['listed'] and _(u'Yes') or _(u'No')
            members.append({'id': member['id'],
                            'home': member_home,
                            'listed': member_listed})
        return tuple(members)
