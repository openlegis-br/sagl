## Script (Python) "valida_unidade_tramitacao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=dat_tramitacao, cod_comissao, dat_extincao, cod_parlamentar, ind_ativo_parlamentar
##title=
##
##  Funcao: validar a unidade de tramitacao  retornando 1=ok, None=invalida
##
##  Argumento: data da tramitacao, cod_comissao, data da extincao, codigo do parlamentar e indicador de parlamentar ativo
##

if (cod_comissao and not(dat_extincao)):
   return 1

if dat_extincao:
   dat_e=context.data_converter_pysc(dat_extincao)

if dat_tramitacao:
   dat_t=context.data_converter_pysc(dat_tramitacao)

if (cod_comissao and dat_extincao and (dat_e > dat_t)):
   return 1

if (cod_parlamentar and ind_ativo_parlamentar):
   return 1

return None
