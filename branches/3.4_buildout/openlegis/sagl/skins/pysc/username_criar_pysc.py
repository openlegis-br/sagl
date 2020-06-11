## Script (Python) "username_criar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=username
##title=
##
passwd = context.sagl_documentos.props_sagl.txt_senha_inicial

ok = 1

if username in context.acl_users.getUserNames():
  ok = 0
else:
  context.acl_users.userFolderAddUser(username, passwd, ['Autor','Alterar Senha'], '')

return ok
