##parameters=b_start=0, key='', reverse=0, ids=(), new_ids=(), rename='', cancel=''
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import html_marshal
from Products.CMFDefault.utils import Message as _

utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
portal_url = utool()


form = context.REQUEST.form
default_kw = {'b_start': b_start, 'key': key, 'reverse': reverse}
if rename and \
        context.folder_rename_control(**form) and \
        context.setRedirect(context, 'object/folderContents', **default_kw):
    return
elif cancel and \
        context.setRedirect(context, 'object/folderContents', **default_kw):
    return


options = {}

c = context.aq_explicit
raw_items = [ getattr(c, id) for id in ids if hasattr(c, id) ]
raw_items = [ item for item in raw_items if item.cb_isMoveable() ]
items = []
for item in raw_items:
    items.append( { 'icon': item.getIconURL(),
                    'id': item.getId(),
                    'title': item.Title(),
                    'type': item.Type() or None } )
options['batch'] = { 'listItemInfos': tuple(items) }

target = context.getActionInfo('object/rename_items')['url']
hidden_vars = []
for name, value in html_marshal(**default_kw):
    hidden_vars.append( {'name': name, 'value': value} )
buttons = []
buttons.append( {'name': 'rename', 'value': _(u'Rename')} )
buttons.append( {'name': 'cancel', 'value': _(u'Cancel')} )
options['form'] = { 'action': target,
                    'listHiddenVarInfos': tuple(hidden_vars),
                    'listButtonInfos': tuple(buttons) }

return context.folder_rename_template(**decode(options, script))
