## Script (Python) "votacao_secreta_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=sec=None, resultado=None, nao_votou=None, expediente=0, cod_ordem=None, cod_sessao_plen=None
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

REQUEST = context.REQUEST

lista = st.ler_token()


if sec:
    token_cookie = REQUEST.get('__token', None)

    voto = ''

    for item in lista:
        if token_cookie == item.keys()[0]:
            voto = item[item.keys()[0]][1]
            break

    return voto

if resultado:
    if not expediente:
        context.zsql.votacao_iniciar_zsql(
            cod_ordem = cod_ordem,
            ind_votacao_iniciada = 0
        )

    if expediente:
        context.zsql.votacao_expediente_iniciar_zsql(
            cod_ordem = cod_ordem,
            ind_votacao_iniciada = 0
        )

    votacao = {}

    sim = 0
    nao = 0
    abstencao = 0

    for item in lista:
        if item[item.keys()[0]][1] == "Sim":
            sim += 1
        elif item[item.keys()[0]][1] == "Não":
            nao += 1
        elif item[item.keys()[0]][1] == "Abstenção":
            abstencao += 1

    votacao['sim'] = sim
    votacao['nao'] = nao
    votacao['abstencao'] = abstencao

    return votacao

if nao_votou:
    if not expediente:
        presenca = context.zsql.presenca_ordem_dia_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0)
    else:
        presenca = context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0)

    return len(presenca) - len([item[item.keys()[0]][1] for item in lista if item[item.keys()[0]][1]])
