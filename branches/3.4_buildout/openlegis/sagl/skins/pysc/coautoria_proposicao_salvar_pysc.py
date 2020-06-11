## Script (Python) "coautoria_proposicao_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao,cod_autor=""
##title=
##

lista_coautores=context.zsql.coautoria_proposicao_obter_zsql(cod_proposicao=cod_proposicao,ind_excluido=0)

autores=[]

for autor in lista_coautores:
  autores.append(str(autor.cod_autor))

if cod_autor == '':
  context.zsql.coautoria_proposicao_excluir_zsql(cod_proposicao=cod_proposicao)

else:
  for i in cod_autor:
    if str(i) not in autores:
      context.zsql.coautoria_proposicao_incluir_zsql(cod_proposicao=cod_proposicao,cod_autor=i)

  for i in autores:
    if str(i) not in cod_autor:
      context.zsql.coautoria_proposicao_excluir_zsql(cod_proposicao=cod_proposicao,cod_autor=i)

return 1

