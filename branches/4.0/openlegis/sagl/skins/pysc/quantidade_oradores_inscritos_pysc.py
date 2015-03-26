## Script (Python) "presenca_sessao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

oradores_inscritos = context.zsql.oradores_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0)
return len(oradores_inscritos)