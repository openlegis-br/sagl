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
 if hasattr(context.sapl_documentos.administrativo, filename):
   if context.REQUEST.ind_publico == 0:
     documento = getattr(context.sapl_documentos.administrativo,filename)
     documento.manage_permission('View', roles=['Manager','Operador','Operador Modulo Administrativo'], acquire=1)
   if context.REQUEST.ind_publico == 1:
     documento = getattr(context.sapl_documentos.administrativo,filename)
     documento.manage_permission('View', roles=['Anonymous','Manager','Operador','Operador Modulo Administrativo'], acquire=0)
