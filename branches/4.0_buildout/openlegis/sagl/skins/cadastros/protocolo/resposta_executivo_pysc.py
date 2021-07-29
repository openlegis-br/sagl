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
        id_materia = 'Responde - ' + materia.des_tipo_materia + ' nº ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica) +' - '+ autoria        

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
    for usuario in context.zsql.usuario_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        if usuario.cod_usuario:
           login_usuario = usuario.col_username

    autor = ''
    for autor in context.zsql.autor_obter_zsql(col_username=REQUEST['AUTHENTICATED_USER'].getUserName()):
        autor = autor.cod_autor

    for tipo_doc in context.zsql.tipo_documento_obter_zsql(ind_excluido=0):
        if 'Resposta' == tipo_doc.des_tipo_documento:
            tip_doc = int(tipo_doc.tip_documento)
        else:
            tip_doc = 11         

    context.zsql.protocolo_legislativo_incluir_zsql(num_protocolo=numero_protocolo(), tip_protocolo=0, tip_processo=1, tip_natureza_materia=3, tip_materia = tip_doc, cod_materia_principal = cod_materia_respondida, txt_assunto_ementa = obter_materia(cod_materia_respondida), cod_autor=autor, txt_user_protocolo=login_usuario, txt_observacao=context.pysc.get_ip())
    
    for codigo in context.zsql.protocolo_incluido_codigo_obter_zsql():
        cod_protocolo = int(codigo.cod_protocolo)
        id_documento = str(cod_protocolo)+'_protocolo.pdf'

    for protocolo in context.zsql.protocolo_obter_zsql(cod_protocolo=cod_protocolo):      
        num_protocolo = str(protocolo.num_protocolo) +'/'+ str(protocolo.ano_protocolo)
        context.sapl_documentos.protocolo.manage_addFile(id=id_documento,file=REQUEST.form['file'])

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

