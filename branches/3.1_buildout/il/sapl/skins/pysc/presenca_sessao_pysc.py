## Script (Python) "presenca_sessao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen,cod_parlamentar,tip_frequencia="",txt_justif_ausencia=""
##title=
##

dic={}
dic = dict(zip(cod_parlamentar, tip_frequencia))

dic2={}
dic2 = dict(zip(cod_parlamentar, txt_justif_ausencia))

parlamentares=[]

lista=context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0)

for parlamentar in lista:
    parlamentares.append(str(parlamentar.cod_parlamentar))

for p in cod_parlamentar:
    if p not in parlamentares:
        context.zsql.presenca_sessao_incluir_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=p,tip_frequencia=dic.get(p),txt_justif_ausencia=dic2.get(p))
    else:
        context.zsql.presenca_sessao_alterar_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=p,tip_frequencia=dic.get(p),txt_justif_ausencia=dic2.get(p))

return 1
