##parameters=text, description='', **kw
##
from Products.CMFDefault.exceptions import IllegalHTML
from Products.CMFDefault.utils import scrubHTML

try:
    description = scrubHTML(description)
    text = scrubHTML(text)
    return context.setStatus(True, text=text, description=description)
except IllegalHTML, errmsg:
    return context.setStatus(False, errmsg)
