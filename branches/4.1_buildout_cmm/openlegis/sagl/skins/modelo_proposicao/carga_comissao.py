## Script (Python) "carga_comissao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia,num_ordem
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

for despacho in context.zsql.despacho_inicial_obter_zsql(cod_materia=cod_materia,num_ordem=num_ordem):
    dic_materia = {}
    materia = context.zsql.materia_obter_zsql(cod_materia=despacho.cod_materia)[0]
    dic_materia['dados_basicos'] = materia.des_tipo_materia + ' nº ' + str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
    dic_materia['txt_ementa'] = materia.txt_ementa
    autorias = context.zsql.autoria_obter_zsql(cod_materia=cod_materia)
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
                   nome_autor = parlamentar.nom_parlamentar 
                else:
                   dic_materia['txt_autoria'] = autor.nom_autor_join
                   nome_autor = autor.nom_autor_join
    comissao = context.zsql.comissao_obter_zsql(cod_comissao=despacho.cod_comissao_sel)[0]
    nom_comissao = comissao.nom_comissao.upper()
    for periodo in context.zsql.periodo_comp_comissao_obter_zsql(data=DateTime(materia.dat_apresentacao, datefmt='international').strftime('%Y-%m-%d'), cod_comissao=comissao.cod_comissao):
      cod_periodo = periodo.cod_periodo_comp

lst_suplentes = []

for suplente in context.zsql.composicao_comissao_obter_zsql(cod_comissao=comissao.cod_comissao,cod_periodo_comp=cod_periodo, ind_titular=0):
  dic_suplente = {}
  dic_suplente['nom_parlamentar'] = suplente.nom_parlamentar
  lst_suplentes.append(dic_suplente)

for item in context.zsql.composicao_comissao_obter_zsql(cod_comissao=comissao.cod_comissao,cod_periodo_comp=cod_periodo, ind_titular=1):

  if str(item['des_cargo']) == 'Presidente':
    if str(item['nom_parlamentar']) != str(nome_autor):
      presidente = item['nom_parlamentar']
      suplente_presidente = ''
    else:
      for suplente in lst_suplentes[0:1]:
        presidente = ''
        suplente_presidente = suplente['nom_parlamentar']

  elif item['des_cargo'] == 'Vice-Presidente':
    if str(item['nom_parlamentar']) != str(nome_autor):
      vicepresidente = item['nom_parlamentar']
      suplente_vicepresidente = ''
    else:
      for suplente in lst_suplentes[1:2]:
        vicepresidente = ''
        suplente_vicepresidente = suplente['nom_parlamentar']

  elif item['des_cargo'] == 'Membro':
    if item['nom_parlamentar'] != nome_autor:
      membro = item['nom_parlamentar']
      suplente_membro = ''
    else:
      for suplente in lst_suplentes[2:3]:
        membro = ''
        suplente_membro = suplente['nom_parlamentar']
 
if suplente_presidente != '':
  suplente = suplente_presidente
elif suplente_vicepresidente != '':
  suplente = suplente_vicepresidente
elif suplente_membro != '':
  suplente = suplente_membro
else:
  suplente = ''

return st.carga_comissao_gerar(inf_basicas_dic, dic_materia, nom_comissao, presidente, vicepresidente, membro, suplente)

