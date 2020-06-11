## Script (Python) "presenca_expediente_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen,cod_parlamentar,dat_ordem
##title=
##

lista_presenca=context.zsql.presenca_expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,dat_ordem=dat_ordem,ind_excluido=0)
parlamentares=[]
for parlamentar in lista_presenca:
    parlamentares.append(str(parlamentar.cod_parlamentar))

lista_presenca_excl=context.zsql.presenca_expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,dat_ordem=dat_ordem,ind_excluido=1)
parlamentares_excl=[]
for parlamentar in lista_presenca_excl:
    parlamentares_excl.append(str(parlamentar.cod_parlamentar))

for i in cod_parlamentar:
    if i not in parlamentares and i not in parlamentares_excl:
        context.zsql.presenca_expediente_incluir_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=i,dat_ordem=dat_ordem)
    else:
        context.zsql.presenca_expediente_alterar_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=i,dat_ordem=dat_ordem,ind_excluido=0)

for i in parlamentares:
    if i not in cod_parlamentar:
        context.zsql.presenca_expediente_alterar_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=i,dat_ordem=dat_ordem,ind_excluido=1)

return 1
