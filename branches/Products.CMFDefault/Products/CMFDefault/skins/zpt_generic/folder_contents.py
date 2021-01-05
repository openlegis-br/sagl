##parameters=b_start=0, key='', reverse=0, ids=(), delta=1, items_copy='', items_cut='', items_delete='', items_paste='', items_rename='', items_up='', items_down='', items_top='', items_bottom='', items_sort=''
##
from ZTUtils import Batch
from ZTUtils import make_query
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.permissions import AddPortalContent
from Products.CMFDefault.permissions import DeleteObjects
from Products.CMFDefault.permissions import ListFolderContents
from Products.CMFDefault.permissions import ManageProperties
from Products.CMFDefault.permissions import ViewManagementScreens
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import html_marshal
from Products.CMFDefault.utils import Message as _

mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
portal_url = utool()


form = context.REQUEST.form
default_target = 'object/folderContents'
default_kw = {'b_start': b_start, 'key': key, 'reverse': reverse}
if items_copy and \
        context.validateItemIds(**form) and \
        context.folder_copy_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return
elif items_cut and \
        context.validateItemIds(**form) and \
        context.folder_cut_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return
elif items_delete and \
        context.validateItemIds(**form) and \
        context.folder_delete_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return
elif items_paste and \
        context.validateClipboardData(**form) and \
        context.folder_paste_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return
elif items_rename and \
        context.validateItemIds(**form) and \
        context.setRedirect(context, 'object/rename_items', ids=ids,
                            **default_kw):
    return
elif items_sort and \
        context.folder_sort_control(**form) and \
        context.setRedirect(context, default_target, b_start=b_start):
    return
elif items_up and \
        context.validateItemIds(**form) and \
        context.folder_up_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return
elif items_down and \
        context.validateItemIds(**form) and \
        context.folder_down_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return
elif items_top and \
        context.validateItemIds(**form) and \
        context.folder_top_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return
elif items_bottom and \
        context.validateItemIds(**form) and \
        context.folder_bottom_control(**form) and \
        context.setRedirect(context, default_target, **default_kw):
    return


options = {}

options['title'] = context.Title()

items_manage_allowed = mtool.checkPermission(ViewManagementScreens, context)
items_delete_allowed = mtool.checkPermission(DeleteObjects, context)
items_add_allowed = mtool.checkPermission(AddPortalContent, context)
upitems_list_allowed = mtool.checkPermission(ListFolderContents, context,
                                             'aq_parent')
items_move_allowed = mtool.checkPermission(ManageProperties, context)

up_info = {}
if upitems_list_allowed:
    up_obj = context.aq_parent
    if hasattr(up_obj, 'portal_url'):
        up_url = up_obj.getActionInfo('object/folderContents')['url']
        up_info = { 'icon': '%s/UpFolder_icon.gif' % portal_url,
                    'id': up_obj.getId(),
                    'url': up_url }
    else:
        up_info = { 'icon': '',
                    'id': 'Root',
                    'url': '' }
options['up_info'] = up_info

target = context.getActionInfo(default_target)['url']

if not key:
    (key, reverse) = context.getDefaultSorting()
    is_default = 1
elif (key, reverse) == context.getDefaultSorting():
    is_default = 1
else:
    is_default = 0

columns = ( {'key': 'Type',
             'title': _(u'Type'),
             'width': '20',
             'colspan': '2'}
          , {'key': 'getId',
             'title': _(u'Name'),
             'width': '360',
             'colspan': None}
          , {'key': 'modified',
             'title': _(u'Last Modified'),
             'width': '180',
             'colspan': None}
          , {'key': 'position',
             'title': _(u'Position'),
             'width': '80',
             'colspan': None }
          )
for column in columns:
    if key == column['key'] and not reverse and key != 'position':
        query = make_query(key=column['key'], reverse=1)
    else:
        query = make_query(key=column['key'])
    column['url'] = '%s?%s' % (target, query)

context.filterCookie()
folderfilter = context.REQUEST.get('folderfilter', '')
filter = context.decodeFolderFilter(folderfilter)
items = context.listFolderContents(contentFilter=filter)
items = sequence.sort( items, ((key, 'cmp', reverse and 'desc' or 'asc'),) )
batch_obj = Batch(items, 25, b_start, orphan=0)
items = []
i = 1
for item in batch_obj:
    item_id = item.getId()
    item_position = key == 'position' and str(b_start + i) or '...'
    i += 1
    item_url = item.getActionInfo( ('object/folderContents',
                                    'object/view') )['url']
    items.append( { 'checkbox': items_manage_allowed and
                                ('cb_%s' % item_id) or '',
                    'icon': item.getIconURL(),
                    'id': item_id,
                    'modified': item.ModificationDate(),
                    'position': item_position,
                    'title': item.Title(),
                    'type': item.Type() or None,
                    'url': item_url } )
navigation = context.getBatchNavigation(batch_obj, target, **default_kw)
options['batch'] = { 'listColumnInfos': tuple(columns),
                     'listItemInfos': tuple(items),
                     'navigation': navigation }

hidden_vars = []
for name, value in html_marshal(**default_kw):
    hidden_vars.append( {'name': name, 'value': value} )
buttons = []
if items_manage_allowed:
    if items and items_add_allowed and context.allowedContentTypes():
        buttons.append( {'name': 'items_rename', 'value': _(u'Rename...')} )
    if items:
        buttons.append( {'name': 'items_cut', 'value': _(u'Cut')} )
        buttons.append( {'name': 'items_copy', 'value': _(u'Copy')} )
    if items_add_allowed and context.cb_dataValid():
        buttons.append( {'name': 'items_paste', 'value': _(u'Paste')} )
    if items_delete_allowed and items:
        buttons.append( {'name': 'items_delete', 'value': _(u'Delete')} )
length = batch_obj.sequence_length
is_orderable = items_move_allowed and (key == 'position') and length > 1
is_sortable = items_move_allowed and not is_default
deltas = range( 1, min(5, length) ) + range(5, length, 5)
options['form'] = { 'action': target,
                    'listHiddenVarInfos': tuple(hidden_vars),
                    'listButtonInfos': tuple(buttons),
                    'listDeltas': tuple(deltas),
                    'is_orderable': is_orderable,
                    'is_sortable': is_sortable }

return context.folder_contents_template(**decode(options, script))
