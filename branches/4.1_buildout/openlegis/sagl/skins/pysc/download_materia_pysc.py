## Script (Python) "download_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia,texto_original=None,redacao_final=None
##title=
##
request=context.REQUEST
response=request.RESPONSE

if cod_materia.isdigit():
 cod_materia = cod_materia
else:
 cod_materia = context.pysc.b64decode_pysc(codigo=str(cod_materia))

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):

  if texto_original:
    download_name = str(materia.des_tipo_materia).replace(" ", "_")+"-"+str(materia.num_ident_basica)+"-"+str(materia.ano_ident_basica)+".pdf"
    id_documento = "%s"%cod_materia+'_texto_integral.pdf'

  if redacao_final:
    download_name = str(materia.des_tipo_materia).replace(" ", "_")+"-"+str(materia.num_ident_basica)+"-"+str(materia.ano_ident_basica)+"_redacao_final.pdf"
    id_documento = "%s"%cod_materia+'_redacao_final.pdf'

  arquivo = getattr(context.sapl_documentos.materia,id_documento) 

context.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
context.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; Filename=%s' % download_name)

return arquivo

