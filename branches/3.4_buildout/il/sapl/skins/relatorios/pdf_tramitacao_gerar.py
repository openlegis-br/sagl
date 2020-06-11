##parameters=imagem,dic_rodape,inf_basicas_dic,cod_tramitacao,tramitacao_dic,hdn_url,sessao=''

"""pdf_tramitacao_gerar.py
   Script python para gerar o PDF da tramitação
   OpenLegis
"""
from trml2pdf import parseString
from cStringIO import StringIO
import time

def cabecalho(inf_basicas_dic,imagem):
    """
    Função que gera o código rml do cabeçalho da página
    """
    tmp=''
    tmp+='\t\t\t\t<image x="4.1cm" y="26.9cm" width="74" height="60" file="' + imagem + '"/>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="15"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="28.1cm">' + inf_basicas_dic['nom_camara'] + '</drawString>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="11"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="27.6cm">' + inf_basicas_dic['nom_estado'] + '</drawString>\n'
    if str(tramitacao_dic['id_materia']) != "" and str(tramitacao_dic['id_materia']) != None:
        tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="12"/>\n'
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

#    tmp+='\t\t\t\t<lines>3.3cm 2.2cm 19.5cm 2.2cm</lines>\n'
#    tmp+='\t\t\t\t<setFont name="Helvetica" size="8"/>\n'
#    tmp+='\t\t\t\t<drawString x="3.3cm" y="2.4cm">' + data_emissao + '</drawString>\n'
#    tmp+='\t\t\t\t<drawString x="18.4cm" y="1cm">Página <pageNumber/></drawString>\n'

    return tmp

def paraStyle():
    """Função que gera o código rml que define o estilo dos parágrafos"""
    
    tmp=''
    tmp+='\t<stylesheet>\n'
    tmp+='\t\t<blockTableStyle id="tramitacao" spaceBefore="12">\n'
    tmp+='\t\t\t<lineStyle kind="OUTLINE" colorName="black" thickness="0.2"/>\n'
    tmp+='\t\t\t<lineStyle kind="GRID" colorName="black" thickness="0.2"/>\n'
    tmp+='\t\t\t<blockFont name="Helvetica-Bold" size="10" leading="12" start="0,0" stop="-1,0"/>\n'
    tmp+='\t\t\t<blockTopPadding length="2"/>\n'
    tmp+='\t\t\t<blockBottomPadding length="2"/>\n'
    tmp+='\t\t\t<blockAlignment value="CENTER"/>\n'
    tmp+='\t\t\t<blockBackground colorName="#f6f6f6" start="0,0" stop="-1,0"/>\n'
    tmp+='\t\t\t<!--body section-->\n'
    tmp+='\t\t\t<blockFont name="Helvetica" size="8" leading="9" start="0,1" stop="-1,-1"/>\n'
    tmp+='\t\t\t<blockTopPadding length="1" start="0,1" stop="-1,-1"/>\n'
    tmp+='\t\t\t<blockAlignment value="LEFT" start="1,1" stop="-1,-1"/>\n'
    tmp+='\t\t\t<blockValign value="MIDDLE"/>\n'
    tmp+='\t\t</blockTableStyle>\n'
    tmp+='\t\t<blockTableStyle id="Standard_Outline">\n'
    tmp+='\t\t\t<blockAlignment value="LEFT"/>\n'
    tmp+='\t\t\t<blockValign value="TOP"/>\n'
    tmp+='\t\t\t<blockLeftPadding length="0"/>\n'
    tmp+='\t\t</blockTableStyle>\n'
    tmp+='\t\t<initialize>\n'
    tmp+='\t\t\t<paraStyle name="all" alignment="justify"/>\n'
    tmp+='\t\t</initialize>\n'
    tmp+='\t\t<paraStyle name="style.Title" fontName="Helvetica" fontSize="11" leading="13" spaceAfter="2" alignment="RIGHT"/>\n'
    tmp+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="12.0" textColor="gray" leading="14" spaceAfter="2" spaceBefore="8" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="10.0" leading="12" spaceAfter="2" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P3" fontName="Helvetica" fontSize="10.0" leading="12" spaceAfter="2" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P5" fontName="Helvetica-Bold" fontSize="9" leading="15" spaceAfter="3" alignment="CENTER" valign="middle" white-space="nowrap" />\n'
    tmp+='\t</stylesheet>\n'

    return tmp

