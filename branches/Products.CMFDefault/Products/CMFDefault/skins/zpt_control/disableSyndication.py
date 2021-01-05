##parameters=
##title=Disable Syndication for a resource
##
from Products.CMFCore.utils import getUtilityByInterfaceName

syndtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ISyndicationTool')
if syndtool.isSyndicationAllowed(context):
    syndtool.disableSyndication(context)
    return context.REQUEST.RESPONSE.redirect(context.absolute_url() +
               '/synPropertiesForm?portal_status_message=Syndication+Disabled')
else:
    return context.REQUEST.RESPONSE.redirect(context.absolute_url() +
            '/synPropertiesForm?portal_status_message=Syndication+Not+Allowed')
