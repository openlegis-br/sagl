## Script (Python) "quantidade_presentes_expediente_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

presenca=0
try:
  presenca = context.zsql.presenca_expediente_contar_zsql(cod_sessao_plen=cod_sessao_plen)[0].presenca
except:
  pass
return presenca
