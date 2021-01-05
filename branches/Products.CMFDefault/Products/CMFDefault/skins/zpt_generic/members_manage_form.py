##parameters=b_start=0, ids=(), members_new='', members_delete=''
##
from ZTUtils import Batch
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import html_marshal
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')


form = context.REQUEST.form
if members_delete and \
        context.validateMemberIds(**form) and \
        context.setRedirect(atool, 'global/members_delete', b_start=b_start,
                            ids=ids):
    return
elif members_new and \
        context.setRedirect(atool, 'global/members_register', b_start=b_start):
    return


options = {}

target = atool.getActionInfo('global/manage_members')['url']

members = mtool.listMembers()
batch_obj = Batch(members, 25, b_start, orphan=0)
items = []
for member in batch_obj:
    member_id = member.getId()
    fullname = member.getProperty('fullname')
    last_login = member.getProperty('login_time')
    never_logged_in = str(last_login).startswith('2000/01/01')
    member_login = never_logged_in and '---' or last_login.Date()
    member_home = mtool.getHomeUrl(member_id, verifyPermission=0)
    items.append( {'checkbox': 'cb_%s' % member_id,
                   'email': member.getProperty('email'),
                   'login': member_login,
                   'id': member_id,
                   'name': '%s (%s)' % (fullname, member_id),
                   'home': member_home } )
navigation = context.getBatchNavigation(batch_obj, target,
                                        'member', 'members')
options['batch'] = { 'listItemInfos': tuple(items),
                     'navigation': navigation }

hidden_vars = []
for name, value in html_marshal(b_start=b_start):
    hidden_vars.append( {'name': name, 'value': value} )
buttons = []
buttons.append( {'name': 'members_new', 'value': _(u'New...')} )
if items:
    buttons.append( {'name': 'members_delete', 'value': _(u'Delete...')} )
options['form'] = { 'action': target,
                    'listHiddenVarInfos': tuple(hidden_vars),
                    'listButtonInfos': tuple(buttons) }

return context.members_manage_template(**decode(options, script))
