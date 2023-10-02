##parameters=lst_processos

"""etiqueta_processo.py
   External method para gerar o arquivo rml da etiqueta de processo
   Autor: Luciano De Fazio
   Empresa: OpenLegis
   versão: 1.0
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
    tmp_data+='\t\t\t<blockValign value="BOTTOM"/>\n'
    tmp_data+='\t\t</blockTableStyle>\n'
    tmp_data+='\t\t<initialize>\n'
    tmp_data+='\t\t\t<paraStyle name="all" alignment="justify"/>\n'
    tmp_data+='\t\t</initialize>\n'
    tmp_data+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="1" leading="2" alignment="CENTER"/>\n'
    tmp_data+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="24" leading="20" alignment="CENTER"/>\n'
    tmp_data+='\t</stylesheet>\n'

    return tmp_data

def processos(lst_processos):
    """Gera o codigo rml do conteudo da pesquisa de protocolos"""

    tmp_data=''

    #inicio do bloco que contem os flowables
    tmp_data+='\t<story>\n'

    for dic in lst_processos:
        #condicao para a quebra de pagina
        tmp_data+='\t\t<condPageBreak height="8mm"/>\n'

        #processos
        if dic['titulo']!=None:

            tmp_data+='\t\t<para style="P2"><b>'+dic['titulo']+'</b></para>\n'

    tmp_data+='\t</story>\n'
    return tmp_data

def principal(lst_processos):
    """Funcao pricipal que gera a estrutura global do arquivo rml"""

    arquivoPdf=str(int(time.time()*100))+".pdf"

    tmp_data=''
    tmp_data+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp_data+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp_data+='<document filename="etiquetas.pdf">\n'
    tmp_data+='\t<template pageSize="(62mm, 15mm)" title="Etiqueta de Processo" author="OpenLegis" allowSplitting="20">\n'
    tmp_data+='\t\t<pageTemplate id="first">\n'
    tmp_data+='\t\t\t<pageGraphics>\n'
    tmp_data+='\t\t\t<frame id="first" x1="0.02cm" y1="0cm" width="62mm" height="15mm"/>\n'
    tmp_data+='\t\t\t</pageGraphics>\n'
    tmp_data+='\t\t</pageTemplate>\n'
    tmp_data+='\t</template>\n'
    tmp_data+=paraStyle()
    tmp_data+=processos(lst_processos)
    tmp_data+='</document>\n'
    tmp_pdf=parseString(tmp_data)

    if hasattr(context.temp_folder,arquivoPdf):
        context.temp_folder.manage_delObjects(ids=arquivoPdf)
    context.temp_folder.manage_addFile(arquivoPdf)
    arq=context.temp_folder[arquivoPdf]
    arq.manage_edit(title='Arquivo PDF temporario.',filedata=tmp_pdf,content_type='application/pdf')

    return "/temp_folder/"+arquivoPdf

return principal(lst_processos)

