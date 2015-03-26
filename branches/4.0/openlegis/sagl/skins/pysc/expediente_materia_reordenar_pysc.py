## Script (Python)
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

# reordena materias no expediente 

# obtem materias no expediente da sessão plenária indicada.
expediente_materia=context.zsql.expediente_materia_reordena_obter_zsql(cod_sessao_plen=cod_sessao_plen)

# reordena materias no expediente.
nd=0
codm=0
cods=0
for materia in expediente_materia:
   nd=nd + 1
   cods=materia.cod_sessao_plen
   codm=materia.cod_materia
   context.zsql.atualiza_expediente_materia_reordena_zsql(cod_sessao_plen=cods, cod_materia=codm, num_ordem=nd)
return 1
