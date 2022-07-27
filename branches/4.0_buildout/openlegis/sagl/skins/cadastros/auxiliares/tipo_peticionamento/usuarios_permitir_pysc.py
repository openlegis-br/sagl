## Script (Python) "usuarios_permitir_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_peticionamento,cod_usuario=""
##title=
##

lista_usuarios=context.zsql.usuario_peticionamento_obter_zsql(tip_peticionamento=tip_peticionamento)

usuarios=[]

for usuario in lista_usuarios:
  usuarios.append(str(usuario.cod_usuario))

if cod_usuario == ['0']:
  context.zsql.usuario_peticionamento_excluir_zsql(tip_peticionamento=tip_peticionamento, cod_usuario=cod_usuario)

elif cod_usuario != ['0']:
  for i in cod_usuario:
    if str(i) not in usuarios:
      context.zsql.usuario_peticionamento_incluir_zsql(tip_peticionamento=tip_peticionamento, cod_usuario=i)
  for i in usuarios:
    if str(i) not in cod_usuario:
      context.zsql.usuario_peticionamento_excluir_zsql(tip_peticionamento=tip_peticionamento, cod_usuario=i)

return 1

