## Script (Python) "discussao_expediente_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_ordem,cod_parlamentar=""
##title=
##

if cod_parlamentar and context.pysc.verifica_string_pysc(cod_parlamentar):
   cod_parlamentar = [cod_parlamentar]
else:
   cod_parlamentar = cod_parlamentar

lista_discussao=context.zsql.discussao_expediente_obter_zsql(cod_ordem=cod_ordem)
parlamentares=[]
for parlamentar in lista_discussao:
    parlamentares.append(str(parlamentar.cod_parlamentar))

if cod_parlamentar:
   for i in cod_parlamentar:
       if i not in parlamentares:
          context.zsql.discussao_expediente_incluir_zsql(cod_ordem=cod_ordem,cod_parlamentar=i)
   for i in parlamentares:
       if i not in cod_parlamentar:
           context.zsql.discussao_expediente_excluir_zsql(cod_ordem=cod_ordem,cod_parlamentar=i)

else:
   for i in parlamentares:
       context.zsql.discussao_expediente_excluir_zsql(cod_ordem=cod_ordem,cod_parlamentar=i)

return 1

