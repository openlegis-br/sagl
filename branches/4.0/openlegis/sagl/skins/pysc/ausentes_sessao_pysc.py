## Script (Python) "ausentes_sessao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, cod_num_legislatura, tipo=0
##title=
##
""" Retorna os parlamentares ausentes na sessao e na ordem do dia
"""

presenca_sessao = len(context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0))
presenca_ordem = len(context.zsql.presenca_ordem_dia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0))
parlamentares = len(context.zsql.parlamentar_obter_zsql(num_legislatura = cod_num_legislatura, ind_ativo=1, ind_excluido=0))

ausentes = 0

if tipo == 1:
    ausentes = parlamentares - presenca_sessao

if tipo == 0:
    ausentes = parlamentares - presenca_ordem

return ausentes
