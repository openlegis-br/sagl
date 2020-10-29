## Script (Python) "materias_expediente_gerar_ods"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=relatorio_dic, total_assuntos, parlamentares, nom_arquivo
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.materias_expediente_gerar_ods(relatorio_dic, total_assuntos, parlamentares, nom_arquivo)
