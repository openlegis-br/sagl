## Script (Python) "tipo_autor_prox_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
proximo_tipo_autor=0

try:
  proximo_tipo_autor=context.zsql.tipo_autor_prox_obter_zsql()[0].proximo_tipo_autor
except:
  proximo_tipo_autor=1

return proximo_tipo_autor
