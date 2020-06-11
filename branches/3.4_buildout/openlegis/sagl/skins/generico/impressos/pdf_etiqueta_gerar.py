##parameters=sessao,lst_materias

"""relatorio_materia.py
   External method para gerar o arquivo rml do resultado de uma pesquisa de materias
   Autor: Sergio Roberto Damiati
   versao: 1.1
"""

from trml2pdf import parseString
from cStringIO import StringIO
import time

    #Gera o codigo rml que define o estilo dos paragrafos

def paraStyle():
        tmp_data=''
    tmp_data+='<stylesheet>\n'
    tmp_data+='<initialize>\n'
    tmp_data+='<paraStyle name="all" value="Etiquetas por Faixa"/>\n'
    tmp_data+='</initialize>\n'
    tmp_data+='<paraStyle name="etiqueta" fontName="Helvetica" fontSize="10" leftIndent="5" alignment="LEFT"/>\n'
    tmp_data+='</stylesheet>\n'
        return tmp_data


    #Gera o codigo rml do conteudo da pesquisa de materias

def dados(lst_materias):
        tmp_data=''
    
    #inicio do bloco que contem os flowables
    tmp_data+='<story>\n'

    for dic in lst_materias:
        #condicao para a quebra de pagina
        tmp_data+='<condPageBreak height="1cm"/>\n'
        
        #materias   
        if dic['processo']!=None:
            tmp_data+='<para style="etiqueta"><b>PROCESSO: ' + dic['processo'] + '<font color="white">\t </font>\n' + dic['tipo_materia'] + ': ' + '</b>' + dic['materia'] + '<font color="white">\t </font>\n' + '<b>Pref:</b> ' + dic['num_externa'] + '</para>\n'

        if dic['dat_apresentacao']!=None:
                        tmp_data+='<para style="etiqueta"><b>DATA DE ENTRADA:</b> ' + dic['dat_apresentacao'] + '</para>\n'

        if dic['nom_autor']!=None:
                        tmp_data+='<para style="etiqueta"><b>AUTOR:</b> ' + dic['nom_autor'] + '</para>\n'

        if dic['txt_ementa']!=None:
                        txt_ementa = dic['txt_ementa'].replace('&','&amp;')
                        tmp_data+='<para style="etiqueta"><b>EMENTA:</b> ' + dic['txt_ementa'] + '</para>\n'

        tmp_data+='<nextFrame/>\n'


    tmp_data+='</story>\n'
        return tmp_data


    #Funcao pricipal que gera a estrutura global do arquivo rml

def principal(sessao,lst_materias):
    arquivoPdf=str(int(time.time()*100)) + ".pdf"
        tmp_data=''
        tmp_data+='<?xml version="1.0" encoding="iso-8859-1" standalone="no" ?>\n'
    tmp_data+='<!DOCTYPE document SYSTEM "rml.dtd">\n'
    tmp_data+='<document filename="etiquetas.pdf">\n'
    tmp_data+='<template pageSize="(21cm, 29.7cm)" leftMargin="2.5cm" rightMargin="2.5cm" topMargin="0.5cm" bottomMargin="0.5cm" title="Etiqueta" author="Sergio Damiati" showBoundary="0" allowSplitting="20">\n'
        tmp_data+='<pageTemplate id="main">\n'
        tmp_data+='<pageGraphics>\n'
        tmp_data+='</pageGraphics>\n'
        tmp_data+='<frame id="etiqueta" x1="3.5cm" y1="25cm" width="14cm" height="4.5cm"/>\n'
        tmp_data+='<frame id="etiqueta" x1="3.5cm" y1="19.8cm" width="14cm" height="4.5cm"/>\n'
        tmp_data+='<frame id="etiqueta" x1="3.5cm" y1="14.6cm" width="14cm" height="4.5cm"/>\n'
        tmp_data+='<frame id="etiqueta" x1="3.5cm" y1="9.3cm" width="14cm" height="4.5cm"/>\n'
        tmp_data+='<frame id="etiqueta" x1="3.5cm" y1="4.1cm" width="14cm" height="4.5cm"/>\n'
        tmp_data+='<frame id="etiqueta" x1="3.5cm" y1="-1cm" width="14cm" height="4.5cm"/>\n'
        tmp_data+='</pageTemplate>\n'
        tmp_data+='</template>\n'
        tmp_data+=paraStyle()
        tmp_data+=dados(lst_materias)
        tmp_data+='</document>\n'

    try:  
      tmp_pdf=parseString(unicode(tmp_data, 'iso-8859-1'))  
    except:  
      tmp_pdf=parseString(unicode(tmp_data, 'utf-8'))

        if hasattr(context.temp_folder,arquivoPdf):
            context.temp_folder.manage_delObjects(ids=arquivoPdf)
        context.temp_folder.manage_addFile(arquivoPdf)
        arq=context.temp_folder[arquivoPdf]
        arq.manage_edit(title='Arquivo PDF temporario.',filedata=tmp_pdf,content_type='application/pdf')

        return "/temp_folder/"+arquivoPdf

return principal(sessao,lst_materias)
