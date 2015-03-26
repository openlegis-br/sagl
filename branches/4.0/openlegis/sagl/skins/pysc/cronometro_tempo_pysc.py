## Script (Python) "cronometro_tempo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tipo
##title=
##


tempos = context.zsql.props_painel_eletronico_obter_zsql()

if tipo == 'discurso':
    tempo = tempos[0].txt_orador_tempo
    minutos, segundos = tempo.split(':')
    minutos = int(minutos)
    segundos = int(segundos)
    milisegundos = int(60000 * minutos + 1000 * segundos)

    return milisegundos

elif tipo == 'aparte':
    tempo = tempos[0].txt_apartante_tempo
    minutos, segundos = tempo.split(':')
    minutos = int(minutos)
    segundos = int(segundos)
    milisegundos = int(60000 * minutos + 1000 * segundos)

    return milisegundos

elif tipo == 'ordem':
    tempo = tempos[0].txt_questao_ordem_tempo
    minutos, segundos = tempo.split(':')
    minutos = int(minutos)
    segundos = int(segundos)
    milisegundos = int(60000 * minutos + 1000 * segundos)

    return milisegundos

else:
    return False