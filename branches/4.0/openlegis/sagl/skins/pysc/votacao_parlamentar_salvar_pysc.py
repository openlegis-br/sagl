## Script (Python) "votacao_parlamentar_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_parlamentar, cod_ordem, cod_materia, tip_votacao, txt_login, vot_parlamentar=""
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

REQUEST = context.REQUEST

votacao=context.zsql.votacao_obter_zsql(cod_ordem=cod_ordem,cod_materia=cod_materia,ind_excluido=0)
try:
    cod_votacao = votacao[0].cod_votacao
except:
    cod_votacao = None
    context.zsql.votacao_incluir_zsql(
        num_votos_sim=0,
        num_votos_nao=0,
        num_abstencao=0,
        num_nao_votou=0,
        txt_observacao='',
        cod_ordem=cod_ordem,
        cod_materia=cod_materia,
        tip_resultado_votacao=0
    )
    votacao_incluida=context.zsql.votacao_incluida_obter_zsql()
    cod_votacao = votacao_incluida[0].cod_votacao

if tip_votacao == '3':
    lista = st.ler_token()

    token_cookie = REQUEST.get('__token', None)

    count = 0
    for item in lista:
        if token_cookie == item.keys()[0]:
            lista[count][item.keys()[0]][1] = vot_parlamentar
            break

        count += 1

    arquivo = st.arquivo_token()

    for item in lista:
        st.grava_token(arquivo, item)


    context.zsql.votacao_parlamentar_incluir_zsql(
        cod_votacao=cod_votacao,
        cod_parlamentar=cod_parlamentar,
        vot_parlamentar='V',
        txt_login=txt_login
    )

    return 1

if cod_votacao:
    votacao_parlamentar = context.zsql.votacao_parlamentar_obter_zsql(
        cod_votacao=cod_votacao,
        cod_parlamentar=cod_parlamentar
    )
    if len(votacao_parlamentar) > 0:
        votou_parlamentar = votacao_parlamentar[0].vot_parlamentar
        context.zsql.votacao_parlamentar_atualizar_zsql(
            cod_votacao=cod_votacao,
            cod_parlamentar=cod_parlamentar,
            vot_parlamentar=vot_parlamentar,
            txt_login=txt_login
        )
    else:
        votou_parlamentar = ''
        context.zsql.votacao_parlamentar_incluir_zsql(
            cod_votacao=cod_votacao,
            cod_parlamentar=cod_parlamentar,
            vot_parlamentar=vot_parlamentar,
            txt_login=txt_login
        )
    votacao=context.zsql.votacao_obter_zsql(
        cod_votacao=cod_votacao,
        cod_ordem=cod_ordem,
        cod_materia=cod_materia,
        ind_excluido=0
    )
    votos_sim = votacao[0].num_votos_sim
    votos_nao = votacao[0].num_votos_nao
    votos_abstencao = votacao[0].num_abstencao

    if votou_parlamentar == 'Sim':
        votos_sim -= 1
    if votou_parlamentar == 'Não':
        votos_nao -= 1
    if votou_parlamentar == 'Abstenção':
        votos_abstencao -= 1

    if vot_parlamentar == 'Sim':
        votos_sim += 1
    if vot_parlamentar == 'Não':
        votos_nao += 1
    if vot_parlamentar == 'Abstenção':
        votos_abstencao += 1

    context.zsql.votacao_atualizar_zsql(
        cod_votacao=cod_votacao,
        num_votos_sim=votos_sim,
        num_votos_nao=votos_nao,
        num_abstencao=votos_abstencao,
        num_nao_votou=0,
        txt_observacao='',
        cod_ordem=cod_ordem,
        cod_materia=cod_materia,
        tip_resultado_votacao=0
    )
else:
    votacao_incluida=context.zsql.votacao_incluida_obter_zsql()
    cod_votacao = votacao_incluida[0].cod_votacao
    context.zsql.votacao_parlamentar_incluir_zsql(
        cod_votacao=cod_votacao,
        cod_parlamentar=cod_parlamentar,
        vot_parlamentar=vot_parlamentar,
        txt_login=txt_login
    )

return 1
