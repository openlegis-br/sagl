import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

cabecalho={}

# tenta buscar o logotipo da casa LOGO_CASA
if hasattr(context.sapl_documentos.props_sapl,'logo_casa.gif'):
  imagem = context.sapl_documentos.props_sapl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao_transp.gif"

#Abaixo é gerado o dic do rodapé da página
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


cod_materia = REQUEST['cod_materia']

if cod_materia.isdigit():
 cod_materia = cod_materia
else:
 cod_materia = context.pysc.b64decode_pysc(codigo=str(cod_materia))

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
#Abaixo é gerado os dados para o bloco Informações Básicas
 if context.portal_membership.isAnonymousUser() and materia.sgl_tipo_materia=='PDL' and materia.txt_indexacao == "TÍTULO" and materia.ano_ident_basica>=2014:
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=materia.cod_materia):
      if len(tramitacao) > 0 and (tramitacao.sgl_status=='APROVADA' or tramitacao.sgl_status=='LEI CAMARA'):
        inf_basicas_dic['texto_projeto']= "CONCEDE TÍTULO HONORÍFICO"
      else:
        inf_basicas_dic['texto_projeto']= materia.txt_ementa
 else:
    inf_basicas_dic['texto_projeto']= materia.txt_ementa 
 inf_basicas_dic['apresentada']= materia.dat_apresentacao
 inf_basicas_dic['formato']= materia.tip_apresentacao
 inf_basicas_dic['publicada']= materia.dat_publicacao
 inf_basicas_dic['objeto']= materia.des_objeto
 inf_basicas_dic['tramitacao']= materia.ind_tramitacao
 inf_basicas_dic['cod_projeto']= materia.des_tipo_materia.decode('utf-8').upper()+" N° "+ str(materia.num_ident_basica)+"/"+ str(materia.ano_ident_basica)
 
 for tramitacao in context.zsql.regime_tramitacao_obter_zsql(cod_regime_tramitacao=materia.cod_regime_tramitacao):
  inf_basicas_dic['reg_tramitacao']= tramitacao.des_regime_tramitacao
  inf_basicas_dic['prazo']= materia.num_dias_prazo
  inf_basicas_dic['fim_prazo']= materia.dat_fim_prazo
  inf_basicas_dic['mat_complementar']= materia.ind_complementar
  inf_basicas_dic['polemica']= materia.ind_polemica
  inf_basicas_dic['apelido']= materia.nom_apelido
  inf_basicas_dic['indexacao']= materia.txt_indexacao
  inf_basicas_dic['observacao']= materia.txt_observacao

 
#o bloco abaixo gera o dicionario da origem externa
 orig_externa_dic = {}
 for origem in context.zsql.origem_obter_zsql(cod_origem = materia.cod_local_origem_externa):
  aux = context.zsql.tipo_materia_legislativa_obter_zsql(tip_materia = materia.tip_origem_externa)
  orig_externa_dic['local']= origem.nom_origem
  orig_externa_dic['tipo']= aux[0].des_tipo_materia
  orig_externa_dic['data']= materia.dat_origem_externa
  orig_externa_dic['numero_ano']= str(materia.num_origem_externa)+ "/"+ str(materia.ano_origem_externa)

 
#o bloco abaixo gera o dicionario das materias anexadas
 lst_mat_anexadas = []
 dic_mat = {}
 for anexada in context.zsql.anexada_obter_zsql(cod_materia_principal=materia.cod_materia):
  aux1 = context.zsql.materia_obter_zsql(cod_materia = anexada.cod_materia_anexada)
  aux2 = context.zsql.tipo_materia_legislativa_obter_zsql(tip_materia = aux1[0].tip_id_basica)
  dic_mat['nom_mat']= aux2[0].sgl_tipo_materia+ "/"+ str(aux1[0].num_ident_basica)+ "/"+ str(aux1[0].ano_ident_basica)
  dic_mat['data']= anexada.dat_anexacao 
  dic_mat['data_fim']= anexada.dat_desanexacao
  lst_mat_anexadas.append(dic_mat)
 
