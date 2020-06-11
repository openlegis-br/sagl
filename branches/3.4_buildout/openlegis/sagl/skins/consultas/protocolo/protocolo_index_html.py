from Products.CMFCore.utils import getToolByName 

request=context.REQUEST

mt = getToolByName(context, 'portal_membership') 

if  mt.isAnonymousUser(): 
    redirect_url=context.portal_url()+'/consultas/protocolo/pesquisa_publica_form' 
else:
    redirect_url=context.portal_url()+'/consultas/protocolo/protocolo_pesquisar_form'

request.RESPONSE.redirect(redirect_url)
