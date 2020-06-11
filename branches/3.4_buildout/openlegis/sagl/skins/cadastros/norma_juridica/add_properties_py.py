## Script (Python) "add_properties_py"
##bind container=container
##bind context=context
##bind namespace=_
##bind script=script
##bind subpath=traverse_subpath
##parameters=id_documento='',inclusao=0
##title=
##
request = context.REQUEST
if id_documento:
 doc = getattr(context.this().documentos.norma_juridica, str(id_documento))
 if inclusao==1:
  doc.manage_addProperty(id='cod_norma',value=request.hdn_cod_norma,type='string')
 else:
  doc.manage_changeProperties(request)
 doc.reindex_object()
return 1
