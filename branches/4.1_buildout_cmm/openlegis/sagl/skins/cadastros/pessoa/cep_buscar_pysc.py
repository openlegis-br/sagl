## Script (Python) "unidades_carregar"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= numcep
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.cep_buscar(numcep)


