##title=Mail a user's password
##parameters=
from Products.CMFCore.utils import getUtilityByInterfaceName

rtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IRegistrationTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
REQUEST = context.REQUEST

rtool.mailPassword(REQUEST['userid'], REQUEST)
return REQUEST.RESPONSE.redirect(utool() + '/mail_password_response')
