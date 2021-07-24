## Script (Python) "vereadores_atuais"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
import simplejson as json

for item in context.zsql.legislatura_atual_obter_zsql():
    num_legislatura = item.num_legislatura

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

lista_exercicio.sort(key=lambda dic: dic['nom_completo'])

return json.dumps(lista_exercicio)
