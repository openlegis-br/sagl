##parameters=sessao,imagem,data,lst_materias,dic_cabecalho,lst_rodape,dic_filtro

"""relatorio_materia.py
   External method para gerar o arquivo rml do resultado de uma pesquisa de matérias
   Autor: Leandro Gasparotto Valladares
   Empresa: Interlegis
   versão: 1.0
"""
from trml2pdf import parseString
from cStringIO import StringIO
import time

def cabecalho(dic_cabecalho,imagem):
    """Gera o codigo rml do cabecalho"""
    tmp_data=''
    tmp_data+='\t\t\t\t<image x="6.1cm" y="26.9cm" width="74" height="80" file="' + imagem + '"/>\n'
    tmp_data+='\t\t\t\t<lines>3.3cm 26.3cm 19.5cm 26.3cm</lines>\n'
    tmp_data+='\t\t\t\t<setFont name="Helvetica-Bold" size="15"/>\n'
    tmp_data+='\t\t\t\t<drawString x="9cm" y="28.1cm">' + dic_cabecalho['nom_casa'] + '</drawString>\n'
    tmp_data+='\t\t\t\t<setFont name="Helvetica" size="11"/>\n'
    tmp_data+='\t\t\t\t<drawString x="10.5cm" y="27.6cm">' + dic_cabecalho['nom_estado'] + '</drawString>\n'
    tmp_data+='\t\t\t\t<setFont name="Helvetica-Bold" size="12"/>\n'
    tmp_data+='\t\t\t\t<drawCentredString x="11.5cm" y="25.2cm">Relatório de Matérias Legislativas</drawCentredString>\n'

    return tmp_data

def rodape(lst_rodape):
    """Gera o codigo rml do rodape"""

    tmp_data=''
    tmp_data+='\t\t\t\t<lines>3.3cm 2.2cm 19.5cm 2.2cm</lines>\n'
    tmp_data+='\t\t\t\t<setFont name="Helvetica" size="8"/>\n'
    tmp_data+='\t\t\t\t<drawString x="3.3cm" y="2.4cm">' + lst_rodape[2] + '</drawString>\n'
    tmp_data+='\t\t\t\t<drawString x="18.4cm" y="2.4cm">Página <pageNumber/></drawString>\n'
    tmp_data+='\t\t\t\t<drawCentredString x="11.5cm" y="1.7cm">' + lst_rodape[0] + '</drawCentredString>\n'
    tmp_data+='\t\t\t\t<drawCentredString x="11.5cm" y="1.3cm">' + lst_rodape[1] + '</drawCentredString>\n'

    return tmp_data

def paraStyle():
    """Gera o codigo rml que define o estilo dos paragrafos"""

    tmp_data=''
    tmp_data+='\t<stylesheet>\n'
    tmp_data+='\t\t<blockTableStyle id="Standard_Outline">\n'
    tmp_data+='\t\t\t<blockAlignment value="LEFT"/>\n'
    tmp_data+='\t\t\t<blockValign value="TOP"/>\n'
    tmp_data+='\t\t</blockTableStyle>\n'
    tmp_data+='\t\t<initialize>\n'
    tmp_data+='\t\t\t<paraStyle name="all" alignment="justify"/>\n'
    tmp_data+='\t\t</initialize>\n'
    tmp_data+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="10.0" leading="12" spaceAfter="2" alignment="left"/>\n'
    tmp_data+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="9.0" leading="12" spaceAfter="2" alignment="justify"/>\n'
    tmp_data+='\t</stylesheet>\n'

    return tmp_data

def materias(lst_materias):
    """Gera o codigo rml do conteudo da pesquisa de materias"""

    tmp_data=''

    #inicio do bloco que contem os flowables
    tmp_data+='\t<story>\n'

    for dic in lst_materias:
        #espaco inicial
        tmp_data+='\t\t<para style="P2">\n'
        tmp_data+='\t\t\t<font color="white"> </font>\n'
        tmp_data+='\t\t</para>\n'

        #condicao para a quebra de pagina
        tmp_data+='\t\t<condPageBreak height="2.5cm"/>\n'

        #materias	
        tmp_data+='\t\t<para style="P1"> <b>'+ dic['titulo'] +'</b> - ' + dic['nom_autor'] + ' </para>\n'
        if dic['txt_ementa']!=None:
            txt_ementa = dic['txt_ementa'].replace('&','&amp;')
            tmp_data+='\t\t<para style="P2"> '+ txt_ementa +' </para>\n'
        if dic['des_situacao'] !=None and dic['des_situacao'] !=" ":
            tmp_data+='\t\t<para style="P2"><b>Situção: </b>' + dic['des_situacao'] + '</para>'
        if dic['norma_vinculada'] != None and dic['norma_vinculada'] != " ":
            tmp_data+='\t\t<para style="P2"><b>Norma derivada: </b>'+ dic['norma_vinculada'] + '</para>\n'

    tmp_data+='\t</story>\n'
    return tmp_data

def principal(sessao,imagem,data,lst_materias,dic_cabecalho,lst_rodape,dic_filtro={}):
    """Funcao pricipal que gera a estrutura global do arquivo rml"""

    arquivoPdf=str(int(time.time()*100))+".pdf"

    tmp_data=''
    tmp_data+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp_data+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp_data+='<document filename="relatorio.pdf">\n'
    tmp_data+='\t<template pageSize="(21cm, 29.7cm)" title="Relatorio de Matérias" author="Interlegis" allowSplitting="20">\n'
    tmp_data+='\t\t<pageTemplate id="first">\n'
    tmp_data+='\t\t\t<pageGraphics>\n'
    tmp_data+=cabecalho(dic_cabecalho,imagem)
    tmp_data+=rodape(lst_rodape)
    tmp_data+='\t\t\t</pageGraphics>\n'
    tmp_data+='\t\t\t<frame id="first" x1="3cm" y1="2cm" width="16cm" height="23cm"/>\n'
    tmp_data+='\t\t</pageTemplate>\n'
    tmp_data+='\t</template>\n'
    tmp_data+=paraStyle()
    tmp_data+=materias(lst_materias)
    tmp_data+='</document>\n'
    tmp_pdf=parseString(tmp_data)

    if hasattr(context.temp_folder,arquivoPdf):
        context.temp_folder.manage_delObjects(ids=arquivoPdf)
    context.temp_folder.manage_addFile(arquivoPdf)
    arq=context.temp_folder[arquivoPdf]
    arq.manage_edit(title='Arquivo PDF temporário.',filedata=tmp_pdf,content_type='application/pdf')

    return "/temp_folder/"+arquivoPdf

return principal(sessao,imagem,data,lst_materias,dic_cabecalho,lst_rodape,dic_filtro)
