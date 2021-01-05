##parameters=title, text, **kw
##title=Reply to content
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import Message as _

dtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IDiscussionTool')

talkback = dtool.getDiscussionFor(context)
replyID = talkback.createReply(title=title, text=text)
reply = talkback.getReply(replyID)

context.setStatus(True, _(u'Reply added.'))
context.setRedirect(reply, 'object/view')
