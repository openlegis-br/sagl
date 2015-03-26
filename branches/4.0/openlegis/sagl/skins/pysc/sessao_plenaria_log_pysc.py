## Script (Python) "sessao_plenaria_log_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=txt_acao, txt_mensagem, cod_sessao_plen=None
##title=
##

from Products.CMFCore.utils import getToolByName

REQUEST = context.REQUEST
membership_tool = getToolByName(context, 'portal_membership')

if membership_tool.isAnonymousUser():
    REQUEST.RESPONSE.expireCookie('endereco_ip', path='/')
    REQUEST.RESPONSE.expireCookie('endereco_mac', path='/')

member = membership_tool.getAuthenticatedMember()
username = member.getUserName()

endereco_ip = REQUEST.get('endereco_ip', None)
endereco_mac = REQUEST.get('endereco_mac', None)

context.zsql.sessao_plenaria_log_incluir_zsql(
    cod_sessao_plen = cod_sessao_plen,
    txt_login = username,
    txt_ip = endereco_ip,
    txt_mac = endereco_mac,
    txt_acao = txt_acao,
    txt_mensagem = txt_mensagem
)
