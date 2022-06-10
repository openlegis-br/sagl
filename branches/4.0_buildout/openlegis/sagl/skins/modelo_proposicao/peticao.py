## Script (Python) "peticao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_peticao, modelo_path
##title=
##
from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE

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

for peticao in context.zsql.peticao_obter_zsql(cod_peticao=cod_peticao):
    nom_arquivo = str(peticao.cod_peticao)+'.odt'
    inf_basicas_dic['txt_descricao'] = peticao.txt_descricao
    inf_basicas_dic['data'] = context.pysc.data_converter_por_extenso_pysc(data=DateTime().strftime("%d/%m/%Y"))
    for usuario in context.zsql.usuario_obter_zsql(cod_usuario=peticao.cod_usuario):
        inf_basicas_dic['nom_completo'] = usuario.nom_completo
        inf_basicas_dic['nom_cargo'] = usuario.nom_cargo
        inf_basicas_dic['dat_nascimento'] = usuario.dat_nascimento
        inf_basicas_dic['num_cpf'] = usuario.num_cpf
        inf_basicas_dic['num_rg'] = usuario.num_rg
        inf_basicas_dic['end_residencial'] = usuario.end_residencial
        inf_basicas_dic['num_cep_resid'] = usuario.num_cep_resid
        inf_basicas_dic['num_tel_resid'] = usuario.num_tel_resid
        inf_basicas_dic['num_tel_celular'] = usuario.num_tel_celular
        inf_basicas_dic['num_tel_comercial'] = usuario.num_tel_comercial

return st.peticao_gerar_odt(inf_basicas_dic, nom_arquivo, modelo_path)

