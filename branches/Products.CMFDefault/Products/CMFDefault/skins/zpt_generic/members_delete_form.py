##parameters=ids, b_start=0, delete='', cancel=''
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import html_marshal
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')


form = context.REQUEST.form
if delete and \
        context.members_delete_control(**form) and \
        context.setRedirect(atool, 'global/manage_members', b_start=b_start):
    return
elif cancel and \
        context.setRedirect(atool, 'global/manage_members', b_start=b_start):
    return


options = {}

target = atool.getActionInfo('global/members_delete')['url']
members = []
for member_id in ids:
    member = mtool.getMemberById(member_id)
    members.append('%s (%s)' % (member.getProperty('fullname'), member_id))
hidden_vars = []
for name, value in html_marshal(b_start=b_start, ids=ids):
    hidden_vars.append( {'name': name, 'value': value} )
buttons = []
buttons.append( {'name': 'delete', 'value': _(u'Delete')} )
buttons.append( {'name': 'cancel', 'value': _(u'Cancel')} )
options['form'] = { 'action': target,
                    'members': ', '.join(members),
                    'listHiddenVarInfos': tuple(hidden_vars),
                    'listButtonInfos': tuple(buttons) }

return context.members_delete_template(**decode(options, script))
