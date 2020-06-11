## Script (Python) "atualiza_primeiro_autor_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia, cod_parlamentar="", cod_comissao="", nom_autor=""
##title=
##
#
#  Função: atualiza primeiro autor
# 
#  Argumentos: cod_materia, cod_parlamentar  --> retorna 1-ok  ou 0-erro.
#
 
codm = str(cod_materia)
if cod_parlamentar:
   cod = str(cod_parlamentar)
   ta = '1'
else:
   if cod_comissao:
      cod = str(cod_comissao)
      ta = '2'
   else:
      if nom_autor:
         cod = nom_autor
         ta = '3'
      else:
         return 0
autorias = context.zsql.autor_obter_zsql(cod_materia=codm, tip_autor=ta) or []
for p in autorias:
     if ta=='1':
        s = str(p.cod_parlamentar)
     else:
        if ta=='2':
           s = str(p.cod_comissao)
        else:
           s = p.nom_autor
     if s == cod:
        context.zsql.limpa_primeiro_autor_zsql(cod_materia=codm)
        context.zsql.atualiza_primeiro_autor_zsql(cod_materia=codm, cod_autor=p.cod_autor)
        return 1   
return 0
