##parameters=type_name='', **kw
##
from Products.CMFDefault.utils import Message as _

if type_name:
    return context.setStatus(True)
else:
    return context.setStatus(False, _(u'Please select a content type.'))
