## Script (Python) "titulo_doc_salvar_proc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id, title
##title=
##

if hasattr(context.sapl_documentos.modelo.materia.documento_acessorio,id):
   arquivo = getattr(context.sapl_documentos.modelo.materia.documento_acessorio,id)
   arquivo.manage_changeProperties(title=title)
   return title
