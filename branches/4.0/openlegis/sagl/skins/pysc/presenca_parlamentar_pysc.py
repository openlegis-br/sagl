## Script (Python) "presenca_parlamentar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=recontagem=False
##title=
##

from Products.CMFCore.utils import getToolByName
import time

REQUEST = context.REQUEST
membership_tool = getToolByName(context, 'portal_membership')

member = membership_tool.getAuthenticatedMember()
username = member.getUserName()

endereco_ip = REQUEST.get('endereco_ip', None)
endereco_mac = REQUEST.get('endereco_mac', None)

tempo_expira = time.time() + 5 * 3600 # expira o cookie em cinco horas
expira = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(tempo_expira))

# verifica se existe alguma sessao iniciada
sessao = context.zsql.sessao_plenaria_obter_zsql(ind_iniciada = 1)

#verifica se o login pertence a algum parlamentar
parlamentar = context.zsql.parlamentar_obter_zsql(txt_login=username)

# verifica se a votacao esta aberta
cod_registro_sessao_pre = context.zsql.recomposicao_presencas_sessao_verificar_ultima_aberta_zsql(cod_sessao_plen = cod_sessao_plen)[0].cod_registro_pre
if cod_registro_sessao_pre:
    sessao_aberta = True
else:
    sessao_aberta = False

# verifica se a votacao esta aberta
cod_registro_ordem_pre = context.zsql.recomposicao_presencas_ordem_verificar_ultima_aberta_zsql(cod_sessao_plen = cod_sessao_plen)[0].cod_registro_pre
if cod_registro_ordem_pre:
    ordem_aberta = True
else:
    ordem_aberta = False

if len(sessao) > 0 and len(parlamentar) > 0 and 'Parlamentar' in member.getRoles():
    if context.pysc.rede_sagl_pysc():
        cod_sessao = sessao[0].cod_sessao_plen
        dat_sessao = context.pysc.data_converter_pysc(data=sessao[0].dat_inicio_sessao)
        cod_parlamentar = parlamentar[0].cod_parlamentar
        if sessao_aberta:
            context.pysc.presenca_sessao_pysc(
                cod_parlamentar,
                cod_sessao,
                endereco_ip,
                endereco_mac,
                cod_perfil='parlamentar',
                login=True,
                recontagem=recontagem
            )
            context.zsql.sessao_plenaria_log_incluir_zsql(
                txt_login = username,
                txt_ip = endereco_ip,
                txt_mac = endereco_mac,
                txt_acao = 'registro de presença sessão',
                txt_mensagem = 'O usuário ' + username + ' registrou presença no sistema na sessão plenária usando o equipamento com o IP ' + endereco_ip,
            )
        if ordem_aberta:
            context.pysc.presenca_ordem_dia_pysc(
                cod_sessao,
                cod_parlamentar,
                dat_sessao,
                endereco_ip,
                endereco_mac,
                cod_perfil='parlamentar',
                login=True,
                recontagem=recontagem
            )
            context.zsql.sessao_plenaria_log_incluir_zsql(
                txt_login = username,
                txt_ip = endereco_ip,
                txt_mac = endereco_mac,
                txt_acao = 'registro de presença ordem',
                txt_mensagem = 'O usuário ' + username + ' registrou presença no sistema na ordem do dia usando o equipamento com o IP ' + endereco_ip,
            )
        return True
    else:
        context.zsql.sessao_plenaria_log_incluir_zsql(
            txt_login = username,
            txt_ip = endereco_ip,
            txt_mac = endereco_mac,
            txt_acao = 'registro de presença',
            txt_mensagem = 'O usuario ' + username + ' não conseguiu registrar presença no sistema usando o equipamento com o IP ' + endereco_ip + ' por estar fora da rede.',
        )
        state.set(status='fora_rede')
        return False

elif len(sessao) == 0:
    context.zsql.sessao_plenaria_log_incluir_zsql(
        txt_login = username,
        txt_ip = endereco_ip,
        txt_mac = endereco_mac,
        txt_acao = 'registro de presença',
        txt_mensagem = 'O usuario ' + username + ' não conseguiu registrar presença no sistema usando o equipamento com o IP ' + endereco_ip + ' pois não existe sessão iniciada.',
    )

elif len(parlamentar) == 0:
    context.zsql.sessao_plenaria_log_incluir_zsql(
        txt_login = username,
        txt_ip = endereco_ip,
        txt_mac = endereco_mac,
        txt_acao = 'login no sagl',
        txt_mensagem = 'O usuario ' + username + ' efetuou login no sistema usando o equipamento com o IP ' + endereco_ip,
    )

elif aberta is False:
    context.zsql.sessao_plenaria_log_incluir_zsql(
        txt_login = username,
        txt_ip = endereco_ip,
        txt_mac = endereco_mac,
        txt_acao = 'registro de presença',
        txt_mensagem = 'O usuario ' + username + ' não conseguiu registrar presença no sistema usando o equipamento com o IP ' + endereco_ip + ' pois não existe votação aberta.',
    )
