## Script (Python) "materia_texto_buscar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=assunto, tipo, numero, ano
##title=
##

from Products.AdvancedQuery import And, Or, Eq, Ge, In

if numero != '':
    numero = int(numero)
else:
    numero = ''

if ano != '':
    ano = int(ano)
else:
    ano = ''

if tipo != '' and numero == '' and ano == '':
    query = (Eq('tipo_materia', tipo) & ~ Eq('ano_materia', ano) & ~ Eq('num_materia', numero)) & (Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto))

if tipo == '' and numero == '' and ano != '':
    query = Eq('ano_materia', ano) & (Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto))

else:
    query = Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto)

results = context.sagl_documentos.materia.Catalog.evalAdvancedQuery(query,('tipo_materia', ('num_materia', 'desc'),))

return results
