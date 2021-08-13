## Script (Python) "presenca_reuniao_comissao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_reuniao, cod_parlamentar
##title=
##

lista_presenca = context.zsql.reuniao_comissao_presenca_obter_zsql(cod_reuniao=cod_reuniao)

parlamentares=[]
for parlamentar in lista_presenca:
    parlamentares.append(str(parlamentar.cod_parlamentar))

for i in cod_parlamentar:
    if i not in parlamentares:
        context.zsql.reuniao_comissao_presenca_incluir_zsql(cod_reuniao=cod_reuniao,cod_parlamentar=i)

for i in parlamentares:
    if i not in cod_parlamentar:
        context.zsql.reuniao_comissao_presenca_excluir_zsql(cod_reuniao=cod_reuniao,cod_parlamentar=i)

return 1
