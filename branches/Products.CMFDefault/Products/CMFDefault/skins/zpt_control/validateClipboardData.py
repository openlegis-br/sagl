##parameters=**kw
##
from Products.CMFDefault.utils import Message as _

if context.cb_dataValid():
    return context.setStatus(True)
else:
    return context.setStatus(False, _(u'Please copy or cut one or more items '
                                      u'to paste first.'))
