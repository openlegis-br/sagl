## Script (Python) "valida_extincao_comissao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_comissao, dat_extincao
##title=
##
'''
  Funcao: validar a data extincao da comissÃ£o informada retornando 1=ok, None=invÃ¡lida

  Argumento: data da extinÃ§Ã£o, cÃ³digo da comissÃ£o 

  Retorno: 1-ok, data vÃ¡lida; 0-nÃ£o, data invÃ¡lida.

'''

if (cod_comissao==''):
   return None

if dat_extincao=='':
   return None

cod_comissao=int(cod_comissao)
dat_criacao=context.zsql.comissao_obter_zsql(cod_comissao=cod_comissao)[0].dat_criacao

if (dat_criacao==''):
   return None

dat_criacao=context.data_converter_pysc(dat_criacao)

dat_extincao=context.data_converter_pysc(dat_extincao)

if (dat_criacao > dat_extincao):
   return None

nom_comissao=context.zsql.comissao_obter_zsql(cod_comissao=cod_comissao)[0].nom_comissao

if nom_comissao=='':
   return None

dat_apresentacao=context.zsql.ultima_autoria_obter_zsql(des_tipo_autor='Comissao', nom_autor=nom_comissao)[0].dat_apresentacao

# data da extinÃ§Ã£o estÃ¡ no formato dd/mm/aaaa e precisa ser convertida para aaaa/mm/dd
 
if (dat_apresentacao > dat_extincao):
   return None

# os dados data de extinÃ§Ã£o e nome da comissÃ£o estÃ£o corretos! 

return 1 
