## Script (Python) "autoria_parlamentar_validar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=txt_dat_apresentacao, cod_parlamentar
##title=
##
"""
  Função: validar se o parlamentar pode ou não ser autor de materia legislativa na data da apresentação indicada
  
  Argumentos: txt_dat_apresentacao e cod_parlamentar  --> retorna 1-verdadeiro ou 0-falso.

"""  
codigo = str(cod_parlamentar)
autores = context.zsql.autores_obter_zsql(txt_dat_apresentacao=txt_dat_apresentacao) or []
for p in autores:
     s = str(p.cod_parlamentar)
     if s == codigo:
        return 1
return 0



