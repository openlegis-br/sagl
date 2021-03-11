## Script (Python) "tramitacao_lote_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=check_tram, txt_dat_tramitacao, unidade_local, hdn_cod_usuario_local, lst_cod_unid_tram_dest, lst_cod_usuario_dest, lst_cod_status, rad_ind_urgencia, txa_txt_tramitacao, txt_dat_fim_prazo
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

v=str(check_tram)
if v.isdigit():
   cod_materia = [check_tram]
else:
   cod_materia = check_tram

lst_ultimas=[]
for item in cod_materia:
    dic_ultimas = {}
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=item, ind_ult_tramitacao=1, ind_excluido=0):
        dic_ultimas['cod_materia'] = tramitacao.cod_materia
        dic_ultimas['cod_tramitacao'] = tramitacao.cod_tramitacao    
        lst_ultimas.append(dic_ultimas)

hdn_dat_encaminha = DateTime().strftime('%Y-%m-%d %H:%M:%S')

if lst_ultimas != []:
   for dic in lst_ultimas:
       context.zsql.tramitacao_ind_ultima_atualizar_zsql(cod_materia = dic['cod_materia'], cod_tramitacao = dic['cod_tramitacao'], ind_ult_tramitacao = 0)
       context.zsql.tramitacao_registrar_recebimento_zsql(cod_tramitacao = dic['cod_tramitacao'], cod_usuario_corrente = hdn_cod_usuario_local)    

if txt_dat_fim_prazo==None or txt_dat_fim_prazo=='':
   data_atual = DateTime()
   for tramitacao in context.zsql.status_tramitacao_obter_zsql(cod_status=lst_cod_status, ind_excluido=0):
       if tramitacao.num_dias_prazo != None:
          data_calculada = data_atual + str(tramitacao.num_dias_prazo)
          txt_dat_fim_prazo = DateTime(data_calculada).strftime('%Y/%m/%d')
       else:
          txt_dat_fim_prazo = ''
elif txt_dat_fim_prazo != '':
   txt_dat_fim_prazo = DateTime(txt_dat_fim_prazo).strftime('%Y/%m/%d')

for item in cod_materia:
    context.zsql.tramitacao_incluir_zsql(cod_materia = item, dat_tramitacao = context.pysc.data_converter_pysc(data=txt_dat_tramitacao), cod_unid_tram_local = unidade_local, cod_usuario_local = hdn_cod_usuario_local, cod_unid_tram_dest = lst_cod_unid_tram_dest, cod_usuario_dest = lst_cod_usuario_dest, dat_encaminha = hdn_dat_encaminha, cod_status = lst_cod_status, ind_urgencia = rad_ind_urgencia, txt_tramitacao = txa_txt_tramitacao, dat_fim_prazo = txt_dat_fim_prazo, ind_ult_tramitacao = 1)

lst_novas = []
for item in cod_materia:
    dic_novas = {}
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=item, ind_ult_tramitacao=1, ind_excluido=0):
        dic_novas['cod_materia'] = tramitacao.cod_materia
        dic_novas['cod_tramitacao'] = tramitacao.cod_tramitacao
        lst_novas.append(dic_novas)

for dic in lst_novas:
    context.pysc.atualiza_indicador_tramitacao_materia_pysc(cod_materia = dic['cod_materia'], cod_status = lst_cod_status)
    context.pysc.envia_tramitacao_autor_pysc(cod_materia = dic['cod_materia'])
    context.pysc.envia_acomp_materia_pysc(cod_materia = dic['cod_materia'])         
    hdn_url = 'tramitacao_mostrar_proc?hdn_cod_tramitacao=' + str(dic['cod_tramitacao'])+ '&hdn_cod_materia=' + str(dic['cod_materia'])+'&lote=1'
    context.relatorios.pdf_tramitacao_preparar_pysc(hdn_cod_tramitacao = dic['cod_tramitacao'], hdn_url = hdn_url)

