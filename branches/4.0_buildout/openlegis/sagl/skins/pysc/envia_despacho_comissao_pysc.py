## Script (Python) "envia_despacho_comissao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia,cod_comissao
##title=
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

remetente = email_casa

cod_materia_base64 = context.pysc.b64encode_pysc(codigo=str(cod_materia))

linkMat = "" + request.SERVER_URL+"/consultas/materia/materia_mostrar_proc?cod_materia=" + cod_materia_base64

for comissao in context.zsql.comissao_obter_zsql(cod_comissao=cod_comissao):
 cod_comissao = comissao.cod_comissao
 nom_comissao = comissao.nom_comissao

for periodo in context.zsql.periodo_comp_comissao_obter_zsql(data = DateTime(),cod_comissao=comissao.cod_comissao):
 cod_periodo = periodo.cod_periodo_comp

destinatarios=[]
for composicao_comissao in context.zsql.composicao_comissao_obter_zsql(cod_comissao=comissao.cod_comissao,cod_periodo_comp=periodo.cod_periodo_comp):
 if composicao_comissao.dat_desligamento == None or composicao_comissao.dat_desligamento >= DateTime():
  for destinatario in context.zsql.autor_obter_zsql(cod_parlamentar=composicao_comissao.cod_parlamentar):
   dic={}
   dic['end_email'] = destinatario.end_email
   if dic['end_email'] != None:
    destinatarios.append(dic)

for dic in destinatarios:
  mMsg = "Senhor(a) Vereador(a),\n\n"
  mMsg = mMsg + "Informamos que a seguinte matéria foi despachada para parecer da " + nom_comissao +  " em " + data_registro + ".\n\n"
  mMsg = mMsg + "" + projeto + "\n"
  mMsg = mMsg + "" + str(ementa) + "\n"
  mMsg = mMsg + "Autoria: " + str(nom_autor) + "\n"
  mMsg = mMsg + "Link: " + linkMat + "\n\n"
  mMsg = mMsg + "Cordialmente,\n\n"
  mMsg = mMsg + "" + str(casa_legislativa) +"\n"
  mMsg = mMsg + "Processo Eletrônico\n"

  mTo = dic['end_email']

  mSubj = projeto +" - Despacho para " + nom_comissao

  mailhost.send(mMsg, mTo, remetente, subject=mSubj, encode='base64')
