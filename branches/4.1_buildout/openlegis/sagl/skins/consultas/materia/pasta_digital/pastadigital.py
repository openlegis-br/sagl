## Script (Python) "pastadigital"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
##

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

return st.pasta_digital(cod_materia)
