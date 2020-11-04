## Script (Python) "materia_apreciada"
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

  # Lista das materias da Ordem do Dia
  lst_votacao=[]
  for votacao in context.zsql.votacao_ordem_dia_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
     # Seleciona os detalhes de uma matéria
      materia = context.zsql.materia_obter_zsql(cod_materia=votacao.cod_materia)[0]
      dic_votacao = {}
      dic_votacao["num_ordem"] = votacao.num_ordem
      dic_votacao["tip_materia"] = materia.des_tipo_materia.upper().encode('utf-8')
      dic_votacao["num_ident_basica"] = materia.num_ident_basica
      dic_votacao["ano_ident_basica"] = materia.ano_ident_basica
      dic_votacao["des_numeracao"]=""
      numeracao = context.zsql.numeracao_obter_zsql(cod_materia=votacao.cod_materia)
      if len(numeracao):
         numeracao = numeracao[0]
         dic_votacao["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
      dic_votacao["des_turno"]=""
      tramitacao = context.zsql.tramitacao_obter_zsql(cod_materia=materia.cod_materia, ind_ult_tramitacao=1)
      if len(tramitacao):
         tramitacao = tramitacao[0]
      tram = context.zsql.tramitacao_turno_obter_zsql(cod_materia=materia.cod_materia)
      if len(tram):
         tram_turno = tram[0]
         if tram_turno.sgl_turno != "":           
            for turno in [("P","Primeiro"), ("S","Segundo"), ("U","Unico"), ("L","Suplementar"), ("A","Votacão Unica em Regime de Urgencia"), ("B","1ª Votacao"), ("C","2ª e 3ª Votacoes")]:
              if tram_turno.sgl_turno == turno[0]:
                  dic_votacao["des_turno"] = turno[1]
      dic_votacao["txt_ementa"] = materia.txt_ementa.encode('utf-8')
      dic_votacao["ordem_observacao"] = votacao.ordem_observacao.encode('utf-8')
      dic_votacao["nom_autor"] = ''
      autoria = context.zsql.autoria_obter_zsql(cod_materia=votacao.cod_materia, ind_primeiro_autor=1)        
      if len(autoria) > 0: # se existe autor
          autoria = autoria[0]
          autor = context.zsql.autor_obter_zsql(cod_autor=autoria.cod_autor)
          if len(autor) > 0:
              autor = autor[0]      
          if autor.des_tipo_autor == "Parlamentar":
              parlamentar = context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar)[0]     
              dic_votacao["nom_autor"] = parlamentar.nom_completo.encode('utf-8')
          elif autor.des_tipo_autor == "Comissao":
              comissao = context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao)[0]
              dic_votacao["nom_autor"] = comissao.nom_comissao.encode('utf-8')
          elif autor.des_tipo_autor == "Bancada":
              bancada = context.zsql.bancada_obter_zsql(cod_bancada=autor.cod_bancada)[0]
              dic_votacao["nom_autor"] = bancada.nom_bancada.encode('utf-8')
          else:
              dic_votacao["nom_autor"] = autor.nom_autor 
      if votacao.tip_resultado_votacao:
          resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=votacao.tip_resultado_votacao, ind_excluido=0)
          for i in resultado:
              dic_votacao["nom_resultado"] = i.nom_resultado.encode('utf-8')
              if votacao.votacao_observacao:
                  dic_votacao["votacao_observacao"] = votacao.votacao_observacao.encode('utf-8')
      else:
          dic_votacao["nom_resultado"] = "Sem registro"
          dic_votacao["votacao_observacao"] = ""
      lst_votacao.append(dic_votacao)

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

return context.materia_apreciada_gerar_odt(inf_basicas_dic, lst_votacao)
