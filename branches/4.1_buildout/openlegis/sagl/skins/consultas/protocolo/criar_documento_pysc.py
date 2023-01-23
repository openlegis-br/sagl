## Script (Python) "criar_documento_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_protocolo, lst_cod_unid_tram_dest
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

for protocolo in context.zsql.protocolo_obter_zsql(cod_protocolo=cod_protocolo):
    tip_documento = protocolo.tip_documento
    ano_documento = protocolo.ano_protocolo
    dat_documento = DateTime().strftime("%Y-%m-%d")
    num_protocolo = protocolo.num_protocolo
    txt_assunto = protocolo.txt_assunto_ementa.encode('utf-8')
    txt_observacao = protocolo.txt_observacao
    txt_interessado = protocolo.txt_interessado.encode('utf-8')

    for numero in context.zsql.numero_documento_administrativo_obter_zsql(tip_documento = protocolo.tip_documento,
ano_documento = protocolo.ano_protocolo):
        num_documento = numero.novo_numero


def criar_documento(tip_documento, num_documento, ano_documento, dat_documento, num_protocolo, txt_assunto, txt_observacao, txt_interessado):

    context.zsql.documento_administrativo_incluir_zsql(tip_documento = tip_documento, num_documento = num_documento, ano_documento = ano_documento, num_protocolo = num_protocolo, dat_documento = dat_documento, ind_tramitacao = 1, txt_assunto = txt_assunto, txt_observacao = txt_observacao, txt_interessado=txt_interessado )
    
    for codigo in context.zsql.documento_administrativo_incluido_codigo_obter_zsql():
        cod_documento = int(codigo.cod_documento)
        id_documento = str(cod_documento)+'_texto_integral.pdf'
        
    id_protocolo = str(cod_protocolo)+'_protocolo.pdf'
    id_protocolo_signed = str(cod_protocolo)+'_protocolo_signed.pdf'
    
    tipo_doc = context.zsql.tipo_documento_administrativo_obter_zsql(tip_documento=tip_documento)[0]

    if hasattr(context.sapl_documentos.protocolo,id_protocolo_signed):
       tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=id_protocolo_signed)
       tmp_id = context.sapl_documentos.administrativo.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.administrativo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_documento]))
       documento = getattr(context.sapl_documentos.administrativo,id_documento)
       if tipo_doc.ind_publico == 0:
          documento.manage_permission('View', roles=['Authenticated', 'Manager'], acquire=0)
       elif tipo_doc.ind_publico == 1:
          documento.manage_permission('View', roles=['Anonymous','Manager'], acquire=1)
    elif hasattr(context.sapl_documentos.protocolo,id_protocolo):
       tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=id_protocolo)
       tmp_id = context.sapl_documentos.administrativo.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.administrativo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_documento]))
       documento = getattr(context.sapl_documentos.administrativo,id_documento)
       if tipo_doc.ind_publico == 0:
          documento.manage_permission('View', roles=['Authenticated', 'Manager'], acquire=0)
       elif tipo_doc.ind_publico == 1:
          documento.manage_permission('View', roles=['Anonymous','Manager'], acquire=1)

    if context.dbcon_logs:
       context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'documento_administrativo', metodo = 'documento_administrativo_incluir_zsql', cod_registro = cod_documento, IP = context.pysc.get_ip()) 

    return tramitar_documento(cod_documento, num_protocolo, ano_documento) 


def tramitar_documento(cod_documento, num_protocolo, ano_documento):

    for unidade in context.zsql.unidade_tramitacao_obter_zsql(ind_excluido=0):
        if 'Protocolo' == unidade.nom_unidade_join:
            cod_unid_tram_local =  int(unidade.cod_unid_tramitacao)
    
    cod_unid_tram_dest = int(lst_cod_unid_tram_dest)
            
    for status in context.zsql.status_tramitacao_administrativo_obter_zsql(sgl_status='PRT'):
        cod_status = status.cod_status
        
    for usuario in context.zsql.usuario_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        if usuario.cod_usuario:
           cod_usuario_corrente = int(usuario.cod_usuario)
        else:
           cod_usuario_corrente = 0
           
    hr_tramitacao = DateTime().strftime('%d/%m/%Y às %H:%M')
    txt_tramitacao = '<p>Protocolo nº ' + str(num_protocolo) + '/' + str(ano_documento) + ' autuado em ' + hr_tramitacao +'</p>'
    hdn_url = 'protocolo_mostrar_proc?cod_protocolo=' + cod_protocolo
    
    if cod_unid_tram_local != None and cod_unid_tram_dest != None and cod_status != None:
       context.zsql.tramitacao_administrativo_incluir_zsql(cod_documento=cod_documento, dat_tramitacao=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_unid_tram_local=cod_unid_tram_local, cod_usuario_local=cod_usuario_corrente, cod_unid_tram_dest=cod_unid_tram_dest, dat_encaminha=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_status=cod_status, txt_tramitacao = txt_tramitacao, ind_ult_tramitacao=1)
        
    for tramitacao in context.zsql.tramitacao_administrativo_incluida_codigo_obter_zsql():
        cod_tramitacao = tramitacao.cod_tramitacao

    return context.relatorios.pdf_tramitacao_administrativo_preparar_pysc(hdn_cod_tramitacao=cod_tramitacao, hdn_url=hdn_url)

  

return criar_documento(tip_documento, num_documento, ano_documento, dat_documento, num_protocolo, txt_assunto, txt_observacao, txt_interessado)
    
    
