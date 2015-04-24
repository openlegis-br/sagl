##parameters=sessao,imagem,dat_ordem,cod_sessao_plen,lst_splen,lst_pauta,dic_cabecalho,lst_rodape,lst_presidente

"""Ordem do Dia
"""
from trml2pdf import parseString
from cStringIO import StringIO
import time
import os

def cabecalho(dic_cabecalho,dat_ordem,imagem):
    """Gera o codigo rml do cabecalho"""

    tmp=''
    tmp+='\t\t\t\t<image x="6.1cm" y="26.9cm" width="74" height="80" file="' + imagem + '"/>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="11"/>\n'
    tmp+='\t\t\t\t<drawString x="10.5cm" y="27.6cm">Estado de ' + str(dic_cabecalho['nom_estado']) + '</drawString>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="14"/>\n'
    tmp+='\t\t\t\t<drawString x="9cm" y="28.1cm">' + str(dic_cabecalho['nom_casa']) + '</drawString>\n'
    return tmp

def rodape(lst_rodape):
    """ Gera o codigo rml do rodape"""

    tmp=''
    tmp+='\t\t\t\t<lines>4.4cm 2.2cm 20cm 2.2cm</lines>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="8"/>\n'
    tmp+='\t\t\t\t<drawString x="4.4cm" y="2.4cm">' + lst_rodape[2] + '</drawString>\n'
    tmp+='\t\t\t\t<drawString x="18.7cm" y="2.4cm">Página <pageNumber/></drawString>\n'
    tmp+='\t\t\t\t<drawCentredString x="11.5cm" y="1.7cm">' + lst_rodape[0] + '</drawCentredString>\n'
    tmp+='\t\t\t\t<drawCentredString x="11.5cm" y="1.3cm">' + lst_rodape[1] + '</drawCentredString>\n'

    return tmp


def paraStyle():
    """ Gera o codigo rml que define o estilo dos paragrafos"""

    tmp=''
    tmp+='\t<stylesheet>\n'
    tmp+='\t\t<blockTableStyle id="Standard_Outline">\n'
    tmp+='\t\t\t<blockAlignment value="LEFT"/>\n'
    tmp+='\t\t\t<blockValign value="TOP"/>\n'
    tmp+='\t\t</blockTableStyle>\n'
    tmp+='\t\t<initialize>\n'
    tmp+='\t\t\t<paraStyle name="all" alignment="justify"/>\n'
    tmp+='\t\t</initialize>\n'
    tmp+='\t\t<paraStyle name="P0" fontName="Helvetica-Bold" fontSize="10.6" leading="12" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="10.0" leading="11" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="9.0" leading="9" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P3" fontName="Helvetica" fontSize="9.0" leading="11" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P4" fontName="Helvetica" fontSize="10.0" leading="11" alignment="CENTER"/>\n'
    tmp+='\t</stylesheet>\n'
    return tmp

#def splen(lst_splen):
def pauta(lst_splen, lst_pauta):
    """ Funcao que gera o codigo rml da sessao plenaria """

    tmp=''

    #inicio do bloco 
    tmp+='\t<story>\n'

    for dicsp in lst_splen:
        #espaço inicial
        tmp+='\t\t<para style="P1">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
        tmp+='\t\t<para style="P1">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'

   

        #sessao plenaria
        if dicsp['sessao']!=None:
           tmp+='\t\t<para style="P0"><u>' + dicsp['sessao'].replace('&','&amp;') +', EM ' + dicsp['datasessao'].replace('&','&amp;')+ '</u></para>\n'
           tmp+='\t\t<para style="P2">\n'
           tmp+='\t\t\t<font color="white"> </font>\n'
           tmp+='\t\t</para>\n'
           tmp+='\t\t<para style="P1">(Ordem do Dia)</para>\n'
           tmp+='\t\t<para style="P2">\n'
           tmp+='\t\t\t<font color="white"> </font>\n'
           tmp+='\t\t</para>\n'


    #inicio do bloco que contem os flowables
    
    for dic in lst_pauta:
        #espaco inicial
        tmp+='\t\t<para style="P2">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'

        #condicao para a quebra de pagina
        tmp+='\t\t<condPageBreak height="5mm"/>\n'

        #pauta
        if dic['num_ordem']!=None:
            tmp+='\t\t<para style="P4"><font color="#303030">Item nº ' + str(dic['num_ordem']) + '</font></para>\n'
            tmp+='\t\t<para style="P2">\n'
            tmp+='\t\t\t<font color="white"> </font>\n'
            tmp+='\t\t</para>\n'
        if dic['id_materia']!=None:
            tmp+='\t\t<para style="P1"><font color="#303030"><u>' + dic['link_materia']+'</u></font> - '+ dic['nom_autor'] + '</para>\n'
            tmp+='\t\t<para style="P2">\n'
            tmp+='\t\t\t<font color="white"> </font>\n'
            tmp+='\t\t</para>\n'
        if dic['txt_ementa']!=None:
            tmp+='\t\t<para style="P3">' + dic['txt_ementa'].replace('&','&amp;') + '</para>\n'
            tmp+='\t\t<para style="P2">\n'
            tmp+='\t\t\t<font color="white"> </font>\n'
            tmp+='\t\t</para>\n'

    return tmp

