##parameters=text_format, text, description='', **kw
##
from Products.CMFDefault.exceptions import ResourceLockedError
from Products.CMFDefault.utils import Message as _

if description != context.Description() or \
        text_format != context.text_format or text != context.EditableBody():
    try:
        context.edit(text=text, description=description,
                     text_format=text_format)
        return context.setStatus(True, _(u'News Item changed.'))
    except ResourceLockedError, errmsg:
        return context.setStatus(False, errmsg)
else:
    return context.setStatus(False, _(u'Nothing to change.'))
