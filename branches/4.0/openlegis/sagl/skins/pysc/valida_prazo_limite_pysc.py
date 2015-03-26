## Script (Python) "valida_prazo_limite_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data
##title=
##
"""  Funcao: validar se há matérias com  prazo limite anterior à data informada via parâmetro
"""
"""  Argumentos: data parâmetro do prazo limite  
"""
"""  Retorno: 1-ok, há matérias, None=não há matérias cujo prazo limite seja anterior à data do parâmetro
"""

if data=='':
   return None

dat_parm_ref=context.data_converter_pysc(data)

qtde_m=0
qtde_t=0
qtde_m=context.zsql.materia_legislativa_prazo_limite_obter_zsql(data=dat_parm_ref)[0].qtde
qtde_t=context.zsql.tramitacao_prazo_limite_obter_zsql(data=dat_parm_ref)[0].qtde

qtde=qtde_m + qtde_t

if qtde==0:
   return None

""" existem matérias o prazo limite informado anterior ou igual à data parâmetro de referência da pesquisa. Ou seja, o prazo limite está vencido ou vencendo no dia!
"""
return 1 
