## Script (Python) "extrai_id_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id=""
##title=
##
""" Retorna id somente com números. """
x=id
y=['0','1','2','3','4','5','6','7','8','9']
z=''
for i in x:
 if i in y:
  z=z+i
return z