#o bloco abaixo gera o dicionario dos autores
 lst_autoria = []

 for autoria in context.zsql.autoria_obter_zsql(cod_materia = materia.cod_materia):
  dic_autor = {}
  if autoria.ind_primeiro_autor: 
   dic_autor['tipo']= "1° Autor"
  else:
   dic_autor['tipo']= "Co-autor"
  
  for autor in context.zsql.autor_obter_zsql(cod_autor = autoria.cod_autor):
   dic_autor['cargo']= " "
   if autor.des_tipo_autor=='Parlamentar':
    for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar):
     dic_autor['nom_autor']=parlamentar.nom_parlamentar
   elif autor.des_tipo_autor=='Comissao':
    for comissao in context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao):
     dic_autor['nom_autor']=comissao.nom_comissao
   elif autor.des_tipo_autor=='Bancada':
    for bancada in context.zsql.bancada_obter_zsql(cod_bancada=autor.cod_bancada):
     dic_autor['nom_autor']=bancada.nom_bancada
   else:
    dic_autor['nom_autor']=autor.nom_autor
    dic_autor['cargo']= autor.des_cargo
  lst_autoria.append(dic_autor)

#o bloco abaixo gera o dicionario de despachos iniciais
 lst_des_iniciais=[]
 for despacho in context.zsql.despacho_inicial_obter_zsql(cod_materia = materia.cod_materia):
  for comissao in context.zsql.comissao_obter_zsql(cod_comissao = despacho.cod_comissao_sel):
   dic_dados={}
   if comissao.nom_comissao==None: 
     comissao.nom_comissao=''
   if comissao.sgl_comissao==None: 
     comissao.sgl_comissao='' 
   dic_dados['nom_comissao']=comissao.nom_comissao+ " - "+ comissao.sgl_comissao
   lst_des_iniciais.append(dic_dados)
 
#o bloco abaixo gera o dicionário de Tramitacoes
 lst_tramitacoes = []
 for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=cod_materia):
   dic_tramitacoes = {}
   dic_tramitacoes['data']= tramitacao.dat_tramitacao
   dic_tramitacoes['data_enc']= tramitacao.dat_encaminha
   dic_tramitacoes['turno']= tramitacao.sgl_turno
   dic_tramitacoes['status']= tramitacao.des_status
   dic_tramitacoes['urgente']= tramitacao.ind_urgencia
   dic_tramitacoes['data_fim']= tramitacao.dat_fim_prazo 
   dic_tramitacoes['texto_acao']= tramitacao.txt_tramitacao  
   for unidade in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = tramitacao.cod_unid_tram_local):
     if unidade.cod_orgao==None:
       for comissao in context.zsql.comissao_obter_zsql(cod_comissao = unidade.cod_comissao):
        if tramitacao.cod_unid_tram_dest!=None:
         for unidade_dest in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = tramitacao.cod_unid_tram_dest): 
            if unidade_dest.cod_orgao==None:
              for comissao_dest in context.zsql.comissao_obter_zsql(cod_comissao = unidade_dest.cod_comissao):
                dic_tramitacoes['unidade']= comissao.nom_comissao
                dic_tramitacoes['destino']= comissao_dest.nom_comissao
            if unidade_dest.cod_comissao==None:
              for orgao_dest in context.zsql.orgao_obter_zsql(cod_orgao = unidade_dest.cod_orgao):
                dic_tramitacoes['unidade']= comissao.nom_comissao
                dic_tramitacoes['destino']= orgao_dest.nom_orgao
        else:
         dic_tramitacoes['unidade']= comissao.nom_comissao
         dic_tramitacoes['destino']= "None"
     if unidade.cod_comissao==None:
       for orgao in context.zsql.orgao_obter_zsql(cod_orgao = unidade.cod_orgao):
        if tramitacao.cod_unid_tram_dest!=None:
         for unidade_dest in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = tramitacao.cod_unid_tram_dest):
            if unidade_dest.cod_orgao==None:
              for comissao_dest in context.zsql.comissao_obter_zsql(cod_comissao = unidade_dest.cod_comissao):
                dic_tramitacoes['unidade']= orgao.nom_orgao
                dic_tramitacoes['destino']= comissao_dest.nom_comissao
            if unidade_dest.cod_comissao==None:
               for orgao_dest in context.zsql.orgao_obter_zsql(cod_orgao = unidade_dest.cod_orgao):
                dic_tramitacoes['unidade']= orgao.nom_orgao
                dic_tramitacoes['destino']= orgao_dest.nom_orgao  
        else:
         dic_tramitacoes['unidade']= orgao.nom_orgao
         dic_tramitacoes['destino']= "None"
   lst_tramitacoes.append(dic_tramitacoes)   
  
