## Script (Python) "presenca_ordem_dia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen,cod_parlamentar,tip_frequencia="",txt_justif_ausencia="",dat_ordem=""
##title=
##

dic={}
dic = dict(zip(cod_parlamentar, tip_frequencia))

dic2={}
dic2 = dict(zip(cod_parlamentar, txt_justif_ausencia))

parlamentares=[]

lista=context.zsql.presenca_ordem_dia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0)

for parlamentar in lista:
    parlamentares.append(str(parlamentar.cod_parlamentar))

for p in cod_parlamentar:
    if p not in parlamentares:
        context.zsql.presenca_ordem_dia_incluir_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=p,tip_frequencia=dic.get(p),txt_justif_ausencia=dic2.get(p),dat_ordem=dat_ordem)
    else:
        context.zsql.presenca_ordem_dia_alterar_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=p,tip_frequencia=dic.get(p),txt_justif_ausencia=dic2.get(p))

for p in parlamentares:
     if p not in cod_parlamentar:
        context.zsql.presenca_ordem_dia_excluir_zsql(cod_sessao_plen=cod_sessao_plen,cod_parlamentar=p)

return 1
