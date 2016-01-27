## Script (Python) "retorna_perfil_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_parlamentar,cod_sessao_plen, num_ordem
##title=
##

oradores=[]
lista_oradores=context.zsql.oradores_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0)
for orador in lista_oradores:
    oradores.append(str(orador.cod_parlamentar))

lista_oradores_excl=context.zsql.oradores_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=1)
oradores_excl=[]
for orador in lista_oradores_excl:
    oradores_excl.append(str(orador.cod_parlamentar))

for i in cod_parlamentar:
    for j in num_ordem:
        if i not in oradores and i not in oradores_excl:
            context.zsql.oradores_incluir_zsql(cod_parlamentar=i,cod_sessao_plen=cod_sessao_plen,num_ordem=j)
        else:
            context.zsql.oradores_alterar_zsql(cod_parlamentar=i,cod_sessao_plen=cod_sessao_plen,num_ordem=j,ind_excluido=0)

for i in oradores:
    for j in num_ordem:
        if i not in cod_parlamentar:
            context.zsql.oradores_alterar_zsql(cod_parlamentar=i,cod_sessao_plen=cod_sessao_plen,num_ordem=j,ind_excluido=1)

return 1