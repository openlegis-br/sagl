##parameters=ids=(), **kw
##
from Products.CMFDefault.utils import Message as _

if ids:
    return context.setStatus(True)
else:
    return context.setStatus(False, _(u'Please select one or more items '
                                      u'first.'))
