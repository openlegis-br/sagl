## Script (Python) "validar_parlamentar_composicao_comissao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=datai, dataf, cod_p
##title=
##
'''Esse script tem como finalidade validar se o parlamentar tem mandato no período indicado da composicao da comissao''' 

di=datai[6:] + '-' + datai[3:5] + '-' + datai[0:2]
df=dataf[6:] + '-' + dataf[3:5] + '-' + dataf[0:2]
cod=cod_p
try:
  if (context.zsql.composicao_comissao_validar_parlamentar_zsql(dat_inicio=di, dat_fim=df, cod_parlamentar=cod)[0].cod_parlamentar):
     return 1
  else:
     return 0
except:
  return 0

