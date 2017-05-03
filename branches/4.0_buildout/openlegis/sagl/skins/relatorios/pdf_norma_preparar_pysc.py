import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

data=DateTime().strftime('%d/%m/%Y')

#Abaixo é gerada a string para o rodapé da página
casa={}
aux=context.documentos.propriedades.propertyItems()
for item in aux:
 casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
if len(casa["num_cep"])==8:
 cep=casa["num_cep"][:4]+"-"+casa["num_cep"][5:]
else:
 cep=""

linha1=casa["end_casa"]
if cep!="":
  if casa["end_casa"]!="" and casa["end_casa"]!=None:
     linha1 = linha1 + " - "
  linha1 = linha1 + "CEP "+cep
if localidade[0].nom_localidade!="" and localidade[0].nom_localidade!=None:
  linha1 = linha1 + " - "+localidade[0].nom_localidade+" "+localidade[0].sgl_uf
if casa["num_tel"]!="" and casa["num_tel"]!=None:
  linha1 = linha1 + " Tel.: "+ casa["num_tel"]

linha2=casa["end_web_casa"]
if casa["end_email_casa"]!="" and casa["end_email_casa"]!=None:
  if casa["end_web_casa"]!="" and casa["end_web_casa"]!=None:
    linha2 = linha2 + " - "
  linha2 =  linha2 + "E-mail: "+casa["end_email_casa"]

data_emissao=DateTime().strftime("%d/%m/%Y")
rodape=[linha1,linha2,data_emissao]

#Por fim, gera-se as entradas para o cabeçalho
estados=context.zsql.localidade_obter_zsql(tip_localidade="u")
for uf in estados:
 if localidade[0].sgl_uf==uf.sgl_uf:
  nom_estado=uf.nom_localidade
  break
cabecalho={}
cabecalho["nom_casa"]=casa["nom_casa"]
cabecalho["nom_estado"]="Estado de "+nom_estado

# tenta buscar o logotipo da casa LOGO_CASA
if hasattr(context.documentos.propriedades,'logo_casa.gif'):
  imagem = context.documentos.propriedades['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao_transp.gif"

#Por fim, utiliza o PythonScript para pesquisar as normas e gerar os dados

normas=[]
REQUEST=context.REQUEST
if REQUEST[str('tipo_norma')] != 'None':
  tipo_norma= REQUEST[str('tipo_norma')]
else: 
  tipo_norma = '' 
for norma in context.zsql.norma_juridica_obter_zsql(tip_norma=tipo_norma, num_norma=REQUEST['txt_numero'],
                                           ano_norma=REQUEST['txt_ano'], des_assunto=REQUEST['txt_assunto'], 
                                           cod_assunto=REQUEST['lst_assunto_norma'], dat_norma=REQUEST['dt_norma'],
                                           dat_norma2=REQUEST['dt_norma2'], dat_publicacao=REQUEST['dt_public'],
                                           cod_situacao=REQUEST['lst_tip_situacao_norma'],
                                           dat_publicacao2=REQUEST['dt_public2'],rd_ordem=REQUEST['rd_ordenacao']):

        dic={}

        dic['titulo']= norma.des_tipo_norma.upper()+" N° "+str(norma.num_norma)+", DE "+str(norma.dat_norma)
        dic['txt_ementa']=norma.txt_ementa 

        dic['materia_vinculada']=" "
        if norma.cod_materia!=None:
           for materia_vinculada in context.zsql.materia_obter_zsql(cod_materia=str(norma.cod_materia)):
                dic['materia_vinculada']= materia_vinculada.sgl_tipo_materia+" "+str(materia_vinculada.num_ident_basica)+"/"+str(materia_vinculada.ano_ident_basica)

        dic['situacao_norma']=" "
        if norma.cod_situacao!=None:
           for situacao_norma in context.zsql.tipo_situacao_norma_obter_zsql(ind_excluido=0, tip_situacao_norma=norma.cod_situacao):
                dic['situacao_norma']= situacao_norma.des_tipo_situacao

        normas.append(dic)

filtro={} # Dicionário que conterá os dados do filtro

# Atribuições diretas do REQUEST
filtro['numero']=REQUEST.txt_numero
filtro['ano']=REQUEST.txt_ano
filtro['assunto']=REQUEST.txt_assunto

filtro['tipo_norma']=''

filtro['situacao_norma']=''
if REQUEST.lst_tip_situacao_norma!='':
    for situacao in context.zsql.tipo_situacao_norma_obter_zsql(ind_exluido=0,tip_situacao_norma=REQUEST.lst_tip_situacao_norma):
        filtro['situacao_norma']=situacao.des_tipo_situacao

sessao=session.id
caminho = context.pdf_norma_gerar(sessao,imagem,data,normas,cabecalho,rodape,filtro)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)
