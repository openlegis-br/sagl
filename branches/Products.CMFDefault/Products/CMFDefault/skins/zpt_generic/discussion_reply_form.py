##parameters=add='', edit='', preview=''
##
from Products.PythonScripts.standard import structured_text
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import html_marshal
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')


form = context.REQUEST.form
is_preview = False
if add and \
        context.validateHTML(**form) and \
        context.discussion_reply(**form):
    return
elif preview and \
        context.validateHTML(**form):
    is_preview = True


options = {}

title = form.get('title', context.Title())
text = form.get('text', '')
options['is_preview'] = is_preview
options['title'] = title
options['text'] = text
options['cooked_text'] = structured_text(text)

if is_preview:
    hidden_vars = [ {'name': n, 'value': v}
                    for n, v in html_marshal(title=title, text=text) ]
else:
    hidden_vars = []
buttons = []
target = atool.getActionInfo('object/reply', context)['url']
buttons.append( {'name': 'add', 'value': _(u'Add')} )
if is_preview:
    buttons.append( {'name': 'edit', 'value': _(u'Edit')} )
else:
    buttons.append( {'name': 'preview', 'value': _(u'Preview')} )
options['form'] = { 'action': target,
                    'listHiddenVarInfos': tuple(hidden_vars),
                    'listButtonInfos': tuple(buttons) }

return context.discussion_reply_template(**decode(options, script))
