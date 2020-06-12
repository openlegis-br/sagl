## Script (Python) "oficio_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, nom_arquivo, sgl_tipo_documento, num_documento, ano_documento, txt_ementa, dat_documento, dia_documento, nom_autor, modelo_documento
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.oficio_gerar_odt(inf_basicas_dic, nom_arquivo, sgl_tipo_documento, num_documento, ano_documento, txt_ementa, dat_documento, dia_documento, nom_autor, modelo_documento)
