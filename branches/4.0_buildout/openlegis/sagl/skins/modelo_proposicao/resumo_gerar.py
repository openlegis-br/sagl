## Script (Python) "resumo_gerar"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

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
  
  # Mesa Diretora da Sessao
  lst_mesa = []
  for composicao in context.zsql.composicao_mesa_sessao_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=composicao.cod_parlamentar,ind_excluido=0):
          for cargo in context.zsql.cargo_mesa_obter_zsql(cod_cargo=composicao.cod_cargo, ind_excluido=0):
              dic_mesa = {}
              dic_mesa['nom_completo'] = parlamentar.nom_completo
              dic_mesa['sgl_partido'] = parlamentar.sgl_partido
              dic_mesa['des_cargo'] = cargo.des_cargo
              lst_mesa.append(dic_mesa)
              
  # Presenca na Sessao
  lst_presenca_sessao = []
  for presenca in context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca.cod_parlamentar,ind_excluido=0):
          nom_completo = parlamentar.nom_completo.title()
          lst_presenca_sessao.append(nom_completo)
  lst_presenca_sessao = ', '.join(['%s' % (value) for (value) in lst_presenca_sessao])
  
  # Materias Apresentadas
  lst_materia_apresentada=[]
  for materia_apresentada in context.zsql.materia_apresentada_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      dic_materia_apresentada = {}
      if materia_apresentada.cod_materia != None:
         materia = context.zsql.materia_obter_zsql(cod_materia=materia_apresentada.cod_materia)[0]
         dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
         dic_materia_apresentada["id_materia"] = materia.des_tipo_materia.decode('utf-8').upper()+" Nº "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
         dic_materia_apresentada["txt_ementa"] = materia.txt_ementa
         dic_materia_apresentada["nom_autor"] = ""
         autores = context.zsql.autoria_obter_zsql(cod_materia=materia_apresentada.cod_materia)
         fields = autores.data_dictionary().keys()
         lista_autor = []
         for autor in autores:
	   for field in fields:
                   nome_autor = autor['nom_autor_join']
  	   lista_autor.append(nome_autor)
         dic_materia_apresentada["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
         lst_materia_apresentada.append(dic_materia_apresentada)
      if materia_apresentada.cod_documento != None:
         materia = context.zsql.documento_administrativo_obter_zsql(cod_documento=materia_apresentada.cod_documento)[0]
         dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
         dic_materia_apresentada["id_materia"] = materia.des_tipo_documento.decode('utf-8').upper()+" Nº "+str(materia.num_documento)+"/"+str(materia.ano_documento)
         dic_materia_apresentada["txt_ementa"] = materia.txt_assunto
         dic_materia_apresentada["nom_autor"] =  materia.txt_interessado
         lst_materia_apresentada.append(dic_materia_apresentada)

  # Matérias do Expediente
  lst_reqplen = []
  lst_reqpres = []   
  lst_indicacao = []   
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,ind_excluido=0):
          # Requerimentos ao Plenario
          if materia.des_tipo_materia == 'Requerimento':    
             dic_reqpl = {}
             dic_reqpl['txt_ementa'] = materia.txt_ementa
             dic_reqpl['num_ident_basica'] = materia.num_ident_basica
             dic_reqpl['ano_ident_basica'] = materia.ano_ident_basica
             dic_reqpl['dat_apresentacao'] = materia.dat_apresentacao
             dic_reqpl["nom_autor"] = ""
             autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
             fields = autores.data_dictionary().keys()
             lista_autor = []
             for autor in autores:
                 for field in fields:
                     nome_autor = autor['nom_autor_join']
                 lista_autor.append(nome_autor)
             dic_reqpl["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
             lst_reqplen.append(dic_reqpl)
          # Requerimentos a Presidencia
          elif materia.des_tipo_materia == 'Requerimento à Presidência':    
             dic_reqpr = {}
             dic_reqpr['txt_ementa'] = materia.txt_ementa
             dic_reqpr['num_ident_basica'] = materia.num_ident_basica
             dic_reqpr['ano_ident_basica'] = materia.ano_ident_basica
             dic_reqpr['dat_apresentacao'] = materia.dat_apresentacao
             dic_reqpr["nom_autor"] = ""
             autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
             fields = autores.data_dictionary().keys()
             lista_autor = []
             for autor in autores:
                 for field in fields:
                     nome_autor = autor['nom_autor_join']
                 lista_autor.append(nome_autor)
             dic_reqpr["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
             lst_reqpres.append(dic_reqpr)
          # Indicacoes
          elif materia.des_tipo_materia == 'Indicação':              
             dic_ind = {}
             dic_ind['txt_ementa'] = materia.txt_ementa
             dic_ind['num_ident_basica'] = materia.num_ident_basica
             dic_ind['ano_ident_basica'] = materia.ano_ident_basica
             dic_ind['dat_apresentacao'] = materia.dat_apresentacao
             dic_ind["nom_autor"] = ""
             autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
             fields = autores.data_dictionary().keys()
             lista_autor = []
             for autor in autores:
                 for field in fields:
                     nome_autor = autor['nom_autor_join']
                 lista_autor.append(nome_autor)
             dic_ind["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])       
             lst_indicacao.append(dic_ind)
      
  # Lista presenca na ordem do dia
  lst_presenca_ordem_dia = []
  for presenca_ordem_dia in context.zsql.presenca_ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_ordem_dia.cod_parlamentar,ind_excluido=0):
          nom_completo = parlamentar.nom_completo
          lst_presenca_ordem_dia.append(nom_completo)
  lst_presenca_ordem_dia = ', '.join(['%s' % (value) for (value) in lst_presenca_ordem_dia])
  qtde_lst_presenca_ordem_dia = len(lst_presenca_ordem_dia)
  
  # Lista das materias da Ordem do Dia
  lst_votacao=[]
  for votacao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0): 
     # Seleciona os detalhes de uma materia
      materia = context.zsql.materia_obter_zsql(cod_materia=votacao.cod_materia)[0]
      dic_votacao = {}
      dic_votacao["num_ordem"] = votacao.num_ordem
      dic_votacao["id_materia"] = materia.des_tipo_materia.decode('utf-8').upper()+" Nº "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
      dic_votacao["des_numeracao"]=""
      numeracao = context.zsql.numeracao_obter_zsql(cod_materia=votacao.cod_materia)
      if len(numeracao):
         numeracao = numeracao[0]
         dic_votacao["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
      dic_votacao["des_turno"]=""
      dic_votacao["txt_ementa"] = materia.txt_ementa
      dic_votacao["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=votacao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      dic_votacao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
      
      nom_resultado = ''
      votacao_observacao = ''
      for votacao in context.zsql.votacao_ordem_dia_obter_zsql(cod_materia=votacao.cod_materia, cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
          contagem_votos = ''
          if votacao.tip_votacao == 2:
              if votacao.num_votos_sim == 0:
                 votos_favoraveis = ''
              elif votacao.num_votos_sim == 1:
                 votos_favoraveis = ' - ' +str(votacao.num_votos_sim) + " voto favorável"
              elif votacao.num_votos_sim > 1:
                 votos_favoraveis = ' - ' + str(votacao.num_votos_sim) + " votos favoráveis"
              if votacao.num_votos_nao == 0:
                 votos_contrarios = ''
              elif votacao.num_votos_nao == 1:
                 votos_contrarios = ' - ' + str(votacao.num_votos_nao) + " voto contrário"
              elif votacao.num_votos_nao > 1:
                 votos_contrarios = ' - ' + str(votacao.num_votos_nao) + " votos contrários"
              if votacao.num_abstencao == 0:
                 abstencoes = ''
              elif votacao.num_abstencao == 1:
                 abstencoes = ' - ' + str(votacao.num_abstencao) + " abstenção"
              elif votacao.num_abstencao > 1:
                 abstencoes =  ' - ' + str(votacao.num_abstencao) + " abstenções"
              contagem_votos = votos_favoraveis + votos_contrarios + abstencoes
          if votacao.votacao_observacao != '':
             votacao_observacao = ' - ' + votacao.votacao_observacao
          else:
             votacao_observacao = ''
          if votacao.tip_resultado_votacao:
             for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=votacao.tip_turno):
                 turno_discussao = turno.des_turno
             resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=votacao.tip_resultado_votacao, ind_excluido=0)
             for i in resultado:
                 nom_resultado= ' (' + i.nom_resultado+ ' em ' + turno_discussao + contagem_votos + votacao_observacao + ')'
          else:
             nom_resultado = " (Matéria não votada)"
             votacao_observacao = ""
      dic_votacao["nom_resultado"] = nom_resultado
      dic_votacao["ordem_observacao"] = votacao_observacao           
      dic_votacao["votacao_observacao"] = votacao_observacao 
          
      lst_votacao.append(dic_votacao)
      
  # Lista presenca no Grande Expediente
  lst_presenca_expediente = []
  for presenca_expediente in context.zsql.presenca_expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_expediente.cod_parlamentar,ind_excluido=0):
          dic_presenca_expediente = {}
          dic_presenca_expediente['nom_completo'] = parlamentar.nom_completo
          dic_presenca_expediente['sgl_partido'] = parlamentar.sgl_partido
          lst_presenca_expediente.append(dic_presenca_expediente)
  lst_presenca_expediente = ', '.join(['%s' % (value) for (value) in lst_presenca_expediente])          
  # Lista dos oradores nas Explicacoes Pessoais (Grande Expediente)
  lst_oradores = []
  for orador in context.zsql.oradores_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador.cod_parlamentar,ind_excluido=0):
          dic_oradores = {}
          dic_oradores["num_ordem"] = orador.num_ordem
          dic_oradores["nom_completo"] = parlamentar.nom_completo
          dic_oradores['sgl_partido'] = parlamentar.sgl_partido
          lst_oradores.append(dic_oradores)
  # Lista presenca no encerramento da Sessao
  lst_presenca_encerramento = []
  for presenca_encerramento in context.zsql.presenca_encerramento_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_encerramento.cod_parlamentar,ind_excluido=0):
          dic_presenca_encerramento = {}
          dic_presenca_encerramento['nom_completo'] = parlamentar.nom_completo
          dic_presenca_encerramento['sgl_partido'] = parlamentar.sgl_partido
          lst_presenca_encerramento.append(dic_presenca_encerramento)
  lst_presenca_encerramento = ', '.join(['%s' % (value) for (value) in lst_presenca_encerramento])                    
  # Presidente
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
  lst_presidente = []
  for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
    for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
      for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
        lst_presidente = presidencia.nom_completo
  # 1o. Secretario
  lst_psecretario = []
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for cod_psecretario in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=3):
      for psecretaria in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_psecretario.cod_parlamentar):
        lst_psecretario = psecretaria.nom_completo
  # 2o. Secretario
  lst_2ssecretario = []
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for cod_ssecretario in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=4):
      for ssecretaria in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_ssecretario.cod_parlamentar):
        lst_ssecretario = ssecretaria.nom_completo
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

return st.resumo_gerar_odt(inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario)
