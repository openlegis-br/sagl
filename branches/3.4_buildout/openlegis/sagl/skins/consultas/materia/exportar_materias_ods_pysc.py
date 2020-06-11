## Script (Python) "exportar_materias_ods_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tipo_materia, txt_numero, txt_ano, rad_tramitando, txt_assunto, lst_status, hdn_cod_autor, txt_num_protocolo, dt_apres, dt_apres2, dt_public, dt_public2, lst_localizacao, rd_ordenacao
##title=
##
REQUEST  = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session  = REQUEST.SESSION

from Products.CMFCore.utils import getToolByName

materias = []
for item in context.zsql.materia_pesquisar_zsql(
                                               tip_id_basica=REQUEST['tipo_materia'],
                                               num_ident_basica=REQUEST['txt_numero'],
                                               ano_ident_basica=REQUEST['txt_ano'],
                                               ind_tramitacao=REQUEST['rad_tramitando'],
                                               des_assunto=REQUEST['txt_assunto'],
                                               cod_status=REQUEST['lst_status'],
                                               cod_autor=REQUEST['hdn_cod_autor'],
                                               num_protocolo=REQUEST['txt_num_protocolo'],
                                               dat_apresentacao=REQUEST['dt_apres'],
                                               dat_apresentacao2=REQUEST['dt_apres2'],
                                               dat_publicacao=REQUEST['dt_public'],
                                               dat_publicacao2=REQUEST['dt_public2'],
                                               cod_unid_tramitacao=REQUEST['lst_localizacao'],
                                               rd_ordem=REQUEST['rd_ordenacao']
                                               ):

    materia = {}
    materia['tipo_materia'] = item.des_tipo_materia
    materia['numero_materia'] = item.num_ident_basica
    materia['ano_materia'] = item.ano_ident_basica
    materia['ementa_materia'] = item.txt_ementa
    materia['data_materia'] = context.pysc.iso_to_port_pysc(item.dat_apresentacao)

    materia["nom_autor"] = ""
    autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
    fields = autores.data_dictionary().keys()
    lista_autor = []
    for autor in autores:
        for field in fields:
            nome_autor = autor['nom_autor_join']
        lista_autor.append(nome_autor)
    materia["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])

    materia['localizacao_atual']= ""
    materia['des_situacao'] = ""
    materia['ultima_acao'] = ""
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=item.cod_materia,ind_ult_tramitacao=1):
        if tramitacao.cod_unid_tram_dest:
            cod_unid_tram = tramitacao.cod_unid_tram_dest
        else:
            cod_unid_tram = tramitacao.cod_unid_tram_local      
        for unidade_tramitacao in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao=cod_unid_tram):
            if unidade_tramitacao.cod_orgao:
                materia['localizacao_atual']=unidade_tramitacao.nom_orgao
            else:
                materia['localizacao_atual']=unidade_tramitacao.nom_comissao
        materia['des_situacao'] = tramitacao.des_status
        materia['ultima_acao'] = tramitacao.txt_tramitacao

    materias.append(materia)

st = getToolByName(context, 'portal_sagl')
return st.materias_exportar(materias)
