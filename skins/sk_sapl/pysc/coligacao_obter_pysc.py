## Script (Python) "coligacao_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lst_cod_coligacao=""
##title=
##
'''Esse script tem como finalidade retornar o codigo da coligacao''' 

codigo=None
if (lst_cod_coligacao):
   try:
     codigo=zsql.coligacao_obter_zsql(nom_coligacao=lst_cod_coligacao)[0].cod_coligacao
   except:
     pass
return codigo

