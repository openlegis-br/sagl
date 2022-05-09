## Script (Python) "modelos_carregar"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters = svalue
##title=
##
import simplejson as json

context.REQUEST.RESPONSE.setHeader("Access-Control-Allow-Origin", "*")

tipo_materia = None
if svalue != '0' and svalue != '':
   for tipo in context.zsql.tipo_peticionamento_obter_zsql(tip_peticionamento=int(svalue)):
       prefixo = str(tipo.tip_peticionamento) + '-'      
       tipo_materia = tipo.des_tipo_peticionamento

modelos=[]      

if svalue == '0' and svalue == '':
   dic = {}
   dic['titulo_arquivo'] = '- Selecione um modelo -'
   dic['id_arquivo'] = '0'
   dic['path_arquivo']  = ''
   modelos.append(dic)

if svalue != '0' and svalue != '':
   dic = {}
   dic['titulo_arquivo'] = '- selecione um modelo -'
   dic['id_arquivo'] = '0'
   dic['path_arquivo']  = ''      
   modelos.append(dic)
   for modelo in context.sapl_documentos.modelo.peticionamento.objectValues('File'):
       dic ={}
       if modelo.title != '':
          dic['titulo_arquivo'] = str(modelo.title)
       else:
          dic['titulo_arquivo'] = modelo.getId()              
       dic['id_arquivo'] = modelo.getId() 
       dic['path_arquivo'] = modelo.virtual_url_path() 
       if prefixo in modelo.getId():
          modelos.append(dic)

   modelos.sort(key=lambda dic: dic['titulo_arquivo'])

return json.dumps(modelos)
