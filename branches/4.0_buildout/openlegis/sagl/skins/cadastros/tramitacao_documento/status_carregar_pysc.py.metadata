## Script (Python) "destinos_carregar"
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

status = context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = svalue)
 
fields = status.data_dictionary().keys()

listaDic={}     
statusArray = []

dic = {}
dic['name'] = 'Selecione'
dic['id'] = ''
statusArray.append(dic)

for item in status:
    status_permitidos = item['status_permitidos_sel']

for item in string.split(str(status_permitidos),','):
    statusDict = {}
    for unidade in context.zsql.status_tramitacao_obter_zsql(cod_status = item):
        statusDict['name'] = unidade['des_status']
        statusDict['id'] = unidade['cod_status']
    statusArray.append(statusDict)

listaDic.update({'options': statusArray})
    
return json.dumps(statusArray)
