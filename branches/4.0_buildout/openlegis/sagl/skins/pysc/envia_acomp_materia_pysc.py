## Script (Python) "envia_acomp_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
from Products.PythonScripts.standard import url_unquote
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

mailhost = context.MailHost

data_registro=DateTime().strftime('%d/%m/%Y às %H:%M')

casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
  casa[item[0]] = item[1]
email_casa = casa['end_email_casa']
casa_legislativa = casa['nom_casa']

destinatarios=[]

for destinatario in context.zsql.acomp_materia_obter_inscritos_zsql(cod_materia=cod_materia):
  dic={}
  dic['end_email']=destinatario.end_email
  dic['txt_hash']=destinatario.txt_hash
  destinatarios.append(dic)

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
   prazo = tramitacao.dat_fim_prazo   
   if tramitacao.txt_tramitacao != None:
     texto_acao = url_unquote(tramitacao.txt_tramitacao)
   else:
     texto_acao = ''
   unidade_local = ''     
   for unid_local in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao=tramitacao.cod_unid_tram_local):
       unidade_local = unid_local.nom_unidade_join
   if tramitacao.cod_usuario_dest != None:
      for usuario_destino in context.zsql.usuario_obter_zsql(cod_usuario=tramitacao.cod_usuario_dest):
          if usuario_destino.end_email != None:
             dic_usuario={} 
             dic_usuario['end_email'] = usuario_destino.end_email
             dic_usuario['txt_hash']= ''
             destinatarios.append(dic_usuario)
             txt_nome=usuario_destino.nom_completo             
   else:
      for unid_destino in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = tramitacao.cod_unid_tram_dest):
          unidade_destino = unid_destino.nom_unidade_join
          if unid_destino.end_email_join != None and unid_destino.end_email_join != '':
             dic_unidade={} 
             dic_unidade['end_email'] = unid_destino.end_email_join
             dic_unidade['txt_hash']= ''
             destinatarios.append(dic_unidade)     
             txt_nome=unidade_destino                         

remetente = email_casa

linkMat = "" + context.consultas.absolute_url()+"/materia/materia_mostrar_proc?cod_materia=" + str(cod_materia)

for dic in destinatarios:
  mMsg = "Prezado(a) Senhor(a),\n\n"
  mMsg = mMsg + "A seguinte matéria legislativa sofreu tramitação registrada em " + data_registro + ":\n\n"
  mMsg = mMsg + "" + projeto + "\n"
  mMsg = mMsg + "" + str(ementa) + "\n"
  mMsg = mMsg + "Autoria: " + str(nom_autor) + "\n"
  mMsg = mMsg + "Link: " + linkMat + "\n\n"
  mMsg = mMsg + "Data da Ação: " + str(data) + "\n"
  mMsg = mMsg + "Origem: " + unidade_local + "\n"
  mMsg = mMsg + "Destino: " + txt_nome + "\n"  
  mMsg = mMsg + "Status: " + str(status) + "\n"
  if prazo != None:
     mMsg = mMsg + "Prazo: " + str(prazo) + "\n\n"  
  mMsg = mMsg + "" + str(casa_legislativa) +"\n"
  mMsg = mMsg + "Processo Eletrônico\n\n"
  if dic['txt_hash'] != None:  
     mMsg = mMsg + "Clique no link abaixo para excluir seu e-mail da lista de envio:\n" 
     mMsg = mMsg + "" + request.SERVER_URL + "/materia/acompanhamento/acomp_materia_excluir_proc?txt_hash=" + str(dic['txt_hash']) +"\n"

  mTo = dic['end_email']

  mSubj = projeto +" - Aviso de tramitação registrada em " + data_registro

  mailhost.send(mMsg, mTo, remetente, subject=mSubj, encode='base64')
