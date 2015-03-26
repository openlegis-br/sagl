## Script (Python) "tempo_sessao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

sessao = context.zsql.sessao_plenaria_obter_zsql(ind_iniciada=1)

stool = context.portal_sagl

if sessao:
    hora = sessao[0].hr_inicio_sessao
    data = sessao[0].dat_inicio_sessao
    tempo = sessao[0].dat_inicio_sessao + ' ' + sessao[0].hr_inicio_sessao

    return stool.tempo_sessao(tempo)

else:
    return None
