## Script (Python)
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_localidade
##title=
##

# obtem nome do município da Casa Legislativa que utiliza o SAPL  

# obtem municipio
codigo=int(cod_localidade)
nom_local=[]
local=""
try:
   nom_local=context.zsql.localidade_obter_zsql(cod_localidade=codigo)[0]
   local=nom_local.nom_localidade + ' - ' + nom_local.sgl_uf
except:
   local=""

return local

