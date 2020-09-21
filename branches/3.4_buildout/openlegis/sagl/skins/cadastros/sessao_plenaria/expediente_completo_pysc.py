## Script (Python) "expediente_completo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= cod_sessao_plen
##title=
##

REQUEST  = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session  = REQUEST.SESSION

from Products.CMFCore.utils import getToolByName

st = getToolByName(context, 'portal_sapl')

return st.pdf_expediente_completo(cod_sessao_plen)

