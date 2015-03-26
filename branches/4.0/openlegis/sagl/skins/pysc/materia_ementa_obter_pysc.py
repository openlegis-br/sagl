## Script (Python)
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
##

# obtem a ementa da materia legislativa   
# obtem ementa

codigo=int(cod_materia)
try:
    ementa_materia=context.zsql.materia_obter_zsql(cod_materia=codigo)[0].txt_ementa
except:
    ementa_materia="não foi possível obter a ementa"

return ementa_materia
