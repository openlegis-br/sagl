## Script (Python) "oficio_ind_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, lst_indicacao, lst_presidente
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.oficio_ind_gerar_odt(inf_basicas_dic, lst_indicacao, lst_presidente)
