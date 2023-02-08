## coding: utf-8
## Script (Python) "materia_texto_buscar_pysc"
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
 query = (Eq('tipo_materia', tipo)) & (Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto))

else:
 query = Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto)

results = context.sapl_documentos.materia.Catalog.evalAdvancedQuery(query,('tipo_materia', ('ano_materia','desc'), ('num_materia','desc'),))

return results
