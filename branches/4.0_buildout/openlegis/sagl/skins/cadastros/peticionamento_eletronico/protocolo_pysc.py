## Script (Python) "protocolo_pysc"
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

for peticao in context.zsql.peticao_obter_zsql(cod_peticao=cod_peticao):
    cod_peticao = peticao.cod_peticao
    tip_peticionamento = peticao.tip_peticionamento
    cod_usuario = peticao.cod_usuario
    data = DateTime().strftime('%Y-%m-%d')
    ano = DateTime().strftime('%Y')
    txt_assunto_ementa = peticao.txt_descricao.encode('utf-8')
    lst_unidade = peticao.cod_unid_tram_dest
    tip_derivado = peticao.tip_derivado
    ind_doc_adm = peticao.ind_doc_adm
    ind_norma = peticao.ind_norma
    ind_doc_materia = peticao.ind_doc_materia
    for usuario in context.zsql.usuario_obter_zsql(cod_usuario=peticao.cod_usuario):
        txt_interessado = usuario.nom_completo
        txt_user_protocolo = usuario.col_username
    if peticao.ind_doc_adm == '1':
       tip_protocolo = 0
       tip_processo = 0
       tip_documento = peticao.tip_derivado
       if peticao.cod_documento_vinculado != None:
          cod_documento_vinculado = peticao.cod_documento_vinculado
       else:
          cod_documento_vinculado = 'Nulo'
    elif peticao.ind_doc_materia == '1':
       tip_protocolo = 0
       tip_processo = 1
       tip_natureza_materia = 3
       tip_documento_acessorio = tip_derivado
       cod_materia_principal = peticao.cod_materia

    if context.sapl_documentos.props_sagl.numero_protocolo_anual == 1:
       for numero in context.zsql.protocolo_numero_obter_zsql(ano_protocolo = DateTime().strftime('%Y')):
           hdn_num_protocolo = int(numero.novo_numero)
    else:
       for numero in zsql.protocolo_codigo_obter_zsql():
           hdn_num_protocolo =  int(numero.novo_codigo)

def criar_protocolo_adm(hdn_num_protocolo, tip_protocolo, tip_processo, tip_documento, txt_assunto_ementa, txt_interessado, txt_user_protocolo, numero, ano, data):
    context.zsql.protocolo_administrativo_incluir_zsql(num_protocolo=hdn_num_protocolo, tip_protocolo=tip_protocolo, tip_processo=tip_processo, tip_documento=tip_documento, txt_assunto_ementa = txt_assunto_ementa, txt_interessado=txt_interessado, txt_user_protocolo=txt_user_protocolo)
    for codigo in context.zsql.protocolo_incluido_codigo_obter_zsql():
        cod_prot = int(codigo.cod_protocolo)

    return criar_documento(numero,ano,data,tip_documento,hdn_num_protocolo,txt_interessado,txt_assunto_ementa)

def criar_documento(numero,ano,data,tip_documento,hdn_num_protocolo,txt_interessado,txt_assunto_ementa):

    for numero_doc in context.zsql.numero_documento_administrativo_obter_zsql(tip_documento=tip_documento, ano_documento=ano):
        numero = numero_doc.novo_numero

    if cod_documento_vinculado == 'Nulo':
       ind_tramitacao = 1
    else:
       ind_tramitacao = 0

    context.zsql.documento_administrativo_incluir_zsql(num_documento=numero, ano_documento=ano, dat_documento=data, tip_documento=tip_documento, num_protocolo=hdn_num_protocolo, txt_interessado=txt_interessado, ind_tramitacao=ind_tramitacao, txt_assunto=txt_assunto_ementa, cod_assunto=tip_peticionamento)
    
    for codigo in context.zsql.documento_administrativo_incluido_codigo_obter_zsql():
        cod_documento = int(codigo.cod_documento)
        id_documento = str(cod_documento)+'_texto_integral.pdf'

    context.zsql.peticao_enviar_zsql(cod_peticao = cod_peticao, num_protocolo=hdn_num_protocolo, cod_documento=cod_documento)

    if hasattr(context.sapl_documentos.peticao, str(cod_peticao) + '.pdf'):
       context.modelo_proposicao.peticao_autuar(cod_peticao=cod_peticao)

    anexos = context.pysc.anexo_peticao_pysc(str(cod_peticao),listar=True)
    for item in anexos:
        id_anexo = string.split(item,'.')[0]
        nom_doc = 'Anexo ' + string.split(id_anexo,'_')[2]
        context.zsql.documento_acessorio_administrativo_incluir_zsql(tip_documento=tip_documento, cod_documento=int(cod_documento), nom_autor_documento=txt_interessado, dat_documento=DateTime().strftime('%Y-%m-%d %H:%M:%S'), nom_documento=nom_doc)
        for cod_acessorio in context.zsql.documento_acessorio_administrativo_incluido_codigo_obter_zsql():
            id_pdf = str(cod_acessorio.cod_documento_acessorio)+'.pdf'
            tmp_copy = context.sapl_documentos.peticao.manage_copyObjects(ids=item)
            tmp_id = context.sapl_documentos.administrativo.manage_pasteObjects(tmp_copy)[0]['new_id']
            context.sapl_documentos.administrativo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_pdf]))
            pdf = getattr(context.sapl_documentos.administrativo, id_pdf)
            pdf.manage_permission('View', roles=['Authenticated'], acquire=1)

    if cod_documento_vinculado != None and cod_documento_vinculado !='Nulo':
        context.zsql.documento_administrativo_vinculado_incluir_zsql(cod_documento_vinculante = cod_documento_vinculado, cod_documento_vinculado = cod_documento)

    if context.dbcon_logs:
       context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'peticionamento_eletronico', metodo = 'documento_administrativo_incluir_zsql', cod_registro = cod_documento, IP = context.pysc.get_ip()) 

    return tramitar_documento(cod_documento)

