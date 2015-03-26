## Script (Python) "get_geolocation_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cep
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

localidade = context.sagl_documentos.props_sagl.cod_localidade
cidade = context.zsql.localidade_obter_zsql(cod_localidade=localidade)
if cidade:
    cidade = cidade[0].nom_localidade

return st.get_geolocations(cidade, cep)