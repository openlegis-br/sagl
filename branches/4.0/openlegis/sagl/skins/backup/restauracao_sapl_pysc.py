## Script (Python) "restauracao_sagl_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=caminho
##title=
##
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION
nome="bkpbancosagl"

oque=context.restaura_backup(banco='interlegis',caminho=caminho,nome=nome)

if oque=="sistema e do banco de dados": #Importa o SAPL

   root = context.aq_parent.aq_parent   
   old = 'sagl_' + context.ZopeTime().strftime('%Y%m%d%H%M%S')
   root.manage_renameObjects(['sagl'],[old])
   try:
      root.manage_importObject("sagl.zexp")
   except:
      root.manage_renameObjects([old],['sagl'])

else: #Importa a pasta 'documentos'

   root=context.aq_parent
   old = 'documentos_' + context.ZopeTime().strftime('%Y%m%d%H%M%S')
   root.manage_renameObjects(['documentos'],[old])
   try:
      root.manage_importObject("documentos.zexp")
   except:
      root.manage_renameObjects([old],['documentos'])

context.apaga_residuos(nome)

return response.redirect('backup_sagl?restaurar_arq=%s'%oque)
