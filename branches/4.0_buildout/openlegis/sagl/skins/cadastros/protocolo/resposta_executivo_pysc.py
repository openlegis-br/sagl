## Script (Python) "resposta_executivo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia_respondida
##title=
##
import simplejson as json

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

usuario = REQUEST['AUTHENTICATED_USER'].getUserName()


def obter_materia(cod_materia_respondida):
    for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia_respondida):
        for autor in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia, ind_excluido=0):
            autoria = autor.nom_autor_join    
        id_materia = 'Resposta - ' + materia.sgl_tipo_materia + ' ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica) +' - '+ autoria        

    return id_materia.encode('utf-8')

def numero_protocolo():
    if context.sapl_documentos.props_sagl.numero_protocolo_anual == 1:
       for numero in context.zsql.protocolo_numero_obter_zsql(ano_protocolo = DateTime().strftime('%Y')):
           hdn_num_protocolo = int(numero.novo_numero)
    else:
       for numero in zsql.protocolo_codigo_obter_zsql():
           hdn_num_protocolo =  int(numero.novo_codigo)

    return hdn_num_protocolo


def criar_protocolo(cod_materia_respondida):
    login_usuario = ''
    cod_usuario = ''
    for usuario in context.zsql.usuario_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        if usuario.cod_usuario:
           login_usuario = usuario.col_username
           cod_usuario = usuario.cod_usuario

    autor = ''
    nome_autor = ''
    for autor in context.zsql.autor_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        autor = autor.cod_autor
        nome_autor = autor.nom_autor_join

    for tipo_doc in context.zsql.tipo_documento_obter_zsql(ind_excluido=0):
        if 'Ofício / Resposta' == tipo_doc.des_tipo_documento:
            tip_doc = int(tipo_doc.tip_documento)
        else:
            tip_doc = 9         

    txt_ementa = obter_materia(cod_materia_respondida)

    context.zsql.protocolo_legislativo_incluir_zsql(num_protocolo=numero_protocolo(), tip_protocolo=0, tip_processo=1, tip_natureza_materia=3, tip_materia = tip_doc, cod_materia_principal = cod_materia_respondida, txt_assunto_ementa = txt_ementa, cod_autor=autor, txt_user_protocolo=login_usuario, txt_observacao=context.pysc.get_ip())
    
    for codigo in context.zsql.protocolo_incluido_codigo_obter_zsql():
        cod_protocolo = int(codigo.cod_protocolo)
        id_documento = str(cod_protocolo)+'_protocolo.pdf'

    for protocolo in context.zsql.protocolo_obter_zsql(cod_protocolo=cod_protocolo):      
        num_protocolo = str(protocolo.num_protocolo) +'/'+ str(protocolo.ano_protocolo)
        #context.sapl_documentos.protocolo.manage_addFile(id=id_documento,file=REQUEST.form['file'])

    return criar_documento(tip_doc, txt_ementa, nome_autor, cod_materia_respondida, cod_protocolo, num_protocolo, cod_usuario)


def criar_documento(tip_doc, txt_ementa, nom_autor, cod_materia_respondida, cod_protocolo, num_protocolo, cod_usuario):

    context.zsql.documento_acessorio_incluir_zsql(tip_documento = tip_doc, nom_documento = txt_ementa, nom_autor_documento = nome_autor, cod_materia = cod_materia_respondida, num_protocolo = num_protocolo, dat_documento = DateTime().strftime('%d/%m/%Y %H:%M:%S'), ind_publico=1)
    
    for codigo in context.zsql.documento_acessorio_incluido_codigo_obter_zsql():
        cod_documento = int(codigo.cod_documento)
        id_documento = str(cod_documento)+'.pdf'

    for documento in context.zsql.documento_acessorio_obter_zsql(cod_documento=cod_documento):
        context.sapl_documentos.materia.manage_addFile(id=id_documento,file=REQUEST.form['file'])

    if context.dbcon_logs:
       context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'documento_acessorio_materia', metodo = 'resposta_executivo_pysc', cod_registro = cod_documento, IP = context.pysc.get_ip())

    return tramitar_materia(cod_documento, cod_materia, cod_protocolo, num_protocolo, cod_usuario)


def tramitar_materia(cod_documento, cod_materia, cod_protocolo, num_protocolo, cod_usuario):

    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=cod_materia, ind_ult_tramitacao=1, ind_excluido=0):
        context.zsql.tramitacao_ind_ultima_atualizar_zsql(cod_materia = cod_materia, cod_tramitacao = tramitacao.cod_tramitacao, ind_ult_tramitacao = 0)    
        context.zsql.tramitacao_registrar_recebimento_zsql(cod_tramitacao = tramitacao.cod_tramitacao, cod_usuario_corrente = cod_usuario)
        context.pysc.atualiza_indicador_tramitacao_materia_pysc(cod_materia = tramitacao.cod_materia, cod_status = 1056)  

    hr_tramitacao = DateTime().strftime('%d/%m/%Y %H:%M:%S')
    txt_tramitacao = '<p>Resposta eletrônica recebida em ' + hr_tramitacao + ' sob protocolo nº ' + str(hdn_num_protocolo) + '/' + DateTime().strftime("%Y") +'</p>'
    context.zsql.tramitacao_incluir_zsql(cod_materia=cod_materia, dat_tramitacao=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_unid_tram_local=4, cod_usuario_local=cod_usuario, cod_unid_tram_dest=19, dat_encaminha=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_status=1056, ind_urgencia=0, txt_tramitacao = txt_tramitacao, ind_ult_tramitacao=1)

    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=cod_materia, ind_ult_tramitacao=1, ind_excluido=0):
        context.pysc.envia_tramitacao_autor_pysc(cod_materia = materia.cod_materia)
        context.pysc.envia_acomp_materia_pysc(cod_materia = materia.cod_materia)  
        hdn_url = context.portal_url() + ''
        context.relatorios.pdf_tramitacao_preparar_pysc(hdn_cod_tramitacao = tramitacao.cod_tramitacao, hdn_url = hdn_url)

    if context.dbcon_logs:
       context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'tramitacao_materia', metodo = 'resposta_executivo_pysc', cod_registro = item, IP = context.pysc.get_ip())

    return criar_reposta(cod_protocolo, num_protocolo)


def criar_reposta(cod_protocolo, num_protocolo):
    resposta = []
    dic_resposta = {}
    dic_resposta['status'] = 'SUCESSO'
    dic_resposta['usuario'] = usuario
    dic_resposta['numero_protocolo'] = str(num_protocolo)
    dic_resposta['codigo'] = str(cod_protocolo)
    dic_resposta['data_protocolo'] = DateTime().strftime('%d/%m/%Y %H:%M:%S')
    dic_resposta['ip_origem'] = context.pysc.get_ip()
    resposta.append(dic_resposta)
    retorno =  json.dumps(resposta)   
    return json.loads(retorno)

return criar_protocolo(cod_materia_respondida)
