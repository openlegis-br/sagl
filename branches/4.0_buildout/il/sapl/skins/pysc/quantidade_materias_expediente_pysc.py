## Script (Python) "quantidade_materias_expediente_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

materias_expediente = context.zsql.expediente_materia_obter_zsql(cod_sessao_plen = cod_sessao_plen)
return len(materias_expediente)
