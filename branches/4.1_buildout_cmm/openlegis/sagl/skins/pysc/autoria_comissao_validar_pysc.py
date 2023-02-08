## Script (Python) "autoria_comissao_validar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=txt_dat_apresentacao, cod_comissao
##title=
##
"""
  Função: validar se a comissão está ativa: está como autora, não foi excluida e nem possui data de extincao na data de apresentação da matéria
 
  Argumentos: cod_comissao  --> retorna 1-verdadeiro ou 0-falso.
""" 
try:
  codigo = str(cod_comissao)
  autores = context.zsql.autores_comissao_zsql(dat_apresentacao=txt_dat_apresentacao) or []
  for p in autores:
      s = str(p.cod_comissao)
      if s == codigo:
         return 1
  return 0     
except:
  return 0