#o bloco abaixo gera o dicionario de relatorias
 lst_relatorias = []
 for relatoria in context.zsql.relatoria_obter_zsql(cod_materia = materia.cod_materia):
  for comissao in context.zsql.comissao_obter_zsql(cod_comissao = relatoria.cod_comissao):
    dic_comissao={}
    dic_comissao['nom_comissao']= comissao.nom_comissao
  for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar = relatoria.cod_parlamentar):
    dic_comissao['parlamentar']= parlamentar.nom_parlamentar
  dic_comissao['data_desig']= relatoria.dat_desig_relator
  dic_comissao['data_dest']= relatoria.dat_destit_relator
  if relatoria.tip_fim_relatoria==None or relatoria.tip_fim_relatoria=='0': 
   num = 0
   dic_comissao['motivo']=""
  else: 
   num=relatoria.tip_fim_relatoria
   for tipo_fim in context.zsql.tipo_fim_relatoria_obter_zsql(tip_fim_relatoria = num):
    dic_comissao['motivo']= tipo_fim.des_fim_relatoria
  lst_relatorias.append(dic_comissao)
   
#o bloco abaixo gera o dicionario de Numeracoes
 lst_numeracoes = []
 dic_dados={}
 for numeracao in context.zsql.numeracao_obter_zsql(cod_materia = materia.cod_materia):
  for tipo_materia in context.zsql.tipo_materia_legislativa_obter_zsql(tip_materia = numeracao.tip_materia):
   dic_dados['nome']= tipo_materia.sgl_tipo_materia+ "-"+ tipo_materia.des_tipo_materia+ "nº"+ numeracao.num_materia
   dic_dados['ano']= numeracao.ano_materia
  lst_numeracoes.append(dic_dados)
 
 
#o bloco abaixo gera o dicionário de legislacoes citadas  
 lst_legis_citadas = []
 dic_dados = {}
 for legislacao in context.zsql.legislacao_citada_obter_zsql(cod_materia = materia.cod_materia):
  norma = context.zsql.norma_juridica_obter_zsql(cod_norma = legislacao.cod_norma_sel)
  dic_dados['nome_lei']= str(norma[0].tip_norma_sel) + " nº"+ str(norma[0].num_norma) + " de"+ str(norma[0].ano_norma)
  dic_dados['disposicao']= legislacao.des_disposicoes
  dic_dados['parte']= legislacao.des_parte
  dic_dados['livro']= legislacao.des_livro
  dic_dados['titulo']= legislacao.des_titulo
  dic_dados['capitulo']= legislacao.des_capitulo
  dic_dados['secao']= legislacao.des_secao
  dic_dados['subsecao']= legislacao.des_subsecao
  dic_dados['artigo']= legislacao.des_artigo
  dic_dados['paragrafo']= legislacao.des_paragrafo
  dic_dados['inciso']= legislacao.des_inciso
  dic_dados['alinea']= legislacao.des_alinea
  dic_dados['item']= legislacao.des_item
  lst_legis_citadas.append(dic_dados)


#o bloco abaixo gera o dicionario de documentos acessórios
 lst_acessorios = []
 for documento in context.zsql.documento_acessorio_obter_zsql(cod_materia = materia.cod_materia,ind_excluido=0):
  dic_dados={}
  if documento.tip_documento==None or documento.tip_documento=='0': 
     tipnum = 0
     dic_dados['tipo']=""
  else:
     tipnum = documento.tip_documento
     for tipo_doc in context.zsql.tipo_documento_obter_zsql(tip_documento = tipnum):
      dic_dados['tipo']= tipo_doc.des_tipo_documento
  dic_dados['nome']= documento.nom_documento
  dic_dados['data']= documento.dat_documento
  dic_dados['autor']= documento.nom_autor_documento
  dic_dados['ementa']= documento.txt_ementa
  dic_dados['indexacao']= documento.txt_indexacao
  lst_acessorios.append(dic_dados)

caminho=context.pdf_detalhe_materia_gerar(imagem,rodape,inf_basicas_dic,orig_externa_dic,lst_mat_anexadas,lst_autoria,
                                          lst_des_iniciais,lst_tramitacoes,lst_relatorias,lst_numeracoes,
                                          lst_legis_citadas,lst_acessorios,sessao=session.id)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)

