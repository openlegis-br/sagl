## Script (Python) "caixa_entrada_contar_pysc"
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
  dic_unid = {}
  dic_unid['cod_unid_tramitacao'] = int(unidade.cod_unid_tramitacao)
  dic_unid['ind_responsavel'] = int(unidade.ind_responsavel)
  unidades.append(dic_unid)

tramitacoes = []
for dic_unid in unidades:
  if dic_unid['ind_responsavel']==1:
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino=dic_unid['cod_unid_tramitacao'],ind_ult_tramitacao=1,ind_encaminha=1,ind_recebido=0,ind_retorno_tramitacao=1,ind_tramitacao=1):
      tramitacoes.append(int(tramitacao.cod_tramitacao))
  elif dic_unid['ind_responsavel']==0:
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino=dic_unid['cod_unid_tramitacao'],cod_usuario_dest=cod_usuario,ind_ult_tramitacao=1,ind_encaminha=1,ind_recebido=0,ind_retorno_tramitacao=1,ind_tramitacao=1):
      tramitacoes.append(int(tramitacao.cod_tramitacao))

tramitacoes = [
    e
    for i, e in enumerate(tramitacoes)
    if tramitacoes.index(e) == i
    ]

tramitacoes.sort()

return len(tramitacoes)
