## Script (Python) "ata_gerar"
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

  nom_arquivo = str(cod_sessao_plen)+'_ata_sessao.odt'

  # Mesa Diretora da Sessao
  lst_mesa = []
  for composicao in context.zsql.composicao_mesa_sessao_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=composicao.cod_parlamentar,ind_excluido=0):
          for cargo in context.zsql.cargo_mesa_obter_zsql(cod_cargo=composicao.cod_cargo, ind_excluido=0):
              dic_mesa = {}
              dic_mesa['nom_completo'] = parlamentar.nom_parlamentar
              dic_mesa['sgl_partido'] = parlamentar.sgl_partido
              dic_mesa['des_cargo'] = cargo.des_cargo
              lst_mesa.append(dic_mesa)

  # Presenca na Sessao
  lst_presenca_sessao = []
  for presenca in context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca.cod_parlamentar,ind_excluido=0):
          nom_completo = parlamentar.nom_completo
          lst_presenca_sessao.append(nom_completo)
  inf_basicas_dic["qtde_lst_presenca_sessao"] = len(lst_presenca_sessao)
  lst_presenca_sessao = ', '.join(['%s' % (value) for (value) in lst_presenca_sessao])

  # Materias Apresentadas
  lst_materia_apresentada1=[]
  for materia_apresentada in context.zsql.materia_apresentada_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      if materia_apresentada.cod_materia != None:
         materia = context.zsql.materia_obter_zsql(cod_materia=materia_apresentada.cod_materia)[0]
         autores = context.zsql.autoria_obter_zsql(cod_materia=materia_apresentada.cod_materia)
         fields = autores.data_dictionary().keys()
         lista_autor = []
         for autor in autores:
   	   for field in fields:
                   nome_autor = autor['nom_autor_join']
	   lista_autor.append(nome_autor)
         autoria = ', '.join(['%s' % (value) for (value) in lista_autor]) 
         materia = str(materia.des_tipo_materia)+" "+str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ autoria +" - "+materia.txt_ementa
         lst_materia_apresentada1.append(materia)
      if materia_apresentada.cod_documento != None:
         materia = context.zsql.documento_administrativo_obter_zsql(cod_documento=materia_apresentada.cod_documento)[0]
         materia = str(materia.des_tipo_documento)+" "+str(materia.num_documento)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_documento)))+" - "+ materia.txt_interessado + " - " + materia.txt_assunto
         lst_materia_apresentada1.append(materia)
      lst_materia_apresentada = '; '.join(['%s' % (value) for (value) in lst_materia_apresentada1])

  # Correspondencias recebidas
  for item in context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=1,ind_excluido=0):
    inf_basicas_dic["correspondencias"] = item.txt_expediente

  # Tribuna Livre
  for item in context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=3,ind_excluido=0):
    inf_basicas_dic["tribuna"] = item.txt_expediente

  # Mocoes
  lst_mocoes=[]
  for mocao in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      for materia in context.zsql.materia_obter_zsql(cod_materia=mocao.cod_materia, des_tipo_materia='Moção', ind_excluido=0):
       autores = context.zsql.autoria_obter_zsql(cod_materia=mocao.cod_materia)
       fields = autores.data_dictionary().keys()
       lista_autor = []
       for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
       autoria = ', '.join(['%s' % (value) for (value) in lista_autor]) 
       materia = str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa + " Autoria: "+ autoria
       lst_mocoes.append(materia)
  lst_reqplen = '; '.join(['%s' % (value) for (value) in lst_mocoes]) 

  # Requerimentos
  lst_reqpres = [] 
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia, des_tipo_materia='Requerimento', ind_excluido=0):
      num_ident_basica = materia.num_ident_basica
      lst_reqpres.append(num_ident_basica)
      inf_basicas_dic["min_req"] = min(lst_reqpres)
      inf_basicas_dic["max_req"] = max(lst_reqpres)

  # Indicacoes
  lst_indicacao = [] 
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia, des_tipo_materia='Indicação', ind_excluido=0):
      num_ident_basica = materia.num_ident_basica
      lst_indicacao.append(num_ident_basica)
      inf_basicas_dic["min_ind"] = min(lst_indicacao)
      inf_basicas_dic["max_ind"] = max(lst_indicacao)

  # Lista de oradores
  lst_oradores = []
  for orador in context.zsql.oradores_expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador.cod_parlamentar,ind_excluido=0):
          num_ordem = orador.num_ordem
          nom_completo = parlamentar.nom_parlamentar
          lst_oradores.append(nom_completo)
  lst_oradores = ', '.join(['%s' % (value) for (value) in lst_oradores])

  # Lista presenca na ordem do dia
  lst_presenca_ordem_dia = []
  for presenca_ordem_dia in context.zsql.presenca_ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_ordem_dia.cod_parlamentar,ind_excluido=0):
          nom_completo = parlamentar.nom_completo
          lst_presenca_ordem_dia.append(nom_completo)
  inf_basicas_dic["qtde_lst_presenca_ordem_dia"] = len(lst_presenca_ordem_dia)
  lst_presenca_ordem_dia = ', '.join(['%s' % (value) for (value) in lst_presenca_ordem_dia])

  mensagem = ". Colocado em discussão e votação, foi "

  # Lista das materias em 1a discussao
  lst_pdiscussao=[]
  for pdiscussao in context.zsql.votacao_ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,tip_turno=1,ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=pdiscussao.cod_materia)[0]
      autores = context.zsql.autoria_obter_zsql(cod_materia=pdiscussao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
      if pdiscussao.tip_resultado_votacao:
          resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=pdiscussao.tip_resultado_votacao, ind_excluido=0)
          for i in resultado:
              nom_resultado = i.nom_resultado.lower()
              if pdiscussao.votacao_observacao:
                  votacao_observacao = pdiscussao.votacao_observacao.encode('utf-8')
              else:
                  votacao_observacao = ""
      else:
          nom_resultado = "Sem registro"
          votacao_observacao = ""
      if pdiscussao.tip_votacao == 1:
          mensagem = ". Colocado em discussao e votacao, foi "
          resultado = mensagem.decode('iso-8859-1').encode('utf-8') + nom_resultado + votacao_observacao
      elif pdiscussao.tip_votacao == 2:
          votos_favoraveis = str(pdiscussao.num_votos_sim) + " votos favoraveis"
          votos_contrarios = str(pdiscussao.num_votos_nao) + " votos contrarios"
          abstencoes = str(pdiscussao.num_abstencao) + " abstencoes"
          lst_parlamentares_sim = []
          for parlamentares_sim in context.zsql.votacao_parlamentar_obter_zsql(cod_votacao=pdiscussao.cod_votacao,vot_parlamentar="Sim"):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parlamentares_sim.cod_parlamentar,ind_excluido=0):
               nom_completo = parlamentar.nom_completo
               lst_parlamentares_sim.append(nom_completo)
          lst_parlamentares_sim = ', '.join(['%s' % (value) for (value) in lst_parlamentares_sim])
          lst_parlamentares_nao = []
          for parlamentares_nao in context.zsql.votacao_parlamentar_obter_zsql(cod_votacao=pdiscussao.cod_votacao,vot_parlamentar="Nao"):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parlamentares_nao.cod_parlamentar,ind_excluido=0):
               nom_completo = parlamentar.nom_completo
               lst_parlamentares_nao.append(nom_completo)
          lst_parlamentares_nao = ', '.join(['%s' % (value) for (value) in lst_parlamentares_nao])
          mensagem = ". Colocado em discussao e votacao nominal, a pedido do Vereador XXXXX, foi "
          resultado = mensagem.decode('iso-8859-1').encode('utf-8') + nom_resultado + " por " + votos_favoraveis.decode('iso-8859-1').encode('utf-8') + " dos Vereadores " + lst_parlamentares_sim + " e " + votos_contrarios.decode('iso-8859-1').encode('utf-8') + " dos Vereadores " + lst_parlamentares_nao + votacao_observacao
      materia = str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa + " Autoria: "+ autoria + resultado
      lst_pdiscussao.append(materia)
  inf_basicas_dic["pdiscussao"] = '; '.join(['%s' % (value) for (value) in lst_pdiscussao])

  # Lista das materias em 2a discussao
  lst_sdiscussao=[]
  for sdiscussao in context.zsql.votacao_ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,tip_turno=2,ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=sdiscussao.cod_materia)[0]
      autores = context.zsql.autoria_obter_zsql(cod_materia=sdiscussao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
      if sdiscussao.tip_resultado_votacao:
          resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=sdiscussao.tip_resultado_votacao, ind_excluido=0)
          for i in resultado:
              nom_resultado = i.nom_resultado.lower()
              if sdiscussao.votacao_observacao:
                  votacao_observacao = sdiscussao.votacao_observacao.encode('utf-8')
              else:
                  votacao_observacao = ""
      else:
          nom_resultado = "Sem registro"
          votacao_observacao = ""
      if sdiscussao.tip_votacao == 1:
          mensagem = ". Colocado em discussao e votacao, foi "
          resultado = mensagem.decode('iso-8859-1').encode('utf-8') + nom_resultado + votacao_observacao
      elif sdiscussao.tip_votacao == 2:
          votos_favoraveis = str(sdiscussao.num_votos_sim) + " votos favoraveis"
          votos_contrarios = str(sdiscussao.num_votos_nao) + " votos contrarios"
          abstencoes = str(sdiscussao.num_abstencao) + " abstencoes"
          lst_parlamentares_sim = []
          for parlamentares_sim in context.zsql.votacao_parlamentar_obter_zsql(cod_votacao=sdiscussao.cod_votacao,vot_parlamentar="Sim"):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parlamentares_sim.cod_parlamentar,ind_excluido=0):
               nom_completo = parlamentar.nom_completo
               lst_parlamentares_sim.append(nom_completo)
          lst_parlamentares_sim = ', '.join(['%s' % (value) for (value) in lst_parlamentares_sim])
          lst_parlamentares_nao = []
          for parlamentares_nao in context.zsql.votacao_parlamentar_obter_zsql(cod_votacao=sdiscussao.cod_votacao,vot_parlamentar="Nao"):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parlamentares_nao.cod_parlamentar,ind_excluido=0):
               nom_completo = parlamentar.nom_completo
               lst_parlamentares_nao.append(nom_completo)
          lst_parlamentares_nao = ', '.join(['%s' % (value) for (value) in lst_parlamentares_nao])
          mensagem = ". Colocado em discussao e votacao nominal, a pedido do Vereador XXXXX, foi "
          resultado = mensagem.decode('iso-8859-1').encode('utf-8') + nom_resultado + " por " + votos_favoraveis.decode('iso-8859-1').encode('utf-8') + " dos Vereadores " + lst_parlamentares_sim + " e " + votos_contrarios.decode('iso-8859-1').encode('utf-8') + " dos Vereadores " + lst_parlamentares_nao + votacao_observacao
      materia = str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa + " Autoria: "+ autoria + resultado
      lst_sdiscussao.append(materia)
  inf_basicas_dic["sdiscussao"] = '; '.join(['%s' % (value) for (value) in lst_sdiscussao])

  # Lista das materias em discussao unica
  lst_discussao_unica=[]
  for discussao_unica in context.zsql.votacao_ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,tip_turno=3,ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=discussao_unica.cod_materia)[0]
      autores = context.zsql.autoria_obter_zsql(cod_materia=discussao_unica.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
      if discussao_unica.tip_resultado_votacao:
          resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=discussao_unica.tip_resultado_votacao, ind_excluido=0)
          for i in resultado:
              nom_resultado = i.nom_resultado.lower()
              if discussao_unica.votacao_observacao:
                  votacao_observacao = discussao_unica.votacao_observacao.encode('utf-8')
              else:
                  votacao_observacao = ""
      else:
          nom_resultado = "Sem registro"
          votacao_observacao = ""
      if discussao_unica.tip_votacao == 1:
          mensagem = ". Colocada em discussao e votacao, foi "
          resultado = mensagem.decode('iso-8859-1').encode('utf-8') + nom_resultado + votacao_observacao
      elif discussao_unica.tip_votacao == 2:
          votos_favoraveis = str(discussao_unica.num_votos_sim) + " votos favoraveis"
          votos_contrarios = str(discussao_unica.num_votos_nao) + " votos contrarios"
          abstencoes = str(discussao_unica.num_abstencao) + " abstencoes"
          lst_parlamentares_sim = []
          for parlamentares_sim in context.zsql.votacao_parlamentar_obter_zsql(cod_votacao=discussao_unica.cod_votacao,vot_parlamentar="Sim"):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parlamentares_sim.cod_parlamentar,ind_excluido=0):
               nom_completo = parlamentar.nom_completo
               lst_parlamentares_sim.append(nom_completo)
          lst_parlamentares_sim = ', '.join(['%s' % (value) for (value) in lst_parlamentares_sim])
          lst_parlamentares_nao = []
          for parlamentares_nao in context.zsql.votacao_parlamentar_obter_zsql(cod_votacao=discussao_unica.cod_votacao,vot_parlamentar="Nao"):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parlamentares_nao.cod_parlamentar,ind_excluido=0):
               nom_completo = parlamentar.nom_completo
               lst_parlamentares_nao.append(nom_completo)
          lst_parlamentares_nao = ', '.join(['%s' % (value) for (value) in lst_parlamentares_nao])
          mensagem = ". Colocada em discussao e votacao nominal, a pedido do Vereador XXXXX, foi "
          resultado = mensagem.decode('iso-8859-1').encode('utf-8') + nom_resultado + " por " + votos_favoraveis.decode('iso-8859-1').encode('utf-8') + " dos Vereadores " + lst_parlamentares_sim + " e " + votos_contrarios.decode('iso-8859-1').encode('utf-8') + " dos Vereadores " + lst_parlamentares_nao + votacao_observacao
      materia = str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa + " Autoria: "+ autoria + resultado
      lst_discussao_unica.append(materia)
  inf_basicas_dic["discussao_unica"] = '; '.join(['%s' % (value) for (value) in lst_discussao_unica])

  # Lista das materias da Ordem do Dia
  lst_votacao=[]

  # Lista presenca no Grande Expediente (inativo)
  lst_presenca_expediente = []

  # Lista de oradores nas Explicacoes Pessoais
  lst_explicacoes_pessoais = []
  for orador in context.zsql.oradores_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador.cod_parlamentar,ind_excluido=0):
          num_ordem = orador.num_ordem
          nom_completo = parlamentar.nom_parlamentar
          lst_explicacoes_pessoais.append(nom_completo)
  inf_basicas_dic['explicacoes_pessoais'] = ', '.join(['%s' % (value) for (value) in lst_explicacoes_pessoais])

  # Lista presenca no encerramento da Sessao (inativo)
  lst_presenca_encerramento = []

  # Presidente
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
  lst_presidente = []
  for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
    for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
      for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
        lst_presidente = presidencia.nom_completo.encode('utf-8')
  # 1o. Secretario
  lst_psecretario = []
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for cod_psecretario in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=3):
      for psecretaria in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_psecretario.cod_parlamentar):
        lst_psecretario = psecretaria.nom_completo.encode('utf-8')
  # 2o. Secretario
  lst_2ssecretario = []
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for cod_ssecretario in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=4):
      for ssecretaria in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_ssecretario.cod_parlamentar):
        lst_ssecretario = ssecretaria.nom_completo.encode('utf-8')

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
  inf_basicas_dic['nom_camara'] = casa['nom_casa']
  inf_basicas_dic['end_camara'] = casa['end_casa']
  inf_basicas_dic["nom_estado"] = nom_estado
  for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
      inf_basicas_dic['nom_localidade']= local.nom_localidade
      inf_basicas_dic['sgl_uf']= local.sgl_uf

#print inf_basicas_dic["pdiscussao"]
#return printed

return context.ata_gerar_odt(inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario, nom_arquivo)
