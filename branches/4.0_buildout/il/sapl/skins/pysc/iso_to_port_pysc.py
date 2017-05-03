## Script (Python) "iso_to_port_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tudo
##title=
##
tudo=str(tudo)
if len(tudo) > 0:
 datapart=string.split(tudo,' ')
 if string.find(datapart[0],'-')!=-1:
  data=string.split(datapart[0],'-')
 elif string.find(datapart[0],'/')!=-1:
  data=string.split(datapart[0],'/')
 if len(datapart) > 1:
  return data[2]+'/'+data[1]+'/'+data[0]
  #return data[2]+'/'+data[1]+'/'+data[0]+' '+string.split(datapart[1], '-')[0]
 else:
  return data[2]+'/'+data[1]+'/'+data[0]
else:
 return ''
