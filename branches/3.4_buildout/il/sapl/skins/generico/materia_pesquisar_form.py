request=context.REQUEST
redirect_url=context.portal_url()+'/consultas/materia?'+request.get('QUERY_STRING')
request.RESPONSE.redirect(redirect_url)
