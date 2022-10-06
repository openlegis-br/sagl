## Script (Python) "capa_processo_adm"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento
##title=
##

from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

capa_dic = {}
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
    casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
estado = context.zsql.localidade_obter_zsql(tip_localidade="U")
for uf in estado:
    if localidade[0].sgl_uf == uf.sgl_uf:
        nom_estado = uf.nom_localidade
        break
capa_dic['nom_camara']= casa['nom_casa']
capa_dic["nom_estado"] = nom_estado
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
    capa_dic['nom_localidade']= local.nom_localidade
    capa_dic['sgl_uf']= local.sgl_uf

for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
 if documento.num_protocolo != None:
   for protocolo in context.zsql.protocolo_pesquisar_zsql(num_protocolo=documento.num_protocolo,ano_protocolo=documento.ano_documento):
     if protocolo.cod_protocolo:
        capa_dic['num_protocolo'] = str(protocolo.num_protocolo) + '/' + str(protocolo.ano_protocolo)
        capa_dic['dat_protocolo'] = context.pysc.iso_to_port_pysc(protocolo.dat_protocolo)
        capa_dic['hor_protocolo'] = protocolo.hor_protocolo[0:2]+':'+protocolo.hor_protocolo[3:5]
        capa_dic["dia_protocolo"] = context.pysc.data_converter_por_extenso_pysc(data=context.pysc.iso_to_port_pysc(protocolo.dat_protocolo))
        capa_dic["dia_semana"] = context.pysc.data_converter_dia_semana_pysc(data=context.pysc.iso_to_port_pysc(protocolo.dat_protocolo))
     else:
        capa_dic['num_protocolo'] = ""
        capa_dic['dat_protocolo'] = documento.dat_documento
        capa_dic['hor_protocolo'] = ''
        capa_dic["dia_protocolo"] = context.pysc.data_converter_por_extenso_pysc(data=context.pysc.iso_to_port_pysc(documento.data_documento))
        capa_dic["dia_semana"] = context.pysc.data_converter_dia_semana_pysc(data=documento.dat_documento)
 else:
    capa_dic['num_protocolo'] = ""
    capa_dic['dat_protocolo'] = documento.dat_documento
    capa_dic['hor_protocolo'] = ''
    capa_dic["dia_protocolo"] = context.pysc.data_converter_por_extenso_pysc(data=context.pysc.iso_to_port_pysc(documento.data_documento))
    capa_dic["dia_semana"] = context.pysc.data_converter_dia_semana_pysc(data=documento.dat_documento)
 capa_dic['dat_vencimento'] = ""
 if documento.dat_fim_prazo != None:
   capa_dic['dat_vencimento'] = documento.dat_fim_prazo
 capa_dic['num_documento'] = str(documento.num_documento) + '/' + str(documento.ano_documento)
 capa_dic['des_tipo_documento'] = documento.des_tipo_documento
 capa_dic['txt_assunto'] = documento.txt_assunto
 capa_dic['txt_interessado'] = documento.txt_interessado
 capa_dic['observacoes'] = documento.txt_observacao

 capa_dic['acessorios'] = ''
 lst_acessorios = []
 for acessorio in context.zsql.documento_acessorio_administrativo_obter_zsql(cod_documento=documento.cod_documento, ind_excluido=0):
     dic_acessorio = {}
     dic_acessorio['id_acessorio'] = acessorio.nom_documento
     lst_acessorios.append(dic_acessorio)
 if len(lst_acessorios) > 0:
    capa_dic['acessorios'] = lst_acessorios
 
 capa_dic['vinculados'] = ''
 lst_vinculados = []
 for vinculado in context.zsql.documento_administrativo_vinculado_obter_zsql(cod_documento_vinculado=documento.cod_documento,  ind_excluido=0):
     dic_vinculo = {}
     dic_vinculado['id_documento'] = vinculado.sgl_tipo_documento_vinculante + 'nº ' + str(dic_vinculo.num_documento_vinculante) + '/' + str(ano_documento_vinculante)
     lst_vinculados.append(dic_vinculo)
 for vinculante in context.zsql.documento_administrativo_vinculado_obter_zsql(cod_documento_vinculante=documento.cod_documento,  ind_excluido=0):
     dic_vinculo = {}
     dic_vinculo['id_documento'] = vinculado.sgl_tipo_documento_vinculado + 'nº ' + str(vinculado.num_documento_vinculado) + '/' + str(ano_documento_vinculado)
     lst_vinculados.append(dic_vinculo)
 if len(lst_vinculados) > 0:
    capa_dic['vinculados'] = lst_vinculados

 capa_dic['materias_vinculadas'] = ''

 capa_dic['situacao'] = None
 for tramitacao in context.zsql.tramitacao_administrativo_obter_zsql(cod_documento=documento.cod_documento, ind_ult_tramitacao=1, ind_excluido=0):
     for unidade in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao=int(tramitacao.cod_unid_tram_dest)):
         unidade_atual = unidade.nom_unidade_join
     capa_dic['situacao'] = 'Último Local: ' + tramitacao.dat_tramitacao + ' - ' + unidade_atual + ' - ' + tramitacao.des_status

 capa_dic['nom_arquivo_odt'] = 'capa-'+documento.sgl_tipo_documento.encode('utf-8')+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+'.odt'
 capa_dic['nom_arquivo_pdf'] = 'capa-'+documento.sgl_tipo_documento.encode('utf-8')+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+'.pdf'

return st.capa_processo_adm_gerar_odt(capa_dic)
