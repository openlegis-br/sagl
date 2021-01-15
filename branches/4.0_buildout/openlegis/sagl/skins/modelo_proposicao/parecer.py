## Script (Python) "parecer"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_relatoria, cod_materia, cod_comissao
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

for relatoria in context.zsql.relatoria_obter_zsql(cod_relatoria=cod_relatoria, cod_materia=cod_materia, cod_comissao=cod_comissao, ind_excluido=0):
 nom_arquivo = str(relatoria.cod_relatoria)+ '_parecer.odt'
 tip_apresentacao = ""
 if relatoria.tip_apresentacao == 'O':
  tip_apresentacao = 'Verbal'
 else:
    tip_apresentacao = ""
 tip_conclusao = ""
 if relatoria.tip_conclusao == 'F':
    tip_conclusao = 'Favoravel'
 elif relatoria.tip_conclusao == 'C':
    tip_conclusao = 'Contrario'
 data_designacao = relatoria.dat_desig_relator
 data_parecer = relatoria.dat_destit_relator
 tip_resultado = ""
 if relatoria.tip_fim_relatoria != None:
   for resultado in context.zsql.tipo_fim_relatoria_obter_zsql(tip_fim_relatoria = relatoria.tip_fim_relatoria):
    tip_resultado = resultado.des_fim_relatoria
 else:
   tip_resultado = ""
 nom_comissao = ""
 for comissao in context.zsql.comissao_obter_zsql(cod_comissao=relatoria.cod_comissao):
  nom_comissao = comissao.nom_comissao
 nom_relator = ""
 for relator in context.zsql.parlamentar_obter_zsql(cod_parlamentar=relatoria.cod_parlamentar):
  nom_relator = relator.nom_completo

 for periodo in context.zsql.periodo_comp_comissao_obter_zsql(data=DateTime(relatoria.dat_desig_relator),cod_comissao=relatoria.cod_comissao):
  cod_periodo = periodo.cod_periodo_comp

 nom_presidente_comissao = ""
 lst_composicao = []
 for composicao_comissao in context.zsql.composicao_comissao_obter_zsql(cod_comissao=relatoria.cod_comissao,cod_periodo_comp=periodo.cod_periodo_comp):
  if composicao_comissao.des_cargo == 'Presidente':
     nom_presidente_comissao = composicao_comissao.nom_completo
     inf_basicas_dic['nom_presidente_comissao'] = nom_presidente_comissao
  dic_composicao = {}
  if composicao_comissao.nom_completo != nom_relator and composicao_comissao.nom_completo != nom_presidente_comissao:
     dic_composicao["nom_completo"] = composicao_comissao.nom_completo
     lst_composicao.append(dic_composicao)

 for materia_vinculada in context.zsql.materia_obter_zsql(cod_materia = relatoria.cod_materia):
  materia = materia_vinculada.des_tipo_materia.decode('utf-8').upper() + ' Nº ' + str(materia_vinculada.num_ident_basica) + '/' + str(materia_vinculada.ano_ident_basica)
  txt_ementa = materia_vinculada.txt_ementa

  nom_autor = ""
  autores = context.zsql.autoria_obter_zsql(cod_materia=relatoria.cod_materia)
  fields = autores.data_dictionary().keys()
  lista_autor = []
  for autor in autores:
    for field in fields:
       nom_autor = autor['nom_autor_join']
  lista_autor.append(nom_autor)
  nom_autor  = ', '.join(['%s' % (value) for (value) in lista_autor]) 

return st.parecer_gerar_odt(inf_basicas_dic,nom_arquivo,nom_comissao, materia, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao)
