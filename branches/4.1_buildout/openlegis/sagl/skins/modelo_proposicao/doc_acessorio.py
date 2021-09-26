## Script (Python) "doc_acessorio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento, cod_materia, modelo_proposicao
##title=
##
from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

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
        nom_estado = uf.nom_localidade
        break
inf_basicas_dic['nom_camara']= casa['nom_casa']
inf_basicas_dic["nom_estado"] = nom_estado
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
    inf_basicas_dic['nom_localidade']= local.nom_localidade
    inf_basicas_dic['sgl_uf']= local.sgl_uf

for documento in context.zsql.documento_acessorio_obter_zsql(cod_documento=cod_documento, cod_materia=cod_materia, ind_excluido=0):
    nom_arquivo = str(documento.cod_documento)+ '.odt'
    nom_documento = documento.nom_documento
    if documento.txt_ementa != None:
       txt_ementa = documento.txt_ementa
    else:
       txt_ementa = " "
    dat_documento = documento.dat_documento
    data_documento = context.pysc.data_converter_por_extenso_pysc(data=documento.dat_documento)    
    apelido_autor = ''
    nom_autor = []
    for proposicao in context.zsql.proposicao_obter_zsql(ind_mat_ou_doc='D', cod_mat_ou_doc=cod_documento):
        if proposicao.cod_proposicao != None:
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
                          inf_basicas_dic['nome_autor'] = autor.nom_autor_join.decode('utf-8').upper()                             
                          autor_dic['nome_autor'] = autor.nom_autor_join.decode('utf-8').upper() + '\n' + partido_autor
                          autor_dic['apelido_autor'] = partido_autor
                   else:
                      autor_dic['nome_autor'] = autor.nom_autor_join.decode('utf-8').upper()
                      autor_dic['apelido_autor'] = ''
                      autor_dic['cod_autor'] = autor['cod_autor']
               nom_autor.append(autor_dic)
        else:
           autor_dic['nome_autor'] = documento.nom_autor_documento
           inf_basicas_dic['nome_autor'] = documento.nom_autor_documento
           nom_autor.append(autor_dic)
 
    for tipo_documento in context.zsql.tipo_documento_obter_zsql(tip_documento=documento.tip_documento):
        des_tipo_documento = tipo_documento.des_tipo_documento

    materia_vinculada = {}
    for materia in context.zsql.materia_obter_zsql(cod_materia = documento.cod_materia):
        materia_vinculada['id_materia'] = materia.des_tipo_materia + ' nº ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica)
        materia_vinculada['txt_ementa'] = materia.txt_ementa
        materia_vinculada['autoria'] = ''
        autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia,)
        fields = autores.data_dictionary().keys()
        lista_autor = []
        for autor in autores:
            for field in fields:
                nome_autor = autor['nom_autor_join']
                inf_basicas_dic['nome_autor'] = autor['nom_autor_join']       
            lista_autor.append(nome_autor)
        materia_vinculada['autoria'] = ', '.join(['%s' % (value) for (value) in lista_autor])

return st.doc_acessorio_gerar_odt(inf_basicas_dic, nom_arquivo, des_tipo_documento, nom_documento, txt_ementa, dat_documento, data_documento, nom_autor, materia_vinculada, modelo_proposicao)
