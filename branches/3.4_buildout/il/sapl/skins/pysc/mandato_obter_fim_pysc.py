## Script (Python) "mandato_obter_fim_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_causa_fim_afastamento
##title=
##
'''Esse script tem como finalidade retornar a descrição do tipo de causa fim mandato''' 
##
des_dispositivo=""
if str(tip_causa_fim_afastamento)==" ":
  return des_dispositivo
   
n=int(tip_causa_fim_afastamento)

try:
  des_dispositivo=zsql.tipo_fim_mandato_obter_zsql(tip_afastamento=n)[0].des_dispositivo
except:
  pass
return des_dispositivo

