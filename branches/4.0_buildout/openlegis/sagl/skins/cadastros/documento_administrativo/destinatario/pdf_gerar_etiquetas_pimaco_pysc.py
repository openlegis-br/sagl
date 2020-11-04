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

results =  context.zsql.destinatario_oficio_obter_zsql(cod_documento=REQUEST['cod_documento'])
dados = []
for row in results:
    r=[]
    # Label, Data
    if row[4]!=None:
       r.append(row[4])
    if row[5]!=None:
       r.append(row[5])
    if row[6]!=None:
       r.append(row[6])
    if row[3]!=None and row[3]!=row[5]:
       r.append(row[3])
    if row[7]!=None:
       r.append(row[7])
    for localidade in context.zsql.localidade_obter_zsql(cod_localidade=row.cod_localidade):
        r.append('CEP '+ row[9] + ' ' + localidade.nom_localidade_pesq+' - '+localidade.sgl_uf)
    dados.append(r)
return context.pdflabels(dados)

