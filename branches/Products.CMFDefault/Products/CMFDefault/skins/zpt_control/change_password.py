##parameters=password, confirm, domains=None, **kw
##title=Action to change password
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import Message as _

mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')
rtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IRegistrationTool')

result = rtool.testPasswordValidity(password, confirm)
if result:
    return context.setStatus(False, result)

member = mtool.getAuthenticatedMember()
mtool.setPassword(password, domains, REQUEST=context.REQUEST)
if member.getProperty('last_login_time') == DateTime('1999/01/01'):
    member.setProperties(last_login_time='2000/01/01')

mtool.credentialsChanged(password, context.REQUEST)

return context.setStatus(True, _(u'Password changed.'))
