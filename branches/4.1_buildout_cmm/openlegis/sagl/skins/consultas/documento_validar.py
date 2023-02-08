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

decoded = context.pysc.b64decode_pysc(codigo=str(codigo))
id_documento = "%s"%decoded+'_texto_integral_signed.pdf'

if hasattr(context.sapl_documentos.administrativo, id_documento):
   for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=decoded):
       for tipo_documento in context.zsql.tipo_documento_administrativo_obter_zsql(tip_documento=documento.tip_documento):
           nom_pdf_amigavel = str(tipo_documento.des_tipo_documento.decode('utf-8').upper())+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+".pdf"
   arquivo = getattr(context.sapl_documentos.administrativo,id_documento)
   context.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
   context.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)
   return arquivo
else:
   return 'Erro de validação. Documento inexistente!'
