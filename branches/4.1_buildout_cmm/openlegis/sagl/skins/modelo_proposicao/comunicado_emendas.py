## Script (Python) "comunicado_emendas"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia, modelo_comunicado
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

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
    dic_materia = {}
    dic_materia['dat_apresentacao'] = materia.dat_apresentacao
    dic_materia['dados_basicos'] = materia.des_tipo_materia + ' nº ' + str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
    dic_materia['txt_ementa'] = materia.txt_ementa
    autorias = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
    fields = autorias.data_dictionary().keys()
    nom_autor = []
    nome_autor = ''
    for autoria in autorias:
       autores = context.zsql.autor_obter_zsql(cod_autor = autoria.cod_autor)
       for autor in autores:
   	for field in fields:
                if autor.cod_parlamentar != None:
                   parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
                   for parlamentar in parlamentares:
                       nom_parlamentar = " - " + parlamentar.nom_parlamentar
                       if parlamentar.sgl_partido !=None:
                          partido_autor = parlamentar.sgl_partido
                       else:
                          partido_autor = "Sem partido"
                       if parlamentar.sex_parlamentar =='M':
                          cargo = "Vereador"
                       elif parlamentar.sex_parlamentar =='F':
                          cargo = "Vereadora"
                   dic_materia['txt_autoria'] = cargo + ' ' + parlamentar.nom_parlamentar + ' (' + partido_autor + ')'
                  
                else:
                   dic_materia['txt_autoria'] = autor.nom_autor_join
                if autor.des_tipo_autor == 'Parlamentar':
                   dic_materia['tip_autor'] = 'de Vereador'
                elif autor.des_tipo_autor == 'Mesa Diretora':
                   dic_materia['tip_autor'] = 'da Mesa da Câmara'
                elif autor.des_tipo_autor == 'Comissao':
                   dic_materia['tip_autor'] = 'de Comissão'
                elif autor.des_tipo_autor == 'Poder Executivo':
                   dic_materia['tip_autor'] = 'do Prefeito Municipal'

lst_vereadores=[]
for vereador in context.zsql.autores_obter_zsql(txt_dat_apresentacao = materia.dat_apresentacao):
 dic_vereadores = {}
 parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = vereador.cod_parlamentar)
 for parlamentar in parlamentares:
   if parlamentar.sgl_partido !=None:
     partido_autor = parlamentar.sgl_partido
   else:
     partido_autor = "Sem partido"
   if parlamentar.sex_parlamentar =='M':
     cargo = "Vereador"
   elif parlamentar.sex_parlamentar =='F':
     cargo = "Vereadora"
   dic_vereadores['nom_parlamentar'] = cargo + ' ' + parlamentar.nom_parlamentar + ' (' + partido_autor + ')'
 lst_vereadores.append(dic_vereadores)

# Presidente
nom_presidente = ''
data = context.pysc.data_converter_pysc(materia.dat_apresentacao)
for sleg in context.zsql.periodo_comp_mesa_obter_zsql(data=data):
  for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
    for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
      nom_presidente = presidencia.nom_completo


return st.comunicado_emendas_gerar_odt(inf_basicas_dic, dic_materia, lst_vereadores, nom_presidente, modelo_comunicado)

