##parameters=member_id, password, member_email, send_password=False, **kw
##title=Add a member
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.permissions import ManageUsers
from Products.CMFDefault.utils import Message as _

mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool')
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
rtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IRegistrationTool')

try:
    rtool.addMember( id=member_id, password=password,
                     properties={'username': member_id,
                                 'email': member_email},
                     REQUEST=context.REQUEST)
except ValueError, errmsg:
    return context.setStatus(False, errmsg)
else:
    if ptool.getProperty('validate_email') or send_password:
        rtool.registeredNotify(member_id, REQUEST=context.REQUEST)
    if mtool.checkPermission(ManageUsers, mtool):
        return context.setStatus(True, _(u'Member registered.'))
    else:
        return context.setStatus(False, _(u'Success!'), is_newmember=True)
