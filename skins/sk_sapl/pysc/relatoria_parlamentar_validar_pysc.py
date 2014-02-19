## Script (Python) "relatoria_parlamentar_validar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data="", data2="" 
##title=
##

''' Este Script compara das datas de designação do parlamentar para composição da Comissão (data2) e a de designação da relatoria (data) '''

datd = data[6:] + data[3:5] + data[0:2]
datd_r = int(datd)
datc = data2[6:] + data2[3:5] + data2[0:2]
datc_c = int(datc)

if (datd_r < datc_c):
   return '1'

return ''



