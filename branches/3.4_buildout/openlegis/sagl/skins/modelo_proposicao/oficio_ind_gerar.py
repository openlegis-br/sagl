## Script (Python) "oficio_ind_gerar"
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

  # Indicacoes
  lst_indicacao = [] 
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,tip_id_basica=8,ind_excluido=0):
      dic_ind = {}
      dic_ind['txt_ementa'] = materia.txt_ementa.encode('utf-8')
      dic_ind['num_ident_basica'] = materia.num_ident_basica
      dic_ind['dat_apresentacao'] = materia.dat_apresentacao
      dic_ind["nom_autor"] = ''
      autoria = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia, ind_primeiro_autor=1)        
      if len(autoria) > 0:
          autoria = autoria[0]
          autor = context.zsql.autor_obter_zsql(cod_autor=autoria.cod_autor)
          if len(autor) > 0:
              autor = autor[0]
          if autor.des_tipo_autor == "Parlamentar":
              parlamentar = context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar)[0]     
              dic_ind["nom_autor"] = parlamentar.nom_completo
          elif autor.des_tipo_autor == "Comissao":
              comissao = context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao)[0]
              dic_ind["nom_autor"] = comissao.nom_comissao
          elif autor.des_tipo_autor == "Bancada":
              bancada = context.zsql.bancada_obter_zsql(cod_bancada=autor.cod_bancada)[0]
              dic_ind["nom_autor"] = bancada.nom_bancada
          else:
              dic_ind["nom_autor"] = autor.nom_autor
      lst_indicacao.append(dic_ind)

  # Presidente
  lst_presidente = []
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
  for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
    for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
      for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
        lst_presidente = presidencia.nom_completo.encode('utf-8')

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

return context.oficio_ind_gerar_odt(inf_basicas_dic, lst_indicacao, lst_presidente)
