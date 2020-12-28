## Script (Python) "confirma_acomp_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=end_email, txt_hash, cod_materia
##title=
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

mailhost = context.MailHost

if hasattr(context.sapl_documentos.props_sagl,'logo_casa.gif'):
  imagem = context.sapl_documentos.props_sagl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao.gif"

casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
  casa[item[0]] = item[1]
email_casa = casa['end_email_casa']
casa_legislativa = casa['nom_casa']

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
 ementa = materia.txt_ementa
 projeto = materia.des_tipo_materia+" nº "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)

 nom_autor = ""
 autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
 fields = autores.data_dictionary().keys()
 lista_autor = []
 for autor in autores:
   for field in fields:
     nome_autor = autor['nom_autor_join']
   lista_autor.append(nome_autor)
 nom_autor = ', '.join(['%s' % (value) for (value) in lista_autor])

remetente = email_casa

destinatario = str(end_email)

hash = str(txt_hash)

link = "" + context.consultas.absolute_url() + "/materia/acompanhamento/acomp_materia_confirmar_proc?txt_hash=" + txt_hash

mMsg = "Prezado(a) Senhor(a),\n\n"
mMsg = mMsg + "Para acompanhar por e-mail o andamento da matéria acima identificada, solicitamos que confirme o recebimento de futuras mensagens eletrônicas, clicando no link:\n\n"
mMsg = mMsg + link + "\n\n"
mMsg = mMsg + "Caso não tenha solicitado o acompanhamento dessa matéria em nosso sistema, favor desconsiderar a presente mensagem.\n\n"
mMsg = mMsg + "Cordialmente,\n\n"
mMsg = mMsg + ""+ str(casa_legislativa) +"\n"
mMsg = mMsg + "Processo Legislativo Eletrônico\n"

mSubj = projeto +" - Acompanhamento por e-mail"

mailhost.send(mMsg, destinatario, remetente, subject=mSubj, encode='base64')
