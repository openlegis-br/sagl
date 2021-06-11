## Script (Python) "exibe_autor_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_autor
##title=
##

for autor in context.zsql.autor_obter_zsql(cod_autor=int(cod_autor)):
    nom_autor = autor.nom_autor_join

return nom_autor

