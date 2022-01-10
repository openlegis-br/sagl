## Script (Python) "criar_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_protocolo
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

for protocolo in context.zsql.protocolo_obter_zsql(cod_protocolo=cod_protocolo):
    tip_materia = protocolo.tip_materia
    ano_materia = protocolo.ano_protocolo
    dat_apresentacao = DateTime().strftime("%Y-%m-%d")
    num_protocolo = protocolo.num_protocolo
    txt_ementa = protocolo.txt_assunto_ementa.encode('utf-8')
    txt_observacao = protocolo.txt_observacao
    cod_autor = protocolo.cod_autor

    for numero in context.zsql.numero_materia_legislativa_obter_zsql(tip_id_basica_sel = protocolo.tip_materia,
ano_ident_basica = protocolo.ano_protocolo, ind_excluido = 0):
        num_ident_basica = numero.novo_numero


def criar_materia(tip_materia, num_ident_basica, ano_materia, dat_apresentacao, num_protocolo, txt_ementa, txt_observacao, cod_autor):

    context.zsql.materia_incluir_zsql(tip_id_basica = tip_materia, num_ident_basica = num_ident_basica, ano_ident_basica = ano_materia, num_protocolo = num_protocolo, dat_apresentacao = dat_apresentacao, tip_apresentacao = 'E', tip_quorum = 1, ind_tramitacao = 1, ind_complementar = 0, cod_regime_tramitacao = 1, txt_ementa = txt_ementa, txt_observacao = txt_observacao)
    
    for codigo in context.zsql.materia_incluida_codigo_obter_zsql():
        cod_materia = int(codigo.cod_materia)
        id_materia = str(cod_materia)+'_texto_integral.pdf'
        
    id_protocolo = str(cod_protocolo)+'_protocolo.pdf'
    id_protocolo_signed = str(cod_protocolo)+'_protocolo_signed.pdf'
    
    if hasattr(context.sapl_documentos.protocolo,id_protocolo_signed):
       tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=id_protocolo_signed)
       tmp_id = context.sapl_documentos.materia.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.materia.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_materia]))
    elif hasattr(context.sapl_documentos.protocolo,id_protocolo):
       tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=id_protocolo)
       tmp_id = context.sapl_documentos.materia.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.materia.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_materia]))

    if context.dbcon_logs:
       context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'materia', metodo = 'materia_incluir_zsql', cod_registro = cod_materia, IP = context.pysc.get_ip())

    return inserir_autoria(cod_materia, cod_autor)
    

def inserir_autoria(cod_materia, cod_autor):

    context.zsql.autoria_incluir_zsql(cod_autor = cod_autor, cod_materia = cod_materia, ind_primeiro_autor = 1)
    
    return tramitar_materia(cod_materia)


def tramitar_materia(cod_materia):

    for unidade in context.zsql.unidade_tramitacao_obter_zsql(ind_excluido=0):
        if 'Protocolo' in unidade.nom_unidade_join:
            cod_unid_tram_local =  int(unidade.cod_unid_tramitacao)
        if 'Departamento Legislativo' in unidade.nom_unidade_join:
            cod_unid_tram_dest = int(unidade.cod_unid_tramitacao)
            
    for status in context.zsql.status_tramitacao_obter_zsql(sgl_status='PRT'):
        cod_status = status.cod_status
        
    for usuario in context.zsql.usuario_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        if usuario.cod_usuario:
           cod_usuario_corrente = int(usuario.cod_usuario)
        else:
           cod_usuario_corrente = 0
           
    hr_tramitacao = DateTime().strftime('%d/%m/%Y às %Hh%M')
    txt_tramitacao = '<p>Matéria incorporada em ' + hr_tramitacao + ' - proveniente do Protocolo nº ' + str(num_protocolo) + '/' + str(ano_materia)+'</p>'
    hdn_url = 'protocolo_mostrar_proc?cod_protocolo=' + cod_protocolo
    
    if cod_unid_tram_local != None and cod_unid_tram_dest != None and cod_status != None:
       context.zsql.tramitacao_incluir_zsql(cod_materia=cod_materia, dat_tramitacao=DateTime().strftime('%Y-%m-%d'), cod_unid_tram_local=cod_unid_tram_local, cod_usuario_local=cod_usuario_corrente, cod_unid_tram_dest=cod_unid_tram_dest, dat_encaminha=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_status=cod_status, ind_urgencia=0, txt_tramitacao = txt_tramitacao, ind_ult_tramitacao=1)
        
    for tramitacao in context.zsql.tramitacao_incluida_codigo_obter_zsql():
        cod_tramitacao = tramitacao.cod_tramitacao

    context.pysc.envia_tramitacao_autor_pysc(cod_materia = cod_materia)

    return context.relatorios.pdf_tramitacao_preparar_pysc(hdn_cod_tramitacao=cod_tramitacao, hdn_url=hdn_url)
  

return criar_materia(tip_materia, num_ident_basica, ano_materia, dat_apresentacao, num_protocolo, txt_ementa, txt_observacao, cod_autor)
    
    
