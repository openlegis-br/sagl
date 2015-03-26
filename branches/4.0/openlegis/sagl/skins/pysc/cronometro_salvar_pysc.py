## Script (Python) "cronometro_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

request = context.REQUEST

tipo = request.form.get('tipo')
status = ''

int_start = request.form.get('int_start', 0)
if int_start == 'iniciar':
    int_start = 1
    status = 'O cronometro foi iniciado com sucesso!'

int_stop = request.form.get('int_stop', 0)
if int_stop == 'parar':
    int_stop = 1
    status = 'O cronometro foi parado com sucesso!'

int_reset = request.form.get('int_reset', 0)
if int_reset == 'reiniciar':
    int_reset = 1
    status = 'O cronometro foi reiniciado com sucesso!'

if tipo == 'aparte':
    context.zsql.cronometro_aparte_atualizar_zsql(
        int_start=int_start,
        int_stop=int_stop,
        int_reset=int_reset
    )
elif tipo == 'discurso':
    context.zsql.cronometro_discurso_atualizar_zsql(
        int_start=int_start,
        int_stop=int_stop,
        int_reset=int_reset
    )

elif tipo == 'ordem':
    context.zsql.cronometro_ordem_atualizar_zsql(
        int_start=int_start,
        int_stop=int_stop,
        int_reset=int_reset
    )

return status