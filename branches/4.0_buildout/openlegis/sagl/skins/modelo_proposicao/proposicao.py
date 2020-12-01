## Script (Python) "proposicao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao, modelo_proposicao, modelo_path
##title=
##
REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

inf_basicas_dic = {}
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
    casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
estado = context.zsql.localidade_obter_zsql(tip_localidade="U")
for uf in estado:
    if localidade[0].sgl_uf == uf.sgl_uf:
       nom_estado = uf.nom_localidade.encode('utf-8')
       break
inf_basicas_dic['nom_camara']= casa['nom_casa']
inf_basicas_dic["nom_estado"] = nom_estado
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
    inf_basicas_dic['nom_localidade']= local.nom_localidade.encode('utf-8')
    inf_basicas_dic['sgl_uf']= local.sgl_uf

inf_basicas_dic['url_validacao'] = "" + context.generico.absolute_url()+"/conferir_assinatura"

for proposicao in context.zsql.proposicao_obter_zsql(cod_proposicao=cod_proposicao):
    num_proposicao = cod_proposicao
    nom_arquivo = str(proposicao.cod_proposicao)+'.odt'
    for tipo_proposicao in context.zsql.tipo_proposicao_obter_zsql(tip_proposicao = proposicao.tip_proposicao):
        des_tipo_materia = tipo_proposicao.des_tipo_proposicao.upper().encode('utf-8')
    num_ident_basica = ''
    ano_ident_basica = DateTime().strftime("%Y")
    txt_ementa = proposicao.txt_descricao.encode('utf-8')
    dat_apresentacao = context.pysc.data_converter_por_extenso_pysc(data=DateTime().strftime("%d/%m/%Y"))

    if proposicao.cod_materia != None:
       for materia_vinculada in context.zsql.materia_obter_zsql(cod_materia = proposicao.cod_materia):
           materia_vinculada = ' - ' +materia_vinculada.des_tipo_materia + '  ' + str(materia_vinculada.num_ident_basica) + '/' + str(materia_vinculada.ano_ident_basica)
    else:
       materia_vinculada = None

    apelido_autor = ''
    nom_autor = []
    autores = context.zsql.autor_obter_zsql(cod_autor = proposicao.cod_autor)
    fields = autores.data_dictionary().keys()
    for autor in autores:
        autor_dic = {}
        for field in fields:
            nom_parlamentar = ''
            partido_autor = ''
            nom_cargo = ''                
            if autor.cod_parlamentar != None:
               parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
               for parlamentar in parlamentares:
                   nom_parlamentar = " - " + parlamentar.nom_parlamentar
                   if parlamentar.sex_parlamentar == 'M':
                      nom_cargo = 'Vereador'
                   elif parlamentar.sex_parlamentar == 'F':
                      nom_cargo = 'Vereadora'                       
                   if parlamentar.sgl_partido !=None:
                      partido_autor = nom_cargo + ' - ' + parlamentar.sgl_partido
                   else:
                      partido_autor = nom_cargo
                   autor_dic['nome_autor'] = autor.nom_autor_join.upper() + '\n' + partido_autor
                   autor_dic['apelido_autor'] = partido_autor
            else:
               autor_dic['nome_autor'] = autor.nom_autor_join.upper()
               autor_dic['apelido_autor'] = ''
               autor_dic['cod_autor'] = autor['cod_autor']
        nom_autor.append(autor_dic)

return context.proposicao_gerar_odt(inf_basicas_dic,num_proposicao,nom_arquivo,des_tipo_materia,num_ident_basica,ano_ident_basica,txt_ementa,materia_vinculada,dat_apresentacao,nom_autor,apelido_autor,modelo_proposicao,modelo_path)
