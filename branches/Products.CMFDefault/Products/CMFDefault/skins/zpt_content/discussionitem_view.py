##parameters=
##
from Products.CMFDefault.utils import decode

options = {}
options['title'] = context.Title()
options['description'] = context.Description()
options['text'] = context.CookedBody()

return context.discussionitem_view_template(**decode(options, script))
