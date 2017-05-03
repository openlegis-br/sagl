## Script (Python) "registrar_recebimento_executivo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=dat_tramitacao="",cod_unid_tram_local="",cod_unid_tram_dest="",cod_status="",txt_tramitacao=""
##title=
##

for status in context.zsql.status_tramitacao_obter_zsql(sgl_status = 'EXE'):
  status_atual = status.cod_status

lista=context.zsql.tramitacao_obter_zsql(cod_unid_tram_destino=cod_unid_tram_dest,cod_status=status_atual,ind_ult_tramitacao=1,ind_excluido=0)

cod_materia=[]

for materia in lista:
    cod_materia.append(str(materia.cod_materia))

## Atualiza tramitacao anterior

cod_tramitacao=[]

for m in cod_materia:
    ult_tram = context.zsql.tramitacao_obter_zsql(cod_materia=m, ind_ult_tramitacao=1)

for tramitacao in lista:
   cod_tramitacao.append(str(tramitacao.cod_tramitacao))

for t in cod_tramitacao:
   context.zsql.tramitacao_ind_ultima_atualizar_zsql(cod_tramitacao=t, ind_ult_tramitacao=0)

for m in cod_materia:
   context.zsql.tramitacao_incluir_zsql(cod_materia=m, dat_tramitacao=dat_tramitacao, cod_unid_tram_local=cod_unid_tram_local, cod_unid_tram_dest=cod_unid_tram_dest, cod_status=cod_status, ind_urgencia=0, txt_tramitacao=txt_tramitacao, ind_ult_tramitacao=1)

for m in cod_materia:
   context.pysc.envia_tramitacao_autor_pysc(cod_materia=m)
   context.pysc.envia_acomp_materia_pysc(cod_materia=m)

return 1
