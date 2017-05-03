## Script (Python) "composicao_comissao_obter_proximo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
'''Esse script tem como finalidade obter proximo codigo valido para inclusao de composicao comissao''' 

cod_comp_comissao=context.zsql.composicao_comissao_obter_proximo_zsql()[0].cod_comp_comissao
return int(cod_comp_comissao)
