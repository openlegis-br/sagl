##parameters=ids, **kw
##title=Delete members
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import Message as _

mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')

mtool.deleteMembers(ids, REQUEST=context.REQUEST)

if len(ids) == 1:
    return context.setStatus(True, _(u'Selected member deleted.'))
else:
    return context.setStatus(True, _(u'Selected members deleted.'))
