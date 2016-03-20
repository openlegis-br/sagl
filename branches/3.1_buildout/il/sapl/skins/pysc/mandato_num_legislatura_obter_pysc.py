## Script (Python) "mandato_num_legislatura_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lst_num_legislatura="" 
##title=
##
'''Esse script retorna o num_legislatura para tratar mandatos''' 

return int(lst_num_legislatura.split('ª')[0])

