## Script (Python) "protocolo_prefeitura_pysc"
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

return st.protocolo_prefeitura(cod_materia)

