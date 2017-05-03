## Script (Python) "busca_palavra_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= 
##title=
##
import simplejson as json

context.REQUEST.RESPONSE.setHeader("Access-Control-Allow-Origin", "*")

autores = context.zsql.autor_obter_zsql(nom_autor_match = context.REQUEST.get('nom_autor'))
 
fields = autores.data_dictionary().keys()

listaDic={} 	
autorArray = []
for autor in autores:
	autorDict = {}
	for field in fields:
                autorDict['text'] = autor['nom_autor_join']
                autorDict['value'] = autor['cod_autor']
#                autor['value'] = field['nom_autor_join']
#		autorDict[field] = autor[field]
	
	autorArray.append(autorDict)

listaDic.update({'options': autorArray})
 	
return json.dumps(listaDic)

#j = json.dumps(listaDic)
#autores_file = 'lista_autores.json'
#return autores_file
