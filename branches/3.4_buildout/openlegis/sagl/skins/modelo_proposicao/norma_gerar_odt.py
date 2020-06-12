## Script (Python) "norma_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, nom_arquivo, des_tipo_norma, num_norma, ano_norma, dat_norma, data_norma, txt_ementa, modelo_norma
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.norma_gerar_odt(inf_basicas_dic, nom_arquivo, des_tipo_norma, num_norma, ano_norma, dat_norma, data_norma, txt_ementa, modelo_norma)
