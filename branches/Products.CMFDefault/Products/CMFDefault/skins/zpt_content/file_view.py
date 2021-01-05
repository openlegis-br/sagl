##parameters=
##
from Products.CMFDefault.utils import decode

options = {}
options['title'] = context.Title()
options['description'] = context.Description()
options['content_type'] = context.getContentType()
options['id'] = context.getId()
options['size'] = context.get_size()
options['url'] = context.absolute_url()

return context.file_view_template(**decode(options, script))
