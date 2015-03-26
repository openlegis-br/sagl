## Script (Python) "tokens_atribuir_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=atribuir=None, remover=None
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

REQUEST = context.REQUEST

if atribuir:
    lista = st.ler_token()
    atribuidos = st.ler_arquivo_atribuido()

#    tokens = [item.keys()[0] for item in lista]

    token_cookie = REQUEST.get('__token', None)

#    if token_cookie and token_cookie not in tokens:
#        REQUEST.RESPONSE.expireCookie('__token', path='/')

    if cod_parlamentar in atribuidos:
        atribuido = True
    else:
        atribuidos.append(cod_parlamentar)
        arquivo_atribuido = st.arquivo_atribuido()
        for item in atribuidos:
            st.grava_arquivo_atribuido(arquivo_atribuido, item)
        atribuido = False

    try:
        token = [item.keys()[0] for item in lista if item.keys()[0] == token_cookie]
    except IndexError:
        token = ''
    count = 0
    for item in lista:
        if token_cookie or atribuido:
            if token_cookie == item.keys()[0]:
                break

        if len(token) == 0 and item[item.keys()[0]][0] != 1 and not atribuido:
            REQUEST.RESPONSE.setCookie('__token', item.keys()[0], path='/')
            lista[count][item.keys()[0]][0] = 1
            break

        if not token_cookie and item[item.keys()[0]][0] != 1 and not atribuido:
            REQUEST.RESPONSE.setCookie('__token', item.keys()[0], path='/')
            lista[count][item.keys()[0]][0] = 1
            break
        count += 1

    arquivo = st.arquivo_token()

    for item in lista:
        st.grava_token(arquivo, item)

if remover:
    REQUEST.RESPONSE.expireCookie('__token', path='/')
