## coding: utf-8
## Script (Python) "norma_texto_buscar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=assunto
##title=
##

from Products.AdvancedQuery import Eq, Ge, In

query = Eq('PrincipiaSearchSource',assunto) | Eq('ementa', assunto)
results = context.sapl_documentos.norma_juridica.Catalog.evalAdvancedQuery(query,('tipo_norma',('num_norma','desc'),))

return results
