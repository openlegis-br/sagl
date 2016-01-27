## Script (Python) "port_to_iso_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=data
##title=
##
data = string.strip(data)
if data!='':
 datapart=string.split(data,' ')
 data=string.split(datapart[0],'/')
 if len(datapart) > 1:
  return data[2]+'-'+data[1]+'-'+data[0]+' '+datapart[1]
 else:
  return data[2]+'-'+data[1]+'-'+data[0]
