request=context.REQUEST
redirect_url=context.portal_url()+'/consultas/sessao_plenaria'
request.RESPONSE.redirect(redirect_url)
