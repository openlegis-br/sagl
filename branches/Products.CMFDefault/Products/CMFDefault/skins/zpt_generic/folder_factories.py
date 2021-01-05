##parameters=add=''
##
from Products.CMFDefault.utils import decode

form = context.REQUEST.form
if add and \
        context.validateType(**form) and \
        context.validateId(**form) and \
        context.folder_add_control(**form):
    return


options = {}

items = []
type_name = form.get('type_name', None)
for item in context.allowedContentTypes():
    item_id = item.getId()
    items.append( { 'checked': type_name == item_id,
                    'description': item.Description(),
                    'id': item_id,
                    'radio': 'cb_%s' % item_id.replace(' ', '_'),
                    'title': item.Title() } )
if len(items) == 1:
    items[0]['checked'] = True
options['batch'] = { 'listItemInfos': tuple(items) }

target = context.getActionInfo('object/new')['url']
id = form.get('id', '')
options['form'] = { 'action': target,
                    'id': id }

return context.folder_factories_template(**decode(options, script))
