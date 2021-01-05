##parameters=b_start=0, member_id='', member_email='', password='', confirm='', send_password='', add='', cancel=''
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.permissions import ManageUsers
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
portal_url = utool()
validate_email = ptool.getProperty('validate_email')
is_anon = mtool.isAnonymousUser()
is_newmember = False
is_usermanager = mtool.checkPermission(ManageUsers, mtool)


form = context.REQUEST.form
if add and \
        context.validatePassword(**form) and \
        context.members_add_control(**form) and \
        context.setRedirect(atool, ('global/members_register', 'user/login'),
                            b_start=b_start):
    return
elif cancel and \
        context.setRedirect(atool, 'global/manage_members', b_start=b_start):
    return


options = {}

if context.REQUEST.get('is_newmember', False) == True:
    is_anon = False
    is_newmember = True

options['title'] = is_usermanager and _(u'Register a New Member') \
                                  or _(u'Become a Member')
options['member_id'] = member_id
options['member_email'] = member_email
options['password'] = is_newmember and context.REQUEST.get('password', '') or ''
options['send_password'] = send_password
options['portal_url'] = portal_url
options['isAnon'] = is_anon
options['isAnonOrUserManager'] = is_anon or is_usermanager
options['isNewMember'] = is_newmember
options['isOrdinaryMember'] = not (is_anon or is_newmember or is_usermanager)
options['validate_email'] = validate_email

buttons = []
if is_newmember:
    target = atool.getActionInfo('user/logged_in')['url']
    buttons.append( {'name': 'login', 'value': _(u'Log in')} )
else:
    target = atool.getActionInfo(('global/members_register',
                                  'user/join'))['url']
    buttons.append( {'name': 'add', 'value': _(u'Register')} )
    buttons.append( {'name': 'cancel', 'value': _(u'Cancel')} )
options['form'] = { 'action': target,
                    'listButtonInfos': tuple(buttons) }

return context.join_template(**decode(options, script))
