## Script (Python) "presenca_sessao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

materias_ordem = context.zsql.ordem_dia_obter_zsql(cod_sessao_plen = cod_sessao_plen)
return len(materias_ordem)
