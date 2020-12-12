## Script (Python) "vereadores_atuais"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=num_legislatura, lista
##title=
##

data_atual = DateTime().strftime("%d/%m/%Y")

titulares = []
suplentes = []
for item in context.zsql.parlamentar_obter_zsql(num_legislatura = num_legislatura):
    if item.ind_titular == 1:     
       titulares.append(int(item.cod_parlamentar))
    if item.ind_titular == 0:     
       suplentes.append(int(item.cod_parlamentar))

lista_exercicio = []
exercicio = []
for item in context.zsql.autores_obter_zsql(txt_dat_apresentacao=data_atual):
    dic = {}
    dic['cod_parlamentar'] = item.cod_parlamentar
    dic['nom_parlamentar'] = item.nom_parlamentar
    dic['nom_completo'] = item.nom_completo           
    lista_exercicio.append(dic)
    exercicio.append(int(item.cod_parlamentar))

em_exercicio = []
titulares_inativos = []
suplentes_inativos = []


for item in titulares:
    if item in exercicio:
        em_exercicio.append(item)

for item in titulares:
    if item not in exercicio:
        titulares_inativos.append(item)

for item in suplentes:
    if item in exercicio:
        em_exercicio.append(item)

for item in suplentes:
    if item not in exercicio:
        suplentes_inativos.append(item)

inativos = []
for item in titulares_inativos:
    for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar = item):
       dic = {}
       dic['cod_parlamentar'] = parlamentar.cod_parlamentar
       dic['nom_parlamentar'] = parlamentar.nom_parlamentar
       dic['nom_completo'] = parlamentar.nom_completo       
       inativos.append(dic)

suplentes = []
for item in suplentes_inativos:
    for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar = item):
       dic = {}
       dic['cod_parlamentar'] = parlamentar.cod_parlamentar
       dic['nom_parlamentar'] = parlamentar.nom_parlamentar
       dic['nom_completo'] = parlamentar.nom_completo              
       suplentes.append(dic)

if lista == 'ativos':
   return lista_exercicio
elif lista =='inativos':
   return inativos
elif lista == 'suplentes':
   return suplentes
