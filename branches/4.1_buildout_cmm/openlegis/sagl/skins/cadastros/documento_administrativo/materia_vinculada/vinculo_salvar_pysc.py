## encoding: utf-8 
## Script (Python) "vinculo_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters = cod_documento, tip_materia="", num_materia="", ano_materia=""
##title=
##

if context.pysc.verifica_lista_pysc(valor=num_materia) == 1:
  for materia in context.zsql.materia_obter_zsql(tip_id_basica = tip_materia, num_ident_basica = num_materia, ano_ident_basica = ano_materia,ind_excluido=0):
    context.zsql.documento_administrativo_materia_incluir_zsql(cod_documento=cod_documento,cod_materia=materia.cod_materia)
    return 1

else:
  lst_materias = []
  for numero in num_materia:
    dic = {}
    dic['numero'] = numero
    for ano in ano_materia:
        dic['ano'] = ano
    for tipo in tip_materia:
        dic['tipo'] = tipo
    lst_materias.append(dic)

  codigos = []
  for dic in lst_materias:
    for materia in context.zsql.materia_obter_zsql(tip_id_basica=dic.get('tipo',dic), num_ident_basica=dic.get('numero',dic), ano_ident_basica=dic.get('ano',dic),ind_excluido=0):
        codigo = int(materia.cod_materia)
        codigos.append(codigo)

  for c in codigos:
    context.zsql.documento_administrativo_materia_incluir_zsql(cod_documento=cod_documento,cod_materia=c)

  return 1

