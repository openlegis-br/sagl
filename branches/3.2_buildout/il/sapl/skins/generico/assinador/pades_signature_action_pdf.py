## Script (Python) "pades_signature_action_pdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=token, codigo, tipo_doc
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sapl')

return st.pades_signature_action(token, codigo, tipo_doc)

