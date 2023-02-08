## Script (Python) "usuarios_permitir_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_peticionamento, cod_usuario=""
##title=
##

v=str(cod_usuario)
if v.isdigit():
   lst_usuario = [cod_usuario]
else:
   lst_usuario = cod_usuario

lista_usuarios=context.zsql.usuario_peticionamento_obter_zsql(tip_peticionamento=tip_peticionamento)

usuarios=[]

for usuario in lista_usuarios:
  usuarios.append(str(usuario.cod_usuario))

if lst_usuario == '' and tip_peticionamento != '':
  for item in usuarios:
      context.zsql.usuario_peticionamento_excluir_zsql(tip_peticionamento=tip_peticionamento, cod_usuario=item)

elif lst_usuario != '':
  for i in lst_usuario:
    if str(i) not in usuarios:
      context.zsql.usuario_peticionamento_incluir_zsql(tip_peticionamento=tip_peticionamento, cod_usuario=i)
  for i in usuarios:
    if str(i) not in lst_usuario:
      context.zsql.usuario_peticionamento_excluir_zsql(tip_peticionamento=tip_peticionamento, cod_usuario=i)

return 1

