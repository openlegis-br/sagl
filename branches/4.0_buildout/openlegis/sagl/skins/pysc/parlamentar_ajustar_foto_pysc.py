## Script (Python) "ajustar_foto_parlamentar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_parlamentar
##title=
##
from Products.CMFCore.utils import getToolByName

fotografia = '%s' % (cod_parlamentar) + "_foto_parlamentar"

if hasattr(context.documentos.parlamentar.fotos,fotografia):
  st = getToolByName(context, 'portal_sagl')
  return st.resize_and_crop(cod_parlamentar)

