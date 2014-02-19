## Script (Python)
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento="",cod_status=""
##title=
##

# atualiza indicação de documento em tramitação (sim ou não)

# obtem ind_fim_tramitacao ou ind_retorno_tramitacao
status=context.zsql.status_tramitacao_administrativo_obter_zsql(cod_status=cod_status)[0]

if status.ind_fim_tramitacao:
   context.zsql.tramitacao_administrativo_fim_processo_zsql(cod_documento=cod_documento)
   
if status.ind_retorno_tramitacao:
   context.zsql.tramitacao_administrativo_retorno_processo_zsql(cod_documento=cod_documento)

return 1
