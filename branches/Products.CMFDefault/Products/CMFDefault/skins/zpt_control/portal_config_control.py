##parameters=**kw
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import Message as _

ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')

kw.setdefault('enable_actionicons', False)
kw.setdefault('enable_permalink', False)

ptool.editProperties(kw)

return context.setStatus(True, _(u'Portal settings changed.'))
