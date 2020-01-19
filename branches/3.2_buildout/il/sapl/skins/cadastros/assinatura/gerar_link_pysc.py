## Script (Python) "gerar_link_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_documento,codigo
##title=
##

for item in context.zsql.assinatura_storage_obter_zsql(tip_documento=tip_documento):
    location = item.pdf_location
    pdf_signed = str(location) + str(codigo) + str(item.pdf_signed)
    pdf_file = str(location) + str(codigo) + str(item.pdf_file)
    nom_arquivo = str(codigo) + str(item.pdf_file)
    nom_arquivo_assinado = str(codigo) + str(item.pdf_signed)

try:
   arquivo = context.restrictedTraverse(pdf_signed)
   nom_arquivo = nom_arquivo_assinado
   link = pdf_signed
except:
   pass

try:
   arquivo = context.restrictedTraverse(pdf_file)
   nom_arquivo = nom_arquivo
   link = pdf_file
except:
   pass

return link
