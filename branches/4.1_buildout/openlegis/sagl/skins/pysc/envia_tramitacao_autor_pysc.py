## Script (Python) "envia_tramitacao_autor_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
from Products.PythonScripts.standard import url_unquote
from email.mime.text import MIMEText
request=context.REQUEST
response=request.RESPONSE

mailhost = context.MailHost

data_registro=DateTime().strftime('%d/%m/%Y às %H:%M')

casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
  casa[item[0]] = item[1]
email_casa = casa['end_email_casa']
casa_legislativa = casa['nom_casa']

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
 ementa = materia.txt_ementa
 projeto = materia.des_tipo_materia+" "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)

 nom_autor = ""
 autorias = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
 fields = autorias.data_dictionary().keys()
 lista_autor = []
 lista_codigo = []
 for autor in autorias:
   for field in fields:
     cod_autor = int(autor['cod_autor'])
     nome_autor = autor['nom_autor_join']
   lista_codigo.append(cod_autor)
   lista_autor.append(nome_autor)
 nom_autor = ', '.join(['%s' % (value) for (value) in lista_autor])

 data = ''
 status = ''
 texto_acao = ''
 for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=cod_materia, ind_ult_tramitacao=1):
   data = tramitacao.dat_tramitacao
   status = tramitacao.des_status
   if tramitacao.txt_tramitacao != None:
     texto_acao = url_unquote(tramitacao.txt_tramitacao)
   else:
     texto_acao = " "

remetente = email_casa

cod_materia_base64 = context.pysc.b64encode_pysc(codigo=str(cod_materia))

linkMat = request.SERVER_URL+"/consultas/materia/materia_mostrar_proc?cod_materia=" + cod_materia_base64

destinatarios=[]
for item in lista_codigo:
 for destinatario in context.zsql.autor_obter_zsql(cod_autor=item):
  dic={}
  dic['end_email']=destinatario.end_email
  if dic['end_email'] != None:
   destinatarios.append(dic)

for dic in destinatarios:
   html = """\
   <html>
     <head></head>
     <body>
       <p>A seguinte matéria de sua autoria sofreu tramitação registrada em {data_registro}:</p>
       <p><a href="{linkMat}" target="blank">{projeto}</a><br>
          {ementa}<br>
          Autoria: {nom_autor}<br>    
          Data da Ação: {data}<br>
          Status: {status}
       </p>
       <p>
          <strong>{casa_legislativa}</strong><br>
          Processo Eletrônico
       </p>
     </body>
   </html>
   """.format(data_registro=data_registro, projeto=projeto, linkMat=linkMat, ementa=ementa, nom_autor=nom_autor, data=data, status=status, casa_legislativa=casa_legislativa)

   mMsg = MIMEText(html, 'html', "utf-8")

   mTo = dic['end_email']

   mSubj = projeto +" - Aviso de tramitação em " + data_registro

   mailhost.send(mMsg, mTo, remetente, subject=mSubj)
