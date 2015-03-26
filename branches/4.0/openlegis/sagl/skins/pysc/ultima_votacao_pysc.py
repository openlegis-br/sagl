## Script (Python) "ultima_votacao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, tipo=0
##title=
##

ordem_dia = context.zsql.ultima_votacao_obter_zsql(cod_sessao_plen = cod_sessao_plen, ind_excluido=0, ind_votacao_iniciada=0)

expediente = context.zsql.ultima_votacao_expediente_obter_zsql(cod_sessao_plen = cod_sessao_plen, ind_excluido=0, ind_votacao_iniciada=0)

if ordem_dia and expediente:
    try:
        ordem_ultima = ordem_dia[0].dat_ultima_votacao
    except IndexError:
        ordem_ultima = None
    try:
        expediente_ultima = expediente[0].dat_ultima_votacao
    except IndexError:
        expediente_ultima = None

    if ordem_ultima > expediente_ultima:
        if tipo:
            return 'ordem'
        else:
            return ordem_dia
    else:
        if tipo:
            return 'expediente'
        else:
            return expediente

elif ordem_dia and not expediente:
    if tipo:
        return 'ordem'
    else:
        return ordem_dia

elif expediente and not ordem_dia:
    if tipo:
        return 'expediente'
    else:
        return expediente

else:
    return None
