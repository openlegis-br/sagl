## Script (Python) "numero_reservar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_documento, txt_interessado, txt_assunto, txt_qtde, cod_materia
##title=
##

ano_documento = DateTime().strftime("%Y")
dat_documento = DateTime().strftime("%Y/%m/%d")
for numero in context.zsql.numero_documento_administrativo_obter_zsql(tip_documento=tip_documento, ano_documento=ano_documento):
   numero_inicial = numero.novo_numero 
qtde = int(txt_qtde)
ind_tramitacao = 1
ind_excluido = 0

for i in range(qtde):
  num_documento = i + numero_inicial
  ano_documento = ano_documento
  tip_documento = tip_documento
  txt_interessado = txt_interessado
  context.zsql.documento_administrativo_incluir_zsql(num_documento = num_documento, 
                                                     ano_documento = ano_documento, 
                                                     dat_documento = DateTime().strftime("%Y/%m/%d"), 
                                                     tip_documento = tip_documento, 
                                                     txt_interessado = txt_interessado,
                                                     txt_assunto = txt_assunto,
                                                     ind_tramitacao = ind_tramitacao,
                                                     ind_excluido = ind_excluido)
  if cod_materia != 0:
    for documento in context.zsql.documento_administrativo_incluido_codigo_obter_zsql():
      context.zsql.documento_administrativo_materia_incluir_zsql(cod_documento = int(documento.cod_documento),
                                                                 cod_materia = cod_materia)
return 1

