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

if hasattr(context.sapl_documentos.parlamentar.fotos,fotografia):
  st = getToolByName(context, 'portal_sapl')
  return st.resize_and_crop(cod_parlamentar)

