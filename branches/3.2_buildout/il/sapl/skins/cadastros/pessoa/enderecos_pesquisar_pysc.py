## Script (Python) "enderecos_pesquisar_pysc"
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

listaDic={} 	
enderecoArray = []

for endereco in context.zsql.pessoa_endereco_obter_zsql():
  enderecoDict = {}
  enderecoDict['text']  = endereco['end_residencial']
  enderecoDict['value'] = endereco['end_residencial']
  enderecoArray.append(enderecoDict)

listaDic.update({'options': enderecoArray})

return json.dumps(listaDic)
