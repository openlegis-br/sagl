## Script (Python) "username_excluir_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=username
##title=
##
names = []
names.append(username)
ok = 1

try:
  context.acl_users.userFolderDelUsers(names)
except KeyError:
  ok = 0

return ok
