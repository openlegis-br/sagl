##parameters=sessao,linha1,linha2,lst_destinatarios

"""pdf_envelope_impresso_gerar.py
   Autor: Luciano De Fazio
   Empresa: OpenLegis
   versão: 1.1
"""
from trml2pdf import parseString
from cStringIO import StringIO
import time

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
    tmp_data+='\t\t<paraStyle name="P1" fontName="Helvetica" fontSize="10" leading="12" alignment="left"/>\n'
    tmp_data+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="9" leading="32" alignment="center"/>\n'
    tmp_data+='\t\t<paraStyle name="P3" fontName="Helvetica" fontSize="20" leading="24" alignment="center"/>\n'
    tmp_data+='\t\t<paraStyle name="P4" fontName="Helvetica" fontSize="14" leading="15" alignment="right"/>\n'
    tmp_data+='\t\t<paraStyle name="P5" fontName="Helvetica" fontSize="9" leading="11" alignment="left"/>\n'
    tmp_data+='\t</stylesheet>\n'

    return tmp_data

def destinatarios(lst_destinatarios):
    """Gera o codigo rml do conteudo da pesquisa de destinatarios"""

    tmp_data=''

    #inicio do bloco que contem os flowables
    tmp_data+='\t<story>\n'

    for dic in lst_destinatarios:
        #condicao para a quebra de pagina
        tmp_data+='\t\t<condPageBreak height="10cm"/>\n'

        #destinatarios
        tmp_data+='\t\t<para style="P3"><b><i>'+linha1+'</i></b></para>\n'
        tmp_data+='\t\t<para style="P2"><i>'+linha2+'</i></para>\n'
        tmp_data+='\t\t<para style="P3">\n'
        tmp_data+='\t\t\t<font color="white"> </font>\n'
        tmp_data+='\t\t</para>\n'
        tmp_data+='\t\t<para style="P3">\n'
        tmp_data+='\t\t\t<font color="white"> </font>\n'
        tmp_data+='\t\t</para>\n'
        if dic['forma_tratamento']!="" and dic['forma_tratamento']!=None:
            tmp_data+='\t\t<para style="P1">'+ dic['forma_tratamento']+ '</para>\n'  
        if dic['nome_responsavel']!="" and dic['nome_responsavel']!=None:
            tmp_data+='\t\t<para style="P1">'+ dic['nome_responsavel']+ '</para>\n'
        if dic['nome_instituicao']!="" and dic['nome_instituicao']!=None:
            tmp_data+='\t\t<para style="P1">'+ dic['nome_instituicao']+ '</para>\n'
        if dic['cargo']!="" and dic['cargo']!=None:
            tmp_data+='\t\t<para style="P1">'+ dic['cargo']+ '</para>\n'
        if dic['endereco']!="" and dic['endereco']!=None and dic['bairro']!='' and dic['bairro']!=None:
            tmp_data+='\t\t<para style="P1">'+ dic['endereco']+' '+dic['bairro']+ '</para>\n'
        else:
            tmp_data+='\t\t<para style="P1">'+ dic['endereco']+ '</para>\n'
        if dic['localidade']!="" and dic['localidade']!=None and dic['cep']!='' and dic['cep']!=None:
            tmp_data+='\t\t<para style="P1">CEP '+ dic['cep']+' - '+dic['localidade']+ '</para>\n'
        else:
            tmp_data+='\t\t<para style="P1">'+ dic['localidade']+ '</para>\n'
        tmp_data+='\t\t<para style="P3">\n'
        tmp_data+='\t\t\t<font color="white"> </font>\n'
        tmp_data+='\t\t</para>\n'
        tmp_data+='\t\t<para style="P3">\n'
        tmp_data+='\t\t\t<font color="white"> </font>\n'
        tmp_data+='\t\t</para>\n'
        tmp_data+='\t\t<para style="P4">\n'
        #tmp_data+='\t\t\t<font color="black"><b>IMPRESSO</b></font>\n'
        tmp_data+='\t\t</para>\n'

    tmp_data+='\t</story>\n'
    return tmp_data

def principal(sessao,linha1,linha2,lst_destinatarios):
    """Funcao pricipal que gera a estrutura global do arquivo rml"""

    arquivoPdf=str(int(time.time()*100))+".pdf"

    tmp_data=''
    tmp_data+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp_data+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp_data+='<document filename="envelopes.pdf">\n'
    tmp_data+='\t<template pageSize="(21cm, 29.7cm)" title="Envelopes" author="OpenLegis" allowSplitting="20" rightMargin="3mm" showBoundary="0">\n'
    tmp_data+='\t\t<pageTemplate id="main">\n'
    tmp_data+='\t\t<pageGraphics>\n'
    imagem=context.sapl_documentos.props_sagl.absolute_url()+"/chancela_correios.png"
    tmp_data+='<image file="'+imagem+'" x="16.2cm" y="16.2cm" width="108.66" height="74.22"/>'
    tmp_data+='\t\t</pageGraphics>\n'
    tmp_data+='\t\t\t<frame id="main" x1="3cm" y1="5cm" width="15cm" height="13cm"/>\n'
    tmp_data+='\t\t</pageTemplate>\n'
    tmp_data+='\t</template>\n'
    tmp_data+=paraStyle()
    tmp_data+=destinatarios(lst_destinatarios)
    tmp_data+='</document>\n'
    tmp_pdf=parseString(tmp_data)

    if hasattr(context.temp_folder,arquivoPdf):
        context.temp_folder.manage_delObjects(ids=arquivoPdf)
    context.temp_folder.manage_addFile(arquivoPdf)
    arq=context.temp_folder[arquivoPdf]
    arq.manage_edit(title='Arquivo PDF temporário.',filedata=tmp_pdf,content_type='application/pdf')

    return "/temp_folder/"+arquivoPdf

return principal(sessao,linha1,linha2,lst_destinatarios)

