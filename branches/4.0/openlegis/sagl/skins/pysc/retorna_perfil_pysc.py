## Script (Python) "retorna_perfil_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
perfil = []
perfil_aux = context.REQUEST.AUTHENTICATED_USER.getRoles()
for item in perfil_aux:
  if item != 'Alterar Senha':
    perfil.append(item)
return perfil
