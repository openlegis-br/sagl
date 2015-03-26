## Script (Python) "voto_parlamentar_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_votacao, cod_parlamentar 
##title=
##
try:
  voto=context.zsql.voto_parlamentar_obter_zsql(cod_votacao=cod_votacao, cod_parlamentar=cod_parlamentar)[0].voto
except:
  voto=""
  return 0
return 1
