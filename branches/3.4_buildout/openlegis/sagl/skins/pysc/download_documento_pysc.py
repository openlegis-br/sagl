## Script (Python) "download_documento_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento
##title=
##
request=context.REQUEST
response=request.RESPONSE

if cod_documento.isdigit():
 cod_documento = cod_documento
else:
 cod_documento = context.pysc.b64decode_pysc(codigo=str(cod_documento))

for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento = cod_documento):
    download_name = documento.des_tipo_documento.replace(" ", "_") + "-" + str(documento.num_documento)+ "-" + str(documento.ano_documento) + ".pdf"
    id_documento = "%s"%cod_documento+'_texto_integral.pdf'
    arquivo = getattr(context.sagl_documentos.adminitrativo,id_documento) 
    context.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
    context.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; Filename=%s' % download_name)

return arquivo

