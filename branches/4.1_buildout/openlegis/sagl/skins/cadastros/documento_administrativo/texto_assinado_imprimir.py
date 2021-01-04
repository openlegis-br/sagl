## Script (Python) "texto_assinado_imprimir"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

filename = str(cod_documento) + "_texto_integral_signed.pdf"
if hasattr(context.sapl_documentos.administrativo, filename):
   documento = getattr(context.sapl_documentos.administrativo,filename)
   documento.manage_permission('View', roles=['Anonymous','Manager','Operador','Operador Materia','Operador Modulo Administrativo'], acquire=0)

return st.documento_assinado_imprimir(cod_documento)

