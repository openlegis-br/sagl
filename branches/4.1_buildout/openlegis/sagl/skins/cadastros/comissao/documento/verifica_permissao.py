## Script (Python) "verifica_permissao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=file
##title=

from AccessControl.PermissionRole import rolesForPermissionOn
roles = rolesForPermissionOn('View', file)
return roles

