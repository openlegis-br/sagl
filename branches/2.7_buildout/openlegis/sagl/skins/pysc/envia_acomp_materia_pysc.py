## Script (Python) "confirma_acomp_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

mailhost = context.MailHost

data_registro=DateTime().strftime('%d/%m/%Y')

if hasattr(context.sagl_documentos.props_sagl,'logo_casa.gif'):
  imagem = context.sagl_documentos.props_sagl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao_transp.gif"

casa={}
aux=context.sagl_documentos.props_sagl.propertyItems()
for item in aux:
  casa[item[0]] = item[1]
email_casa = casa['end_email_casa']
casa_legislativa = casa['nom_casa']

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
 ementa = materia.txt_ementa.encode('utf-8')
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

 for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=cod_materia, ind_ult_tramitacao=1):
   data = tramitacao.dat_tramitacao
   status = tramitacao.des_status.encode('utf-8')
   if tramitacao.txt_tramitacao != None:
     texto_acao = tramitacao.txt_tramitacao.encode('utf-8')
   else:
     texto_acao = " "

remetente = email_casa

linkMat = "" + context.consultas.absolute_url()+"/materia/materia_mostrar_proc?cod_materia=" + cod_materia

destinatarios=[]
for destinatario in context.zsql.acomp_materia_obter_inscritos_zsql(cod_materia=cod_materia):
  dic={}
  dic['end_email']=destinatario.end_email.encode('utf-8')
  dic['txt_hash']=destinatario.txt_hash
  destinatarios.append(dic)

for dic in destinatarios:
  hash = dic['txt_hash']
  mMsg = "Prezado(a) Senhor(a),\n\n"
  mMsg = mMsg + "A seguinte matéria de seu interesse sofreu tramitação registrada em " + data_registro + ":\n\n"
  mMsg = mMsg + "" + projeto + "\n"
  mMsg = mMsg + "" + str(ementa) + "\n"
  mMsg = mMsg + "Autoria: " + str(nom_autor) + "\n\n"
  mMsg = mMsg + "Link: " + linkMat + "\n\n"
  mMsg = mMsg + "Data da Ação: " + str(data) + "\n"
  mMsg = mMsg + "Status: " + str(status) + "\n"
  mMsg = mMsg + "Texto da Ação: " + str(texto_acao) + "\n\n"
  mMsg = mMsg + "Cordialmente,\n\n"
  mMsg = mMsg + "" + str(casa_legislativa) +"\n"
  mMsg = mMsg + "Sistema Aberto de Gestão Legislativa\n\n\n"
  mMsg = mMsg + "Clique no link abaixo para excluir seu E-mail da lista de envio:\n" 
  mMsg = mMsg + "" + context.consultas.absolute_url() + "/materia/acompanhamento/acomp_materia_excluir_proc?txt_hash=" + str(hash) +"\n"

  mTo = dic['end_email']

  mSubj = projeto +" - Aviso de Tramitação"

  mailhost.send(mMsg, mTo, remetente, subject=mSubj, encode='base64')
