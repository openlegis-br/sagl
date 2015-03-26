## Script (Python) "verifica_vigencia_norma_dh_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=
##
import string
datahora=DateTime()
datahora=str(datahora)
sodata=string.split(datahora,' ')
dh=sodata[0]
dhp=string.replace(dh, "/", "-")
return dhp
