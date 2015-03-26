## Script (Python)
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

# reordena materias na Ordem do Dia  

# obtem materias na Ordem do Dia da sessão plenária indicada.
ordem_dia_materia=context.zsql.ordem_dia_reordena_obter_zsql(cod_sessao_plen=cod_sessao_plen)

# reordena materias na Ordem do Dia.
nd=0
codm=0
cods=0
for materia in ordem_dia_materia:
   nd=nd + 1
   cods=materia.cod_sessao_plen
   codm=materia.cod_materia
   context.zsql.atualiza_ordem_dia_reordena_zsql(cod_sessao_plen=cods, cod_materia=codm, num_ordem=nd)
return 1
