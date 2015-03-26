## Script (Python) "autor_materia_validar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia, cod_parlamentar="", cod_comissao="", nom_autor="", ta=1
##
"""
  Função: verifica se o parlamentar é autor da materia informados

  Argumentos: cod_parlamentar, cod_comissao, cod_orgao e cod_materia  --> retorna 1-verdadeiro ou 0-falso.

"""
codm = str(cod_materia)
tipo = str(ta)
cod  = ""
try:
    if tipo=='1':
        cod = str(cod_parlamentar)
        s = context.zsql.autoria_obter_zsql(cod_materia=codm, cod_parlamentar=cod)[0].cod_parlamentar or []
    else:
        if tipo=='2':
            cod = str(cod_comissao)
            s = context.zsql.autoria_obter_zsql(cod_materia=codm, cod_comissao=cod)[0].cod_comissao or []
        else:
            cod = nom_autor
            s = context.zsql.autoria_obter_zsql(cod_materia=codm, nom_autor=cod)[0].nom_autor or []

    if s == cod:
        return 1 #  é autor na matéria indicada

    return 0
except:
    return 0 # não é autor na matéria indicada



