## Script (Python) "votacao_assinalar_voto_presidente_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=dat_ordem="", cod_sessao_plen="", cod_materia="" 
##title=
##

presenca=0
tvotos=0
try:
  presenca = context.zsql.presenca_ordem_dia_contar_zsql(dat_ordem=dat_ordem, cod_sessao_plen=cod_sessao_plen)[0].presenca
  votacao  = context.zsql.votacao_materia_obter_zsql(dat_ordem=dat_ordem, cod_sessao_plen=cod_sessao_plen, cod_materia=cod_materia)[0]
  tvotos   = int(votacao.num_votos_sim) + int(votacao.num_votos_nao) + int(votacao.num_abstencao)
  if (presenca==tvotos):
     return 1
  else:
     pass
except:
  pass
return 0
