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
    dat_apresentacao = DateTime().strftime("%Y-%m-%d")
    txt_ementa = proposicao.txt_descricao
    txt_observacao = proposicao.txt_observacao
    cod_autor = proposicao.cod_autor
    if proposicao.tip_mat_ou_doc == 'Projeto de Lei Complementar':
       tip_quorum = 3
       ind_complementar = 1
    else:
       tip_quorum = 1
       ind_complementar = 0

    for numero in context.zsql.numero_materia_legislativa_obter_zsql(tip_id_basica_sel = proposicao.tip_mat_ou_doc,
ano_ident_basica = ano_materia, ind_excluido = 0):
        num_ident_basica = numero.novo_numero


def criar_materia(tip_materia, num_ident_basica, ano_materia, dat_apresentacao, txt_ementa, txt_observacao, cod_autor, tip_quorum, ind_complementar, cod_proposicao):

    context.zsql.materia_incluir_zsql(tip_id_basica = tip_materia, num_ident_basica = num_ident_basica, ano_ident_basica = ano_materia, dat_apresentacao = dat_apresentacao, tip_apresentacao = 'E', tip_quorum = tip_quorum, ind_tramitacao = 1, ind_complementar = ind_complementar, cod_regime_tramitacao = 1, txt_ementa = txt_ementa, txt_observacao = txt_observacao)
    
    for codigo in context.zsql.materia_incluida_codigo_obter_zsql():
        cod_materia = int(codigo.cod_materia)
        id_materia = str(cod_materia)+'_texto+_integral.pdf'
        
    id_proposicao_signed = str(cod_proposicao)+'_signed.pdf'
    id_proposicao_odt = str(cod_proposicao)+'.odt'
    
    if hasattr(context.sapl_documentos.proposicao,id_proposicao_odt):
       tmp_copy = context.sapl_documentos.proposicao.manage_copyObjects(ids=id_proposicao_odt)
       tmp_id = context.sapl_documentos.materia.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.materia.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id_materia]))
       
    return inserir_autoria(cod_materia, cod_autor, cod_proposicao)
    

def inserir_autoria(cod_materia, cod_autor, cod_proposicao):
    context.zsql.autoria_incluir_zsql(cod_autor = cod_autor, cod_materia = cod_materia, ind_primeiro_autor = 1)
    
    return autuar_materia(cod_materia, cod_proposicao)


def autuar_materia(cod_materia, cod_proposicao):
    if hasattr(context.sapl_documentos.proposicao,id_proposicao_signed):
       context.modelo_proposicao.proposicao_autuar(cod_proposicao=cod_proposicao)

    return tramitar_materia(cod_materia)       

def tramitar_materia(cod_materia):

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
           
    hr_tramitacao = DateTime().strftime('%d/%m/%Y às %H:%M')
    txt_tramitacao = 'Matéria incorporada em ' + hr_tramitacao
    hdn_url = context.url() + '/cadastros/materia/materia_mostrar_proc?cod_materia=' + str(cod_materia)
#    context.portal_url() + '/cadastros/materia/materia_mostrar_proc?cod_materia=' + str(cod_materia)    

    
    if cod_unid_tram_local != None and cod_unid_tram_dest != None and cod_status != None:
       context.zsql.tramitacao_incluir_zsql(cod_materia=cod_materia, dat_tramitacao=DateTime().strftime('%Y-%m-%d'), cod_unid_tram_local=cod_unid_tram_local, cod_usuario_local=cod_usuario_corrente, cod_unid_tram_dest=cod_unid_tram_dest, dat_encaminha=DateTime().strftime('%Y-%m-%d %H:%M:%S'), cod_status=cod_status, ind_urgencia=0, txt_tramitacao = txt_tramitacao, ind_ult_tramitacao=1)
        
    for tramitacao in context.zsql.tramitacao_incluida_codigo_obter_zsql():
        cod_tramitacao = tramitacao.cod_tramitacao

    return context.relatorios.pdf_tramitacao_preparar_pysc(hdn_cod_tramitacao=cod_tramitacao, hdn_url=hdn_url)
  

return criar_materia(tip_materia, num_ident_basica, ano_materia, dat_apresentacao, txt_ementa, txt_observacao, cod_autor, tip_quorum, ind_complementar, cod_proposicao)
    
    
