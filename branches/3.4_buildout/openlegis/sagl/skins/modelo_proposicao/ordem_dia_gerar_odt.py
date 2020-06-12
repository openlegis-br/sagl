## Script (Python) "ordem_dia_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, lst_pdiscussao, lst_sdiscussao, lst_discussao_unica, lst_presidente, nom_arquivo
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.ordem_dia_gerar_odt(inf_basicas_dic, lst_pdiscussao, lst_sdiscussao, lst_discussao_unica, lst_presidente, nom_arquivo)
