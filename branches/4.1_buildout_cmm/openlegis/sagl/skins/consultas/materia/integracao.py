## Script (Python) "integracao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
##
import simplejson as json
data = {}
for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia, ind_excluido=0):
    data['codmateria'] = materia.cod_materia
    data['tipo'] = materia.des_tipo_materia
    data['numero'] = materia.num_ident_basica
    data['ano'] = materia.ano_ident_basica
    data['ementa'] = materia.txt_ementa
    data['autoria'] = ''
    autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia, ind_excluido=0)
    fields = autores.data_dictionary().keys()
    lista_autor = []
    for autor in autores:
        for field in fields:
            nome_autor = autor['nom_autor_join']
        lista_autor.append(nome_autor)
    data['autoria'] = ', '.join(['%s' % (value) for (value) in lista_autor])
    data['linkarquivo'] = ''
    if hasattr(context.sapl_documentos.materia, str(materia.cod_materia) + '_texto_integral.pdf'):
       data['linkarquivo'] = context.portal_url() + '/sapl_documentos/materia/' + str(materia.cod_materia) + '_texto_integral.pdf'
    data['casalegislativa'] = context.sapl_documentos.props_sagl.nom_casa
    data['prazo'] = ''
    for tram in context.zsql.tramitacao_obter_zsql(cod_materia=cod_materia, ind_ult_tramitacao=1):
        if tram.dat_fim_prazo != None:
           data['prazo'] = tram.dat_fim_prazo
serialized = json.dumps(data, sort_keys=True, indent=3, ensure_ascii=False).encode('utf8')
print(serialized.decode())
return printed

