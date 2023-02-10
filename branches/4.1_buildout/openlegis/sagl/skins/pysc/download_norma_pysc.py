## Script (Python) "download_norma_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_norma,texto_original=None,texto_consolidado=None
##title=
##
request=context.REQUEST
response=request.RESPONSE

for norma in context.zsql.norma_juridica_obter_zsql(cod_norma=cod_norma):
  if texto_original:
    if hasattr(context.sapl_documentos.norma_juridica, "%s"%cod_norma+'_texto_integral_signed.pdf'):
       download_name = str(norma.des_tipo_norma).replace(" ", "_")+"-"+str(norma.num_norma)+"-"+str(norma.ano_norma)+"-signed.pdf"
       id_documento = "%s"%cod_norma+'_texto_integral_signed.pdf'
    elif hasattr(context.sapl_documentos.norma_juridica, "%s"%cod_norma+'_texto_integral.pdf'):
       download_name = str(norma.des_tipo_norma).replace(" ", "_")+"-"+str(norma.num_norma)+"-"+str(norma.ano_norma)+"-original.pdf"
       id_documento = "%s"%cod_norma+'_texto_integral.pdf'
  if texto_consolidado:
    download_name = norma.des_tipo_norma.replace(" ", "_")+"-"+str(norma.num_norma)+"-"+str(norma.ano_norma)+"_consolidacao.pdf"
    id_documento = "%s"%cod_norma+'_texto_consolidado.pdf'
  arquivo = getattr(context.sapl_documentos.norma_juridica,id_documento) 

context.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
context.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; Filename=%s' % download_name)

return arquivo

