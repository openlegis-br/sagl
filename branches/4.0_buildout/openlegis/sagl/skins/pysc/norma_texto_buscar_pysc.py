## coding: utf-8
## Script (Python) "norma_texto_buscar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=assunto, tipo,
##title=
##

from Products.AdvancedQuery import And, Or, Eq, Ge, In

if tipo != '':
 query = (Eq('tipo_norma', tipo)) & (Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto))

else:
 query = Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto)

results = context.documentos.norma_juridica.Catalog.evalAdvancedQuery(query,('tipo_norma',('num_norma','desc'),))

return results
