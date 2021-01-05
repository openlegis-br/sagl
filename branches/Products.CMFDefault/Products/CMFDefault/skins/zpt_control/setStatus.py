##parameters=success, message='', **kw
##
from Products.CMFDefault.utils import translate

if message:
    message = translate(message, context)
    context.REQUEST.other['portal_status_message'] = message
if kw:
    for k, v in kw.items():
        context.REQUEST.form[k] = v

return success
