## Script (Python) "norma_gerar_pdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_norma, tipo_texto
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.norma_gerar_pdf(cod_norma, tipo_texto)
