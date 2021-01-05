##parameters=ids, new_ids, **kw
##title=Rename objects in a folder
##
from Products.CMFDefault.exceptions import CopyError
from Products.CMFDefault.utils import Message as _

if not ids == new_ids:
    try:
        context.manage_renameObjects(ids, new_ids)
        if len(ids) == 1:
            return context.setStatus(True, _(u'Item renamed.'))
        else:
            return context.setStatus(True, _(u'Items renamed.'))
    except CopyError:
        return context.setStatus(False, _(u'CopyError: Rename failed.'))
else:
    return context.setStatus(False, _(u'Nothing to change.'))
