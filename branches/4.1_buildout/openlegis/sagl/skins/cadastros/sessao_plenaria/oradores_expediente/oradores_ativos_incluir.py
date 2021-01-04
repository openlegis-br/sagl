## Script (Python) "oradores_ativos_incluir"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, dat_sessao
##title=
##

lst_oradores = []

oradores = context.zsql.autores_obter_zsql(txt_dat_apresentacao=dat_sessao)

for orador in oradores:
    dic = {}
    dic['cod_parlamentar'] = orador.cod_parlamentar
    lst_oradores.append(dic)

lista = [(i + 1, j) for i, j in enumerate(lst_oradores)]

for i, dic in lista:
  context.zsql.oradores_expediente_incluir_zsql(cod_parlamentar=dic.get('cod_parlamentar',dic), num_ordem=i, cod_sessao_plen=cod_sessao_plen)

return 1
