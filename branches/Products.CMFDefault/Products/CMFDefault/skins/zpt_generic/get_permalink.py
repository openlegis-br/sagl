##parameters=
##title=Returns the permalink url or None
##
from Products.CMFCore.utils import getUtilityByInterfaceName

# calculate the permalink if the uid handler tool exists, permalinks
# are configured to be shown and the object is not folderish
uidtool = getUtilityByInterfaceName('Products.CMFUid.interfaces.IUniqueIdHandler', None)
if uidtool is not None:
    ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
    showPermalink = getattr(ptool, 'enable_permalink', None)
    isFolderish = getattr(context.aq_explicit, 'isPrincipiaFolderish', None)

    if showPermalink and not isFolderish:
        # returns the uid (generates one if necessary)
        utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
        uid = uidtool.register(context)
        url = "%s/permalink/%s" % (utool(), uid)
        return url
