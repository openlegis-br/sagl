##parameters=change='', cancel=''
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
member = mtool.getAuthenticatedMember()
portal_url = utool()

form = context.REQUEST.form
if change and \
        context.change_password(**form) and \
        context.setRedirect(atool, 'user/mystuff'):
    return
elif cancel and \
        context.setRedirect(atool, 'user/mystuff'):
    return


options = {}

is_first_login = (member.getProperty('last_login_time') == DateTime('1999/01/01'))
options['is_first_login'] = is_first_login
if is_first_login:
    options['title'] = _(u'Welcome!')
    options['portal_title'] = ptool.getProperty('title')
else:
    options['title'] = _(u'Change your Password')
options['member_id'] = member.getId()
buttons = []
target = '%s/password_form' % portal_url
buttons.append( {'name': 'change', 'value': _(u'Change')} )
if not is_first_login:
    buttons.append( {'name': 'cancel', 'value': _(u'Cancel')} )
options['form'] = { 'action': target,
                    'listButtonInfos': tuple(buttons) }

return context.password_form_template(**decode(options, script))
