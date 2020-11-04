## Script (Python) "materia_apresentada"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##
REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
  inf_basicas_dic = {}
  tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
  inf_basicas_dic["cod_sessao_plen"] = sessao.cod_sessao_plen
  inf_basicas_dic["num_sessao_plen"] = sessao.num_sessao_plen
  inf_basicas_dic["nom_sessao"] = tipo_sessao.nom_sessao
  inf_basicas_dic["num_legislatura"] = sessao.num_legislatura
  inf_basicas_dic["num_sessao_leg"] = sessao.num_sessao_leg
  inf_basicas_dic["dat_inicio_sessao"] = sessao.dat_inicio_sessao
  inf_basicas_dic["dia_sessao"] = context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao)
  inf_basicas_dic["hr_inicio_sessao"] = sessao.hr_inicio_sessao
  inf_basicas_dic["dat_fim_sessao"] = sessao.dat_fim_sessao
  inf_basicas_dic["hr_fim_sessao"] = sessao.hr_fim_sessao

  # Materias Apresentadas
  lst_materia_apresentada=[]
  for materia_apresentada in context.zsql.materia_apresentada_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      dic_materia_apresentada = {}
      if materia_apresentada.cod_materia != None:
         materia = context.zsql.materia_obter_zsql(cod_materia=materia_apresentada.cod_materia)[0]
         dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
         dic_materia_apresentada["tip_materia"] = materia.des_tipo_materia.upper().encode('utf-8')
         dic_materia_apresentada["num_ident_basica"] = materia.num_ident_basica
         dic_materia_apresentada["ano_ident_basica"] = materia.ano_ident_basica
         dic_materia_apresentada["txt_ementa"] = materia.txt_ementa.encode('utf-8')
         dic_materia_apresentada["nom_autor"] = ''
         autoria = context.zsql.autoria_obter_zsql(cod_materia=materia_apresentada.cod_materia, ind_primeiro_autor=1)        
         if len(autoria) > 0: # se existe autor
             autoria = autoria[0]
             autor = context.zsql.autor_obter_zsql(cod_autor=autoria.cod_autor)
             if len(autor) > 0:
                 autor = autor[0]
             if autor.des_tipo_autor == "Parlamentar":
                 parlamentar = context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar)[0]     
                 dic_materia_apresentada["nom_autor"] = parlamentar.nom_completo.encode('utf-8')
             elif autor.des_tipo_autor == "Comissao":
                 comissao = context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao)[0]
                 dic_materia_apresentada["nom_autor"] = comissao.nom_comissao.encode('utf-8')
             elif autor.des_tipo_autor == "Bancada":
                 bancada = context.zsql.bancada_obter_zsql(cod_bancada=autor.cod_bancada)[0]
                 dic_materia_apresentada["nom_autor"] = bancada.nom_bancada.encode('utf-8')
             else:
                 dic_materia_apresentada["nom_autor"] = autor.nom_autor
         lst_materia_apresentada.append(dic_materia_apresentada)
      if materia_apresentada.cod_documento != None:
         materia = context.zsql.documento_administrativo_obter_zsql(cod_documento=materia_apresentada.cod_documento)[0]
         dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
         dic_materia_apresentada["tip_materia"] = materia.des_tipo_documento.upper()
         dic_materia_apresentada["num_ident_basica"] = materia.num_documento
         dic_materia_apresentada["ano_ident_basica"] = materia.ano_documento
         dic_materia_apresentada["txt_ementa"] = materia.txt_assunto
         dic_materia_apresentada["nom_autor"] =  materia.txt_interessado
         lst_materia_apresentada.append(dic_materia_apresentada)

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

return context.materia_apresentada_gerar_odt(inf_basicas_dic, lst_materia_apresentada)