def tramitar_documento(cod_documento):
    for unidade in context.zsql.unidade_tramitacao_obter_zsql(ind_excluido=0):
        if 'Protocolo' == unidade.nom_unidade_join:
            cod_unid_tram_local =  int(unidade.cod_unid_tramitacao)
    cod_unid_tram_dest = int(lst_unidade)            
    for status in context.zsql.status_tramitacao_administrativo_obter_zsql(sgl_status='PRT'):
        cod_status = status.cod_status
    cod_usuario_corrente = cod_usuario
    hr_tramitacao = DateTime().strftime('%d/%m/%Y às %H:%M')
    txt_tramitacao = '<p>Protocolo nº ' + str(hdn_num_protocolo) + '/' + str(ano) + ' autuado em ' + hr_tramitacao +'</p>'
    if cod_unid_tram_local != None and cod_unid_tram_dest != None and cod_status != None:
        context.zsql.tramitacao_administrativo_incluir_zsql(cod_documento=cod_documento, dat_tramitacao=DateTime().strftime('%Y-%m-%d %H:%M'), cod_unid_tram_local=cod_unid_tram_local, cod_usuario_local=cod_usuario_corrente, cod_unid_tram_dest=cod_unid_tram_dest, dat_encaminha=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_status=cod_status, txt_tramitacao=txt_tramitacao, ind_urgencia=0, ind_ult_tramitacao=1)

    for tramitacao in context.zsql.tramitacao_administrativo_incluida_codigo_obter_zsql():
        cod_tramitacao = tramitacao.cod_tramitacao

    mensagem = 'Protocolo realizado com sucesso!'
    mensagem_obs = ''   
    redirect_url=context.portal_url()+'/mensagem_emitir?modal=1&tipo_mensagem=success&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs
    return context.relatorios.pdf_tramitacao_administrativo_preparar_pysc(hdn_cod_tramitacao=cod_tramitacao, hdn_url=redirect_url)

if ind_doc_adm == '1':

   return criar_protocolo_adm(hdn_num_protocolo, tip_protocolo, tip_processo, tip_documento, txt_assunto_ementa, txt_interessado, txt_user_protocolo, numero, ano, data)

elif ind_norma == '1':

   context.zsql.peticao_enviar_norma_zsql(cod_peticao = cod_peticao)
   mensagem = 'Protocolo realizado com sucesso!'
   mensagem_obs = '' 
   redirect_url=context.portal_url()+'/mensagem_emitir?modal=1&tipo_mensagem=success&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs
   RESPONSE.redirect(redirect_url)

elif ind_doc_materia == '1':

   context.zsql.documento_acessorio_incluir_zsql(cod_materia=cod_materia_principal, nom_documento=txt_assunto_ementa, dat_documento=DateTime().strftime('%Y-%m-%d %H:%M:%S'), nom_autor_documento=txt_interessado, tip_documento=tip_derivado)

   for codigo in context.zsql.documento_acessorio_incluido_codigo_obter_zsql():
       cod_documento_acessorio = int(codigo.cod_documento)
       id_documento = str(codigo.cod_documento)+'.pdf'
        
   context.zsql.peticao_enviar_zsql(cod_peticao = cod_peticao, cod_doc_acessorio=cod_documento_acessorio)

   if hasattr(context.sapl_documentos.peticao, str(cod_peticao) + '.pdf'):
      context.modelo_proposicao.peticao_autuar(cod_peticao=cod_peticao)

   if context.dbcon_logs:
      context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'documento_acessorio_materia', metodo = 'protocolo_pysc', cod_registro = cod_documento_acessorio, IP = context.pysc.get_ip()) 

   mensagem = 'Protocolo realizado com sucesso!'
   mensagem_obs = '' 
   redirect_url=context.portal_url()+'/mensagem_emitir?modal=1&tipo_mensagem=success&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs
   RESPONSE.redirect(redirect_url)

