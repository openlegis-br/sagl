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
dat_apresentacao = DateTime(context.pysc.data_converter_pysc(txt_dat_apresentacao))
codigo = str(cod_parlamentar)
autores = context.zsql.autores_obter_zsql(txt_dat_apresentacao=txt_dat_apresentacao) or []

for p in autores:
  s = str(p.cod_parlamentar)
  if s == codigo:
    for item in context.zsql.afastamento_obter_zsql(cod_parlamentar=codigo):
     dat_inicio = DateTime(item.dat_inicio)
     dat_fim = DateTime(item.dat_fim)
     if dat_inicio < dat_apresentacao < dat_fim:
       return 0
    else: 
     return 1





