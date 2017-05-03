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

usuarios = context.zsql.usuario_unid_tram_obter_zsql(cod_unid_tramitacao = context.REQUEST.get('svalue'))
 
fields = usuarios.data_dictionary().keys()

listaDic={} 	
usuarioArray = []
for usuario in usuarios:
	usuarioDict = {}
	for field in fields:
                usuarioDict['text'] = usuario['nom_completo']
                usuarioDict['value'] = usuario['cod_usuario']
	usuarioArray.append(usuarioDict)

listaDic.update({'options': usuarioArray})
 	
return json.dumps(listaDic)

