##parameters=imagem, dic_rodape,dic_inf_basicas,dic_orig_externa,lst_mat_anexadas,lst_autoria,lst_des_iniciais,lst_tramitacoes,lst_relatorias,lst_numeracoes,lst_leg_citadas,lst_acessorios,sessao=''

"""relatorio_detalhe_materia.py
   External method para gerar o arquivo rml do resultado da pesquisa de uma matéria
   OpenLegis
"""
from trml2pdf import parseString
from cStringIO import StringIO
import time

def cabecalho(dic_inf_basicas,imagem):
    """
    Função que gera o código rml do cabeçalho da página
    """
    tmp=''
    tmp+='\t\t\t\t<image x="4cm" y="26.7cm" width="70" height="70" file="' + imagem + '"/>\n'
    tmp+='\t\t\t\t<lines>3.3cm 26.3cm 19.5cm 26.3cm</lines>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="15"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="28.1cm">' + dic_inf_basicas['nom_camara'] + '</drawString>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="11"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="27.6cm">' + dic_inf_basicas['nom_estado'] + '</drawString>\n'
    if str(dic_inf_basicas['cod_projeto']) != "" and str(dic_inf_basicas['cod_projeto']) != None:
        tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="12"/>\n'
        tmp+='\t\t\t\t<drawCentredString x="11.5cm" y="25.6cm">' + str(dic_inf_basicas['cod_projeto']) + '</drawCentredString>\n'
    return tmp

def rodape(dic_rodape):
    """
    Função que gera o codigo rml do rodape da pagina.
    """

    tmp=''
    linha1 = dic_rodape['end_casa']
    if dic_rodape['end_casa']!="" and dic_rodape['end_casa']!=None:
        linha1 = linha1 + " - "
    if dic_rodape['num_cep']!="" and dic_rodape['num_cep']!=None:
        linha1 = linha1 + "CEP " + dic_rodape['num_cep']
    if dic_rodape['nom_localidade']!="" and dic_rodape['nom_localidade']!=None:
        linha1 = linha1 + " - " + dic_rodape['nom_localidade']
    if dic_rodape['sgl_uf']!="" and dic_rodape['sgl_uf']!=None:
        inha1 = linha1 + " " + dic_rodape['sgl_uf']
    if dic_rodape['num_tel']!="" and dic_rodape['num_tel']!=None:
        linha1 = linha1 + " Tel: "+ dic_rodape['num_tel']
    if dic_rodape['end_web_casa']!="" and dic_rodape['end_web_casa']!=None:
        linha2 = dic_rodape['end_web_casa']
    if dic_rodape['end_email_casa']!="" and dic_rodape['end_email_casa']!=None:
        linha2 = linha2 + " - E-mail: " + dic_rodape['end_email_casa']
    if dic_rodape['data_emissao']!="" and dic_rodape['data_emissao']!=None:
        data_emissao = dic_rodape['data_emissao']

    tmp+='\t\t\t\t<lines>3.3cm 2.2cm 19.5cm 2.2cm</lines>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="8"/>\n'
    tmp+='\t\t\t\t<drawString x="3.3cm" y="2.4cm">' + data_emissao + '</drawString>\n'
    tmp+='\t\t\t\t<drawString x="18.4cm" y="2.4cm">Página <pageNumber/></drawString>\n'
    tmp+='\t\t\t\t<drawCentredString x="11.5cm" y="1.7cm">' + linha1 + '</drawCentredString>\n'
    tmp+='\t\t\t\t<drawCentredString x="11.5cm" y="1.3cm">' + linha2 + '</drawCentredString>\n'

    return tmp

def paraStyle():
    """Função que gera o código rml que define o estilo dos parágrafos"""
    
    tmp=''
    tmp+='\t<stylesheet>\n'
    tmp+='\t\t<blockTableStyle id="Standard_Outline">\n'
    tmp+='\t\t\t<blockAlignment value="LEFT"/>\n'
    tmp+='\t\t\t<blockValign value="TOP"/>\n'
    tmp+='\t\t</blockTableStyle>\n'
    tmp+='\t\t<initialize>\n'
    tmp+='\t\t\t<paraStyle name="all" alignment="justify"/>\n'
    tmp+='\t\t</initialize>\n'
    tmp+='\t\t<paraStyle name="style.Title" fontName="Helvetica" fontSize="11" leading="13" spaceAfter="2" alignment="RIGHT"/>\n'
    tmp+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="12.0" textColor="gray" leading="14" spaceAfter="2" spaceBefore="8" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="10.0" leading="12" spaceAfter="2" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="texto_projeto" fontName="Helvetica" fontSize="11.0" leading="14" spaceAfter="5" alignment="JUSTIFY"/>\n'
    tmp+='\t</stylesheet>\n'

    return tmp

