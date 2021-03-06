## Script (Python) "protocolo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

lst_assunto = REQUEST.form['lst_assunto']
lst_unidade = REQUEST.form['lst_cod_unid_tram_dest']

txa_txt_assunto = REQUEST.form['txa_txt_assunto']
if context.sapl_documentos.props_sagl.numero_protocolo_anual == 1:
    for numero in context.zsql.protocolo_numero_obter_zsql(ano_protocolo = DateTime().strftime('%Y')):
        hdn_num_protocolo = int(numero.novo_numero)
else:
    for numero in zsql.protocolo_codigo_obter_zsql():
        hdn_num_protocolo =  int(numero.novo_codigo)
tip_protocolo = 0
for tipo_doc in context.zsql.tipo_documento_administrativo_obter_zsql(ind_excluido=0):
    if 'Requerimento Diverso' == tipo_doc.des_tipo_documento:
        tip_documento = tipo_doc.tip_documento
tip_processo = 0
txt_assunto_ementa = lst_assunto + ' - ' + txa_txt_assunto
txt_interessado =  REQUEST.form['txa_txt_interessado']
txt_user_protocolo = 'Protocolo Eletrônico'

ano = DateTime().strftime('%Y')
data = DateTime().strftime('%Y-%m-%d')
for numero_doc in context.zsql.numero_documento_administrativo_obter_zsql(tip_documento=tip_documento,ano_documento=ano):
    numero = numero_doc.novo_numero

def criar_protocolo(hdn_num_protocolo,tip_protocolo,tip_processo,tip_documento,txt_assunto_ementa,txt_interessado,txt_user_protocolo,numero,ano,data):
    context.zsql.protocolo_administrativo_incluir_zsql(num_protocolo=hdn_num_protocolo,tip_protocolo=tip_protocolo,tip_processo=tip_processo,tip_documento=tip_documento,txt_assunto_ementa = txt_assunto_ementa,txt_interessado=txt_interessado,txt_user_protocolo=txt_user_protocolo)
    for codigo in context.zsql.protocolo_incluido_codigo_obter_zsql():
        cod_prot = int(codigo.cod_protocolo)
        id_documento = str(cod_prot)+'_protocolo.pdf'

    return criar_documento(numero,ano,data,tip_documento,hdn_num_protocolo,txt_interessado,txt_assunto_ementa)

def criar_documento(numero,ano,data,tip_documento,hdn_num_protocolo,txt_interessado,txt_assunto_ementa):
    context.zsql.documento_administrativo_incluir_zsql(num_documento=numero,ano_documento=ano,dat_documento=data,tip_documento=tip_documento,num_protocolo=hdn_num_protocolo,txt_interessado=txt_interessado,ind_tramitacao=1,txt_assunto=txt_assunto_ementa)
    for codigo in context.zsql.documento_administrativo_incluido_codigo_obter_zsql():
        cod_documento = int(codigo.cod_documento)
        id_documento = str(cod_documento)+'_texto_integral.pdf'

    if REQUEST.form['codigo']:
       hdn_codigo =  REQUEST.form['codigo']
       peticao = str(hdn_codigo)+'.pdf'
       peticao_signed = str(hdn_codigo)+'_signed.pdf'

       if hasattr(context.sapl_documentos.administrativo,peticao_signed):
          tmp_copy = context.sapl_documentos.administrativo.manage_copyObjects(ids=peticao_signed)
          tmp_id = context.sapl_documentos.administrativo.manage_pasteObjects(tmp_copy)[0]['new_id']
          context.sapl_documentos.administrativo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_documento]))
          context.sapl_documentos.administrativo.manage_delObjects(ids=peticao_signed)
       elif hasattr(context.sapl_documentos.administrativo,peticao):
          tmp_copy = context.sapl_documentos.administrativo.manage_copyObjects(ids=peticao)
          tmp_id = context.sapl_documentos.administrativo.manage_pasteObjects(tmp_copy)[0]['new_id']
          context.sapl_documentos.administrativo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_documento]))
          context.sapl_documentos.administrativo.manage_delObjects(ids=peticao)

    return tramitar_documento(cod_documento)

def tramitar_documento(cod_documento):
    for unidade in context.zsql.unidade_tramitacao_obter_zsql(ind_excluido=0):
        if 'Protocolo' == unidade.nom_unidade_join:
            cod_unid_tram_local =  int(unidade.cod_unid_tramitacao)
#        if REQUEST.form['lst_assunto'] == 'Adiantamento de 13º salário' or REQUEST.form['lst_assunto'] == 'Licença-prêmio' or REQUEST.form['lst_assunto'] == 'Férias':
#           if 'Recursos Humanos' == unidade.nom_unidade_join:
#              cod_unid_tram_dest = int(unidade.cod_unid_tramitacao)
#        else:
#           if 'Diretor Geral' == unidade.nom_unidade_join:
#              cod_unid_tram_dest = int(unidade.cod_unid_tramitacao)
    cod_unid_tram_dest = int(lst_unidade)            
    for status in context.zsql.status_tramitacao_administrativo_obter_zsql(sgl_status='PRT'):
        cod_status = status.cod_status
    for usuario in context.zsql.usuario_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        if usuario.cod_usuario:
           cod_usuario_corrente = int(usuario.cod_usuario)
        else:
           cod_usuario_corrente = 0
    if cod_unid_tram_local != None and cod_unid_tram_dest != None and cod_status != None:
        context.zsql.tramitacao_administrativo_incluir_zsql(cod_documento=cod_documento,dat_tramitacao=DateTime().strftime('%Y-%m-%d'),cod_unid_tram_local=cod_unid_tram_local,cod_usuario_local=cod_usuario_corrente,cod_unid_tram_dest=cod_unid_tram_dest,dat_encaminha=DateTime().strftime('%Y-%m-%d %H:%M:%S'),cod_status=cod_status,ind_urgencia=0,ind_ult_tramitacao=1)

    mensagem = 'Petição protocolada com sucesso!'
    mensagem_obs = ''   
    redirect_url=context.portal_url()+'/mensagem_emitir?modal=1&tipo_mensagem=success&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs
    RESPONSE.redirect(redirect_url)
  

return criar_protocolo(hdn_num_protocolo,tip_protocolo,tip_processo,tip_documento,txt_assunto_ementa,txt_interessado,txt_user_protocolo,numero,ano,data)

