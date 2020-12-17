## Script (Python) "materias_expediente"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    relatorio_dic = {}
    tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
    relatorio_dic["id_sessao"] = str(sessao.num_sessao_plen)+'ª Sessão ' + tipo_sessao.nom_sessao + ', em ' + sessao.dat_inicio_sessao
    nom_arquivo = str(sessao.cod_sessao_plen)+ '_materias_expediente.odt'
    data_sessao = sessao.dat_inicio_sessao

lst_indicacao = []
lst_requerimento = []
lst_mocao = []
lst_geral = []

total_indicacao = []
total_requerimento = []
total_mocao = []
total_geral = []
assuntos= []

autores = []

for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):

    for autoria in context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia):
        dic_autores = {}
        dic_autores["cod_autor"] = autoria['cod_autor']
        dic_autores["nom_autor_join"] = autoria['nom_autor_join']
        autores.append(dic_autores)

    if item.cod_materia != None:

       for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,ind_excluido=0):

           if materia.des_tipo_materia == 'Indicação':
              num_ident_basica = materia.num_ident_basica
              dic_indicacao = {}
              dic_indicacao['num_materia'] = str(materia.num_ident_basica)
              dic_indicacao['des_assunto'] = None
              if materia.cod_assunto_sel != None:
                 for assunto in context.zsql.assunto_materia_obter_zsql(cod_assunto=materia.cod_assunto_sel):
                     dic_indicacao['des_assunto'] = assunto.des_assunto
              for autor in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia):
                  if autor.cod_autor != None:
                     total_indicacao.append(num_ident_basica)
                     dic_indicacao['cod_autor'] = int(autor.cod_autor)
                     lst_indicacao.append(dic_indicacao)

           if materia.des_tipo_materia == 'Requerimento':
              num_ident_basica = materia.num_ident_basica
              dic_requerimento = {}
              dic_requerimento['num_materia'] = str(materia.num_ident_basica)
              dic_requerimento['des_assunto'] = None
              if materia.cod_assunto_sel != None:
                 for assunto in context.zsql.assunto_materia_obter_zsql(cod_assunto=materia.cod_assunto_sel):
                     dic_requerimento['des_assunto'] = assunto.des_assunto
                     dic_requerimento['cod_assunto'] = int(assunto.cod_assunto)
                     dic_assunto = {}
                     dic_assunto['cod_assunto'] = int(assunto.cod_assunto)
                     dic_assunto['des_assunto'] = assunto.des_assunto
                     assuntos.append(dic_assunto)
              for autor in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia):
                  if autor.cod_autor != None:
                     dic_requerimento['cod_autor'] = int(autor.cod_autor)
                     total_requerimento.append(num_ident_basica)
                     lst_requerimento.append(dic_requerimento)

           if materia.des_tipo_materia == 'Moção':
              num_ident_basica = materia.num_ident_basica
              dic_mocao = {}
              dic_mocao['num_materia'] = str(materia.num_ident_basica)
              dic_mocao['des_assunto'] = None
              if materia.cod_assunto_sel != None:
                 for assunto in context.zsql.assunto_materia_obter_zsql(cod_assunto=materia.cod_assunto_sel):
                     dic_mocao['des_assunto'] = assunto.des_assunto
                     dic_mocao['cod_assunto'] = assunto.cod_assunto
              for autor in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia):
                  if autor.cod_autor != None:
                     dic_mocao['cod_autor'] = int(autor.cod_autor)
                     total_mocao.append(num_ident_basica)
                     lst_mocao.append(dic_mocao)

           num_ident_basica = materia.num_ident_basica
           dic_geral = {}
           dic_geral['num_materia'] = materia.sgl_tipo_materia[0] + '-' + str(materia.num_ident_basica)
           dic_geral['des_assunto'] = None
           if materia.cod_assunto_sel != None:
              for assunto in context.zsql.assunto_materia_obter_zsql(cod_assunto=materia.cod_assunto_sel):
                  dic_geral['des_assunto'] = assunto.des_assunto
                  dic_geral['cod_assunto'] = assunto.cod_assunto
           for autor in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia):
               if autor.cod_autor != None:
                  dic_geral['cod_autor'] = int(autor.cod_autor)
                  total_geral.append(num_ident_basica)
                  lst_geral.append(dic_geral)

