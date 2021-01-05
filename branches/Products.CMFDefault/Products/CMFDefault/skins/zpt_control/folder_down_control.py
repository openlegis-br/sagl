##parameters=ids, delta, **kw
##
from Products.CMFDefault.utils import Message as _

subset_ids = [ obj.getId() for obj in context.listFolderContents() ]
try:
    attempt = context.moveObjectsDown(ids, delta, subset_ids=subset_ids)
    if attempt == 1:
        return context.setStatus(True, _(u'Item moved down.'))
    elif attempt > 1:
        return context.setStatus(True, _(u'Items moved down.'))
    else:
        return context.setStatus(False, _(u'Nothing to change.'))
except ValueError:
    return context.setStatus(False, _(u'ValueError: Move failed.'))
