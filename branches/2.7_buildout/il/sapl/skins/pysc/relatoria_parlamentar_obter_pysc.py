## Script (Python) "relatoria_parlamentar_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=dados="", parm=""
##title=
##
"""
  Função: separar as variáveis cod_parlamentar e dat_designacao do parlamentar na composição da Comissão
  
  Argumento: Dados: cod_parlamentar - dat_designacao; se parm="" --> retorna cod_parlamentar, se parm=1 --> retorna dat_designacao.

"""  

import string

x=string.split(dados)

if parm!='1':
   return x[0]

return x[2]



