## Script (Python) "proposicao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao, modelo_proposicao, modelo_path
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

inf_basicas_dic['url_validacao'] = "" + context.generico.absolute_url()+"/conferir_assinatura"

inf_basicas_dic['id_materia'] = ''

inf_basicas_dic['des_tipo_proposicao'] = ''

for proposicao in context.zsql.proposicao_obter_zsql(cod_proposicao=cod_proposicao):
    inf_basicas_dic['des_tipo_proposicao']= proposicao.des_tipo_proposicao
    num_proposicao = 'PN ' + str(cod_proposicao)
    nom_arquivo = str(proposicao.cod_proposicao)+'.odt'
    des_tipo_materia = proposicao.des_tipo_proposicao.decode('utf-8').upper()
    num_ident_basica = ''
    ano_ident_basica = DateTime().strftime("%Y")
    txt_ementa = proposicao.txt_descricao
    dat_apresentacao = context.pysc.data_converter_por_extenso_pysc(data=DateTime().strftime("%d/%m/%Y"))

    materia_vinculada = {}
    if proposicao.cod_materia != None:
       for materia in context.zsql.materia_obter_zsql(cod_materia = proposicao.cod_materia):
           materia_vinculada['id_materia'] = materia.des_tipo_materia + ' nº ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica)
           materia_vinculada['txt_ementa'] = materia.txt_ementa.decode('utf-8')
           materia_vinculada['autoria'] = ''
           autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
           fields = autores.data_dictionary().keys()
           lista_autor = []
           for autor in autores:
               for field in fields:
                   nome_autor = autor['nom_autor_join']
               lista_autor.append(nome_autor)
           inf_basicas_dic['nome_autor'] = autor.nom_autor_join.decode('utf-8').upper()               
           materia_vinculada['autoria'] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
       
       if proposicao.des_tipo_proposicao == 'Parecer' or proposicao.des_tipo_proposicao == 'Parecer de Comissão':
          inf_basicas_dic['nom_comissao'] = 'COMISSÃO DE XXXXXXX'
          inf_basicas_dic['id_materia'] = materia_vinculada['id_materia']
          inf_basicas_dic['data_parecer'] = context.pysc.data_converter_por_extenso_pysc(data=DateTime().strftime("%d/%m/%Y"))
          for relator in context.zsql.autor_obter_zsql(cod_autor = proposicao.cod_autor):
              inf_basicas_dic['nom_relator'] = relator.nom_autor_join
          inf_basicas_dic['nom_presidente_comissao'] = 'XXXXXXXX'

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
                   autor_dic['nome_autor'] = autor.nom_autor_join.decode('utf-8').upper() + '\n' + partido_autor
                   autor_dic['apelido_autor'] = partido_autor
            else:
               autor_dic['nome_autor'] = autor.nom_autor_join.decode('utf-8').upper()
               autor_dic['apelido_autor'] = ''
               autor_dic['cod_autor'] = autor['cod_autor']
        nom_autor.append(autor_dic)

return st.proposicao_gerar_odt(inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao, modelo_path)

#return inf_basicas_dic['id_materia']
