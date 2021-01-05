##parameters=provider, action_path, **kw
##
from ZTUtils import make_query
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.exceptions import zExceptions_Unauthorized
from Products.CMFDefault.utils import getBrowserCharset

utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
portal_url = utool()


try:
    target = provider.getActionInfo(action_path, check_condition=1)['url']
except (ValueError, zExceptions_Unauthorized):
    target = portal_url

message = context.REQUEST.other.get('portal_status_message', '')
if message:
    if isinstance(message, unicode):
        message = unicode(message).encode(getBrowserCharset(context.REQUEST))
    kw['portal_status_message'] = message
for k, v in kw.items():
    if not v:
        del kw[k]

query = kw and ('?%s' % make_query(kw)) or ''
context.REQUEST.RESPONSE.redirect('%s%s' % (target, query))

return True
