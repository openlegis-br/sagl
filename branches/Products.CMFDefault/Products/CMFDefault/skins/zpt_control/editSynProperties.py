##parameters=
##title=Enable Syndication for a resource
##
from Products.CMFCore.utils import getUtilityByInterfaceName

REQUEST = context.REQUEST
syndtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ISyndicationTool')
syndtool.editSyInformationProperties(context,
                                     REQUEST['updatePeriod'],
                                     REQUEST['updateFrequency'],
                                     REQUEST['updateBase'],
                                     REQUEST['max_items'],
                                     REQUEST)
return REQUEST.RESPONSE.redirect(context.absolute_url() + '/synPropertiesForm?portal_status_message=Syndication+Properties+Updated.')
