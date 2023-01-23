import os

request=context.REQUEST
response=request.RESPONSE
REQUEST=context.REQUEST

data=DateTime().strftime('%d/%m/%Y')
data_emissao=DateTime().strftime("%d/%m/%Y")

#Abaixo é gerada a string para o rodapé da página
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
 casa[item[0]]=item[1]
nom_casa = casa["nom_casa"].decode('utf-8')

# tenta buscar o logotipo da casa LOGO_CASA
if hasattr(context.sapl_documentos.props_sagl,'logo_casa.gif'):
  imagem = context.sapl_documentos.props_sagl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao.gif"

#Por fim, utiliza o PythonScript para pesquisar os dados da visita

visitas=[]
for visita in context.zsql.visita_obter_zsql(cod_visita=REQUEST['cod_visita']):
        dic={}
        dic['cod_visita'] = visita.cod_visita
        dic['nom_pessoa'] = str(visita.nom_pessoa)
        dic['nom_funcionario'] = str(visita.nom_funcionario)
        visitas.append(dic)

caminho = context.pdf_cracha_visitante_gerar(imagem,nom_casa,data,visitas)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)

