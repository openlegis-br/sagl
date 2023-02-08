## Script (Python) "numero_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= tvalue, svalue
##title=
##
import simplejson as json

context.REQUEST.RESPONSE.setHeader("Access-Control-Allow-Origin", "*")

numeroArray = []
numero = ""
if tvalue != None:
   for item in context.zsql.numero_sessao_plenaria_obter_zsql(tip_sessao = tvalue, cod_sessao_leg = svalue):
       dic = {}
       dic['num_sessao_plen'] = item.novo_numero_sessao
       numeroArray.append(dic)
     
return json.dumps(numeroArray)
