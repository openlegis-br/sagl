## Script (Python) "parecer_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, nom_arquivo, nom_comissao, materia, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.parecer_gerar_odt(inf_basicas_dic, nom_arquivo, nom_comissao, materia, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao)
