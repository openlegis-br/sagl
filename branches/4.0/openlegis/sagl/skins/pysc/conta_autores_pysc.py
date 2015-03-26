## Script (Python) "conta_autores_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
##
"""
  Esse script tem como finalidade retornar a quantidade de autores de uma materia
"""
qtd=None
try:
  qtd=context.zsql.autor_contar_zsql(cod_materia=cod_materia)[0].qtd_autores
except:
  pass
return qtd

