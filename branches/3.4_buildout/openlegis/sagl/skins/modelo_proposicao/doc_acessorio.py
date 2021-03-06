## Script (Python) "doc_acessorio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento, cod_materia, modelo_proposicao
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
inf_basicas_dic['nom_camara']= casa['nom_casa']
inf_basicas_dic["nom_estado"] = nom_estado
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
    inf_basicas_dic['nom_localidade']= local.nom_localidade.encode('utf-8')
    inf_basicas_dic['sgl_uf']= local.sgl_uf

for documento in context.zsql.documento_acessorio_obter_zsql(cod_documento=cod_documento,cod_materia=cod_materia,ind_excluido=0):
 nom_arquivo = str(documento.cod_documento)+ '.odt'
 nom_documento = documento.nom_documento.encode('utf-8')
 if documento.txt_ementa != None:
  txt_ementa = documento.txt_ementa.encode('utf-8')
 else:
  txt_ementa = " "
 dat_documento = documento.dat_documento
 data_documento = context.pysc.data_converter_por_extenso_pysc(data=documento.dat_documento)
 nom_autor = documento.nom_autor_documento.encode('utf-8')
 
 for tipo_documento in context.zsql.tipo_documento_obter_zsql(tip_documento=documento.tip_documento):
  des_tipo_documento = tipo_documento.des_tipo_documento.encode('utf-8')

 for materia_vinculada in context.zsql.materia_obter_zsql(cod_materia = documento.cod_materia):
  materia_vinculada = materia_vinculada.des_tipo_materia + '  ' + str(materia_vinculada.num_ident_basica) + '/' + str(materia_vinculada.ano_ident_basica)

return context.doc_acessorio_gerar_odt(inf_basicas_dic,nom_arquivo,des_tipo_documento,nom_documento,txt_ementa,dat_documento,data_documento,nom_autor,materia_vinculada,modelo_proposicao)
