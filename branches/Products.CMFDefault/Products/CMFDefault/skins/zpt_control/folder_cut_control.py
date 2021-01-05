##parameters=ids, **kw
##title=Cut objects from a folder and copy to the clipboard
##
from Products.CMFDefault.exceptions import CopyError
from Products.CMFDefault.exceptions import zExceptions_Unauthorized
from Products.CMFDefault.utils import Message as _

try:
    context.manage_cutObjects(ids, context.REQUEST)
    if len(ids) == 1:
        return context.setStatus(True, _(u'Item cut.'))
    else:
        return context.setStatus(True, _(u'Items cut.'))
except CopyError:
    return context.setStatus(False, _(u'CopyError: Cut failed.'))
except zExceptions_Unauthorized:
    return context.setStatus(False, _(u'Unauthorized: Cut failed.'))
