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
for item in context.zsql.tipo_proposicao_obter_zsql(tip_proposicao=int(svalue)):
    if item.ind_mat_ou_doc == 'M':
       for tipo in context.zsql.tipo_materia_legislativa_obter_zsql(tip_materia = item.tip_mat_ou_doc):
           tipo_proposicao = 'M'       
           prefixo = tipo.sgl_tipo_materia + '-'      
           tipo_materia = tipo.des_tipo_materia
    elif item.ind_mat_ou_doc == 'D':
       tipo_proposicao = 'D'       
       tipo_materia = item.des_tipo_proposicao

modelos=[]      

if svalue == '0':
   dic = {}
   dic['titulo_arquivo'] = ''
   dic['id_arquivo'] = '0'
   dic['path_arquivo']  = ''
   modelos.append(dic)

if tipo_materia != None:
   if svalue != '0':
      dic = {}
      dic['titulo_arquivo'] = ''
      dic['id_arquivo'] = '0'
      dic['path_arquivo']  = ''      
      modelos.append(dic)
   if tipo_proposicao == 'M':
      for modelo in context.sapl_documentos.modelo.materia.objectValues('File'):
          dic ={}
          if modelo.title != '':
             dic['titulo_arquivo'] = str(modelo.title)
          else:
             dic['titulo_arquivo'] = modelo.getId()              
          dic['id_arquivo'] = modelo.getId() 
          dic['path_arquivo'] = modelo.virtual_url_path() 
          if prefixo in modelo.getId():
             modelos.append(dic)    
   elif tipo_proposicao == 'D':
      if tipo_materia =='Emenda':
         for modelo in context.sapl_documentos.modelo.materia.emenda.objectValues('File'):
             dic ={}
             dic['titulo_arquivo'] = str(modelo.title)
             dic['id_arquivo'] = modelo.getId() 
             dic['path_arquivo'] = modelo.virtual_url_path() 
             modelos.append(dic)       
      elif tipo_materia =='Parecer':
         for modelo in context.sapl_documentos.modelo.materia.parecer.objectValues('File'):
             dic ={}
             dic['titulo_arquivo'] = str(modelo.title)
             dic['id_arquivo'] = modelo.getId() 
             dic['path_arquivo'] = modelo.virtual_url_path() 
             modelos.append(dic)       
      elif tipo_materia =='Substitutivo':
         for modelo in context.sapl_documentos.modelo.materia.substitutivo.objectValues('File'):
             dic ={}
             dic['titulo_arquivo'] = str(modelo.title)
             dic['id_arquivo'] = modelo.getId() 
             dic['path_arquivo'] = modelo.virtual_url_path() 
             modelos.append(dic) 
      else:   
         for modelo in context.sapl_documentos.modelo.materia.documento_acessorio.objectValues('File'):
             dic ={}
             dic['titulo_arquivo'] = str(modelo.title)
             dic['id_arquivo'] = modelo.getId() 
             dic['path_arquivo'] = modelo.virtual_url_path() 
             modelos.append(dic) 

modelos.sort(key=lambda dic: dic['titulo_arquivo'])

return json.dumps(modelos)
