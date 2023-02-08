## Script (Python) "thumb_gerar"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_parlamentar
##title=
##
from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sagl')

foto = cod_parlamentar + '_foto_parlamentar'

if hasattr(context.sapl_documentos.parlamentar.fotos,foto):
 return st.resize_and_crop(cod_parlamentar)
