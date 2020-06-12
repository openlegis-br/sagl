## Script (Python) "capa_processo_adm"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento
##title=
##
REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

inf_basicas_dic = {}
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
    casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
estado = context.zsql.localidade_obter_zsql(tip_localidade="U")
for uf in estado:
    if localidade[0].sgl_uf == uf.sgl_uf:
        nom_estado = uf.nom_localidade.encode('utf-8')
        break
inf_basicas_dic['nom_camara']= casa['nom_casa'].encode('utf-8')
inf_basicas_dic["nom_estado"] = nom_estado.encode('utf-8')
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
    inf_basicas_dic['nom_localidade']= local.nom_localidade.encode('utf-8')
    inf_basicas_dic['sgl_uf']= local.sgl_uf

for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
 if documento.num_protocolo != None:
   for protocolo in context.zsql.protocolo_pesquisar_zsql(num_protocolo=documento.num_protocolo,ano_protocolo=documento.ano_documento):
     if protocolo.cod_protocolo:
        num_protocolo = str(protocolo.num_protocolo) + '/' + str(protocolo.ano_protocolo)
        dat_protocolo = context.pysc.iso_to_port_pysc(protocolo.dat_protocolo)
        hor_protocolo = protocolo.hor_protocolo[0:2]+':'+protocolo.hor_protocolo[3:5]
        inf_basicas_dic["dia_protocolo"] = context.pysc.data_converter_por_extenso_pysc(data=context.pysc.iso_to_port_pysc(protocolo.dat_protocolo))
        inf_basicas_dic["dia_semana"] = context.pysc.data_converter_dia_semana_pysc(data=context.pysc.iso_to_port_pysc(protocolo.dat_protocolo))
     else:
        num_protocolo = ''
        dat_protocolo = documento.dat_documento
        hor_protocolo = '00:00'
        inf_basicas_dic["dia_protocolo"] = context.pysc.data_converter_por_extenso_pysc(data=context.pysc.iso_to_port_pysc(documento.data_documento))
        inf_basicas_dic["dia_semana"] = context.pysc.data_converter_dia_semana_pysc(data=documento.dat_documento)
 else:
    num_protocolo = ''
    dat_protocolo = documento.dat_documento
    hor_protocolo = '00:00'
    inf_basicas_dic["dia_protocolo"] = context.pysc.data_converter_por_extenso_pysc(data=context.pysc.iso_to_port_pysc(documento.data_documento))
    inf_basicas_dic["dia_semana"] = context.pysc.data_converter_dia_semana_pysc(data=documento.dat_documento)
 dat_vencimento = " "
 if documento.dat_fim_prazo != None:
   dat_vencimento = documento.dat_fim_prazo
 num_documento = str(documento.num_documento) + '/' + str(documento.ano_documento)
 des_tipo_documento = documento.des_tipo_documento.encode('utf-8')
 txt_assunto = documento.txt_assunto.encode('utf-8')
 txt_interessado = documento.txt_interessado.encode('utf-8')
 nom_arquivo = 'capa-'+documento.sgl_tipo_documento+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+'.odt'
 nom_arquivo = nom_arquivo.encode('utf-8')

return context.capa_processo_adm_gerar_odt(inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_documento, des_tipo_documento, txt_interessado, txt_assunto, nom_arquivo)
#return inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_documento, des_tipo_documento, txt_interessado, txt_assunto, nom_arquivo
