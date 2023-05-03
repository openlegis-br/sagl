## Script (Python) "respostas_obter_pysc"
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

lst_respostas = []
for tramitacao in context.zsql.tramitacao_obter_zsql(cod_status=128, ind_ult_tramitacao=1):
    materia = context.zsql.materia_obter_zsql(cod_materia=tramitacao.cod_materia)[0]
    dic={}
    dic['texto'] = 'Resposta eletrônica do Poder Executivo, protocolada em ' + DateTime(tramitacao.dat_tramitacao, datefmt='international').strftime('%d/%m/%Y') + \
            ', ao ' + str(materia.des_tipo_materia) + ' nº ' + str(tramitacao.num_ident_basica)+'/'+str(tramitacao.ano_ident_basica)
    dic['cod_materia'] = tramitacao.cod_materia
    dic['cod_tramitacao'] = tramitacao.cod_tramitacao
    dic['dat_tramitacao'] = DateTime(tramitacao.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
    lst_respostas.append(dic)       

lst_respostas.sort(key=lambda dic: dic['dat_tramitacao'])
lst_respostas = [(i + 1, j) for i, j in enumerate(lst_respostas)]

lst_texto = []
for i, resposta in lst_respostas:
    item = str(i) + ' - ' + resposta['texto']
    lst_texto.append(item)

lst_texto = '; '.join(['%s' % (value) for (value) in lst_texto])
    
serialized = json.dumps(lst_texto, sort_keys=True, indent=3, ensure_ascii=False).encode('utf8')

return serialized

