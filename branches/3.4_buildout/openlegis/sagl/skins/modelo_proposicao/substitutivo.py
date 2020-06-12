## Script (Python) "substitutivo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_substitutivo, modelo_proposicao
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

for substitutivo in context.zsql.substitutivo_obter_zsql(cod_substitutivo=cod_substitutivo):
 num_proposicao = " "
 des_tipo_materia = 'SUBSTITUTIVO'
 num_ident_basica = substitutivo.num_substitutivo
 ano_ident_basica = DateTime().strftime("%Y")
 txt_ementa = substitutivo.txt_ementa.encode('utf-8')
 dat_apresentacao = context.pysc.data_converter_por_extenso_pysc(data=substitutivo.dat_apresentacao)

 for materia_vinculada in context.zsql.materia_obter_zsql(cod_materia = substitutivo.cod_materia):
  materia_vinculada = ' - ' +materia_vinculada.des_tipo_materia.upper().encode('utf-8') + '  ' + str(materia_vinculada.num_ident_basica) + '/' + str(materia_vinculada.ano_ident_basica)
  nom_arquivo = str(substitutivo.num_substitutivo) + '_substitutivo.odt'

 for autor in context.zsql.autor_obter_zsql(cod_autor = substitutivo.cod_autor):
  nom_autor = " "
  apelido_autor = " "
  if autor.des_tipo_autor=='Parlamentar':
   for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar):
    nom_autor = parlamentar.nom_completo.encode('utf-8')
    if parlamentar.nom_parlamentar != parlamentar.nom_completo:
     apelido_autor = "'"+parlamentar.nom_parlamentar.encode('utf-8')+"'"
    else:
     apelido_autor = " "
  elif autor.des_tipo_autor=='Comissao':
   for comissao in context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao):
    nom_autor = comissao.nom_comissao.encode('utf-8')
    apelido_autor = " "
  elif autor.des_tipo_autor=='Bancada':
   for bancada in context.zsql.bancada_obter_zsql(cod_bancada=autor.cod_bancada):
    nom_autor = bancada.nom_bancada.encode('utf-8')
    apelido_autor = " "
  else:
   nom_autor=autor.nom_autor
   apelido_autor = " "

return context.substitutivo_gerar_odt(inf_basicas_dic,num_proposicao,nom_arquivo,des_tipo_materia,num_ident_basica,ano_ident_basica,txt_ementa,materia_vinculada,dat_apresentacao,nom_autor,apelido_autor,modelo_proposicao)
