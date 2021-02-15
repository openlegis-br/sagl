## Script (Python) "caixa_entrada_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_usuario, cod_unidade
##title=
##

ind_responsavel = ''
for unidade in context.zsql.usuario_unid_tram_obter_zsql(cod_usuario=cod_usuario, cod_unid_tramitacao=cod_unidade):
  ind_responsavel = unidade.ind_responsavel

tramitacoes = []

if ind_responsavel==1:
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino=unidade.cod_unid_tramitacao,ind_ult_tramitacao=1,ind_encaminha=1,ind_recebido=0,ind_retorno_tramitacao=1,ind_tramitacao=1):
      tramitacoes.append(int(tramitacao.cod_tramitacao))
elif ind_responsavel==0:
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino=unidade.cod_unid_tramitacao,cod_usuario_dest=cod_usuario,ind_ult_tramitacao=1,ind_encaminha=1,ind_recebido=0,ind_retorno_tramitacao=1,ind_tramitacao=1):
      tramitacoes.append(int(tramitacao.cod_tramitacao))

tramitacoes = [
    e
    for i, e in enumerate(tramitacoes)
    if tramitacoes.index(e) == i
    ]

return tramitacoes
