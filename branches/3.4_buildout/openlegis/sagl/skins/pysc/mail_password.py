## Script (Python) "mail_password"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=userid
##title=
##
REQUEST=context.REQUEST
return context.portal_sagl.mailPassword(userid, REQUEST)
