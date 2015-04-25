## Script (Python) "data_converter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=hora=""
##title=
##
"""
  Função: formatar hora: hh:mm -  o formato troca : por h.
"""
if hora != '':
   return hora[0:2] + 'h' + hora[3:]
else:
   return ''
