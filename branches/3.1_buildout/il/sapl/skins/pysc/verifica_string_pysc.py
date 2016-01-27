## Script (Python) "verifica_string_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=valor
##title=
##
v=valor
if isinstance(v, str):
   return 1
else:
   return 0
