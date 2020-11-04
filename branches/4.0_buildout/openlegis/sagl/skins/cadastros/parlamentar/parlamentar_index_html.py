request=context.REQUEST

redirect_url=context.portal_url()+'/consultas/parlamentar'

request.RESPONSE.redirect(redirect_url)

