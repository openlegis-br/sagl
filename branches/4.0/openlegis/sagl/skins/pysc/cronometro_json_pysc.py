## Script (Python) "cronometro_json_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tipo=""
##title=
##

import simplejson as json
cronometros = ''
if tipo == 'aparte':
    cronometros = context.zsql.cronometro_aparte_obter_zsql()[0]
elif tipo == 'discurso':
    cronometros = context.zsql.cronometro_discurso_obter_zsql()[0]
elif tipo == 'ordem':
    cronometros = context.zsql.cronometro_ordem_obter_zsql()[0]

dump=json.dumps({"start": cronometros.int_start,
                   "stop": cronometros.int_stop,
                   "reset": cronometros.int_reset})

return dump
