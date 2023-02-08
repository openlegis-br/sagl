## Script (Python) "num_ordem_obter"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

lista = []
for item in context.zsql.sessao_plenaria_painel_obter_zsql(cod_sessao_plen=cod_sessao_plen):
    num_ordem = item.num_ordem 
    lista.append(num_ordem)

num_ordem = len(lista) + 1

return num_ordem


