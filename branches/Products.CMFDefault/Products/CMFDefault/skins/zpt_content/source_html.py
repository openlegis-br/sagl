##parameters=
##
from Products.CMFDefault.utils import decode

options = {}

metadata = [ {'name': field[0], 'body': field[1]}
             for field in context.getMetadataHeaders()
             if field[0].lower() != 'title' ]
options['title'] = context.Title()
options['listMetadataFields'] = metadata
options['editable_body'] = context.EditableBody()

return context.source_html_template(**decode(options, script))
