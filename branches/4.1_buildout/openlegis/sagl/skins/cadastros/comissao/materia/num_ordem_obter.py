## Script (Python) "resposta_executivo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=hdn_cod_materia, hdn_cod_comissao
##title=
##


maior_num_ordem = []
for despacho in context.zsql.despacho_inicial_obter_zsql(cod_materia=hdn_cod_materia, ind_excluido=0):
    if despacho.cod_materia != None:
       num_ordem = despacho.num_ordem
    else:
       num_ordem = 1
    maior_num_ordem.append(num_ordem)

max_num = len(maior_num_ordem)

if context.zsql.despacho_inicial_obter_zsql(cod_materia=hdn_cod_materia, cod_comissao=hdn_cod_comissao, ind_excluido=0):
   for despacho in context.zsql.despacho_inicial_obter_zsql(cod_materia=hdn_cod_materia, cod_comissao=hdn_cod_comissao, ind_excluido=0):
       if context.zsql.relatoria_obter_zsql(cod_materia=despacho.cod_materia, num_ordem=despacho.num_ordem, ind_excluido=0):
          for relatoria in context.zsql.relatoria_obter_zsql(cod_materia=despacho.cod_materia, num_ordem=despacho.num_ordem, ind_excluido=0): 
              num_ordem = int(max_num) + 1
       else:
          num_ordem = despacho.num_ordem

elif context.zsql.despacho_inicial_obter_zsql(cod_materia=hdn_cod_materia, ind_excluido=0):
     num_ordem = int(max_num) + 1

else:
    num_ordem = 1

return num_ordem
