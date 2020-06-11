## Script (Python) "tramitacao_juntar_pdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_tramitacao
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sapl')
return st.tramitacao_materia_juntar(cod_tramitacao=cod_tramitacao)


