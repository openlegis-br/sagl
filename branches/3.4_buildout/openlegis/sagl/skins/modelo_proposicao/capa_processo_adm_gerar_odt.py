## Script (Python) "capa_processo_adm_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_documento, des_tipo_documento, txt_interessado, txt_assunto, nom_arquivo
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.capa_processo_adm_gerar_odt(inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_documento, des_tipo_documento, txt_interessado, txt_assunto, nom_arquivo)
