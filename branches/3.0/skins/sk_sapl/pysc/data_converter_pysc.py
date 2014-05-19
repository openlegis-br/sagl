## Script (Python) "data_converter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data
##title=
##
"""
  Função: Converter a data do formato DD/MM/AAAA para
          o formato AAAA/MM/DD, utilizado para gravar 
          no formato aceito pelo banco de dados.
  
  Argumento: Data a ser convertida.
  
  Retorno: Data convertida.
"""
if data != '':
   return data[6:] + '/' + data[3:5] + '/' + data[0:2]
else:
   return ''
