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
dic = {}
for unidade in context.zsql.usuario_unid_tram_obter_zsql(cod_usuario=cod_usuario):
  dic["cod_unid_tramitacao"]  = int(unidade.cod_unid_tramitacao)
  dic["ind_responsavel"] = int(unidade.ind_responsavel)
  unidades.append(dic)

tramitacoes = []
for unidade in unidades:
  if dic["ind_responsavel"] == 1:
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino= dic["cod_unid_tramitacao"],ind_ult_tramitacao=1,ind_encaminha=1,ind_recebido=0,ind_retorno_tramitacao=1,ind_tramitacao=1):
      tramitacoes.append(int(tramitacao.cod_tramitacao))
  else:
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino= dic["cod_unid_tramitacao"],cod_usuario_dest=cod_usuario,ind_ult_tramitacao=1,ind_encaminha=1,ind_recebido=0,ind_retorno_tramitacao=1,ind_tramitacao=1):
      tramitacoes.append(int(tramitacao.cod_tramitacao))

tramitacoes = [
    e
    for i, e in enumerate(tramitacoes)
    if tramitacoes.index(e) == i
    ]

tramitacoes.sort()

return len(tramitacoes)
