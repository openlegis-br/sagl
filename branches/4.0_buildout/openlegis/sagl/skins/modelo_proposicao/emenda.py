## Script (Python) "emenda"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_emenda, modelo_proposicao
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

inf_basicas_dic['url_validacao'] = "" + context.generico.absolute_url()+"/proposicao_validar"

for emenda in context.zsql.emenda_obter_zsql(cod_emenda=cod_emenda):
 num_proposicao = " "
 des_tipo_materia = emenda.des_tipo_emenda
 num_ident_basica = emenda.num_emenda
 ano_ident_basica = DateTime().strftime("%Y")
 txt_ementa = emenda.txt_ementa.encode('utf-8')
 dat_apresentacao = context.pysc.data_converter_por_extenso_pysc(data=emenda.dat_apresentacao)

 for materia_vinculada in context.zsql.materia_obter_zsql(cod_materia = emenda.cod_materia):
  materia_vinculada = ' - ' +materia_vinculada.des_tipo_materia.upper().encode('utf-8') + '  ' + str(materia_vinculada.num_ident_basica) + '/' + str(materia_vinculada.ano_ident_basica)
  nom_arquivo = str(emenda.cod_emenda)+ '_emenda.odt'

 nom_autor = []
 apelido_autor = " "
 for autoria in context.zsql.autoria_emenda_obter_zsql(cod_emenda = emenda.cod_emenda):
     autor_dic = {}
     autor_dic['nome_autor'] = autoria.nom_autor_join
     nom_autor.append(autor_dic)     

return context.emenda_gerar_odt(inf_basicas_dic,num_proposicao,nom_arquivo,des_tipo_materia,num_ident_basica,ano_ident_basica,txt_ementa,materia_vinculada,dat_apresentacao,nom_autor,apelido_autor,modelo_proposicao)
