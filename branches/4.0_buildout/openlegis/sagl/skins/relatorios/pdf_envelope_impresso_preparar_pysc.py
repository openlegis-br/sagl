import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

data=DateTime().strftime('%d/%m/%Y')

#Abaixo é gerada a string para o remetente
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
 casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
if len(casa["num_cep"])==9:
 cep=casa["num_cep"][:5]+"-"+casa["num_cep"][6:]
else:
 cep=""

linha1=casa["nom_casa"]

linha2=casa["end_casa"]
if cep!="":
  if casa["end_casa"]!="" and casa["end_casa"]!=None:
     linha2 = linha2 + " - "
  linha2 = linha2 + "CEP "+cep
if localidade[0].nom_localidade!="" and localidade[0].nom_localidade!=None:
  linha2 = linha2 + " - "+localidade[0].nom_localidade+" "+localidade[0].sgl_uf

remetente=[linha1,linha2]

#Por fim, utiliza o PythonScript para pesquisar os destinatarios e gerar os dados

destinatarios=[]
REQUEST=context.REQUEST
for destinatario in context.zsql.destinatario_oficio_obter_zsql(cod_documento=REQUEST['cod_documento']):
        dic={}
        dic['codigo']=str(destinatario.cod_documento)
        dic['forma_tratamento']=str(destinatario.txt_forma_tratamento)
        dic['nome_responsavel']=destinatario.nom_responsavel
        dic['cargo']=destinatario.des_cargo
        dic['nome_instituicao']=destinatario.nom_instituicao
        dic['endereco']=destinatario.end_instituicao
        dic['bairro']=destinatario.nom_bairro
        dic['cep']=destinatario.num_cep
        dic['localidade']=''
        for localidade in context.zsql.localidade_obter_zsql(cod_localidade=destinatario.cod_localidade):
               dic['localidade']=localidade.nom_localidade_pesq+' '+localidade.sgl_uf
        destinatarios.append(dic)

sessao=session.id
caminho = context.pdf_envelope_impresso_gerar(sessao,linha1,linha2,destinatarios)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)

