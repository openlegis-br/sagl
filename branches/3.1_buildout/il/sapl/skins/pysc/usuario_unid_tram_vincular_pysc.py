## Script (Python) "usuario_unid_tram_vincular_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_usuario,cod_unid_tramitacao=""
##title=
##

lista_unidades=context.zsql.usuario_unid_tram_obter_zsql(cod_usuario=cod_usuario)

unidades=[]

for unidade in lista_unidades:
  unidades.append(str(unidade.cod_unid_tramitacao))

if cod_unid_tramitacao == '':
  context.zsql.usuario_unid_tram_excluir_zsql(cod_usuario=cod_usuario)

else:
  for i in cod_unid_tramitacao:
    if str(i) not in unidades:
      context.zsql.usuario_unid_tram_incluir_zsql(cod_usuario=cod_usuario,cod_unid_tramitacao=i)

  for i in unidades:
    if str(i) not in cod_unid_tramitacao:
      context.zsql.usuario_unid_tram_excluir_zsql(cod_usuario=cod_usuario,cod_unid_tramitacao=i)

return 1

