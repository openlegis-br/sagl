## Script (Python) "criar_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao
##title=
##

from Products.CMFCore.utils import getToolByName

utool = getToolByName(context, 'portal_url')
portal = utool.getPortalObject()

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION


for proposicao in context.zsql.proposicao_obter_zsql(cod_proposicao=cod_proposicao, ind_mat_ou_doc='M'):
    cod_proposicao = proposicao.cod_proposicao
    des_tipo_proposicao = proposicao.des_tipo_proposicao    
    tip_materia = proposicao.tip_mat_ou_doc
    ano_materia = DateTime().strftime("%Y")
    cod_mat = proposicao.cod_mat_ou_doc
    dat_apresentacao = DateTime().strftime("%Y-%m-%d")
    txt_ementa = proposicao.txt_descricao.encode('utf-8')
    txt_observacao = proposicao.txt_observacao
    cod_autor = proposicao.cod_autor
    if proposicao.tip_mat_ou_doc == 'Projeto de Lei Complementar':
       tip_quorum = 3
       ind_complementar = 1
    else:
       tip_quorum = 1
       ind_complementar = 0
       
    for autor in context.zsql.autor_obter_zsql(cod_autor=proposicao.cod_autor):
        des_tipo_autor = autor.des_tipo_autor

    for numero in context.zsql.numero_materia_legislativa_obter_zsql(tip_id_basica_sel = proposicao.tip_mat_ou_doc,
ano_ident_basica = ano_materia, ind_excluido = 0):
        num_ident_basica = numero.novo_numero


def criar_protocolo(tip_materia, num_ident_basica, ano_materia, dat_apresentacao, txt_ementa, txt_observacao, cod_autor, tip_quorum, ind_complementar, cod_proposicao):

    if context.sapl_documentos.props_sagl.numero_protocolo_anual == 1:
       for numero in context.zsql.protocolo_numero_obter_zsql(ano_protocolo = DateTime().strftime('%Y')):
           hdn_num_protocolo = int(numero.novo_numero)
    else:
       for numero in context.zsql.protocolo_codigo_obter_zsql():
           hdn_num_protocolo =  int(numero.novo_codigo)
    txt_user = REQUEST['AUTHENTICATED_USER'].getUserName()

    try:
       context.zsql.trans_begin_zsql()    
       context.zsql.protocolo_legislativo_incluir_zsql(num_protocolo = hdn_num_protocolo, tip_protocolo = 0, tip_processo = 1, tip_materia=tip_materia, tip_natureza_materia = 1, txt_assunto_ementa = txt_ementa, cod_autor = cod_autor, txt_user_protocolo = txt_user)
       context.zsql.trans_commit_zsql()       
    except:
       context.zsql.trans_rollback_zsql()
    
    for codigo in context.zsql.protocolo_incluido_codigo_obter_zsql():
        cod_prot = int(codigo.cod_protocolo)
        id_documento = str(cod_prot)+'_protocolo.pdf'

    return criar_materia(hdn_num_protocolo, tip_materia, num_ident_basica, ano_materia, dat_apresentacao, txt_ementa, txt_observacao, cod_autor, tip_quorum, ind_complementar, cod_proposicao)



def criar_materia(hdn_num_protocolo, tip_materia, num_ident_basica, ano_materia, dat_apresentacao, txt_ementa, txt_observacao, cod_autor, tip_quorum, ind_complementar, cod_proposicao):

    try:
       context.zsql.trans_begin_zsql() 
       context.zsql.materia_incluir_zsql(tip_id_basica = tip_materia, num_ident_basica = num_ident_basica, ano_ident_basica = ano_materia, dat_apresentacao = dat_apresentacao, num_protocolo = hdn_num_protocolo, tip_apresentacao = 'E', tip_quorum = tip_quorum, ind_tramitacao = 1, ind_complementar = ind_complementar, cod_regime_tramitacao = 1, txt_ementa = txt_ementa)
       context.zsql.trans_commit_zsql()
    except:
       context.zsql.trans_rollback_zsql()

    for codigo in context.zsql.materia_incluida_codigo_obter_zsql():
        cod_materia = int(codigo.cod_materia)

    if context.dbcon_logs:
       try:
          context.zsql.trans_begin_zsql()    
          context.zsql.logs_registrar_zsql(usuario = REQUEST['AUTHENTICATED_USER'].getUserName(), data = DateTime().strftime('%Y-%m-%d %H:%M:%S'), modulo = 'materia', metodo = 'materia_incluir_zsql', cod_registro = cod_materia, IP = context.pysc.get_ip())
          context.zsql.trans_commit_zsql()
       except:
          context.zsql.trans_rollback_zsql()

    return inserir_autoria(cod_materia, cod_autor, cod_proposicao, hdn_num_protocolo)



