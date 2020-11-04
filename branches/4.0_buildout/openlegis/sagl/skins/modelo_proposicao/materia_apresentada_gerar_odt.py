## Script (Python) "materia_apresentada_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, lst_materia_apresentada
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.materia_apresentada_gerar_odt(inf_basicas_dic, lst_materia_apresentada)
