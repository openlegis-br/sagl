## Script (Python) "oficio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento, modelo_documento
##title=
##

from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

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
        nom_estado = uf.nom_localidade
        break
inf_basicas_dic['nom_camara']= casa['nom_casa']
inf_basicas_dic["nom_estado"] = nom_estado
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
    inf_basicas_dic['nom_localidade']= local.nom_localidade
    inf_basicas_dic['sgl_uf']= local.sgl_uf

for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento,ind_excluido=0):
    nom_arquivo = str(documento.cod_documento)+'_texto_integral.odt'
    sgl_tipo_documento = documento.sgl_tipo_documento
    num_documento = documento.num_documento
    ano_documento = documento.ano_documento
    txt_ementa = documento.txt_assunto
    dat_documento = documento.dat_documento
    dia_documento = context.pysc.data_converter_por_extenso_pysc(data=documento.dat_documento)
    nom_autor = documento.txt_interessado

return st.oficio_gerar_odt(inf_basicas_dic, nom_arquivo, sgl_tipo_documento, num_documento, ano_documento, txt_ementa, dat_documento, dia_documento, nom_autor, modelo_documento)
