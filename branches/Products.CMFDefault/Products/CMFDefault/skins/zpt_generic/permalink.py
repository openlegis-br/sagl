## Script (Python) "permalink"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Returns an object by unique id
##
from Products.CMFCore.utils import getUtilityByInterfaceName

subpath = traverse_subpath[0]
uid_handler=getUtilityByInterfaceName('Products.CMFUid.interfaces.IUniqueIdHandler')

# appending 'isAvailable' instead of a unique id returns if
# the site permalink feature is available.
if str(subpath).strip() == 'isAvailable':
    # no permalink feature without an uid handler tool being installed
    if uid_handler is None:
        return '0'
    ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
    isAvailable = getattr(ptool, 'enable_permalink', 0)
    return str(int(isAvailable))

obj = uid_handler.getObject(subpath)
# workarround for an acquisition wrapping problem.
obj = context.restrictedTraverse(obj.getPhysicalPath())

ti = obj.getTypeInfo()
method_id = ti and ti.queryMethodID('view', context=obj)
if method_id:
    return getattr(obj, method_id)()
return obj()
