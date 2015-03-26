## Script (Python) "parlamentar_verificar_nome_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=nom_parlamentar="", nom_completo="" 
##title=
##

parlamentares_nomp=[]
parlamentares_nomc=[]

nom_p=nom_parlamentar.lower()
nom_c=nom_completo.lower()

lista_parlamentares=context.zsql.parlamentar_verificar_zsql()

for parlamentar in lista_parlamentares:
    parlamentares_nomp.append(parlamentar.nom_parlamentar.lower())
    parlamentares_nomc.append(parlamentar.nom_completo.lower())

jaexiste="0"
for nomp in parlamentares_nomp:
    if (nomp == nom_p):
       jaexiste="1"
   
for nomc in parlamentares_nomc:
    if (nomc == nom_c):
       jaexiste="1"

return jaexiste
