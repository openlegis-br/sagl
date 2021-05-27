## Script (Python) "materias_comissao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_comissao
##title=
##
materias = []
for despacho in context.zsql.despacho_inicial_obter_zsql(cod_comissao=cod_comissao, ind_excluido=0):
    if not context.zsql.relatoria_obter_zsql(cod_comissao=cod_comissao,cod_materia=despacho.cod_materia,num_ordem=despacho.num_ordem):
       for materia in context.zsql.materia_obter_zsql(cod_materia=despacho.cod_materia, ind_excluido=0):
           if materia.ind_tramitacao == 1:
              materias.append(int(despacho.cod_materia))

return materias

