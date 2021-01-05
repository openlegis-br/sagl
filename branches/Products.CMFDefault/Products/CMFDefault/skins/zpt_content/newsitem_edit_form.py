##parameters=change='', change_and_view=''
##
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import Message as _

form = context.REQUEST.form
if change and \
        context.validateHTML(**form) and \
        context.newsitem_edit_control(**form) and \
        context.setRedirect(context, 'object/edit'):
    return
elif change_and_view and \
        context.validateHTML(**form) and \
        context.newsitem_edit_control(**form) and \
        context.setRedirect(context, 'object/view'):
    return


options = {}

options['title'] = context.Title()
options['description'] = form.get('description', context.Description())
options['text_format'] = form.get('text_format', context.text_format)
options['text'] = form.get('text', context.EditableBody())

buttons = []
target = context.getActionInfo('object/edit')['url']
buttons.append( {'name': 'change', 'value': _(u'Change')} )
buttons.append( {'name': 'change_and_view', 'value': _(u'Change and View')} )
options['form'] = { 'action': target,
                    'listButtonInfos': tuple(buttons) }

return context.newsitem_edit_template(**decode(options, script))