def inf_basicas(dic_inf_basicas):
    """
    Função que gera o código rml das funções básicas do relatório
    """

    tmp=''
    #Texto do projeto
    texto_projeto = str(dic_inf_basicas['texto_projeto'])
    if texto_projeto != "" and texto_projeto != None :
        tmp+='\t\t<para style="texto_projeto">' + texto_projeto.replace('&','&amp;') + '</para>\n'

    #iní­cio das informações básicas
    tmp+='\t\t<para style="P1">Dados Básicos da Matéria</para>\n'
    if str(dic_inf_basicas['apresentada']) != "" and str(dic_inf_basicas['apresentada']) != None:
        tmp+='\t\t<para style="P2"><b>Data de Apresentação: </b> ' + str(dic_inf_basicas['apresentada']) + '</para>\n'

    if str(dic_inf_basicas['formato']) == 'E':
        tmp+='\t\t<para style="P2"><b>Forma de Apresentação: </b> Escrito</para>\n'
    else:
        tmp+='\t\t<para style="P2"><b>Forma de Apresentação: </b> Oral</para>\n'

    if dic_inf_basicas['tramitacao']==0:
        tmp+='\t\t<para style="P2"><b>Tramitando:</b> Não</para>\n'
    else:
        tmp+='\t\t<para style="P2"><b>Tramitando:</b> Sim</para>\n'

    if str(dic_inf_basicas['reg_tramitacao']) != " " and str(dic_inf_basicas['reg_tramitacao']) != None:
        tmp+='\t\t<para style="P2"><b>Regime de tramitação: </b> ' + str(dic_inf_basicas['reg_tramitacao']) + '</para>\n'

    prazo = (dic_inf_basicas['prazo'])
    if prazo != " " and prazo != None:
        tmp+='\t\t<para style="P2"><b>Dias de prazo: </b> ' + str(dic_inf_basicas['prazo']) + '</para>\n'

    fim_prazo = (dic_inf_basicas['fim_prazo'])
    if fim_prazo != "" and fim_prazo != None:
        tmp+='\t\t<para style="P2"><b>Data de fim do prazo: </b> ' + str(dic_inf_basicas['fim_prazo']) + '</para>\n'

    apelido = dic_inf_basicas['apelido']
    if apelido != "" and apelido != None:
        tmp+='\t\t<para style="P2"><b>Apelido: </b> ' + apelido.replace('&','&amp;') + '</para>\n'

    indexacao = dic_inf_basicas['indexacao']
    if indexacao != "" and indexacao != None:
        tmp+='\t\t<para style="P2"><b>Indexação: </b> ' + indexacao.replace('&','&amp;') + '</para>\n'

    observacao = dic_inf_basicas['observacao']
    if observacao != "" and observacao != None:
        tmp+='\t\t<para style="P2"><b>Observações: </b> ' + observacao.replace('&','&amp;') + '</para>\n'

    return tmp

def orig_externa(dic_orig_externa):
    """
    Função que gera o código rml da origem externa
    """

    tmp=''
    tmp+='\t\t<para style="P1">Origem Externa</para>\n'
    try:
        if dic_orig_externa['local'] != "" and dic_orig_externa['local'] != None:
            tmp+='\t\t<para style="P2"><b>Local:</b> ' + dic_orig_externa['local'] + '</para>\n'

        if dic_orig_externa['data'] != "" and dic_orig_externa['data'] != None:
            tmp+='\t\t<para style="P2"><b>Data:</b> ' + dic_orig_externa['data'] + '</para>\n'

        if dic_orig_externa['tipo'] != "" and dic_orig_externa['tipo'] != None:
            tmp+='\t\t<para style="P2"><b>Tipo:</b> ' + dic_orig_externa['tipo'] + '</para>\n'

        if dic_orig_externa['numero_ano'] != "" and dic_orig_externa['numero_ano'] != None:
            tmp+='\t\t<para style="P2"><b>Número/Ano:</b> ' + dic_orig_externa['numero_ano'] + '</para>\n'
    except: pass

    return tmp

