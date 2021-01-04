## Script (Python) "materia_apreciada"
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

  # Lista das materias da Ordem do Dia
  lst_votacao=[]
  for votacao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):  
     # Seleciona os detalhes de uma matéria
      materia = context.zsql.materia_obter_zsql(cod_materia=votacao.cod_materia)[0]
      dic_votacao = {}
      dic_votacao["num_ordem"] = votacao.num_ordem
      dic_votacao["tip_materia"] = materia.des_tipo_materia.decode('utf-8').upper()
      dic_votacao["num_ident_basica"] = materia.num_ident_basica
      dic_votacao["ano_ident_basica"] = materia.ano_ident_basica
      dic_votacao["des_numeracao"]=""
      numeracao = context.zsql.numeracao_obter_zsql(cod_materia=votacao.cod_materia)
      if len(numeracao):
         numeracao = numeracao[0]
         dic_votacao["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
      dic_votacao["des_turno"]=""
      for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=votacao.tip_turno):
         dic_votacao["des_turno"] = turno.des_turno                  
      dic_votacao["txt_ementa"] = materia.txt_ementa
      dic_votacao["nom_autor"] = ''
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

return st.materia_apreciada_gerar_odt(inf_basicas_dic, lst_votacao)
