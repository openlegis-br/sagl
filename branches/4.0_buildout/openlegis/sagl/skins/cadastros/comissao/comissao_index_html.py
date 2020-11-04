request=context.REQUEST

redirect_url=context.portal_url()+'/consultas/comissao'

request.RESPONSE.redirect(redirect_url)

