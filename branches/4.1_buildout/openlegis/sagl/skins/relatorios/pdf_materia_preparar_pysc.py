import os

request=context.REQUEST
response=request.RESPONSE

data=DateTime().strftime('%d/%m/%Y')

# string para o rodapé da página
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
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

# gera as entradas para o cabeçalho
estados=context.zsql.localidade_obter_zsql(tip_localidade="u")
for uf in estados:
 if localidade[0].sgl_uf==uf.sgl_uf:
  nom_estado=uf.nom_localidade
  break
cabecalho={}
cabecalho["nom_casa"]=casa["nom_casa"]
cabecalho["nom_estado"]="Estado de "+nom_estado

# tenta buscar o logotipo da casa LOGO_CASA
if hasattr(context.sapl_documentos.props_sagl,'logo_casa.gif'):
  imagem = context.sapl_documentos.props_sagl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao.gif"

# PythonScript para pesquisar as matérias e gerar os dados
REQUEST=context.REQUEST
if REQUEST[str('tipo_materia')] != 'None':
   tipo_materia = REQUEST[str('tipo_materia')]
else: 
   tipo_materia = '' 

materias=[]
for materia in context.zsql.materia_pesquisar_zsql(tip_id_basica=tipo_materia,
                                                   num_ident_basica=REQUEST['txt_numero'],
                                                   ano_ident_basica=REQUEST['txt_ano'], 
                                                   ind_tramitacao=REQUEST['rad_tramitando'],
                                                   des_assunto=REQUEST['txt_assunto'], 
                                                   cod_status=REQUEST['lst_status'],
                                                   dat_apresentacao=REQUEST['dt_apres'], 
                                                   dat_apresentacao2=REQUEST['dt_apres2'],
                                                   dat_publicacao=REQUEST['dt_public'], 
                                                   dat_publicacao2=REQUEST['dt_public2'],
                                                   cod_autor=REQUEST['hdn_cod_autor'],
                                                   cod_unid_tramitacao=REQUEST['lst_localizacao'],
                                                   cod_unid_tramitacao2=REQUEST['lst_tramitou'],
                                                   rd_ordem=REQUEST['rd_ordenacao']):
    dic={}
    dic['titulo'] = materia.des_tipo_materia.decode('utf-8').upper()+" N° "+str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica)
    dic['txt_ementa']= materia.txt_ementa
    dic["dat_apresentacao"] = context.pysc.iso_to_port_pysc(materia.dat_apresentacao)
    dic["nom_autor"] = ''
    autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
    fields = autores.data_dictionary().keys()
    lista_autor = []
    for autor in autores:
        for field in fields:
            nome_autor = autor['nom_autor_join']
        lista_autor.append(nome_autor)
    dic["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
    dic['localizacao_atual'] = ''
    for tramitacao in context.zsql.tramitacao_obter_zsql(cod_materia=materia.cod_materia,ind_ult_tramitacao=1):
        if tramitacao.cod_unid_tram_dest:
           cod_unid_tram = tramitacao.cod_unid_tram_dest
        else:
           cod_unid_tram = tramitacao.cod_unid_tram_local
        for unidade_tramitacao in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = cod_unid_tram):
            if unidade_tramitacao.cod_orgao:
               dic['localizacao_atual']=unidade_tramitacao.nom_orgao
            else:
               dic['localizacao_atual']=unidade_tramitacao.nom_comissao
        dic['prazo'] = ''
        if tramitacao.dat_fim_prazo != '':
           dic['prazo'] = 'Prazo: ' + str(tramitacao.dat_fim_prazo)
        dic['des_situacao'] = tramitacao.des_status
        dic['ultima_acao'] = tramitacao.txt_tramitacao
        dic['dat_tramitacao'] = tramitacao.dat_tramitacao

    dic["parecer"] = ''
    lst_qtde_pareceres = []
    lst_pareceres = []
    for relatoria in context.zsql.relatoria_obter_zsql(cod_materia=materia.cod_materia):
        dic_parecer = {}
        comissao = context.zsql.comissao_obter_zsql(cod_comissao=relatoria.cod_comissao)[0]
        relator = context.zsql.parlamentar_obter_zsql(cod_parlamentar=relatoria.cod_parlamentar)[0]
        dic_parecer["link_materia"] = '<link href="' + context.sapl_documentos.absolute_url() + '/parecer_comissao/' + str(relatoria.cod_relatoria) + '_parecer.pdf' + '">' + 'Parecer ' + comissao.sgl_comissao + ' nº ' + str(relatoria.num_parecer) + '/' + str(relatoria.ano_parecer) + '</link>'
        lst_pareceres.append(dic_parecer)
        lst_qtde_pareceres.append(relatoria.cod_relatoria)
    dic["pareceres"] = lst_pareceres
    dic["parecer"] = len(lst_qtde_pareceres)

    dic['norma_vinculada'] = ''
    for norma_vinculada in context.zsql.materia_buscar_norma_juridica_zsql(cod_materia=materia.cod_materia):
        dic['norma_vinculada']= norma_vinculada.sgl_norma+" "+str(norma_vinculada.num_norma)+"/"+str(norma_vinculada.ano_norma)

    materias.append(dic)

filtro={} # Dicionário que conterá os dados do filtro

# Atribuições diretas do REQUEST
filtro['numero']=REQUEST.txt_numero
filtro['ano']=REQUEST.txt_ano
filtro['autor']=REQUEST.hdn_txt_autor
filtro['tipo_autor']=REQUEST.lst_tip_autor
filtro['assunto']=REQUEST.txt_assunto

# Atribuição do restante dos dados que precisam de processamento
if REQUEST.hdn_txt_autor=='  ':
    filtro['autor']=''

filtro['tipo_materia']=''

filtro['tramitando']=''
if REQUEST.rad_tramitando=='1':
    filtro['tramitacao']='Sim'
elif REQUEST['rad_tramitando']=='0':
    filtro['tramitacao']='Não'

filtro['situacao_atual']=''
if REQUEST.lst_status!='':
    for status in context.zsql.status_tramitacao_obter_zsql(ind_excluido=0,cod_status=REQUEST.lst_status):
        filtro['situacao_atual']=status.sgl_status + ' - ' + status.des_status

filtro['localizacao']=''
if REQUEST.lst_localizacao!='':
    for unidade_tramitacao in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao = REQUEST.lst_localizacao):
        if unidade_tramitacao.cod_orgao:
           filtro['localizacao']=unidade_tramitacao.nom_orgao
        else:
           filtro['localizacao']=unidade_tramitacao.nom_comissao

caminho = context.pdf_materia_gerar(imagem,data,materias,cabecalho,rodape,filtro)
if caminho=='aviso':
   return response.redirect('mensagem_emitir_proc')
else:
   response.redirect(caminho)
