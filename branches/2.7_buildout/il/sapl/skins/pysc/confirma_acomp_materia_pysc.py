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

if hasattr(context.sapl_documentos.props_sapl,'logo_casa.gif'):
  imagem = context.sapl_documentos.props_sapl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao_transp.gif"

casa={}
aux=context.sapl_documentos.props_sapl.propertyItems()
for item in aux:
  casa[item[0]] = item[1]
email_casa = casa['end_email_casa']
casa_legislativa = casa['nom_casa']

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
 ementa = materia.txt_ementa
 projeto = materia.sgl_tipo_materia.encode('utf-8')+" "+materia.des_tipo_materia.encode('utf-8')+" "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)

 for autoria in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia,ind_primeiro_autor=1):
  dic_autor = {}
  for autor in context.zsql.autor_obter_zsql(cod_autor = autoria.cod_autor):
   nom_autor = " "
   if autor.des_tipo_autor=='Parlamentar':
    for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar):
     nom_autor = parlamentar.nom_completo
   elif autor.des_tipo_autor=='Comissao':
    for comissao in context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao):
     nom_autor = comissao.nom_comissao
   elif autor.des_tipo_autor=='Bancada':
    for bancada in context.zsql.bancada_obter_zsql(cod_bancada=autor.cod_bancada):
     nom_autor = bancada.nom_bancada
   else:
    nom_autor=autor.nom_autor

remetente = email_casa

destinatario = str(end_email)

hash = str(txt_hash)

link = "" + context.consultas.absolute_url() + "/materia/acompanhamento/acomp_materia_confirmar_proc?txt_hash=" + txt_hash

mMsg = "Prezado(a) Senhor(a),\n\n"
mMsg = mMsg + "Para acompanhar por E-mail o andamento da matéria acima identificada, solicitamos que confirme o recebimento de futuras mensagens eletrônicas, clicando no link:\n\n"
mMsg = mMsg + link + "\n\n"
mMsg = mMsg + "Caso não tenha solicitado o acompanhamento dessa matéria em nosso sistema, favor desconsiderar esta mensagem.\n\n"
mMsg = mMsg + "Cordialmente,\n\n"
mMsg = mMsg + ""+ str(casa_legislativa) +"\n"
mMsg = mMsg + "Sistema Aberto de Gestão Legislativa\n"

mSubj = projeto +" - Acompanhamento por E-mail"

mailhost.send(mMsg, destinatario, remetente, subject=mSubj, encode='base64')
