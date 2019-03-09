## Script (Python) "documento_validar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=codigo
##title=
##
request=context.REQUEST
response=request.RESPONSE

id_documento = "%s"%codigo+'_texto_integral_signed.pdf'

if hasattr(context.sapl_documentos.administrativo, id_documento):
   arquivo = getattr(context.sapl_documentos.administrativo,id_documento)
   context.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
   context.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %id_documento)
   return arquivo
else:
   return 'Documento Inexistente'
