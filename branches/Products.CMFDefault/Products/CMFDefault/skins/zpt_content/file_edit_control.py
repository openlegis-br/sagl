##parameters=file, **kw
##
from Products.CMFDefault.exceptions import ResourceLockedError
from Products.CMFDefault.utils import Message as _

try:
    context.edit(file=file)
    return context.setStatus(True, _(u'File changed.'))
except ResourceLockedError, errmsg:
    return context.setStatus(False, errmsg)
