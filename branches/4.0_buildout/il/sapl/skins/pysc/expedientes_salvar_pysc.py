## Script (Python)
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen,cod_expediente,txt_expediente
##title=
##

dic={}

# verifica se existe apenas um expediente e caso não exista ele faz um laço para construir um dicionário
if len(cod_expediente) > 1:
    for n in range(len(cod_expediente)):
        dic[cod_expediente[n]]=txt_expediente[n]

else:
    dic[cod_expediente]=txt_expediente
    
for cod in cod_expediente:
    expedientes=context.zsql.expediente_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0)
expediente=[]
for e in expedientes:
    expediente.append(str(e.cod_expediente))

for e in cod_expediente:
    if e not in expediente:
        context.zsql.expediente_incluir_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=e,txt_expediente=dic.get(e))
    else:
        context.zsql.expediente_alterar_zsql(cod_sessao_plen=cod_sessao_plen,cod_expediente=e,txt_expediente=dic.get(e),ind_excluido=0)

return 1
