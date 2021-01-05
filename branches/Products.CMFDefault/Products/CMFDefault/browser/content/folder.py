##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Browser views for folders.
"""

import urllib

from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.formlib import form
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.sequencesort.ssort import sort
from ZTUtils import LazyFilter

from .interfaces import IDeltaItem
from Products.CMFCore.interfaces import IDynamicType
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFDefault.browser.utils import decode
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.widgets.batch import BatchFormMixin
from Products.CMFDefault.browser.widgets.batch import BatchViewBase
from Products.CMFDefault.exceptions import CopyError
from Products.CMFDefault.exceptions import zExceptions_Unauthorized
from Products.CMFDefault.formlib.form import EditFormBase
from Products.CMFDefault.permissions import AddPortalContent
from Products.CMFDefault.permissions import DeleteObjects
from Products.CMFDefault.permissions import ListFolderContents
from Products.CMFDefault.permissions import ManageProperties
from Products.CMFDefault.permissions import ViewManagementScreens
from Products.CMFDefault.utils import Message as _

def contents_delta_vocabulary(context):
    """Vocabulary for the pulldown for moving objects up and down.
    """
    length = len(context.contentIds())
    deltas = [SimpleTerm(i, str(i), str(i))
            for i in range(1, min(5, length)) + range(5, length, 5)]
    return SimpleVocabulary(deltas)


class ContentProxy(object):

    """Utility wrapping content item for display purposes"""

    def __init__(self, context):
        self.name = context.getId()
        self.title = context.Title() or context.getId()
        self.type = context.Type() or None
        self.icon = context.getIconURL()
        self.url = context.getActionInfo(('object/folderContents',
                                          'object/edit',
                                          'object/download',
                                          'object/view'))['url']
        self.ModificationDate = context.ModificationDate()


class ContentsView(BatchFormMixin, EditFormBase):

    """Folder contents view"""

    template = ViewPageTemplateFile('folder_contents.pt')
    rename_template = ViewPageTemplateFile('folder_rename.pt')

    object_actions = form.Actions(
        form.Action(
            name='select_for_rename',
            label=_(u'Rename...'),
            validator='validate_items',
            condition='show_select_for_rename',
            success='handle_select_for_rename_success',
            failure='handle_failure'),
        form.Action(
            name='cut',
            label=_(u'Cut'),
            condition='show_basic',
            validator='validate_items',
            success='handle_cut_success',
            failure='handle_failure'),
        form.Action(
            name='copy',
            label=_(u'Copy'),
            condition='show_basic',
            validator='validate_items',
            success='handle_copy_success',
            failure='handle_failure'),
        form.Action(
            name='paste',
            label=_(u'Paste'),
            condition='show_paste',
            success='handle_paste_success',
            failure='handle_failure'),
        form.Action(
            name='delete',
            label=_(u'Delete'),
            condition='show_delete',
            validator='validate_items',
            success='handle_delete_success',
            failure='handle_failure')
            )

    delta_actions = form.Actions(
        form.Action(
            name='up',
            label=_(u'Up'),
            condition='is_orderable',
            validator='validate_items',
            success='handle_up_success',
            failure='handle_failure'),
        form.Action(
            name='down',
            label=_(u'Down'),
            condition='is_orderable',
            validator='validate_items',
            success='handle_down_success',
            failure='handle_failure')
            )

    absolute_actions = form.Actions(
        form.Action(
            name='top',
            label=_(u'Top'),
            condition='is_orderable',
            validator='validate_items',
            success='handle_top_success',
            failure='handle_failure'),
        form.Action(
            name='bottom',
            label=_(u'Bottom'),
            condition='is_orderable',
            validator='validate_items',
            success='handle_bottom_success',
            failure='handle_failure')
            )

    sort_actions = form.Actions(
        form.Action(
            name='sort_order',
            label=_(u'Set as Default Sort'),
            condition='can_sort_be_changed',
            success='handle_sort_order_success',
            failure='handle_failure')
            )

    rename_actions = form.Actions(
        form.Action(
            name='rename',
            label=_(u'Rename'),
            validator='validate_items',
            success='handle_rename_success',
            failure='handle_rename_failure'),
        form.Action(
            name='cancel',
            label=_(u'Cancel'),
            validator='handle_cancel_validate',
            success='handle_cancel_success'))

    actions = (object_actions + delta_actions + absolute_actions + sort_actions
               + rename_actions)
    form_fields = form.FormFields()
    delta_field = form.FormFields(IDeltaItem)
    description = u''

    @property
    def label(self):
        return _(u'Folder Contents: ${obj_title}',
                 mapping={'obj_title': self.title()})

    @memoize
    def listBatchItems(self):
        """List batched items.
        """
        show_checkboxes = self._checkPermission(ViewManagementScreens)
        contents = []
        b_start = self._getBatchStart()
        key, _reverse = self._get_sorting()
        for idx, item in enumerate(self._getBatchObj()):
            content = ContentProxy(item)
            content.checkbox = show_checkboxes
            if key == 'position':
                content.position = b_start + idx + 1
            else:
                content.position = '...'
            contents.append(content)
        return tuple(contents)

    @memoize
    def listSelectedItems(self):
        ids = self._get_ids()
        contents = []
        for item in self._getBatchObj():
            if not item.getId() in ids:
                continue
            if not item.cb_isMoveable():
                continue
            contents.append(ContentProxy(item))
        return tuple(contents)

    @memoize
    @decode
    def up_info(self):
        """Link to the contens view of the parent object"""
        up_obj = aq_parent(aq_inner(self.context))
        mtool = getUtility(IMembershipTool)
        allowed = mtool.checkPermission(ListFolderContents, up_obj)
        if allowed:
            if IDynamicType.providedBy(up_obj):
                up_url = up_obj.getActionInfo('object/folderContents')['url']
                return {'icon': '%s/UpFolder_icon.gif' % self._getPortalURL(),
                        'id': up_obj.getId(),
                        'url': up_url}
            else:
                return {'icon': '',
                        'id': 'Root',
                        'url': ''}
        else:
            return {}

    def setUpWidgets(self, ignore_request=False):
        """Create widgets for the folder contents."""
        super(ContentsView, self).setUpWidgets(ignore_request)
        self.widgets = form.setUpWidgets(
                self.delta_field, self.prefix, self.context,
                self.request, ignore_request=ignore_request)

    @memoize
    def _get_sorting(self):
        """How should the contents be sorted"""
        data = self._getNavigationVars()
        key = data.get('sort_key')
        if key:
            return (key, data.get('reverse', 0))
        else:
            return self.context.getDefaultSorting()

    @memoize
    def column_headings(self):
        key, reverse = self._get_sorting()
        columns = ({'sort_key': 'Type',
                    'title': _(u'Type'),
                    'class': 'contents_type_col',
                    'colspan': '2'},
                   {'sort_key': 'getId',
                    'title': _(u'Name'),
                    'class': 'contents_name_col'},
                   {'sort_key': 'modified',
                    'title': _(u'Last Modified'),
                    'class': 'contents_modified_col'},
                   {'sort_key': 'position',
                    'title': _(u'Position'),
                    'class': 'contents_position_col'})
        for column in columns:
            paras = {'form.sort_key': column['sort_key']}
            if key == column['sort_key'] \
            and not reverse and key != 'position':
                paras['form.reverse'] = 1
            query = urllib.urlencode(paras)
            column['url'] = '%s?%s' % (self._getViewURL(), query)
        return tuple(columns)

    @memoize
    def _get_items(self):
        key, reverse = self._get_sorting()
        items = self.context.contentValues()
        return sort(items, ((key, 'cmp', reverse and 'desc' or 'asc'),))

    @memoize
    def _get_ids(self):
        """Identify objects that have been selected"""
        ids = self.request.form.get('{0}.select_ids'.format(self.prefix), [])
        if isinstance(ids, basestring):
            ids = [ids]
        return [ str(id) for id in ids ]

    @memoize
    def _get_new_ids(self):
        ids = self.request.form.get('{0}.new_ids'.format(self.prefix), [])
        if isinstance(ids, basestring):
            ids = [ids]
        return [ str(id) for id in ids ]

    #Action conditions
    @memoize
    def show_basic(self, action=None):
        if not self._checkPermission(ViewManagementScreens):
            return False
        return bool(self._get_items())

    @memoize
    def show_delete(self, action=None):
        if not self.show_basic():
            return False
        return self._checkPermission(DeleteObjects)

    @memoize
    def show_paste(self, action=None):
        """Any data in the clipboard"""
        if not self._checkPermission(ViewManagementScreens):
            return False
        if not self._checkPermission(AddPortalContent):
            return False
        return bool(self.context.cb_dataValid())

    @memoize
    def show_select_for_rename(self, action=None):
        if not self.show_basic():
            return False
        if not self._checkPermission(AddPortalContent):
            return False
        return self.context.allowedContentTypes()

    @memoize
    def can_sort_be_changed(self, action=None):
        """Returns true if the default sort key may be changed
            may be sorted for display"""
        if not self._checkPermission(ViewManagementScreens):
            return False
        if not self._checkPermission(ManageProperties):
            return False
        return not self._get_sorting() == self.context.getDefaultSorting()

    @memoize
    def is_orderable(self, action=None):
        """Returns true if the displayed contents can be
            reorded."""
        if not self._checkPermission(ViewManagementScreens):
            return False
        if not self._checkPermission(ManageProperties):
            return False
        key, _reverse = self._get_sorting()
        return key == 'position' and len(self._get_items()) > 1

    #Action validators
    def validate_items(self, action=None, data=None):
        """Check whether any items have been selected for
        the requested action."""
        errors = self.validate(action, data)
        if errors:
            return errors
        if self._get_ids() == []:
            errors.append(_(u"Please select one or more items first."))
        return errors

    #Action handlers

    def handle_select_for_rename_success(self, action, data):
        """Redirect to rename template.
        """
        return self.rename_template()

    def handle_cut_success(self, action, data):
        """Cut the selected objects and put them in the clipboard"""
        ids = self._get_ids()
        try:
            self.context.manage_cutObjects(ids, self.request)
            if len(ids) == 1:
                self.status = _(u'Item cut.')
            else:
                self.status = _(u'Items cut.')
        except CopyError:
            self.status = _(u'CopyError: Cut failed.')
            return self.handle_failure(action, data, ())
        except zExceptions_Unauthorized:
            return self.handle_failure(action, data, ())
            self.status = _(u'Unauthorized: Cut failed.')
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_copy_success(self, action, data):
        """Copy the selected objects to the clipboard"""
        ids = self._get_ids()
        try:
            self.context.manage_copyObjects(ids, self.request)
            if len(ids) == 1:
                self.status = _(u'Item copied.')
            else:
                self.status = _(u'Items copied.')
        except CopyError:
            self.status = _(u'CopyError: Copy failed.')
            return self.handle_failure(action, data, ())
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_paste_success(self, action, data):
        """Paste the objects from the clipboard into the folder"""
        try:
            result = self.context.manage_pasteObjects(self.request['__cp'])
            if len(result) == 1:
                self.status = _(u'Item pasted.')
            else:
                self.status = _(u'Items pasted.')
        except CopyError:
            self.request.response.expireCookie('__cp',
                    path='%s' % (self.request['BASEPATH1'] or "/"))
            self.status = _(u'CopyError: Paste failed.')
        except ValueError:
            self.status = _(u'ValueError: Paste failed.')
            return self.handle_failure(action, data, ())
        except zExceptions_Unauthorized:
            self.status = _(u'Unauthorized: Paste failed.')
            return self.handle_failure(action, data, ())
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_delete_success(self, action, data):
        """Delete the selected objects"""
        ids = self._get_ids()
        self.context.manage_delObjects(list(ids))
        if len(ids) == 1:
            self.status = _(u'Item deleted.')
        else:
            self.status = _(u'Items deleted.')
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_up_success(self, action, data):
        """Move the selected objects up the selected number of places"""
        ids = self._get_ids()
        delta = data.get('delta', 1)
        subset_ids = [obj.getId()
                       for obj in self.context.listFolderContents()]
        try:
            attempt = self.context.moveObjectsUp(ids, delta,
                                                 subset_ids=subset_ids)
            if attempt == 1:
                self.status = _(u'Item moved up.')
            elif attempt > 1:
                self.status = _(u'Items moved up.')
            else:
                self.status = self.noChangesMessage
        except ValueError:
            self.status = _(u'ValueError: Move failed.')
            return self.handle_failure(action, data, ())
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_down_success(self, action, data):
        """Move the selected objects down the selected number of places"""
        ids = self._get_ids()
        delta = data.get('delta', 1)
        subset_ids = [obj.getId()
                       for obj in self.context.listFolderContents()]
        try:
            attempt = self.context.moveObjectsDown(ids, delta,
                                                 subset_ids=subset_ids)
            if attempt == 1:
                self.status = _(u'Item moved down.')
            elif attempt > 1:
                self.status = _(u'Items moved down.')
            else:
                self.status = self.noChangesMessage
        except ValueError:
            self.status = _(u'ValueError: Move failed.')
            return self.handle_failure(action, data, ())
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_top_success(self, action, data):
        """Move the selected objects to the top of the page"""
        ids = self._get_ids()
        subset_ids = [obj.getId()
                       for obj in self.context.listFolderContents()]
        try:
            attempt = self.context.moveObjectsToTop(ids,
                                                    subset_ids=subset_ids)
            if attempt == 1:
                self.status = _(u'Item moved to top.')
            elif attempt > 1:
                self.status = _(u'Items moved to top.')
            else:
                self.status = self.noChangesMessage
        except ValueError:
            self.status = _(u'ValueError: Move failed.')
            return self.handle_failure(action, data, ())
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_bottom_success(self, action, data):
        """Move the selected objects to the bottom of the page"""
        ids = self._get_ids()
        subset_ids = [obj.getId()
                       for obj in self.context.listFolderContents()]
        try:
            attempt = self.context.moveObjectsToBottom(ids,
                                                       subset_ids=subset_ids)
            if attempt == 1:
                self.status = _(u'Item moved to bottom.')
            elif attempt > 1:
                self.status = _(u'Items moved to bottom.')
            else:
                self.status = self.noChangesMessage
        except ValueError:
            self.status = _(u'ValueError: Move failed.')
            return self.handle_failure(action, data, ())
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_sort_order_success(self, action, data):
        """Set the sort options for the folder."""
        self.context.setDefaultSorting(*self._get_sorting())
        self.status = _(u'Default sort order changed.')
        return self._setRedirect('portal_types', 'object/folderContents')

    def handle_rename_success(self, action, data):
        """Rename objects in a folder.
        """
        ids = self._get_ids()
        new_ids = self._get_new_ids()
        if not ids == new_ids:
            try:
                self.context.manage_renameObjects(ids, new_ids)
                if len(ids) == 1:
                    self.status = _(u'Item renamed.')
                else:
                    self.status = _(u'Items renamed.')
            except CopyError:
                self.status = _(u'CopyError: Rename failed.')
                return self.handle_rename_failure(action, data, ())
        else:
            self.status = self.noChangesMessage
        return self._setRedirect('portal_types', 'object/folderContents',
                  '{0}.b_start, {0}.sort_key, {0}.reverse'.format(self.prefix))

    def handle_cancel_success(self, action, data):
        return self._setRedirect('portal_types', 'object/folderContents',
                  '{0}.b_start, {0}.sort_key, {0}.reverse'.format(self.prefix))

    def handle_rename_failure(self, action, data, errors):
        super(ContentsView, self).handle_failure(action, data, errors)
        return self.rename_template()


class FolderView(BatchViewBase):

    """View for IFolderish.
    """

    @memoize
    def _get_items(self):
        key, reverse = self.context.getDefaultSorting()
        items = self.context.contentValues()
        items = sort(items, ((key, 'cmp', reverse and 'desc' or 'asc'),))
        return LazyFilter(items, skip='View')

    @memoize
    def has_local(self):
        return 'local_pt' in self.context.objectIds()


# XXX: quick-and-dirty port from oldstyle skin
class FolderShareView(EditFormBase):

    """Set local roles.
    """

    def __call__(self, ADD=None, DELETE=None):
        if ADD:
            self.mtool.setLocalRoles(
                obj=self.context,
                member_ids=self.request.get('member_ids', ()),
                member_role=self.request.get('member_role', ''),
                REQUEST=self.request)
        elif DELETE:
            self.mtool.deleteLocalRoles(
                obj=self.context,
                member_ids=self.request.get('member_ids', ()),
                REQUEST=self.request)
        else:
            return self.index()
        self.status = _(u'Local Roles changed.')
        return self._setRedirect('portal_types', 'object/localroles')

    @property
    @memoize
    def mtool(self):
        return getUtility(IMembershipTool)

    @property
    def searching(self):
        return self.request.get('role_submit', None)

    def found(self):
        search_param = self.request.get('search_param', '')
        search_term = self.request.get('search_term', '')
        return self.mtool.searchMembers(search_param=search_param,
                                        search_term=search_term)

    @property
    def roles(self):
        return self.mtool.getCandidateLocalRoles(self.context)

    @property
    def lroles(self):
        return self.context.get_local_roles()

    @property
    @memoize
    def auth_name(self):
        return self.mtool.getAuthenticatedMember().getId()
