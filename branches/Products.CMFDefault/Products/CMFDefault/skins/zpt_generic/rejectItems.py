##parameters=items, comment=''
##
from Products.CMFCore.utils import getUtilityByInterfaceName

wtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IWorkflowTool')
for path in items:
    object = context.restrictedTraverse( path )
    wtool.doActionFor( object, 'reject', comment=comment )

context.REQUEST[ 'RESPONSE' ].redirect( '%s/review?%s'
                   % ( context.portal_url()
                     , 'portal_status_message=Items+rejected.'
                     ) )
