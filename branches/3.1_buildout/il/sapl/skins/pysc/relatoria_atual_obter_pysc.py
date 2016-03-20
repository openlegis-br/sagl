## Script (Python) "relatoria_atual_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=codigo="", data=""
##title=
##
"""
  Função: retornar a relatoria atual: cod_parlamentar e dat_designacao do parlamentar na composição da Comissão
  
  Argumento: Dados: codigo=cod_parlamentar, data=dat_desig_relator

"""  

import string

x=str(codigo) + ' - ' + str(data)

return x



