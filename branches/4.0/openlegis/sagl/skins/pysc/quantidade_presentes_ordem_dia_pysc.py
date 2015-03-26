## Script (Python) "quantidade_presentes_ordem_dia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=dat_ordem, cod_sessao_plen
##title=
##

presenca=0
try:
  presenca = context.zsql.presenca_ordem_dia_contar_zsql(dat_ordem=dat_ordem, cod_sessao_plen=cod_sessao_plen)[0].presenca
except:
  pass
return presenca
