## Script (Python) "current_year_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
data=DateTime().ISO()
ano=data[:4]
return int(ano)
