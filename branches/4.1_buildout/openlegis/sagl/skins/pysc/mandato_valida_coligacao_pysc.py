## Script (Python) "mandato_valida_coligacao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lst_num_legislatura,lst_cod_coligacao
##title=
##
'''Esse script tem como finalidade validar coligacao indicada na inclusao de mandato''' 

if (lst_cod_coligacao==""):
   return true

n=int(lst_num_legislatura.split('ª')[0])
try:
  nc=zsql.coligacao_obter_zsql(num_legislatura=n, cod_coligacao=lst_cod_coligacao)[0].nom_coligacao
  return true
except:
  return false
