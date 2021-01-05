##parameters=type_name, id, **kw
##title=Add an object to a folder
##
context.invokeFactory(type_name, id, context.REQUEST.RESPONSE)

return context.setStatus(True)
