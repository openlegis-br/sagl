## Script (Python) "recomposicao_presencas_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, ind_status_pre
##title=
##

from Products.CMFCore.utils import getToolByName

abrir = context.REQUEST.form.get('abrir', None)
fechar = context.REQUEST.form.get('fechar', None)

st = getToolByName(context, 'portal_sagl')

if abrir:
    recomposicao = context.zsql.recomposicao_presencas_sessao_incluir_zsql(
        cod_sessao_plen = cod_sessao_plen,
        ind_status_pre = ind_status_pre
    )

    context.pysc.presenca_sessao_pysc(cod_parlamentar=[],cod_sessao_plen=cod_sessao_plen)

    #verifica se existe uma votacao iniciada
#    ordem_dia = context.zsql.ordem_dia_obter_zsql(cod_sessao_plen = cod_sessao_plen, ind_excluido=0, ind_votacao_iniciada = 1)
#    if ordem_dia:
#        context.zsql.votacao_iniciar_zsql(
#            cod_ordem = ordem_dia[0].cod_ordem,
#            ind_votacao_iniciada = 0
#        )
#
#        cod_ordem = ordem_dia[0].cod_ordem
#        if context.zsql.votacao_obter_zsql(cod_ordem = cod_ordem, ind_excluido = 0):
#            cod_materia = context.zsql.votacao_obter_zsql(cod_ordem = cod_ordem, ind_excluido = 0)[0].cod_materia
#            cod_votacao = context.zsql.votacao_obter_zsql(cod_ordem = cod_ordem, ind_excluido = 0)[0].cod_votacao
#            context.zsql.votacao_atualizar_zsql(
#                cod_votacao=cod_votacao,
#                num_votos_sim=0,
#                num_votos_nao=0,
#                num_abstencao=0,
#                txt_observacao='',
#                cod_ordem=cod_ordem,
#                cod_materia=cod_materia,
#                tip_resultado_votacao=0
#            )
#            if context.zsql.votacao_parlamentar_obter_zsql(cod_votacao = cod_votacao):
#                for voto in context.zsql.votacao_parlamentar_obter_zsql(cod_votacao = cod_votacao):
#                    context.zsql.votacao_parlamentar_atualizar_zsql(
#                        cod_votacao = cod_votacao,
#                        cod_parlamentar = voto.cod_parlamentar,
#                        vot_parlamentar=None
#                    )
#
#    # remove os tokens gerados e atribuidos
#    st.remover_token()
#    st.remover_arquivo_atribuido()
#
#    dat_sessao = context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0)[0].dat_inicio_sessao
#    context.pysc.presenca_ordem_dia_pysc(cod_parlamentar=[],cod_sessao_plen=cod_sessao_plen,dat_ordem=context.pysc.data_converter_pysc(data=dat_sessao))

    return True

elif fechar:
    num_id_quorum = len(context.zsql.presenca_sessao_obter_zsql(
        cod_sessao_plen=cod_sessao_plen,
        ind_excluido=0
    ))

    cod_registro_pre = context.zsql.recomposicao_presencas_sessao_verificar_ultima_aberta_zsql(cod_sessao_plen = cod_sessao_plen)[0].cod_registro_pre

    recomposicao =  context.zsql.recomposicao_presencas_sessao_atualizar_zsql(
        cod_registro_pre=int(cod_registro_pre),
        cod_sessao_plen=int(cod_sessao_plen),
        num_id_quorum = int(num_id_quorum),
        ind_status_pre=ind_status_pre
    )

    return True

else:
    return False
