## Script (Python) "resumo_gerar_odt"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.resumo_gerar_odt(inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario)
