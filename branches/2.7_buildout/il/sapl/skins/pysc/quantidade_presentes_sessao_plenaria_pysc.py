## Script (Python) "presenca_sessao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, tip_sessao
##title=
##

quorum=None
quorum_busca = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=tip_sessao)
for i in quorum_busca:
    quorum=i.num_minimo

lista=context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen,tip_frequencia="P",ind_excluido=0)

if len(lista) >= quorum:
    return "Quórum atingido para a abertura da Sessão Plenária."
else:
    return "Quórum não atingido para a abertura da Sessão Plenária!"
