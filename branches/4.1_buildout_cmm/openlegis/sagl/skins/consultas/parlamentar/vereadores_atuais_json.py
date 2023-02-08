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

context.REQUEST.RESPONSE.setHeader("Access-Control-Allow-Origin", "*")
request=context.REQUEST

for item in context.zsql.legislatura_atual_obter_zsql():
    num_legislatura = item.num_legislatura

data_atual = DateTime().strftime("%d/%m/%Y")

lista_exercicio = []
exercicio = []
for item in context.zsql.autores_obter_zsql(txt_dat_apresentacao=data_atual):
    dic = {}
    dic['cod_parlamentar'] = item.cod_parlamentar
    dic['nom_parlamentar'] = item.nom_parlamentar
    dic['nom_completo'] = item.nom_completo
    foto = str(item.cod_parlamentar) + "_foto_parlamentar"
    if hasattr(context.sapl_documentos.parlamentar.fotos, foto):    
       dic['foto'] = request.SERVER_URL + '/sapl_documentos/parlamentar/fotos/' + foto
    else:
       dic['foto'] = request.SERVER_URL + '/imagens/avatar.png'   
    dic['link'] = request.SERVER_URL + '/consultas/parlamentar/parlamentar_mostrar_proc?cod_parlamentar=' + item.cod_parlamentar + '%26iframe=1'
    dic['partido'] = ''
    for filiacao in context.zsql.parlamentar_data_filiacao_obter_zsql(num_legislatura=num_legislatura, cod_parlamentar=item.cod_parlamentar):    
        if filiacao.dat_filiacao != '0' and filiacao.dat_filiacao != None:
            for partido in context.zsql.parlamentar_partido_obter_zsql(dat_filiacao=filiacao.dat_filiacao, cod_parlamentar=item.cod_parlamentar):
                dic['partido'] = partido.sgl_partido               
    lista_exercicio.append(dic)

lista_exercicio.sort(key=lambda dic: dic['nom_completo'])

#listaVereador={}  

#listaVereador.update({'vereadores': lista_exercicio})

return json.dumps(lista_exercicio)
