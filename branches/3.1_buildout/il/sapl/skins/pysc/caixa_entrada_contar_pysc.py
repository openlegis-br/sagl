## Script (Python) "caixa_entrada_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_usuario
##title=
##
unidades = []
for unidade in context.zsql.usuario_unid_tram_obter_zsql(cod_usuario=cod_usuario):
  cod_unid_tramitacao = int(unidade.cod_unid_tramitacao)
  unidades.append(cod_unid_tramitacao)

tramitacoes = []
for unidade in unidades:
  for tramitacao in context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino=unidade,ind_ult_tramitacao=1,ind_encaminha=1,ind_recebido=0,ind_retorno_tramitacao=1):
    tramitacoes.append(int(tramitacao.cod_tramitacao))

return len(tramitacoes)
