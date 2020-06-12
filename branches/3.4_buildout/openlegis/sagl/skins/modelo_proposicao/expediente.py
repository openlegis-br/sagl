## Script (Python) "expediente"
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
  data = context.pysc.data_converter_pysc(sessao.dat_inicio_sessao)
  nom_arquivo = str(sessao.cod_sessao_plen)+ '_expediente.odt'

  # Presidente
  lst_presidente = []
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
  for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
    for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
      for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
        lst_presidente = presidencia.nom_completo.encode('utf-8')

  # Correspondencias
  for item in context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=1,ind_excluido=0):
    inf_basicas_dic["correspondencias"] = item.txt_expediente

  # Tribuna Livre
  for item in context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=3,ind_excluido=0):
    inf_basicas_dic["tribuna"] = item.txt_expediente

  # Indicacoes
  lst_indicacoes = [] 
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,des_tipo_materia='Indicação',ind_excluido=0):
      dic_indicacoes = {}
      dic_indicacoes['txt_ementa'] = materia.txt_ementa
      dic_indicacoes['num_ident_basica'] = materia.num_ident_basica
      dic_indicacoes["ano_ident_basica"] = context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))
      dic_indicacoes['dat_apresentacao'] = materia.dat_apresentacao
      dic_indicacoes["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      dic_indicacoes["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      lst_indicacoes.append(dic_indicacoes)

  # Requerimentos
  lst_requerimentos = [] 
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,des_tipo_materia='Requerimento',ind_excluido=0):
      dic_requerimentos = {}
      dic_requerimentos['txt_ementa'] = materia.txt_ementa
      dic_requerimentos['num_ident_basica'] = materia.num_ident_basica
      dic_requerimentos['ano_ident_basica'] = context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))
      dic_requerimentos['dat_apresentacao'] = materia.dat_apresentacao
      dic_requerimentos["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      dic_requerimentos["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      lst_requerimentos.append(dic_requerimentos)

  # Mocoes
  lst_mocoes = [] 
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia, des_tipo_materia='Moção',ind_excluido=0):
      dic_mocoes = {}
      dic_mocoes['txt_ementa'] = materia.txt_ementa
      dic_mocoes['num_ident_basica'] = materia.num_ident_basica
      dic_mocoes['ano_ident_basica'] = context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))
      dic_mocoes['dat_apresentacao'] = materia.dat_apresentacao
      dic_mocoes["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      dic_mocoes["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      lst_mocoes.append(dic_mocoes)

  # Oradores
  lst_oradores = []
  for orador in context.zsql.oradores_expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador.cod_parlamentar,ind_excluido=0):
          num_ordem = orador.num_ordem
          nom_completo = parlamentar.nom_parlamentar
          lst_oradores.append(nom_completo)
  lst_oradores = ', '.join(['%s' % (value) for (value) in lst_oradores])

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

return context.expediente_gerar_odt(inf_basicas_dic, lst_indicacoes, lst_requerimentos, lst_mocoes, lst_oradores, lst_presidente, nom_arquivo)