def mat_anexadas(lst_mat_anexadas):
    tmp=''
    for dic_mat in  lst_mat_anexadas:
        if dic_mat['nom_mat']!=" " and dic_mat['nom_mat']!= None:
            tmp+='\t\t<para style="P1">Matérias Anexadas</para>\n'
            tmp+='\t\t<para style="P2"><b>Matéria:</b> ' + dic_mat['nom_mat'] + '</para>\n'
            tmp+='\t\t<para style="P2"><b>Anexação:</b> ' + dic_mat['data'] + '</para>\n'
    return tmp

def autoria(lst_autoria):

    tmp=''
    tmp+='\t\t<para style="P1">Autoria</para>\n'
    for dic_autor in lst_autoria:
        if dic_autor['nom_autor'] != " " and dic_autor['nom_autor'] != None:
            tmp+='\t\t<para style="P2">' + dic_autor['nom_autor'] + '</para>\n'

    return tmp

def despachos_iniciais(lst_des_iniciais):
    tmp=''
    tmp+='\t\t<para style="P1">Despacho Inicial</para>\n'
    for dic_dados in lst_des_iniciais:
        if dic_dados['nom_comissao']==None:
            dic_dados['nom_comissao']=" "
        tmp+='\t\t<para style="P2"><b>Comissão:</b> ' + dic_dados['nom_comissao'] + '</para>\n'
    return tmp

