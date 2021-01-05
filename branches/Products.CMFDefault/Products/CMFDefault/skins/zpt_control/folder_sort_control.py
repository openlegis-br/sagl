##parameters=key='position', reverse=0, **kw
##title=Sort objects in a folder
##
from Products.CMFDefault.utils import Message as _

context.setDefaultSorting(key, reverse)
return context.setStatus(True, _(u'Default sort order changed.'))
