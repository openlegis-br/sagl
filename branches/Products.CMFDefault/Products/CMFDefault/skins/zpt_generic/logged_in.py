##parameters=
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
stool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ISkinsTool')


if stool.updateSkinCookie():
    skinname = context.getSkinNameFromRequest(context.REQUEST)
    context.changeSkin(skinname, context.REQUEST)


options = {}

isAnon = mtool.isAnonymousUser()
if isAnon:
    context.REQUEST.RESPONSE.expireCookie('__ac', path='/')
    options['is_anon'] = True
    options['title'] = _(u'Login failure')
    options['admin_email'] = ptool.getProperty('email_from_address')
else:
    mtool.createMemberArea()
    member = mtool.getAuthenticatedMember()
    now = context.ZopeTime()
    last_login = member.getProperty('login_time')
    never_logged_in = str(last_login).startswith('2000/01/01')
    if never_logged_in and ptool.getProperty('validate_email'):
        member.setProperties(last_login_time='1999/01/01', login_time=now)
        target = atool.getActionInfo('user/change_password')['url']
        context.REQUEST.RESPONSE.redirect(target)
        return
    member.setProperties(last_login_time=last_login, login_time=now)
    came_from = context.REQUEST.get('came_from', None)
    if came_from:
        context.REQUEST.RESPONSE.redirect(came_from)
        return
    options['is_anon'] = False
    options['title'] = _(u'Login success')

return context.logged_in_template(**decode(options, script))
