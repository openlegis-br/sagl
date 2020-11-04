## Script (Python) "tramitacao_signature_action_pdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=token, cod_tramitacao
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.tramitacao_signature_action(token, cod_tramitacao)
