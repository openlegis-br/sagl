## Script (Python) "data_corrente_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=ano_corrente=0
##title=
##
x=DateTime()
if ano_corrente:
   s=""
   s=DateTime.year(x)
   x=""
   x=s
return DateTime.year(DateTime())
