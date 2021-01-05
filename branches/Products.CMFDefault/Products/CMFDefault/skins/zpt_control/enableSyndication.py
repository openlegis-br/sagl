##parameters=
##title=Enable Syndication for a resource
##
from Products.CMFCore.utils import getUtilityByInterfaceName

syndtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ISyndicationTool')
if syndtool.isSiteSyndicationAllowed():
    syndtool.enableSyndication(context)
    msg = 'Syndication+Enabled'
else:
    msg = 'Syndication+Not+Allowed'

target = '%s/synPropertiesForm' % context.absolute_url()
qs = 'portal_status_message=%s' % msg

return context.REQUEST.RESPONSE.redirect('%s?%s' % (target, qs))
