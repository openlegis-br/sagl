## Script (Python) "confirma_acomp_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=end_email, txt_hash, cod_materia
##title=
from email.mime.text import MIMEText
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

mailhost = context.MailHost

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

link = request.SERVER_URL + "/consultas/materia/acompanhamento/acomp_materia_confirmar_proc?txt_hash=" + str(txt_hash)

html = """\
<html>
  <head></head>
  <body>
    <p>
       Para receber em seu e-mail o andamento da matéria identificada como {projeto}, solicitamos que confirme o recebimento de futuras mensagens eletrônicas, <a href="{link}" target="blank">clicando aqui</a>.
    </p>
    <p>
       Caso não tenha solicitado o acompanhamento dessa matéria, favor ignorar a presente mensagem.          
    </p>
    <p>
       <strong>{casa_legislativa}</strong><br>
       Processo Eletrônico
    </p>
  </body>
</html>
""".format(link=link, projeto=projeto, casa_legislativa=casa_legislativa)

mMsg = MIMEText(html, 'html', "utf-8")

mSubj = projeto +" - Acompanhamento por e-mail"

mailhost.send(mMsg, destinatario, remetente, subject=mSubj)
