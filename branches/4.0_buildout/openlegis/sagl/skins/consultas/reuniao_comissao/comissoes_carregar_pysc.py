## Script (Python) "comissoes_carregar"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= svalue=''
##title=
##
context.REQUEST.RESPONSE.setHeader("Access-Control-Allow-Origin", "*")

listaDic={}     
comissaoArray = []

if svalue == '':
   for reuniao in context.zsql.reuniao_comissao_obter_zsql():
       comissao = context.zsql.comissao_obter_zsql(cod_comissao = reuniao.cod_comissao)[0]
       dic = {}
       dic['cod_comissao'] = reuniao.cod_comissao
       dic['nom_comissao'] = comissao.nom_comissao
       comissaoArray.append(dic)

if svalue != '':
   for reuniao in context.zsql.reuniao_comissao_obter_zsql(ano_reuniao = svalue):
       comissao = context.zsql.comissao_obter_zsql(cod_comissao = reuniao.cod_comissao)[0]
       dic = {}   
       dic['cod_comissao'] = reuniao.cod_comissao
       dic['nom_comissao'] = comissao.nom_comissao
       comissaoArray.append(dic)

comissaoArray = [
    e
    for i, e in enumerate(comissaoArray)
    if comissaoArray.index(e) == i
    ]

comissaoArray.sort(key=lambda dic: dic['nom_comissao'])
    
return comissaoArray