def inserir_autoria(cod_materia, cod_autor, cod_proposicao, hdn_num_protocolo):

    if context.sapl_documentos.props_sagl.restpki_access_token != '' and des_tipo_autor == 'Parlamentar':
       for assinatura in context.zsql.assinatura_documento_obter_zsql(codigo=cod_proposicao, tipo_doc='proposicao', ind_assinado=1):
           for usuario in context.zsql.usuario_obter_zsql(cod_usuario=assinatura.cod_usuario, ind_excluido=0): 
               for autor in context.zsql.autor_obter_zsql(col_username=usuario.col_username, ind_excluido=0):
                   if int(cod_autor) == int(autor.cod_autor):
                      context.zsql.autoria_incluir_zsql(cod_autor = cod_autor, cod_materia = cod_materia, ind_primeiro_autor = 1)
                   else:
                      try:
                         context.zsql.trans_begin_zsql()
                         context.zsql.autoria_incluir_zsql(cod_autor = autor.cod_autor, cod_materia = cod_materia, ind_primeiro_autor = 0)
                         context.zsql.trans_commit_zsql()
                      except:
                         context.zsql.trans_rollback_zsql()                         
    else:
       try:
          context.zsql.trans_begin_zsql()       
          context.zsql.autoria_incluir_zsql(cod_autor = cod_autor, cod_materia = cod_materia, ind_primeiro_autor = 1)
          context.zsql.trans_commit_zsql()          
       except:
          context.zsql.trans_rollback_zsql() 
    
    return tramitar_materia(cod_materia, cod_proposicao, hdn_num_protocolo)



def tramitar_materia(cod_materia, cod_proposicao, hdn_num_protocolo):

    for unidade in context.zsql.unidade_tramitacao_obter_zsql(ind_excluido=0):
        if 'Protocolo Eletrônico' == unidade.nom_unidade_join:
            cod_unid_tram_local =  int(unidade.cod_unid_tramitacao)
        if des_tipo_proposicao == 'Requerimento' or des_tipo_proposicao == 'Indicação' or des_tipo_proposicao == 'Moção':
           if 'Assessoria Legislativa' in unidade.nom_unidade_join:
               cod_unid_tram_dest = int(unidade.cod_unid_tramitacao)
        else:
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
    txt_tramitacao = '<p>Matéria incorporada em ' + hr_tramitacao + ' - protocolo nº ' + str(hdn_num_protocolo) + '/' + DateTime().strftime("%Y") +' (enviada por meio eletrônico)</p>'    
#    hdn_url = context.portal_url() + '/cadastros/materia/materia_mostrar_proc?cod_materia=' + str(cod_materia)+ '&modal=1'   
    hdn_url = context.portal_url() + '/cadastros/recebimento_proposicao/recebimento_proposicao_index_html#incorporada'
    
    if cod_unid_tram_local != None and cod_unid_tram_dest != None and cod_status != None:
       try:        
          context.zsql.trans_begin_zsql()    
          context.zsql.tramitacao_incluir_zsql(cod_materia=cod_materia, dat_tramitacao=DateTime().strftime('%Y-%m-%d'), cod_unid_tram_local=cod_unid_tram_local, cod_usuario_local=cod_usuario_corrente, cod_unid_tram_dest=cod_unid_tram_dest, dat_encaminha=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_status=cod_status, ind_urgencia=0, txt_tramitacao = txt_tramitacao, ind_ult_tramitacao=1)
          context.zsql.trans_commit_zsql()                  
       except:
          context.zsql.trans_rollback_zsql()  
        
    for tramitacao in context.zsql.tramitacao_incluida_codigo_obter_zsql():
        cod_tramitacao = tramitacao.cod_tramitacao

    odt_proposicao = str(cod_proposicao) + '.odt'
    if hasattr(context.sapl_documentos.proposicao,odt_proposicao):
       context.pysc.proposicao_salvar_como_texto_integral_materia_pysc(cod_proposicao,cod_materia,0)

    try:        
       context.zsql.trans_begin_zsql()
       context.zsql.proposicao_registrar_recebimento_zsql(cod_proposicao = cod_proposicao, dat_recebimento = context.pysc.data_atual_iso_pysc(),cod_mat_ou_doc = int(cod_materia))
       context.zsql.trans_commit_zsql()           
    except:
       context.zsql.trans_rollback_zsql()       

    id_proposicao_signed = str(cod_proposicao)+'_signed.pdf'
    if cod_materia != None:
       if hasattr(context.sapl_documentos.proposicao,id_proposicao_signed):
          context.modelo_proposicao.proposicao_autuar(cod_proposicao=cod_proposicao)

    return context.relatorios.pdf_tramitacao_preparar_pysc(hdn_cod_tramitacao=cod_tramitacao, hdn_url=hdn_url)


if cod_mat == None:
   return criar_protocolo(tip_materia, num_ident_basica, ano_materia, dat_apresentacao, txt_ementa, txt_observacao, cod_autor, tip_quorum, ind_complementar, cod_proposicao)
else:
   mensagem = 'Proposição já convertida em matéria legislativa!'
   mensagem_obs = 'Verifique a listagem de proposições incorporadas.'   
   redirect_url=context.portal_url()+'/mensagem_emitir?tipo_mensagem=danger&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs
   RESPONSE.redirect(redirect_url)
    
