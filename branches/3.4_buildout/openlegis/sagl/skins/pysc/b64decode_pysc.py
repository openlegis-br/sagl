## Script (Python) "b64encode_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=codigo
##title=
##

import base64

codigo = base64.b64decode(codigo)

return codigo
