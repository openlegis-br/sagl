## Script (Python) "oradores_sessao_anterior_incluir"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

cod_sessao_anterior = int(cod_sessao_plen) - 1

lst_oradores = []

oradores = context.zsql.oradores_expediente_obter_zsql(cod_sessao_plen=cod_sessao_anterior)

for orador in oradores:
    ultimo = len(oradores)

for orador in oradores:
    dic = {}
    dic['cod_parlamentar'] = orador.cod_parlamentar
    if orador.num_ordem == ultimo:
       lst_oradores.append(dic)

for orador in oradores:
    dic = {}
    dic['cod_parlamentar'] = orador.cod_parlamentar
    if orador.num_ordem != ultimo:
       lst_oradores.append(dic)

lista = [(i + 1, j) for i, j in enumerate(lst_oradores)]

for i, dic in lista:
  context.zsql.oradores_expediente_incluir_zsql(cod_parlamentar=dic.get('cod_parlamentar',dic), num_ordem=i, cod_sessao_plen=cod_sessao_plen)

return 1

