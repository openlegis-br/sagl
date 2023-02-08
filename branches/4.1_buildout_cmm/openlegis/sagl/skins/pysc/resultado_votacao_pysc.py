## Script (Python) "retorna_resultado_votacao_da_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_votacao, cod_materia 
##title=
##
try:
  resultado=context.zsql.resultado_votacao_obter_zsql(cod_votacao=cod_votacao, cod_materia=cod_materia)[0].nom_resultado
except:
  resultado="ainda não consta o resultado"
return resultado
