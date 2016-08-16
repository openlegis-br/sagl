## Script (Python) "relatoria_comissao_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia="", parm="" 
##title=
##
try:
  if parm:
     resultado=context.zsql.relatoria_comissao_obter_zsql(cod_materia=cod_materia)[0].nom_comissao
  else:
     resultado=context.zsql.relatoria_comissao_obter_zsql(cod_materia=cod_materia)[0].cod_comissao
except:
  resultado="O local atual deve ser uma Comissao!"
return resultado
