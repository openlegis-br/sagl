##parameters=
##title=Delete reply
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import Message as _

dtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IDiscussionTool')

parent = context.inReplyTo()
talkback = dtool.getDiscussionFor(parent)
talkback.deleteReply( context.getId() )

context.setStatus(True, _(u'Reply deleted.'))
context.setRedirect(parent, 'object/view')
