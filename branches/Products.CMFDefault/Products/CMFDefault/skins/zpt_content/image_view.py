##parameters=
##
from Products.CMFDefault.utils import decode

options = {}
options['title'] = context.Title()
options['description'] = context.Description()
options['image'] = context.tag()

return context.image_view_template(**decode(options, script))
