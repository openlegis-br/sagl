## Script (Python) "envia_acomp_materia_pysc"
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

data_registro=DateTime().strftime('%d/%m/%Y às %H:%M')

casa={}
aux=context.sapl_documentos.props_sapl.propertyItems()
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

 for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=cod_materia, ind_ult_tramitacao=1):
   data = tramitacao.dat_tramitacao
   status = tramitacao.des_status
   if tramitacao.txt_tramitacao != None:
     texto_acao = tramitacao.txt_tramitacao
   else:
     texto_acao = " "

remetente = email_casa

linkMat = "" + context.consultas.absolute_url()+"/materia/materia_mostrar_proc?cod_materia=" + cod_materia

destinatarios=[]
for destinatario in context.zsql.acomp_materia_obter_inscritos_zsql(cod_materia=cod_materia):
  dic={}
  dic['end_email']=destinatario.end_email
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
  mMsg = mMsg + "Processo Legislativo Eletrônico\n\n\n"
  mMsg = mMsg + "Clique no link abaixo para excluir seu e-mail da lista de envio:\n" 
  mMsg = mMsg + "" + context.consultas.absolute_url() + "/materia/acompanhamento/acomp_materia_excluir_proc?txt_hash=" + str(hash) +"\n"

  mTo = dic['end_email']

  mSubj = projeto +" - Aviso de Tramitação" + data_registro

  mailhost.send(mMsg, mTo, remetente, subject=mSubj, encode='base64')
