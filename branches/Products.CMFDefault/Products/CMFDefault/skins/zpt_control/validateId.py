##parameters=id='', **kw
##
from Products.CMFDefault.utils import Message as _

if id:
    if context.checkIdAvailable(id):
        return context.setStatus(True)
    else:
        return context.setStatus(False, _(u'Please choose another ID.'))
else:
    return context.setStatus(False, _(u'Please enter an ID.'))
