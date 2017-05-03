## Script (Python) "tipo_afastamento_validar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lst_tip_afastamento
##title=
##
'''Esse script tem como finalidade validar o codigo do tipo de afastamento de parlamentar''' 

codigo=0
tipo=0
if (lst_tip_afastamento):
   try:
     tipo=int(lst_tip_afastamento)
     codigo=context.zsql.tipo_afastamento_obter_zsql(tip_afastamento=tipo)[0].tip_afastamento
     return codigo  
   except:
     pass
return codigo

