## Script (Python) "bla"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=instancia=None
##title=
##

root = context.portal_url.getPortalObject()

# Verifica o tipo do conector do banco de dados
# Caso necessite mudar a instancia, customize o script e faça a mudança necessária
if root.objectValues('Z MySQL Database Connection'):
    return 1
else:
    return 0
