##parameters=text_format, text, SafetyBelt='', **kw
##
from Products.CMFDefault.exceptions import EditingConflict
from Products.CMFDefault.exceptions import ResourceLockedError
from Products.CMFDefault.utils import Message as _

if text_format != context.text_format or text != context.EditableBody():
    try:
        context.edit(text_format, text, safety_belt=SafetyBelt)
        return context.setStatus(True, _(u'Document changed.'))
    except (ResourceLockedError, EditingConflict), errmsg:
        return context.setStatus(False, errmsg)
else:
    return context.setStatus(False, _(u'Nothing to change.'))
