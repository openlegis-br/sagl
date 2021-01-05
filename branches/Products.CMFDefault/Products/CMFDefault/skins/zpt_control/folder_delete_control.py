##parameters=ids, **kw
##title=Delete objects from a folder
##
from Products.CMFDefault.utils import Message as _

context.manage_delObjects( list(ids) )

if len(ids) == 1:
    return context.setStatus(True, _(u'Item deleted.'))
else:
    return context.setStatus(True, _(u'Items deleted.'))
