## Script (Python) "tipo_peticionamento_permitir_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_usuario,tip_peticionamento=""
##title=
##

lista_peticionamentos=context.zsql.usuario_peticionamento_obter_zsql(cod_usuario=cod_usuario)

peticionamentos=[]

for peticionamento in lista_peticionamentos:
  peticionamentos.append(str(peticionamento.tip_peticionamento))

if tip_peticionamento == ['0']:
  context.zsql.usuario_peticionamento_excluir_zsql(cod_usuario=cod_usuario)

elif tip_peticionamento != ['0']:
  for i in tip_peticionamento:
    if str(i) not in peticionamentos:
      context.zsql.usuario_peticionamento_incluir_zsql(cod_usuario=cod_usuario, tip_peticionamento=i)
  for i in peticionamentos:
    if str(i) not in tip_peticionamento:
      context.zsql.usuario_peticionamento_excluir_zsql(cod_usuario=cod_usuario,tip_peticionamento=i)

return 1

