request=context.REQUEST
redirect_url=context.portal_url()+'/consultas/materia/materia_pesquisar_proc?'+request.get('QUERY_STRING')
request.RESPONSE.redirect(redirect_url)
