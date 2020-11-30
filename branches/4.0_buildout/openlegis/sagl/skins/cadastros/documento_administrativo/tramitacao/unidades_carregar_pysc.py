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

unidades = context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = svalue)
 
fields = unidades.data_dictionary().keys()

listaDic={}     
unidadeArray = []

unidades_destino = None

if svalue == '0':
   dic = {}
   dic['name'] = ''
   dic['id'] = '0'
   unidadeArray.append(dic)

for unidade in unidades:
    unidades_destino = unidade['unid_dest_permitidas_sel']

if unidades_destino != None:
   if svalue != '0':
      dic = {}
      dic['name'] = 'Selecione'
      dic['id'] = '0'
      unidadeArray.append(dic)
   for item in string.split(str(unidades_destino),','):
       unidadeDict = {}
       for unidade in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = item):
           if unidade.ind_leg == 1:
              unidadeDict['name'] = unidade['nom_unidade_join']
              unidadeDict['id'] = unidade['cod_unid_tramitacao']
              unidadeArray.append(unidadeDict)
   listaDic.update({'options': unidadeArray})
else:
   if svalue != '0':
      unidadeDict = {}
      unidadeDict['name'] = '* Configure as permissões da unidade da origem !'
      unidadeDict['id'] = ''
      unidadeArray.append(unidadeDict)

listaDic.update({'options': unidadeArray})
    
return json.dumps(unidadeArray)
