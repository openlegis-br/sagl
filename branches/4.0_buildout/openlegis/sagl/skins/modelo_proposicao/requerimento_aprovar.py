## Script (Python) "requerimento_aprovar"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, nom_resultado, cod_materia
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.requerimento_aprovar(cod_sessao_plen, nom_resultado, cod_materia)