def tramitacoes(lst_tramitacoes):
    tmp=''
    tmp+='\t\t<para style="P1">Histórico de Tramitações</para>\n'
    for dic_tramitacoes in lst_tramitacoes:
        tmp+='\t\t<para style="P2"><b>Data da Tramitação:</b> ' + str(dic_tramitacoes['data']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Origem:</b> ' + dic_tramitacoes['unidade'] + '</para>\n'
        data_enc = dic_tramitacoes['data_enc']
        if data_enc != "" and data_enc != None:
            tmp+='\t\t<para style="P2"><b>Encaminhada em:</b> ' + str(dic_tramitacoes['data_enc']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Destino:</b> ' + dic_tramitacoes['destino'] + '</para>\n'
        turno = dic_tramitacoes['turno']
        tmp+='\t\t<para style="P2"><b>Status:</b> ' + dic_tramitacoes['status'] + '</para>\n'
        if dic_tramitacoes['urgente']==0:
            tmp+='\t\t<para style="P2"><b>Urgente:</b> Não</para>\n'
        else: 
            tmp+='\t\t<para style="P2"><b>Urgente:</b> Sim</para>\n'
        data_fim = dic_tramitacoes['data_fim']
        if data_fim != "" and data_fim != None:
            tmp+='\t\t<para style="P2"><b>Fim do prazo:</b> ' + str(dic_tramitacoes['data_fim']) + '</para>\n'
        if dic_tramitacoes['texto_acao'] != "" and dic_tramitacoes['texto_acao'] != None :
            tmp+='\t\t<para style="P2"><b>Texto da Ação:</b> ' + dic_tramitacoes['texto_acao'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2"></para>\n'
        tmp+='\t\t<para style="P2"></para>\n'
    return tmp

def relatorias(lst_relatorias):
    tmp=''
    tmp+='\t\t<para style="P1">Relatoria</para>\n'
    for dic_comissao in lst_relatorias:
        tmp+='\t\t<para style="P2"><b>Comissão:</b> ' + dic_comissao['nom_comissao'] + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Relator:</b> ' + dic_comissao['parlamentar'] + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Data de Designação:</b> ' + str(dic_comissao['data_desig']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Data do Parecer:</b> ' + str(dic_comissao['data_dest']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Resultado na Comissão:</b> ' + dic_comissao['motivo'] + '</para>\n'
        tmp+='\t\t<para style="P2"></para>\n'
        tmp+='\t\t<para style="P2"></para>\n'
    return tmp

def numeracoes(lst_numeracoes):
    tmp=''
    tmp+='\t\t<para style="P1">Outras Numerações</para>\n'
    for dic_dados in lst_numeracoes:
        tmp+='\t\t<para style="P2"><b>Número:</b> ' + dic_dados['nome'] + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Ano:</b> ' + str(dic_dados['ano']) + '</para>\n'
    return tmp

def legislacoes_citadas(lst_leg_citadas):
    tmp=''
    tmp+='\t\t<para style="P1">Legislações Citadas</para>\n'
    for dic_dados in lst_leg_citadas:
        tmp+='\t\t<para style="P2"><b>Tipo Norma:</b> ' + str(dic_dados['nome_lei']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Disposição:</b> ' + str(dic_dados['disposicao']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Parte:</b> ' + str(dic_dados['parte']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Livro:</b> ' + str(dic_dados['livro']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Tí­tulo:</b> ' + str(dic_dados['titulo']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Capí­tulo:</b> ' + str(dic_dados['capitulo']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Seção:</b> ' + str(dic_dados['secao']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Subseção:</b> ' + str(dic_dados['subsecao']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Artigo:</b> ' + str(dic_dados['artigo']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Parágrafo:</b> ' + str(dic_dados['paragrafo']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Inciso:</b> ' + str(dic_dados['inciso']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Alí­nea:</b> ' + str(dic_dados['alinea']) + '</para>\n'
        tmp+='\t\t<para style="P2"><b>Item:</b> ' + str(dic_dados['item']) + '</para>\n'
    return tmp

def documentos_acessorios(lst_acessorios):
    tmp=''
    tmp+='\t\t<para style="P1">Documentos Acessórios</para>\n'
    for dic_dados in lst_acessorios:
        if dic_dados['tipo']!=None:
            tmp+='\t\t<para style="P2"><b>Tipo:</b> ' + dic_dados['tipo'] + '</para>\n'

        if dic_dados['nome']!=None:
            tmp+='\t\t<para style="P2"><b>Nome:</b> ' + dic_dados['nome'] + '</para>\n'

        tmp+='\t\t<para style="P2"><b>Data:</b> ' + dic_dados['data'] + '</para>\n'
        if dic_dados['autor']!=None:
            tmp+='\t\t<para style="P2"><b>Autor:</b> ' + dic_dados['autor'] + '</para>\n'

        if dic_dados['ementa']!=None:
            tmp+='\t\t<para style="P2"><b>Ementa:</b> ' + dic_dados['ementa'].replace('&','&amp;') + '</para>\n'
        if dic_dados['indexacao']!=None:
            tmp+='\t\t<para style="P2"><b>Ementa:</b> ' + dic_dados['indexacao'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2"></para>\n'
        tmp+='\t\t<para style="P2"></para>\n'
    return tmp

def principal(imagem, dic_rodape,dic_inf_basicas,dic_orig_externa,lst_mat_anexadas,lst_autoria,lst_des_iniciais,
              dic_tramitacoes,lst_relatorias,lst_numeracoes,lst_leg_citadas,lst_acessorios,sessao=''):
    """
    Função principal responsável por chamar as funções que irão gerar o código rml apropriado
    """

    arquivoPdf=str(int(time.time()*100))+".pdf"

    tmp=''
    tmp+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp+='<document filename="relatorio.pdf">\n'
    tmp+='\t<template pageSize="(21cm, 29.7cm)" title="Relatorio de Materias" author="OpenLegis" allowSplitting="20">\n'
    tmp+='\t\t<pageTemplate id="first">\n'
    tmp+='\t\t\t<pageGraphics>\n'
    tmp+=cabecalho(dic_inf_basicas,imagem)
    tmp+=rodape(dic_rodape)
    tmp+='\t\t\t</pageGraphics>\n'
    tmp+='\t\t\t<frame id="first" x1="3cm" y1="2.6cm" width="16cm" height="23cm"/>\n'
    tmp+='\t\t</pageTemplate>\n'
    tmp+='\t</template>\n'
    tmp+=paraStyle()
    tmp+='\t<story>\n'
    tmp+=inf_basicas(dic_inf_basicas)
    tmp+=autoria(lst_autoria)
    tmp+=orig_externa(dic_orig_externa)
    tmp+=documentos_acessorios(lst_acessorios)
    tmp+=mat_anexadas(lst_mat_anexadas)
    tmp+=relatorias(lst_relatorias)
    tmp+=tramitacoes(lst_tramitacoes)
    tmp+='\t</story>\n'
    tmp+='</document>\n'
    tmp_pdf=parseString(tmp)

    if hasattr(context.temp_folder,arquivoPdf):
        context.temp_folder.manage_delObjects(ids=arquivoPdf)
    context.temp_folder.manage_addFile(arquivoPdf)
    arq=context.temp_folder[arquivoPdf]
    arq.manage_edit(title='Arquivo PDF temporário.',filedata=tmp_pdf,content_type='application/pdf')

    return "/temp_folder/"+arquivoPdf

return principal(imagem, dic_rodape,dic_inf_basicas,dic_orig_externa,lst_mat_anexadas,lst_autoria,lst_des_iniciais,
                 lst_tramitacoes,lst_relatorias,lst_numeracoes,lst_leg_citadas,lst_acessorios,sessao)
