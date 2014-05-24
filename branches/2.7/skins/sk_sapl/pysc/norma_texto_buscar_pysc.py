## coding: utf-8
## Script (Python) "norma_texto_buscar_pysc"
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

if tipo != '' and numero =='' and ano =='':
 query = (Eq('tipo_norma', tipo) & ~ Eq('ano_norma', ano) & ~ Eq('num_norma', numero)) & (Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto))

if tipo == '' and numero =='' and ano !='':
 query = Eq('ano_norma', ano) & (Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto))

else:
 query = Eq('ementa', assunto) | Eq('PrincipiaSearchSource', assunto)

results = context.sapl_documentos.norma_juridica.Catalog.evalAdvancedQuery(query,('tipo_norma',('num_norma','desc'),))

return results
