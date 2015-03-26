## Script (Python) "tokens_gerar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, criar=None, remover=None
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

if criar:
    tip_sessao = context.REQUEST.form.get('tip_sessao', None)

    tokens = st.gera_token(cod_sessao_plen, criar=True)
    st.remover_arquivo_atribuido()

    if tip_sessao:

        if 'token_quantidade' in context.REQUEST['HTTP_REFERER']:
            url = context.REQUEST['HTTP_REFERER'][:-19] + '&token_quantidade=' + str(tokens)
        else:
            url = context.REQUEST['HTTP_REFERER'] + '&token_quantidade=' + str(tokens)

        return context.REQUEST.RESPONSE.redirect(url)

    else:

        if tokens:
            return True
        else:
            return False

if remover:
    st.remover_token()
    st.remover_arquivo_atribuido()