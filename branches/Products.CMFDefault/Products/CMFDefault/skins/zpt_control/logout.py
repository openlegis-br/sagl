## Script (Python) "logout"
##title=Logout handler
##parameters=
from Products.CMFCore.utils import getUtilityByInterfaceName

stool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ISkinsTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
REQUEST = context.REQUEST

stool.clearSkinCookie()
try:
    cctool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ICookieCrumbler')
    cctool.logout(REQUEST.RESPONSE)
except AttributeError:
    REQUEST.RESPONSE.expireCookie('__ac', path='/')

return REQUEST.RESPONSE.redirect(utool() + '/logged_out')
