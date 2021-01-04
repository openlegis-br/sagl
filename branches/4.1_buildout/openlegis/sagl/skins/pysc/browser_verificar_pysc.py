## Script (Python) "browser_verificar_pysc"
##bind container=container
##bind context=context
##bind namespace=_
##bind script=script
##bind subpath=traverse_subpath
##parameters=user_agent
##title=
##
import string
a=-1
if string.rfind(user_agent, "MSIE")==a:
   return 0
else:
   return 1
