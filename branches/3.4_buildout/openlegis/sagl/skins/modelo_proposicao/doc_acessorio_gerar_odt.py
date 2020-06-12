## Script (Python) "doc_acessorio_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic,nom_arquivo,des_tipo_documento,nom_documento,txt_ementa,dat_documento,data_documento,nom_autor,materia_vinculada,modelo_proposicao
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.doc_acessorio_gerar_odt(inf_basicas_dic,nom_arquivo,des_tipo_documento,nom_documento,txt_ementa,dat_documento,data_documento,nom_autor,materia_vinculada,modelo_proposicao)
