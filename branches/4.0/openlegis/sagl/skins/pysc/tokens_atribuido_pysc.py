## Script (Python) "tokens_atribuido_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_votacao=None, votou=None, verificar=None
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

# identifica o login do parlamentar que esta buscando atribuicao do token
membership_tool = getToolByName(context, 'portal_membership')
member = membership_tool.getAuthenticatedMember()
username = member.getUserName()

# apos identificar o login, identificamos o parlamentar pelo codigo
parlamentar = context.zsql.parlamentar_obter_zsql(txt_login=username)
if len(parlamentar) > 0:
    cod_parlamentar = parlamentar[0].cod_parlamentar

request = context.REQUEST

if votou:
    if cod_votacao:
        try:
            context.zsql.votacao_parlamentar_obter_zsql(cod_parlamentar=cod_parlamentar, cod_votacao = cod_votacao)[0].vot_parlamentar
            return True
        except:
            return False
    else:
        return False

if verificar:
    token_cookie = request.get('__token', None)
    atribuidos = st.ler_arquivo_atribuido()
    if token_cookie:
        lista = st.ler_token()

        try:
            token = [item.keys()[0] for item in lista if item.keys()[0] == token_cookie]
            if len(token[0]) > 0:
                return True
            else:
                return False
        except IndexError:
            return False
    else:
        return False


