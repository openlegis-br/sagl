##parameters=
##
from Products.CMFDefault.utils import decode

options = {}
options['title'] = context.Title()
options['description'] = context.Description()
options['url'] = context.getRemoteUrl()

return context.link_view_template(**decode(options, script))
