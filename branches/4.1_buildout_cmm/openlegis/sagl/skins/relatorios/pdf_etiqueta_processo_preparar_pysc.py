import os

request=context.REQUEST
response=request.RESPONSE
REQUEST=context.REQUEST

lst_processos = []

for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=REQUEST['cod_documento']):
    dic={}
    dic['titulo'] = str(documento.sgl_tipo_documento) + ' ' + str(documento.num_documento) + '/' + str(DateTime(documento.data_documento).strftime('%y'))
    lst_processos.append(dic)

caminho = context.pdf_etiqueta_processo_gerar(lst_processos)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)

