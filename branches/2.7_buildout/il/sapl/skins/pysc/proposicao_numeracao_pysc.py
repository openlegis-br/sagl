## Script (Python) "proposicao_numeracao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao
##title=
##

''' Script para a verificação do número da proposição e inclusão de um novo.'''
''' Faz a inclusão por tipo e ano da proposição. '''

# Obtém o proximo "num_proposicao" do tipo de proposicao que está sendo incluída ----- 31/08/2010


# Define o ano corrente
ano_corrente = DateTime().year()

# Busca a proposição
tip_proposicao = context.zsql.proposicao_obter_tipo_zsql(cod_proposicao = cod_proposicao)[0].tip_proposicao

# Busca a última numeração + 1 do mesmo tipo que está sendo incluída no ano
num_proposicao = context.zsql.proposicao_ultima_numeracao_obter_zsql(tip_proposicao = tip_proposicao, ano = ano_corrente)[0].num_proposicao

# ano_ultima_num = context.zsql.proposicao_ano_ult_numeracao_obter_zsql(num_proposicao = ultima_numeracao.num_proposicao)[0]

# Compara o ano e caso seja diferente, recomeça a numeração
# if int(ano_ultima_num.dat_recebimento) != (ano_corrente):
#    numeracao = 0001
# else:
#    numeracao = ultima_numeracao.num_proposicao + 1

context.zsql.proposicao_incluir_numeracao_zsql(cod_proposicao = cod_proposicao, num_proposicao = num_proposicao)

return 1