relatorio_dic["total_ind"] = str(len(total_indicacao))
relatorio_dic["total_req"] = str(len(total_requerimento))
relatorio_dic["total_moc"] = str(len(total_mocao))
relatorio_dic["total_geral"] = str(len(total_geral))

total_assuntos = []
for materia in lst_geral:
    id_assunto = materia.get('des_assunto',materia)
    if id_assunto != None:
       total_assuntos.append(id_assunto)

a = total_assuntos
total_assuntos = dict((i, a.count(i)) for i in a)

qtde_assuntos = []
for key in total_assuntos:
    assunto = str(key) + ':' +str(total_assuntos[key])
    qtde_assuntos.append(assunto)  

total_assuntos = ' / '.join(['%s' % (value) for (value) in qtde_assuntos])

autores = [
  e
  for i, e in enumerate(autores)
  if autores.index(e) == i
]

autores.sort(key=lambda dic_autores: dic_autores['nom_autor_join'])

parlamentares= []
for parlamentar in autores:
    dic_parlamentar = {}
    dic_parlamentar['nom_parlamentar'] = parlamentar.get('nom_autor_join',parlamentar)
    dic_parlamentar['cod_autor'] = int(parlamentar.get('cod_autor',parlamentar))

    dic_parlamentar["materias"] = ''
    lista_materias = []
    for materia in lst_geral:
        if int(parlamentar.get('cod_autor',parlamentar)) == int(materia.get('cod_autor',materia)):
           if materia.get('des_assunto',materia) != None:         
              materias = materia.get('num_materia',materia) + ' (' + str(materia.get('des_assunto',materia)) + ')'
           else:
              materias = materia.get('num_materia',materia)
           lista_materias.append(materias)
    dic_parlamentar["qtde_materias"] = str(len(lista_materias))

    lista_ind = []
    for materia in lst_indicacao:
        if int(parlamentar.get('cod_autor',parlamentar)) == int(materia.get('cod_autor',materia)):
           if materia.get('des_assunto',materia) != None:         
              materias = materia.get('num_materia',materia) + ' (' + str(materia.get('des_assunto',materia)) + ')'
           else:
              materias = materia.get('num_materia',materia)
           lista_ind.append(materias)
    if len(lista_ind) > 0:
       lista_ind = ', '.join(['%s' % (value) for (value) in lista_ind])
    else:
       lista_ind = ''
    dic_parlamentar["lista_ind"] = lista_ind

    lista_req = []
    for materia in lst_requerimento:
        if int(parlamentar.get('cod_autor',parlamentar)) == int(materia.get('cod_autor',materia)):
           if materia.get('des_assunto',materia) != None:         
              materias = materia.get('num_materia',materia) + ' (' + str(materia.get('des_assunto',materia)) + ')'
           else:
              materias = materia.get('num_materia',materia)
           lista_req.append(materias)
    if len(lista_req) > 0:
       lista_req = ', '.join(['%s' % (value) for (value) in lista_req])
    else:
       lista_req = ''
    dic_parlamentar["lista_req"] = lista_req

    lista_moc = []
    for materia in lst_mocao:
        if int(parlamentar.get('cod_autor',parlamentar)) == int(materia.get('cod_autor',materia)):
           if materia.get('des_assunto',materia) != None:         
              materias = materia.get('num_materia',materia) + ' (' + str(materia.get('des_assunto',materia)) + ')'
           else:
              materias = materia.get('num_materia',materia)
           lista_moc.append(materias)
    if len(lista_moc) > 0:
       lista_moc = ', '.join(['%s' % (value) for (value) in lista_moc])
    else:
       lista_moc = ''
    dic_parlamentar["lista_moc"] = lista_moc

    parlamentares.append(dic_parlamentar)

return st.materias_expediente_gerar_ods(relatorio_dic, total_assuntos, parlamentares, nom_arquivo)