def tramitacao(tramitacao_dic):
    """
    Função que gera o código rml das funções básicas do relatório
    """

    tmp=''
    tmp+='\t\t<para style="P1">\n'
    tmp+='\t\t\t<font color="white">-</font>\n'
    tmp+='\t\t</para>\n'
    tmp+='<blockTable style="tramitacao" repeatRows="1" colWidths="460">\n'
    tmp+='<tr><td>PROCESSO LEGISLATIVO</td></tr>\n'
    tmp+='\t\t</blockTable>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white">-</font>\n'
    tmp+='\t\t</para>\n'

    tmp+='\t\t<para style="P2">' + str(tramitacao_dic['id_materia']) + '</para>\n\n'

    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white">-</font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='<blockTable style="tramitacao" repeatRows="1" colWidths="460">\n'
    tmp+='<tr><td>TRAMITAÇÃO</td></tr>\n'
    tmp+='\t\t</blockTable>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white">-</font>\n'
    tmp+='\t\t</para>\n'

    tmp+='<blockTable style="Standard_Outline" repeatRows="1" colWidths="110,350">\n'
    tmp+='<tr><td>Data da Ação</td><td>' +str(tramitacao_dic['dat_tramitacao'])+ '</td></tr>\n'
    tmp+='<tr><td>Unidade de Origem</td><td>' +str(tramitacao_dic['unidade_origem'])+ '</td></tr>\n'
    tmp+='<tr><td>Unidade de Destino</td><td>' +str(tramitacao_dic['unidade_destino'])+ '</td></tr>\n'
    tmp+='<tr><td>Status</td><td>' +str(tramitacao_dic['des_status'])+ '</td></tr>\n'
    dat_fim_prazo = str(tramitacao_dic['dat_fim_prazo'])
    if dat_fim_prazo != None and dat_fim_prazo != "":
      tmp+='<tr><td>Prazo</td><td>' +str(tramitacao_dic['dat_fim_prazo'])+ '</td></tr>\n'
    tmp+='\t\t</blockTable>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white">-</font>\n'
    tmp+='\t\t</para>\n'

    texto_tramitacao = str(tramitacao_dic['txt_tramitacao'])
    if texto_tramitacao != '' and texto_tramitacao != "None":
      tmp+='<blockTable style="tramitacao" repeatRows="1" colWidths="460">\n'
      tmp+='<tr><td>TEXTO DA AÇÃO</td></tr>\n'
      tmp+='\t\t</blockTable>\n'
      tmp+='\t\t<para style="P2">\n'
      tmp+='\t\t\t<font color="white">-</font>\n'
      tmp+='\t\t</para>\n'

      tmp+='\t\t<para style="P2">' + str(tramitacao_dic['txt_tramitacao']) + '</para>\n\n'
      tmp+='\t\t<para style="P2">\n'
      tmp+='\t\t\t<font color="white">-</font>\n'
      tmp+='\t\t</para>\n'

    tmp+='\t\t<para style="P3">' + str(dic_rodape['nom_localidade']) +', '+tramitacao_dic['dat_extenso']+ '.</para>\n\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white">-</font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white">-</font>\n'
    tmp+='\t\t</para>\n'

    tmp+='\t\t<para style="P3"><b>' + str(tramitacao_dic['nom_usuario_origem']) +'</b></para>\n\n'
    tmp+='\t\t<para style="P3">' + str(tramitacao_dic['nom_cargo_usuario_origem']) +'</para>\n\n'

    return tmp

def principal(imagem,dic_rodape,inf_basicas_dic,tramitacao_dic,hdn_url,sessao=''):
    """
    Função principal responsável por chamar as funções que irão gerar o código rml apropriado
    """

    arquivoPdf=str(cod_tramitacao)+"_tram.pdf"
    arquivoAssinado=str(cod_tramitacao)+"_tram_signed.pdf"

    tmp=''
    tmp+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp+='<document filename="tramitacao.pdf">\n'
    tmp+='\t<template pageSize="(21cm, 29.7cm)" title="Despacho em Matéria" author="OpenLegis" allowSplitting="20">\n'
    tmp+='\t\t<pageTemplate id="first">\n'
    tmp+='\t\t\t<pageGraphics>\n'
    tmp+=cabecalho(inf_basicas_dic,imagem)
    tmp+=rodape(dic_rodape)
    tmp+='\t\t\t</pageGraphics>\n'
    tmp+='\t\t\t<frame id="first" x1="3cm" y1="3.5cm" width="16.7cm" height="23cm"/>\n'
    tmp+='\t\t</pageTemplate>\n'
    tmp+='\t</template>\n'
    tmp+=paraStyle()
    tmp+='\t<story>\n'
    tmp+=tramitacao(tramitacao_dic)
    tmp+='\t</story>\n'
    tmp+='</document>\n'
    tmp_pdf=parseString(tmp)

    if hasattr(context.sapl_documentos.materia.tramitacao,arquivoPdf):
        context.sapl_documentos.materia.tramitacao.manage_delObjects(ids=arquivoPdf)
    if hasattr(context.sapl_documentos.materia.tramitacao,arquivoAssinado):
        context.sapl_documentos.materia.tramitacao.manage_delObjects(ids=arquivoAssinado)
    context.sapl_documentos.materia.tramitacao.manage_addFile(arquivoPdf)
    arq=context.sapl_documentos.materia.tramitacao[arquivoPdf]
    arq.manage_edit(title='PDF Tramitação Matéria',filedata=tmp_pdf,content_type='application/pdf')

    return hdn_url
    #return "tramitacao_mostrar_proc?hdn_cod_tramitacao="+str(cod_tramitacao)

return principal(imagem, dic_rodape,inf_basicas_dic,tramitacao_dic,hdn_url,sessao)
