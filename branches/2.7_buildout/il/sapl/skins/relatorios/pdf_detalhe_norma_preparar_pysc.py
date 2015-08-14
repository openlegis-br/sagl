import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

cabecalho={}

#tenta buscar o logotipo da casa LOGO_CASA
if hasattr(context.sapl_documentos.props_sapl,'logo_casa.gif'):
  imagem = context.sapl_documentos.props_sapl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao_transp.gif"

#abaixo é gerado o dic do rodapé da página
casa={}
aux=context.sapl_documentos.props_sapl.propertyItems()
for item in aux:
  casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
data_emissao= DateTime().strftime("%d/%m/%Y")
rodape= casa 
rodape['data_emissao']= data_emissao

estados=context.zsql.localidade_obter_zsql(tip_localidade="u")
for uf in estados:
 if localidade[0].sgl_uf==uf.sgl_uf:
  nom_estado=uf.nom_localidade
  break
inf_basicas_dic = {}
inf_basicas_dic['nom_camara']= casa['nom_casa']
inf_basicas_dic["nom_estado"]="Estado de "+nom_estado
REQUEST=context.REQUEST
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
  rodape['nom_localidade']= "   "+local.nom_localidade
  rodape['sgl_uf']= local.sgl_uf

for norma in context.zsql.norma_juridica_obter_zsql(cod_norma=REQUEST['cod_norma']):
#Abaixo é gerado os dados para o bloco das informações básicas da norma
 inf_basicas_dic['titulo']= norma.des_tipo_norma.upper()+" N° "+str(norma.num_norma)+" DE "+str(norma.dat_norma)
 inf_basicas_dic['txt_ementa']=norma.txt_ementa
 inf_basicas_dic['dat_norma']= norma.dat_norma
 inf_basicas_dic['dat_publicacao']= norma.dat_publicacao
 inf_basicas_dic['veiculo_publicacao']= norma.des_veiculo_publicacao
 inf_basicas_dic['indexacao']= norma.txt_indexacao
 inf_basicas_dic['observacao']= norma.txt_observacao
 inf_basicas_dic['situacao_norma']= " "
 if norma.cod_situacao!=None:
   for situacao_norma in context.zsql.tipo_situacao_norma_obter_zsql(ind_excluido=0, tip_situacao_norma=norma.cod_situacao):
     inf_basicas_dic['situacao_norma']= situacao_norma.des_tipo_situacao
 inf_basicas_dic['materia_vinculada']=" "
 if norma.cod_materia!=None:
  for materia_vinculada in context.zsql.materia_obter_zsql(cod_materia=str(norma.cod_materia)):
      nom_autor = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=materia_vinculada.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      nom_autor = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      inf_basicas_dic['materia_vinculada'] = materia_vinculada.des_tipo_materia+"  n°  "+str(materia_vinculada.num_ident_basica)+"/"+str(materia_vinculada.ano_ident_basica)+" - Autoria: "+ str(nom_autor)


# assuntos
 lst_assuntos = []
 assuntos = norma.cod_assunto_sel.split(",")
 for assunto in assuntos:
   assuntos_dic = {}
   assuntos_dic['assunto']= ' '
   for des_assunto in context.zsql.assunto_norma_juridica_obter_zsql(cod_assunto = assunto):
     assuntos_dic = {}
     assuntos_dic['assunto']= des_assunto[2]
     lst_assuntos.append(assuntos_dic)

#o bloco abaixo gera o dicionario de vinculos ativos
 lst_vinculos_ativos = []
 for norma_vinculada in context.zsql.vinculo_norma_juridica_referidas_obter_zsql(cod_norma=norma.cod_norma):
  vinculos_ativos_dic = {}
  vinculos_ativos_dic['norma']= str(norma_vinculada.des_tipo_norma) +" n° "+ str(norma_vinculada.num_norma)+ " de " + norma_vinculada.dat_norma
  if norma_vinculada.tip_vinculo=='R':
      vinculos_ativos_dic['vinculo'] = 'Revogação'
  elif norma_vinculada.tip_vinculo=='A':
      vinculos_ativos_dic['vinculo'] = 'Alteração'
  elif norma_vinculada.tip_vinculo=='S':
     vinculos_ativos_dic['vinculo'] = 'Ineficácia'
  elif norma_vinculada.tip_vinculo=='P':
      vinculos_ativos_dic['vinculo'] = 'Revogação parcial'
  elif norma_vinculada.tip_vinculo=='C':
      vinculos_ativos_dic['vinculo'] = 'Norma Correlata'
  elif norma_vinculada.tip_vinculo=='G':
      vinculos_ativos_dic['vinculo'] = 'Regulamentação'
  elif norma_vinculada.tip_vinculo=='I':
      vinculos_ativos_dic['vinculo'] = 'Suspensão de Execução'
  else:
      vinculos_ativos_dic['vinculo']= norma_vinculada.tip_vinculo
  lst_vinculos_ativos.append(vinculos_ativos_dic)
  

#o bloco abaixo gera o dicionario de vinculos passivos
 lst_vinculos_passivos = []
 for norma_vinculada in context.zsql.vinculo_norma_juridica_referentes_obter_zsql(cod_norma=norma.cod_norma):
  vinculos_passivos_dic = {}
  vinculos_passivos_dic['norma']= str(norma_vinculada.des_tipo_norma) +" n° "+ str(norma_vinculada.num_norma)+ " de " + norma_vinculada.dat_norma
  if norma_vinculada.tip_vinculo=='R':
      vinculos_passivos_dic['vinculo'] = 'Revogação'
  elif norma_vinculada.tip_vinculo=='A':
      vinculos_passivos_dic['vinculo'] = 'Alteração'
  elif norma_vinculada.tip_vinculo=='S':
      vinculos_passivos_dic['vinculo'] = 'Ineficácia'
  elif norma_vinculada.tip_vinculo=='P':
      vinculos_passivos_dic['vinculo'] = 'Revogação parcial'
  elif norma_vinculada.tip_vinculo=='C':
      vinculos_passivos_dic['vinculo'] = 'Norma Correlata'
  elif norma_vinculada.tip_vinculo=='G':
      vinculos_passivos_dic['vinculo'] = 'Regulamentação'
  elif norma_vinculada.tip_vinculo=='I':
      vinculos_passivos_dic['vinculo'] = 'Suspensão de Execução'
  else:
      vinculos_passivos_dic['vinculo']= norma_vinculada.tip_vinculo
  lst_vinculos_passivos.append(vinculos_passivos_dic)
 
caminho=context.pdf_detalhe_norma_gerar(imagem,rodape,inf_basicas_dic,lst_assuntos,lst_vinculos_ativos,lst_vinculos_passivos,sessao=session.id)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)

