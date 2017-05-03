## Script (Python) "comp_cargo_mesa_contar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_cargo
##title=
##
"""
  Esse script retorna a quantidade de parlamentares em cargo da mesa diretora
"""
qtd=None
try:
  qtd=context.zsql.cargo_mesa_consultar_zsql(cod_cargo=cod_cargo)[0].qtd_designados
except:
  pass
return qtd

