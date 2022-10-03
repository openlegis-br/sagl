## Script (Python) "incorporar_norma"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_peticao
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE

for peticao in context.zsql.peticao_obter_zsql(cod_peticao=cod_peticao, ind_norma=1, ind_enviado = 1, ind_excluido=0):
    cod_peticao = peticao.cod_peticao
    cod_usuario = peticao.cod_usuario
    tip_norma = peticao.tip_derivado
    num_norma = peticao.num_norma
    ano_norma = peticao.ano_norma
    dat_norma = peticao.data_norma
    txt_ementa = peticao.txt_descricao.encode('utf-8')
    if peticao.cod_materia != None:
       cod_materia = peticao.cod_materia
    else:
       cod_materia = ''
    if peticao.des_tipo_peticionamento == 'Lei Complementar':
       ind_complemento = 1
    else:
       ind_complemento = 0
    cod_situacao = 1
    for usuario in context.zsql.usuario_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        cod_usuario = usuario.cod_usuario
    nom_pdf_assinado = ''
    for validacao in context.zsql.assinatura_documento_obter_zsql(tipo_doc='peticao', codigo=cod_peticao, ind_assinado=1):
        nom_pdf_assinado = str(validacao.cod_assinatura_doc) + ".pdf"

    context.zsql.norma_juridica_incluir_zsql(tip_norma=tip_norma, num_norma=num_norma, ano_norma=ano_norma, tip_esfera_federacao='M', cod_materia=cod_materia, dat_norma=dat_norma, txt_ementa=txt_ementa, ind_complemento=ind_complemento, cod_situacao=cod_situacao)

    for codigo in context.zsql.norma_juridica_incluida_codigo_obter_zsql():
        cod_norma = codigo.cod_norma
        id_odt = str(cod_norma)+'_texto_integral.odt'
        id_pdf = str(cod_norma)+'_texto_integral.pdf'

    context.zsql.peticao_incorporar_norma_zsql(cod_peticao = cod_peticao, cod_norma=cod_norma)

    if nom_pdf_assinado != '':
       if hasattr(context.sapl_documentos.documentos_assinados,nom_pdf_assinado):
          context.modelo_proposicao.peticao_autuar(cod_peticao=cod_peticao)
    else:
       if hasattr(context.sapl_documentos.peticao, str(cod_peticao) + '.pdf'):
          tmp_copy = context.sapl_documentos.peticao.manage_copyObjects(ids=str(cod_peticao) + '.pdf')
          tmp_id = context.sapl_documentos.norma_juridica.manage_pasteObjects(tmp_copy)[0]['new_id']
          context.sapl_documentos.norma_juridica.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_pdf]))
          pdf = getattr(context.sapl_documentos.norma_juridica, id_pdf)
          pdf.manage_permission('View', roles=['Anonymous'], acquire=1)
          context.sapl_documentos.norma_juridica.Catalog.atualizarCatalogo(cod_norma=cod_norma)

    if hasattr(context.sapl_documentos.peticao, str(cod_peticao) + '.odt'):
       tmp_copy = context.sapl_documentos.peticao.manage_copyObjects(ids=str(cod_peticao) + '.odt')
       tmp_id = context.sapl_documentos.norma_juridica.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.norma_juridica.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_odt]))
       odt = getattr(context.sapl_documentos.norma_juridica, id_odt)
       odt.manage_permission('View', roles=['Anonymous'], acquire=1)

    if context.dbcon_logs:
       context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'norma_juridica', metodo = 'incorporar_norma.pysc', cod_registro = cod_norma, IP = context.pysc.get_ip()) 
   
    hdn_url = context.portal_url()+'/cadastros/norma_juridica/norma_juridica_mostrar_proc?cod_norma=' + str(cod_norma)
    mensagem = 'Norma incorporada com sucesso!'
    mensagem_obs = '' 
    redirect_url=context.portal_url()+'/mensagem_emitir?tipo_mensagem=success&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs + '&url=' + hdn_url
    RESPONSE.redirect(redirect_url)