def presidente(lst_presidente):
    """ Gera o codigo rml da assinatura"""
    tmp=''
    tmp+='\t\t<para style="P3">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P3">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P3">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P1"><b>' + str(lst_presidente) + '</b></para>\n'
    tmp+='\t\t<para style="P4">Presidente </para>\n'
    tmp+='\t</story>\n'
    return tmp

def principal(sessao,imagem,dat_ordem,lst_splen,lst_pauta,dic_cabecalho,lst_rodape,lst_presidente):
    """Funcao principal que gera a estrutura global do arquivo rml contendo o relatorio de uma ordem do dia.
    ordem_dia_[data da ordem do dia do relatório].pdf
    Retorna:
    Parâmetros:
    dat_ordem       => A data da ordem do dia.
        splen       => Uma lista de dicionários contendo as sessões plenárias do dia.
        pauta       => Uma lista de dicionários contendo a pauta da ordem do dia numa sessão plenária.
        cabecalho   => Um dicionário contendo informações para o Cabeçalho do relatório, incluindo a imagem.
        rodapé      => Uma lista contendo informações para o Rodapé do relatório.
    """

    #arquivoTemporario=str(cod_sessao_plen)+"_pauta_sessao.pdf"
    arquivoPdf=str(cod_sessao_plen)+"_pauta_sessao.pdf"

    tmp=''
    tmp+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp+='<document filename="relatorio.pdf">\n'
    tmp+='\t<template pageSize="(21cm, 29.7cm)" title="Ordem do Dia" author="OpenLegis" allowSplitting="20">\n'
    tmp+='\t\t<pageTemplate id="first">\n'
    tmp+='\t\t\t<pageGraphics>\n'
    tmp+=cabecalho(dic_cabecalho,dat_ordem,imagem)
    tmp+=rodape(lst_rodape)
    tmp+='\t\t\t</pageGraphics>\n'
    tmp+='\t\t\t<frame id="first" x1="4cm" y1="3cm" width="16cm" height="24cm"/>\n'
    tmp+='\t\t</pageTemplate>\n'
    tmp+='\t</template>\n'
    tmp+=paraStyle()
#   tmp+=splen(lst_splen)
    tmp+=pauta(lst_splen, lst_pauta)
    tmp+=presidente(lst_presidente)    
    tmp+='</document>\n'
    tmp_pdf=parseString(tmp)   

    if hasattr(context.sagl_documentos.pauta_sessao,arquivoPdf):
        context.sagl_documentos.pauta_sessao.manage_delObjects(ids=arquivoPdf)
    context.sagl_documentos.pauta_sessao.manage_addFile(arquivoPdf)
    arq=context.sagl_documentos.pauta_sessao[arquivoPdf]
    arq.manage_edit(title='Ordem do Dia',filedata=tmp_pdf,content_type='application/pdf')
   
    return "/sagl/sagl_documentos/pauta_sessao/"+arquivoPdf

return principal(sessao,imagem,dat_ordem,lst_splen,lst_pauta,dic_cabecalho,lst_rodape,lst_presidente)
