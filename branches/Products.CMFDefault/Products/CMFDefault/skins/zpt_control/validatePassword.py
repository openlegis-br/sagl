##parameters=password='', confirm='', **kw
##
from Products.CMFCore.utils import getUtilityByInterfaceName

ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
rtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IRegistrationTool')

if ptool.getProperty('validate_email'):
    password = rtool.generatePassword()
    return context.setStatus(True, password=password)
else:
    result = rtool.testPasswordValidity(password, confirm)
    if result:
        return context.setStatus(False, result)
    else:
        return context.setStatus(True)
