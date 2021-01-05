##parameters=include_root=1
##title=Return breadcrumbs
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import Message as _

ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
portal_url = utool()
result = []

if include_root:
    result.append( { 'id'      : _(u'root')
                   , 'title'   : ptool.title()
                   , 'url'     : portal_url
                   }
                 )

relative = utool.getRelativeContentPath(context)
portal = utool.getPortalObject()

for i in range( len( relative ) ):
    now = relative[ :i+1 ]
    obj = portal.restrictedTraverse( now )
    if not now[ -1 ] == 'talkback':
        result.append( { 'id'      : now[ -1 ]
                       , 'title'   : obj.Title()
                       , 'url'     : portal_url + '/' + '/'.join(now)
                       }
                    )

return result
