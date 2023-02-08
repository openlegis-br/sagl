## Script (Python) "busca_palavra_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= svalue
##title=
##
import simplejson as json

context.REQUEST.RESPONSE.setHeader("Access-Control-Allow-Origin", "*")

if svalue != '':
   usuarios = context.zsql.usuario_unid_tram_obter_zsql(cod_unid_tramitacao = svalue)
   fields = usuarios.data_dictionary().keys()
   listaDic={}     
   usuarioArray = []
   dic = {}
   dic['name'] = ''
   dic['id'] = ''
   usuarioArray.append(dic)
   for usuario in usuarios:
       usuarioDict = {}
       for field in fields:
           usuarioDict['name'] = usuario['nom_completo']
           usuarioDict['id'] = usuario['cod_usuario']
       usuarioArray.append(usuarioDict)
   listaDic.update({'options': usuarioArray})
   return json.dumps(usuarioArray)
else:
   listaDic={}     
   usuarioArray = []
   usuarioDict = {}
   usuarioDict['name'] = ''
   usuarioDict['id'] = ''
   usuarioArray.append(usuarioDict)
   listaDic.update({'options': usuarioArray})
   return json.dumps(usuarioArray)  
