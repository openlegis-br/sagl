## Script (Python) "ajusta_permissao.py"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_documento, ind_publico
##title=
REQUEST=context.REQUEST

for documento in context.zsql.documento_administrativo_pesquisar_publico_zsql(tip_documento=tip_documento,ind_publico=ind_publico,ind_excluido=0):
 filename = str(documento.cod_documento) + "_texto_integral.pdf"
 assinado = str(documento.cod_documento) + "_texto_integral_signed.pdf"
 if hasattr(context.sapl_documentos.administrativo, filename):
   if context.REQUEST.ind_publico == 0:
     documento = getattr(context.sapl_documentos.administrativo,filename)
     documento.manage_permission('View', roles=['Authenticated', 'Manager','Operador','Operador Modulo Administrativo'], acquire=1)
   if context.REQUEST.ind_publico == 1:
     documento = getattr(context.sapl_documentos.administrativo,filename)
     documento.manage_permission('View', roles=['Anonymous','Manager','Operador','Operador Materia','Operador Modulo Administrativo'], acquire=0)
     documento.manage_permission('Delete objects', roles=['Manager','Operador','Operador Materia','Operador Modulo Administrativo'], acquire=0)
 if hasattr(context.sapl_documentos.administrativo, assinado):
   if context.REQUEST.ind_publico == 0:
     documento = getattr(context.sapl_documentos.administrativo,assinado)
     documento.manage_permission('View', roles=['Authenticated', 'Manager','Operador','Operador Modulo Administrativo'], acquire=1)
   if context.REQUEST.ind_publico == 1:
     documento = getattr(context.sapl_documentos.administrativo,assinado)
     documento.manage_permission('View', roles=['Anonymous','Manager','Operador','Operador Materia','Operador Modulo Administrativo'], acquire=0)
     documento.manage_permission('Delete objects', roles=['Manager','Operador','Operador Materia','Operador Modulo Administrativo'], acquire=0)

for documento in context.zsql.documento_acessorio_administrativo_obter_zsql(tip_documento=tip_documento,ind_excluido=0):
 filename_acessorio = str(documento.cod_documento_acessorio) + ".pdf"
 if hasattr(context.sapl_documentos.administrativo, filename_acessorio):
   if context.REQUEST.ind_publico == 0:
     documento = getattr(context.sapl_documentos.administrativo,filename_acessorio)
     documento.manage_permission('View', roles=['Authenticated','Manager','Operador','Operador Modulo Administrativo'], acquire=1)
   if context.REQUEST.ind_publico == 1:
     documento = getattr(context.sapl_documentos.administrativo,filename_acessorio)
     documento.manage_permission('View', roles=['Anonymous','Manager','Operador','Operador Materia','Operador Modulo Administrativo'], acquire=0)
     documento.manage_permission('Delete objects', roles=['Manager','Operador','Operador Materia','Operador Modulo Administrativo'], acquire=0)
