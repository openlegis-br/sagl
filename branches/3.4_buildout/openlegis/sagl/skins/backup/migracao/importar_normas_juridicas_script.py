## Script (Python) "migracao_import_script"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = context.REQUEST
file_upload = request.get('file_upload')
file_upload_name = file_upload.filename

if not file_upload_name.endswith('.csv'):
    msg = 'Voce deve carregar um arquivo no formato CSV.'
    return request.RESPONSE.redirect('importar_normas_juridicas?portal_status_message=' + msg)

file_content = context.processCSVFile(file_upload, as_dict=1)
count = 0
fail_list = []
#return context.dbcon_interlegis.columns('norma_juridica')

for row in file_content:
  try:
    tip_norma = row.get('tip_norma', '')
    cod_materia = row.get('cod_materia', None)
    num_norma = row.get('num_norma', '')
    ano_norma = row.get('ano_norma', '')
    tip_esfera_federacao = row.get('tip_esfera_federacao', 'E')
    dat_norma = row.get('dat_norma', '2000/12/31')
    dat_publicacao = row.get('dat_publicacao', None)
    des_veiculo_publicacao = row.get('des_veiculo_publicacao', '')
    num_pag_inicio_publ = row.get('num_pag_inicio_publ', None)
    num_pag_fim_publ = row.get('num_pag_fim_publ', None)
    txt_ementa = row.get('txt_ementa', '')
    txt_indexacao = row.get('txt_indexacao', '')
    txt_observacao = row.get('txt_observacao', '')
    count += 1
 
    #context.zsql.norma_juridica_incluir_zsql(
    #    tip_norma=tip_norma,
    #    num_norma=num_norma,
    #    ano_norma=ano_norma,
    #    dat_norma=dat_norma,
    #    tip_esfera_federacao=tip_esfera_federacao,
    #    des_veiculo_publicacao=des_veiculo_publicacao, 
    #    txt_ementa=txt_ementa,
    #    txt_indexacao=txt_indexacao,
    #    txt_observacao =txt_observacao)

    #nome_antigo = 'lei.'+(4-len(str(num_norma)))*'0'+str(num_norma)+'.doc'
    #max_cod_norma = context.zsql.max_cod_norma_zsql()[0].max_cod_norma
    #nome_novo = str(max_cod_norma)+'_texto_integral'
    #context.sapl_documentos.norma_juridica.manage_renameObjects([nome_antigo],[nome_novo])
  except:
    fail_list.append(row)
  fail_list.append(row)

request.set('resultado_importacao', count)
request.set('falhou_importacao', fail_list)
request.set('tipo_importacao', 'normas jur&iacute;dicas')

msg = 'Foram importados %s registros.' % count
return context.migracao_index_html(context, request, portal_status_message=msg)

