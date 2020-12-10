## Script (Python) "pdf_gerar_etiquetas_pimaco_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= cod_documento
##title=
##

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

results = context.zsql.destinatario_oficio_obter_zsql(cod_documento=REQUEST['cod_documento'])

dados = []
for row in results:
    r=[]
    # Label, Data
    if row.txt_forma_tratamento != None:
       r.append(row.txt_forma_tratamento)

    if (row.nom_responsavel != None and row.nom_responsavel != '') and (row.nom_responsavel != row.nom_instituicao):
       r.append(row.nom_responsavel)

    if row.des_cargo != None and row.des_cargo != '':
       r.append(row.des_cargo)

    if row.nom_instituicao != None and row.nom_instituicao != '':
       r.append(row.nom_instituicao)

    if row.end_instituicao != None and row.nom_bairro != None and row.nom_bairro != '':
       r.append(row.end_instituicao + " - " +row.nom_bairro)

    elif row.end_instituicao!=None and row.nom_bairro==None:
       r.append(row.end_instituicao)

    nom_cidade = ""
    for localidade in context.zsql.localidade_obter_zsql(cod_localidade=row.cod_localidade):
        nom_cidade = str(localidade.nom_localidade_pesq).decode('utf-8').upper() + ' - ' + str(localidade.sgl_uf)

    if row.num_cep != None:
       r.append('CEP '+row.num_cep+' ' +str(nom_cidade))
    else:
       r.append(str(nom_cidade))

    dados.append(r)

return context.pdflabels(dados)

