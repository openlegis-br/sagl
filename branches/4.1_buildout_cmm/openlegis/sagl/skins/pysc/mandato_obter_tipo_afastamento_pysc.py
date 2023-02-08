## Script (Python) "mandato_obter_tipo_fim_afastamento_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_afastamento
##title=
##
'''Esse script tem como finalidade retornar a descrição do tipo fim de afastamento''' 

des_afastamento=" "
if str(tip_afastamento)==" ":
   return des_afastamento

n=int(tip_afastamento)
try:
  des_afastamento=zsql.tipo_afastamento_obter_zsql(tip_afastamento=n)[0].des_afastamento
except:
  pass
return des_afastamento
