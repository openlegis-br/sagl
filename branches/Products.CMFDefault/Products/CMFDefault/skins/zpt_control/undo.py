##parameters=transaction_info
##title=Undo transactions
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import Message as _

utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IUndoTool')

utool.undo(context, transaction_info)

context.setStatus(True, _(u'Transaction(s) undone.'))
context.setRedirect(context, 'object/folderContents')
