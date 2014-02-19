## Script (Python) "mandato_coligacao_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lst_num_legislatura="", lst_cod_coligacao=""
##title=
##
'''Esse script tem como finalidade validar coligacao indicada na inclusao de mandato''' 

if not lst_cod_coligacao:
   return ""

n=int(lst_num_legislatura.split('ª')[0])
nc=""
try:
  nc=context.zsql.coligacao_obter_zsql(num_legislatura=n, cod_coligacao=lst_cod_coligacao)[0].cod_coligacao
except:
  pass
return nc

