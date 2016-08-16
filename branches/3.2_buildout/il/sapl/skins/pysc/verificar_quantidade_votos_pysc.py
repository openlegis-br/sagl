## Script (Python) "verificar_quantidade_votos_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=txt_votos_sim,txt_votos_nao,txt_votos_abstencao,ivp,dat_ordem
##title=
##
qtd=None
try:
  qtd=context.zsql.presenca_ordem_dia_contar_zsql(dat_ordem=dat_ordem,ind_excluido=0)[0].presenca
  quantidade_votos = int(txt_votos_sim) + int(txt_votos_nao) + int(txt_votos_abstencao)
  if qtd != quantidade_votos:
     if ivp == 1:
        return 1
     else:
        return 0
  else:
     return 0
except:
  return 1
