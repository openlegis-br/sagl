##parameters=ids, **kw
##
from Products.CMFDefault.utils import Message as _

subset_ids = [ obj.getId() for obj in context.listFolderContents() ]
try:
    attempt = context.moveObjectsToTop(ids, subset_ids=subset_ids)
    if attempt == 1:
        return context.setStatus(True, _(u'Item moved to top.'))
    elif attempt > 1:
        return context.setStatus(True, _(u'Items moved to top.'))
    else:
        return context.setStatus(False, _(u'Nothing to change.'))
except ValueError:
    return context.setStatus(False, _(u'ValueError: Move failed.'))
