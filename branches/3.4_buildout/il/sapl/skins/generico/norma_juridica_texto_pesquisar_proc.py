request=context.REQUEST
redirect_url=context.portal_url()+'/consultas/norma_juridica/norma_juridica_texto_pesquisar_proc?'+request.get('QUERY_STRING')
request.RESPONSE.redirect(redirect_url)
