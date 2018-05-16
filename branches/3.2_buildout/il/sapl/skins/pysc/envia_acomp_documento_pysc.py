## Script (Python) "envia_acomp_documento_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento
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
remetente = email_casa

for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
 ementa = documento.txt_assunto
 proc_adm = documento.des_tipo_documento+" nº "+str(documento.num_documento)+"/"+str(documento.ano_documento)
 nom_autor = documento.txt_interessado

 for tramitacao in context.zsql.tramitacao_administrativo_obter_zsql(cod_documento=cod_documento, ind_ult_tramitacao=1, ind_excluido=0):
   data = tramitacao.dat_encaminha
   status = tramitacao.des_status
   if tramitacao.txt_tramitacao != None:
     texto_acao = tramitacao.txt_tramitacao
   else:
     texto_acao = ""
   unidade_local = ""
   for unid_local in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao=tramitacao.cod_unid_tram_local):
       unidade_local = unid_local.nom_unidade_join
   destinatarios=[]
   cod_usuario_dest = tramitacao.cod_usuario_dest
   unidade_destino = ""
   for unid_destino in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao=tramitacao.cod_unid_tram_dest):
       unidade_destino = unid_destino.nom_unidade_join
       dic={}
       if cod_usuario_dest == None:
          if unid_destino.end_email_join != None:
             dic['end_email']=unid_destino.end_email_join
             dic['txt_nome']=unid_destino.nom_unidade_join
       else:
          for usuario_destino in context.zsql.usuario_obter_zsql(cod_usuario=cod_usuario_dest):
              if usuario_destino.end_email != None:
                 dic['end_email']=usuario_destino.end_email
                 dic['txt_nome']=usuario_destino.nom_completo
       destinatarios.append(dic)

   prazo = tramitacao.dat_fim_prazo

   linkDoc = "" + context.absolute_url()

for dic in destinatarios:
  nome = dic['txt_nome']
  mMsg = "Origem: " + unidade_local + "\n"
  mMsg = "Destino: " + nome + "\n\n"
  mMsg = mMsg + "O seguinte processo administrativo foi despachado aos seus cuidados, para as providências cabíveis:\n\n"
  mMsg = mMsg + "" + proc_adm + "\n"
  mMsg = mMsg + "" + str(ementa) + "\n"
  mMsg = mMsg + "Interessado: " + str(nom_autor) + "\n\n"
  mMsg = mMsg + "Encaminhado em: " + str(data) + "\n"
  mMsg = mMsg + "Status: " + str(status) + "\n"
  if texto_acao != None:
     mMsg = mMsg + "Texto do Despacho: " + str(texto_acao) + "\n\n"
  if prazo != None:
     mMsg = mMsg + "Prazo: " + str(prazo) + "\n\n"
  mMsg = mMsg + "Autentique-se no sistema pelo endereço " + linkDoc + " e verifique sua Caixa de Entrada - módulo Tramitação de Documentos - para maiores detalhes.\n\n"
  mMsg = mMsg + "" + str(casa_legislativa) +"\n"
  mMsg = mMsg + "Processo Administrativo Eletrônico\n\n\n"

  mTo = dic['end_email']

  mSubj = "Processo Administrativo - " + proc_adm +" - Notificação de Despacho em " + data_registro

  mailhost.send(mMsg, mTo, remetente, subject=mSubj, encode='base64')
