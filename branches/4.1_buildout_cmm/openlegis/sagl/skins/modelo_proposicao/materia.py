## Script (Python) "materia"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia, modelo_proposicao
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

inf_basicas_dic['nom_prefeito'] = 'Não Cadastrado'
inf_basicas_dic['par_prefeito'] = 'Não Cadastrado'

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
    num_proposicao = " "
    nom_arquivo = str(materia.cod_materia)+'_texto_integral.odt'
    des_tipo_materia = materia.des_tipo_materia.decode('utf-8').upper()
    num_ident_basica = materia.num_ident_basica
    ano_ident_basica = materia.ano_ident_basica
    txt_ementa = materia.txt_ementa
    dat_apresentacao = context.pysc.data_converter_por_extenso_pysc(data=materia.dat_apresentacao)
    for prefeito in context.zsql.prefeito_atual_obter_zsql(data_composicao = materia.dat_apresentacao):
        inf_basicas_dic['nom_prefeito'] = prefeito.nom_completo
        inf_basicas_dic['par_prefeito'] = prefeito.sgl_partido        
    materia_vinculada = ''
    nom_autor = []
    autores = context.zsql.autor_obter_zsql(cod_autor = proposicao.cod_autor)
    fields = autores.data_dictionary().keys()
    for autor in autores:
        autor_dic = {}
        for field in fields:
            if autor.cod_parlamentar != None:
               parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
               for parlamentar in parlamentares:
                   if parlamentar.sex_parlamentar == 'M':
                      nom_cargo = 'Vereador'
                   elif parlamentar.sex_parlamentar == 'F':
                      nom_cargo = 'Vereadora'
                   if parlamentar.sgl_partido != None:
                      partido_autor = parlamentar.sgl_partido
                   else:
                      partido_autor = ''
                   autor_dic['nome_autor'] = parlamentar.nom_completo
                   autor_dic['apelido_autor'] = parlamentar.nom_parlamentar
                   autor_dic['partido'] = partido_autor
                   autor_dic['cargo'] = nom_cargo
            else:
               autor_dic['nome_autor'] = autor.nom_autor_join.decode('utf-8').upper()
               autor_dic['apelido_autor'] = autor.nom_autor_join.decode('utf-8').upper()
               autor_dic['partido'] = ''
               autor_dic['cargo'] = autor.des_cargo
            autor_dic['cod_autor'] = int(autor['cod_autor'])
        nom_autor.append(autor_dic)

data_atual = DateTime().strftime("%d/%m/%Y")

subscritores = []
outros_autores = context.zsql.autores_obter_zsql(txt_dat_apresentacao=data_atual)
fields = outros_autores.data_dictionary().keys()
for autor in outros_autores:
    outros_dic = {}
    for field in fields:
        if autor.cod_parlamentar != None:
           parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
           for parlamentar in parlamentares:
               if parlamentar.sgl_partido != None:
                  partido_autor = parlamentar.sgl_partido
               else:
                  partido_autor = "Sem partido"
               if parlamentar.sex_parlamentar == 'M':
                  cargo = "Vereador"
               elif parlamentar.sex_parlamentar == 'F':
                  cargo = "Vereadora"
           outros_dic['nome_autor'] = parlamentar.nom_completo
           outros_dic['apelido_autor'] = parlamentar.nom_parlamentar
           outros_dic['partido'] = partido_autor
           outros_dic['cargo'] = cargo
        outros_dic['cod_autor'] = int(autor['cod_autor'])
    subscritores.append(outros_dic)

outros=[]
for autor in nom_autor:
    for subscritor in subscritores:
        if autor.get('cod_autor',autor) != subscritor.get('cod_autor',subscritor):
           outros.append(subscritor)
subscritores = outros

return st.materia_gerar_odt(inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, subscritores, modelo_proposicao)
