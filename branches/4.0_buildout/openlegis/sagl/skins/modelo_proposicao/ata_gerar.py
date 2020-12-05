## Script (Python) "ata_gerar"
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
  nom_arquivo = str(cod_sessao_plen)+'_ata_sessao.odt'
  ata_dic = {}
  tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
  ata_dic["cod_sessao_plen"] = sessao.cod_sessao_plen
  ata_dic["num_sessao_plen"] = sessao.num_sessao_plen
  # CM Jaboticabal
  #ata_dic["num_tip_sessao"] = sessao.num_tip_sessao
  ata_dic["nom_sessao"] = tipo_sessao.nom_sessao
  ata_dic["num_legislatura"] = sessao.num_legislatura
  ata_dic["num_sessao_leg"] = sessao.num_sessao_leg
  ata_dic["dat_inicio_sessao"] = sessao.dat_inicio_sessao
  ata_dic["dia_sessao"] = context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao)
  ata_dic["hr_inicio_sessao"] = sessao.hr_inicio_sessao
  ata_dic["dat_fim_sessao"] = sessao.dat_fim_sessao
  ata_dic["hr_fim_sessao"] = sessao.hr_fim_sessao

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

  ata_dic["lst_mesa"] = lst_mesa

  # Presenca na Sessao
  ata_dic["qtde_presenca_sessao"] = ""
  ata_dic["lst_presenca_sessao"] = ""  
  lst_presenca_sessao = []
  for presenca in context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca.cod_parlamentar,ind_excluido=0):
          nom_completo = parlamentar.nom_completo
          lst_presenca_sessao.append(nom_completo)

  ata_dic["qtde_presenca_sessao"] = len(lst_presenca_sessao)
  ata_dic["lst_presenca_sessao"] = ', '.join(['%s' % (value) for (value) in lst_presenca_sessao])

  # Materias Apresentadas
  lst_materia_apresentada=[]
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
         materia = str(materia.des_tipo_materia).decode('utf-8').upper()+ ' Nº ' +str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ autoria +" - " +materia.txt_ementa
         lst_materia_apresentada.append(materia)
      elif materia_apresentada.cod_emenda != None:
           for emenda in context.zsql.emenda_obter_zsql(cod_emenda=materia_apresentada.cod_emenda):
               materia = context.zsql.materia_obter_zsql(cod_materia=emenda.cod_materia)[0]
               dic_materia_apresentada["nom_autor"] = ""
               autores = context.zsql.autoria_emenda_obter_zsql(cod_emenda=emenda.cod_emenda)
               fields = autores.data_dictionary().keys()
               lista_autor = []
               for autor in autores:
	           for field in fields:
                       nome_autor = autor['nom_autor_join']
	           lista_autor.append(nome_autor)
               autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
               materia = 'Emenda ' + str(emenda.des_tipo_emenda).decode('utf-8').upper() + ' Nº ' + str(emenda.num_emenda) + " - " + materia.sgl_tipo_materia + str(materia.num_ident_basica) + "/" + str(materia.ano_ident_basica) +" - "+ autoria +" - " +emenda.txt_ementa
           lst_materia_apresentada.append(materia)
      elif materia_apresentada.cod_substitutivo != None:
           for substitutivo in context.zsql.substitutivo_obter_zsql(cod_substitutivo=materia_apresentada.cod_substitutivo):
               materia = context.zsql.materia_obter_zsql(cod_materia=substitutivo.cod_materia)[0]
               autores = context.zsql.autoria_substitutivo_obter_zsql(cod_substitutivo=substitutivo.cod_substitutivo)
               fields = autores.data_dictionary().keys()
               lista_autor = []
               for autor in autores:
	           for field in fields:
                       nome_autor = autor['nom_autor_join']
	           lista_autor.append(nome_autor)
               autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
               materia = 'SUBSTITUTIVO ' + ' Nº ' + str(substitutivo.num_substitutivo) + " - " + materia.sgl_tipo_materia + str(materia.num_ident_basica) + "/" + str(materia.ano_ident_basica)  +" - "+ autoria +" - " +substitutivo.txt_ementa
           lst_materia_apresentada.append(materia)
      elif materia_apresentada.cod_parecer != None:
           for parecer in context.zsql.relatoria_obter_zsql(cod_relatoria=materia_apresentada.cod_parecer):
               materia = context.zsql.materia_obter_zsql(cod_materia=parecer.cod_materia)[0]
               dic_materia_apresentada["txt_ementa"] = materia_apresentada.txt_observacao
               for comissao in context.zsql.comissao_obter_zsql(cod_comissao=parecer.cod_comissao):
                   sgl_comissao = comissao.sgl_comissao
                   nom_comissao = comissao.nom_comissao
               autoria = nom_comissao.decode('utf-8').upper()
               materia = 'PARECER ' + str(sgl_comissao) + ' Nº ' + str(parecer.num_parecer) + '/' + str(parecer.ano_parecer) + " - " +  str(materia.sgl_tipo_materia) +' ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica)  + " - " + autoria + " - " + materia_apresentada.txt_observacao
           lst_materia_apresentada.append(materia)
      elif materia_apresentada.cod_documento != None:
           materia = context.zsql.documento_administrativo_obter_zsql(cod_documento=materia_apresentada.cod_documento)[0]
           materia = str(materia.des_tipo_documento).decode('utf-8').upper() + ' Nº ' +str(materia.num_documento)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_documento)))+" - "+ materia.txt_interessado + " - " + materia.txt_assunto
           lst_materia_apresentada.append(materia)

  ata_dic["lst_materia_apresentada"] = '; '.join(['%s' % (value) for (value) in lst_materia_apresentada])

  # Correspondencias recebidas
  ata_dic["correspondencias"] = ''
  for item in context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=1,ind_excluido=0):
      ata_dic["correspondencias"] = item.txt_expediente

  # Tribuna Livre
  ata_dic["tribuna"] = ''
  for item in context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=3,ind_excluido=0):
      ata_dic["tribuna"] = item.txt_expediente

  # Biblia
  ata_dic["biblia"] = ""
  for item in context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=4,ind_excluido=0):
    ata_dic["biblia"] = item.txt_expediente

  # Descontinuado
  lst_reqplen = ''
  lst_reqpres = ''

  # Indicacoes
  lst_indicacao = []
  lst_num_ind = []

  # Requerimentos
  lst_requerimento = []
  lst_num_req = []

  # Mocoes
  lst_mocao=[]

  # Pareceres
  lst_parecer = []

  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      # Materias Legislativas
      if item.cod_materia != None:
         for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,ind_excluido=0):
             # Indicações
             if materia.des_tipo_materia == 'Indicação':
                autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
                fields = autores.data_dictionary().keys()
                lista_autor = []
                for autor in autores:
                    for field in fields:
                        nome_autor = autor['nom_autor_join']
	            lista_autor.append(nome_autor)
                autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
                for votacao in context.zsql.votacao_expediente_materia_obter_zsql(cod_materia=item.cod_materia, cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
                    if votacao.tip_resultado_votacao:
                       resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao = votacao.tip_resultado_votacao, ind_excluido=0)
                       for i in resultado:
                           votacao_observacao = ""
                           if votacao.votacao_observacao:
                              votacao_observacao = ' - ' + votacao.votacao_observacao
                           nom_resultado = ' (' + i.nom_resultado + votacao_observacao + ')'
                    else:
                       nom_resultado = "(Matéria não votada)"
                       votacao_observacao = ""
                num_ident_basica = materia.num_ident_basica
                materia = str(materia.des_tipo_materia).decode('utf-8').upper() + ' Nº ' +str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))) + " - " + autoria + " - " + materia.txt_ementa + nom_resultado
                lst_indicacao.append(materia)
                lst_num_ind.append(num_ident_basica)                
             # Requerimentos
             elif materia.des_tipo_materia == 'Requerimento':
                autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
                fields = autores.data_dictionary().keys()
                lista_autor = []
                for autor in autores:
                    for field in fields:
                        nome_autor = autor['nom_autor_join']
	            lista_autor.append(nome_autor)
                autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
                for votacao in context.zsql.votacao_expediente_materia_obter_zsql(cod_materia=item.cod_materia, cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
                    if votacao.tip_resultado_votacao:
                       resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao = votacao.tip_resultado_votacao, ind_excluido=0)
                       for i in resultado:
                           votacao_observacao = ""
                           if votacao.votacao_observacao:
                              votacao_observacao = ' - ' + votacao.votacao_observacao
                           nom_resultado = ' (' + i.nom_resultado + votacao_observacao + ')'
                    else:
                       nom_resultado = "(Matéria não votada)"
                       votacao_observacao = ""
                num_ident_basica = materia.num_ident_basica                
                materia = str(materia.des_tipo_materia).decode('utf-8').upper() + ' Nº ' +str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))) + " - " + autoria + " - " + materia.txt_ementa  + nom_resultado
                lst_requerimento.append(materia)
                lst_num_req.append(num_ident_basica)                                
             # Moções
             elif materia.des_tipo_materia == 'Moção':
                autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
                fields = autores.data_dictionary().keys()
                lista_autor = []
                for autor in autores:
                    for field in fields:
                        nome_autor = autor['nom_autor_join']
	            lista_autor.append(nome_autor)
                autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
                for votacao in context.zsql.votacao_expediente_materia_obter_zsql(cod_materia=item.cod_materia, cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
                    if votacao.tip_resultado_votacao:
                       resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao = votacao.tip_resultado_votacao, ind_excluido=0)
                       for i in resultado:
                           votacao_observacao = ""
                           if votacao.votacao_observacao:
                              votacao_observacao = ' - ' + votacao.votacao_observacao
                           nom_resultado = ' (' + i.nom_resultado + votacao_observacao + ')'
                    else:
                       nom_resultado = ""
                       votacao_observacao = ""
                materia = str(materia.des_tipo_materia).decode('utf-8').upper() + ' Nº ' +str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))) + " - " + autoria + " - " + materia.txt_ementa + nom_resultado
                lst_mocao.append(materia)
      # Pareceres
      elif item.cod_parecer != None:
           for parecer in context.zsql.relatoria_obter_zsql(cod_relatoria=item.cod_parecer,ind_excluido=0):
               for materia in context.zsql.materia_obter_zsql(cod_materia=parecer.cod_materia, ind_excluido=0):
                   sgl_tipo_materia = materia.sgl_tipo_materia
                   num_ident_basica = materia.num_ident_basica
                   ano_ident_basica = materia.ano_ident_basica
               for comissao in context.zsql.comissao_obter_zsql(cod_comissao=parecer.cod_comissao):
                   nom_comissao = comissao.nom_comissao.decode('utf-8').upper()
                   sgl_comissao = comissao.sgl_comissao
               for votacao in context.zsql.votacao_expediente_materia_obter_zsql(cod_materia=item.cod_parecer, cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
                   if votacao.tip_resultado_votacao:
                      resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao = votacao.tip_resultado_votacao, ind_excluido=0)
                      for i in resultado:
                          votacao_observacao = ""
                          if votacao.votacao_observacao:
                             votacao_observacao = ' - ' + votacao.votacao_observacao
                          nom_resultado = ' (' + i.nom_resultado + votacao_observacao + ')'
                   else:
                      nom_resultado = "(Parecer não votado)"
                      votacao_observacao = ""
               materia = 'PARECER ' + str(sgl_comissao) + ' Nº ' + str(parecer.num_parecer) + '/' + str(parecer.ano_parecer)+' ao '+str(sgl_tipo_materia) + ' ' + str(num_ident_basica) + '/' + str(ano_ident_basica) + ' - ' + nom_comissao + ' - ' + item.txt_observacao  + nom_resultado
               lst_parecer.append(materia)

  # Juntar Indicações
  ata_dic["indicacao"] = '; '.join(['%s' % (value) for (value) in lst_indicacao])
  ata_dic["min_ind"] = min(lst_num_ind)
  ata_dic["max_ind"] = max(lst_num_ind)  

  # Juntar Requerimentos
  ata_dic["requerimento"] = '; '.join(['%s' % (value) for (value) in lst_requerimento])
  ata_dic["min_req"] = min(lst_num_req)
  ata_dic["max_req"] = max(lst_num_req)   

  # Juntar Mocoes
  ata_dic["mocao"] = '; '.join(['%s' % (value) for (value) in lst_mocao])

  # Juntar Pareceres
  ata_dic["parecer"] = '; '.join(['%s' % (value) for (value) in lst_parecer])

  # Lista de oradores
  lst_oradores = []
  for orador in context.zsql.oradores_expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador.cod_parlamentar,ind_excluido=0):
          num_ordem = orador.num_ordem
          nom_completo = parlamentar.nom_parlamentar
          lst_oradores.append(nom_completo)

  ata_dic["lst_oradores"] = ', '.join(['%s' % (value) for (value) in lst_oradores])

  # Lista presenca na ordem do dia
  lst_presenca_ordem_dia = []
  for presenca_ordem_dia in context.zsql.presenca_ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_ordem_dia.cod_parlamentar,ind_excluido=0):
          nom_completo = parlamentar.nom_completo
          lst_presenca_ordem_dia.append(nom_completo)

  ata_dic["qtde_presenca_ordem_dia"] = len(lst_presenca_ordem_dia)
  ata_dic["lst_presenca_ordem_dia"] = ', '.join(['%s' % (value) for (value) in lst_presenca_ordem_dia])

  # Matérias da Ordem do Dia, incluindo resultados das votacoes
  lst_votacao=[]
  for ordem in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=ordem.cod_materia)[0]
      dic_votacao = {}
      dic_votacao["num_ordem"] = ordem.num_ordem
      autores = context.zsql.autoria_obter_zsql(cod_materia=ordem.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
          for field in fields:
              nome_autor = autor['nom_autor_join']
	  lista_autor.append(nome_autor)
      autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
      nom_resultado = ''
      for votacao in context.zsql.votacao_ordem_dia_obter_zsql(cod_materia=ordem.cod_materia, cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
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
      dic_votacao["materia"] = materia.des_tipo_materia.decode('utf-8').upper() +" Nº " + str(materia.num_ident_basica) + "/" + str(materia.ano_ident_basica) + ' - ' + autoria + ' - ' + materia.txt_ementa + nom_resultado

      lst_qtde_substitutivos=[]
      lst_substitutivos=[]
      for substitutivo in context.zsql.substitutivo_obter_zsql(cod_materia=ordem.cod_materia,ind_excluido=0):
          autores = context.zsql.autoria_substitutivo_obter_zsql(cod_substitutivo=substitutivo.cod_substitutivo, ind_excluido=0)
          dic_substitutivo = {}
          fields = autores.data_dictionary().keys()
          lista_autor = []
          for autor in autores:
              for field in fields:
                  nome_autor = autor['nom_autor_join']
	      lista_autor.append(nome_autor)
          autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
          nom_resultado = ''
          for votacao in context.zsql.votacao_ordem_dia_obter_zsql(cod_substitutivo=substitutivo.cod_substitutivo, cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
             if votacao.votacao_observacao != '':
                votacao_observacao = ' - ' + votacao.votacao_observacao
             else:
                votacao_observacao = ''
             if votacao.tip_resultado_votacao:
                for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=votacao.tip_turno):
                    turno_discussao = turno.des_turno
                resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=votacao.tip_resultado_votacao, ind_excluido=0)
                for i in resultado:
                    nom_resultado = ' (' + i.nom_resultado+ ' em ' + turno_discussao + votacao_observacao + ')'
                    if votacao.votacao_observacao:
                       votacao_observacao = votacao.ordem_observacao
             else:
                nom_resultado = " (Substitutivo não votado)"
                votacao_observacao = ""

          dic_substitutivo["materia"] = 'SUBSTITUTIVO Nº ' + str(substitutivo.num_substitutivo) + ' - ' +  autoria + ' - ' + substitutivo.txt_ementa + nom_resultado

          lst_substitutivos.append(dic_substitutivo)
          cod_substitutivo = substitutivo.cod_substitutivo
          lst_qtde_substitutivos.append(cod_substitutivo)
      dic_votacao["substitutivos"] = lst_substitutivos
      dic_votacao["qtde_substitutivos"] = len(lst_qtde_substitutivos)

      lst_qtde_emendas=[]
      lst_emendas=[]
      for emenda in context.zsql.emenda_obter_zsql(cod_materia=ordem.cod_materia,ind_excluido=0,exc_pauta=0):
          autores = context.zsql.autoria_emenda_obter_zsql(cod_emenda=emenda.cod_emenda,ind_excluido=0)
          dic_emenda = {}
          fields = autores.data_dictionary().keys()
          lista_autor = []
          for autor in autores:
              for field in fields:
                  nome_autor = autor['nom_autor_join']
	      lista_autor.append(nome_autor)
          autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
          nom_resultado = ''
          for votacao in context.zsql.votacao_ordem_dia_obter_zsql(cod_emenda=emenda.cod_emenda, cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
             if votacao.votacao_observacao != '':
                votacao_observacao = ' - ' + votacao.votacao_observacao
             else:
                votacao_observacao = ''
             if votacao.tip_resultado_votacao:
                for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=votacao.tip_turno):
                    turno_discussao = turno.des_turno
                resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=votacao.tip_resultado_votacao, ind_excluido=0)
                for i in resultado:
                    nom_resultado = ' (' + i.nom_resultado+ ' em ' + turno_discussao + votacao_observacao + ')'
                    if votacao.votacao_observacao:
                        votacao_observacao = votacao.ordem_observacao
             else:
                nom_resultado = " (Emenda não votada)"
                votacao_observacao = ""
          dic_emenda["materia"] = 'EMENDA Nº ' + str(emenda.num_emenda) + ' (' + emenda.des_tipo_emenda.decode('utf-8').upper() + ') - ' +  autoria + ' - ' + emenda.txt_ementa + nom_resultado
          lst_emendas.append(dic_emenda)
          cod_emenda = emenda.cod_emenda
          lst_qtde_emendas.append(cod_emenda)
      dic_votacao["emendas"] = lst_emendas
      dic_votacao["qtde_emenda"] = len(lst_qtde_emendas)

      lst_votacao.append(dic_votacao)

  ata_dic["lst_votacao"] = lst_votacao

  # Lista das materias em 1a discussao
  lst_pdiscussao=[]
  for pdiscussao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_turno=1, ind_excluido=0):  
      materia = context.zsql.materia_obter_zsql(cod_materia=pdiscussao.cod_materia)[0]
      autores = context.zsql.autoria_obter_zsql(cod_materia=pdiscussao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
      materia = str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa + " Autoria: "+ autoria
      lst_pdiscussao.append(materia)
  ata_dic["pdiscussao"] = '; '.join(['%s' % (value) for (value) in lst_pdiscussao])

  # Lista das materias em 2a discussao
  lst_sdiscussao=[]
  for sdiscussao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_turno=2, ind_excluido=0):    
      materia = context.zsql.materia_obter_zsql(cod_materia=sdiscussao.cod_materia)[0]
      autores = context.zsql.autoria_obter_zsql(cod_materia=sdiscussao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
      materia = str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa + " Autoria: "+ autoria
      lst_sdiscussao.append(materia)
  ata_dic["sdiscussao"] = '; '.join(['%s' % (value) for (value) in lst_sdiscussao])

  # Lista das materias em discussao unica
  lst_discussao_unica=[]
  for discussao_unica in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_turno=3, ind_excluido=0):  
      materia = context.zsql.materia_obter_zsql(cod_materia=discussao_unica.cod_materia)[0]
      autores = context.zsql.autoria_obter_zsql(cod_materia=discussao_unica.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	for field in fields:
                nome_autor = autor['nom_autor_join']
	lista_autor.append(nome_autor)
      autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
      materia = str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa + " Autoria: "+ autoria
      lst_discussao_unica.append(materia)
  ata_dic["discussao_unica"] = '; '.join(['%s' % (value) for (value) in lst_discussao_unica])

  # Lista de oradores nas Explicacoes Pessoais
  lst_explicacoes_pessoais = []
  for orador in context.zsql.oradores_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
      for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador.cod_parlamentar,ind_excluido=0):
          num_ordem = orador.num_ordem
          nom_completo = parlamentar.nom_parlamentar
          lst_explicacoes_pessoais.append(nom_completo)
  ata_dic['explicacoes_pessoais'] = ', '.join(['%s' % (value) for (value) in lst_explicacoes_pessoais])

  # Presidente
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
  ata_dic['presidente'] = ''
  for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
    for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
      for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
        ata_dic['presidente'] = presidencia.nom_completo
  # 1o. Secretario
  ata_dic['1secretario'] = ''
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for cod_psecretario in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=3):
      for psecretaria in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_psecretario.cod_parlamentar):
        ata_dic['1secretario'] = psecretaria.nom_completo
  # 2o. Secretario
  ata_dic['2secretario'] = ''
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for cod_ssecretario in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=4):
      for ssecretaria in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_ssecretario.cod_parlamentar):
        ata_dic['2secretario'] = ssecretaria.nom_completo

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
  ata_dic['nom_camara'] = casa['nom_casa']
  ata_dic['end_camara'] = casa['end_casa']
  ata_dic["nom_estado"] = nom_estado
  for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
      ata_dic['nom_localidade']= local.nom_localidade
      ata_dic['sgl_uf']= local.sgl_uf

return st.ata_gerar_odt(ata_dic, nom_arquivo)

