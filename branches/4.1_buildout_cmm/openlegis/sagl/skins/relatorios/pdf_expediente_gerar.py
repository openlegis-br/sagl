##parameters=rodape_dic, imagem, inf_basicas_dic, lst_materia_apresentada, lst_indicacoes, lst_requerimentos, lst_mocoes, lst_pareceres, lst_outros, lst_presidente, sessao=''
"""Script para geração da pauta das matérias do expediente em PDF
   Autor: Luciano De Fázio - OpenLegis
   versão: 1.0
"""
from trml2pdf import parseString
from cStringIO import StringIO
import time

def cabecalho(inf_basicas_dic,imagem):
    """
    """
    tmp=''
    tmp+='\t\t\t\t<image x="4.1cm" y="26.9cm" width="74" height="60" file="' + imagem + '"/>\n'
    tmp+='\t\t\t\t<lines>3.3cm 26.3cm 19.5cm 26.3cm</lines>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="15"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="28.1cm">' + str(inf_basicas_dic['nom_camara']) + '</drawString>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="11"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="27.6cm">' + 'Estado de ' + str(inf_basicas_dic['nom_estado']) + '</drawString>\n'

    return tmp

def rodape(rodape_dic):
    """
    """
    tmp=''
    linha1 = rodape_dic['end_casa']
    if rodape_dic['end_casa']!="" and rodape_dic['end_casa']!=None:
        linha1 = linha1 + " - "
    if rodape_dic['num_cep']!="" and rodape_dic['num_cep']!=None:
        linha1 = linha1 + "CEP " + rodape_dic['num_cep']
    if rodape_dic['nom_localidade']!="" and rodape_dic['nom_localidade']!=None:
        linha1 = linha1 + " - " + rodape_dic['nom_localidade']
    if rodape_dic['sgl_uf']!="" and rodape_dic['sgl_uf']!=None:
        linha1 = linha1 + " " + rodape_dic['sgl_uf']
    if rodape_dic['num_tel']!="" and rodape_dic['num_tel']!=None:
        linha1 = linha1 + " Tel: "+ rodape_dic['num_tel']
    if rodape_dic['end_web_casa']!="" and rodape_dic['end_web_casa']!=None:
        linha2 = rodape_dic['end_web_casa']
    if rodape_dic['end_email_casa']!="" and rodape_dic['end_email_casa']!=None:
        linha2 = linha2 + " - E-mail: " + rodape_dic['end_email_casa']
    if rodape_dic['data_emissao']!="" and rodape_dic['data_emissao']!=None:
        data_emissao = rodape_dic['data_emissao']

    tmp+='\t\t\t\t<lines>3.3cm 2.2cm 19.5cm 2.2cm</lines>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="8"/>\n'
    tmp+='\t\t\t\t<drawString x="3.3cm" y="2.4cm">' + data_emissao + '</drawString>\n'
    tmp+='\t\t\t\t<drawString x="18.4cm" y="2.4cm">Página <pageNumber/></drawString>\n'
    tmp+='\t\t\t\t<drawCentredString x="11.5cm" y="1.7cm">' + linha1 + '</drawCentredString>\n'
    tmp+='\t\t\t\t<drawCentredString x="11.5cm" y="1.3cm">' + linha2 + '</drawCentredString>\n'

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
    tmp+='\t\t<paraStyle name="P0" fontName="Helvetica-Bold" fontSize="11" leading="12" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="10.0" leading="12" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="9.0" leading="9" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P3" fontName="Helvetica" fontSize="10.0" leading="12" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P4" fontName="Helvetica" fontSize="10.0" leading="11" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P5" fontName="Helvetica" fontSize="11.0" leading="12" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P6" fontName="Helvetica" fontSize="11.0" leading="12" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P7" fontName="Helvetica-Bold" fontSize="12.0" textColor="#333333" leading="16" spaceAfter="2" spaceBefore="8" alignment="LEFT"/>\n'
    tmp+='\t</stylesheet>\n'
    return tmp


def inf_basicas(inf_basicas_dic):
    """
    """
    nom_sessao = inf_basicas_dic['nom_sessao']
    num_sessao_plen = inf_basicas_dic["num_sessao_plen"]
    num_sessao_leg = inf_basicas_dic["num_sessao_leg"]
    num_legislatura = inf_basicas_dic["num_legislatura"]
    dat_inicio_sessao = inf_basicas_dic["dat_inicio_sessao"]
    dia_sessao = inf_basicas_dic["dia_sessao"]
    hr_inicio_sessao =  inf_basicas_dic["hr_inicio_sessao"]
    dat_fim_sessao = inf_basicas_dic["dat_fim_sessao"]
    hr_fim_sessao = inf_basicas_dic["hr_fim_sessao"]

    tmp=""
    tmp+='\t\t<para style="P0">' + str(inf_basicas_dic['num_sessao_plen']) + 'ª SESSÃO ' + str(inf_basicas_dic['nom_sessao']) + ' DA ' + str(inf_basicas_dic['num_legislatura']) + 'ª LEGISLATURA' + ', EM '+ str(inf_basicas_dic["dia_sessao"])+'</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="4">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P4">(Pauta das Matérias do Expediente)</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="12">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<condPageBreak height="3cm"/>\n'
 
    return tmp

lst_materia_apresentada = [(i + 1, j) for i, j in enumerate(lst_materia_apresentada)]
def materia_apresentada(lst_materia_apresentada):
    """
    """
    tmp = ''
    if lst_materia_apresentada != []:
       tmp+='\t\t<para style="P7" spaceBefore="8"><b><u>LEITURA DE MATÉRIAS E DOCUMENTOS</u></b></para>\n\n'
       tmp+='\t\t<para style="P2" spaceAfter="6">\n'
       tmp+='\t\t\t<font color="white"> </font>\n'
       tmp+='\t\t</para>\n'
    for i, materia_apresentada in lst_materia_apresentada:
     if materia_apresentada != []:
        tmp+='\t\t<para style="P1">' + str(i) +') <font color="#126e90">' + materia_apresentada['link_materia']+'</font> - '+ materia_apresentada['nom_autor'] + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="2">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
        tmp+='\t\t<para style="P3">' + materia_apresentada['txt_ementa'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="8">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
     else:
        tmp+='\t\t<para style="P3">Não há itens para leitura nesta Sessão.</para>\n'

    return tmp

lst_indicacoes = [(i + 1, j) for i, j in enumerate(lst_indicacoes)]
def indicacoes(lst_indicacoes):
    """
    """
    tmp = ''
    if lst_indicacoes != []:
       tmp+='\t\t<para style="P7" spaceBefore="15"><b><u>LEITURA DE INDICAÇÕES</u></b></para>\n\n'
       tmp+='\t\t<para style="P2" spaceAfter="6">\n'
       tmp+='\t\t\t<font color="white"> </font>\n'
       tmp+='\t\t</para>\n'
    for i, indicacao in lst_indicacoes:
     if len(indicacao) > 0:
        tmp+='\t\t<para style="P1">' + str(i) +') <font color="#126e90">' + str(indicacao['link_materia'])+'</font> - '+ indicacao['nom_autor'] + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="2">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
        tmp+='\t\t<para style="P3">' + indicacao['txt_ementa'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="8">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
     else:
        tmp+='\t\t<para style="P3">Não há nenhuma Indicação</para>\n'

    return tmp

lst_pareceres = [(i + 1, j) for i, j in enumerate(lst_pareceres)]
def pareceres(lst_pareceres):
    """
    """
    tmp = ''
    if lst_pareceres != []:
       tmp+='\t\t<para style="P7" spaceBefore="15"><b><u>VOTAÇÃO DE PARECERES</u></b></para>\n\n'
       tmp+='\t\t<para style="P2" spaceAfter="6">\n'
       tmp+='\t\t\t<font color="white"> </font>\n'
       tmp+='\t\t</para>\n'
    for i, parecer in lst_pareceres:
     if len(parecer) > 0:
        tmp+='\t\t<para style="P1">'+ str(i) +') <font color="#126e90">' + parecer['link_materia']+'</font> - '+ parecer['nom_autor'] + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="2">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
        tmp+='\t\t<para style="P3">' + parecer['txt_ementa'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="8">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
     else:
        tmp+='\t\t<para style="P3">Não há nenhum Requerimento</para>\n'

    return tmp

lst_requerimentos = [(i + 1, j) for i, j in enumerate(lst_requerimentos)]
def requerimentos(lst_requerimentos):
    """
    """
    tmp = ''
    if lst_requerimentos != []:
       tmp+='\t\t<para style="P7" spaceBefore="15"><b><u>VOTAÇÃO DE REQUERIMENTOS</u></b></para>\n\n'
       tmp+='\t\t<para style="P2" spaceAfter="6">\n'
       tmp+='\t\t\t<font color="white"> </font>\n'
       tmp+='\t\t</para>\n'
    for i, requerimento in lst_requerimentos:
     if len(requerimento) > 0:
        tmp+='\t\t<para style="P1">'+ str(i) +') <font color="#126e90">' + requerimento['link_materia']+'</font> - '+ requerimento['nom_autor'] + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="2">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
        tmp+='\t\t<para style="P3">' + requerimento['txt_ementa'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="8">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
     else:
        tmp+='\t\t<para style="P3">Não há nenhum Requerimento</para>\n'

    return tmp

lst_mocoes = [(i + 1, j) for i, j in enumerate(lst_mocoes)]
def mocoes(lst_mocoes):
    """
    """
    tmp = ''
    if lst_mocoes != []:
       tmp+='\t\t<para style="P7" spaceBefore="15"><b><u>VOTAÇÃO DE MOÇÕES</u></b></para>\n\n'
       tmp+='\t\t<para style="P2" spaceAfter="6">\n'
       tmp+='\t\t\t<font color="white"> </font>\n'
       tmp+='\t\t</para>\n'
    for i, mocao in lst_mocoes:
     if lst_mocoes != []:
        tmp+='\t\t<para style="P1">'+ str(i) +') <font color="#126e90">' + mocao['link_materia']+'</font> - '+ mocao['nom_autor'] + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="2">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
        tmp+='\t\t<para style="P3">' + mocao['txt_ementa'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="8">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
     else:
        tmp+='\t\t<para style="P3">Não há nenhuma Moção</para>\n'

    return tmp

lst_outros = [(i + 1, j) for i, j in enumerate(lst_outros)]
def outros(lst_outros):
    """
    """
    tmp = ''
    if lst_outros != []:
       tmp+='\t\t<para style="P7" spaceBefore="15"><b><u>VOTAÇÕES DIVERSAS</u></b></para>\n\n'
       tmp+='\t\t<para style="P2" spaceAfter="6">\n'
       tmp+='\t\t\t<font color="white"> </font>\n'
       tmp+='\t\t</para>\n'
    for i, outro in lst_outros:
     if len(outro) > 0:
        tmp+='\t\t<para style="P1">'+ str(i) +') <font color="#126e90">' + outro['link_materia']+'</font> - '+ outro['nom_autor'] + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="2">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
        tmp+='\t\t<para style="P3">' + outro['txt_ementa'].replace('&','&amp;') + '</para>\n'
        tmp+='\t\t<para style="P2" spaceAfter="8">\n'
        tmp+='\t\t\t<font color="white"> </font>\n'
        tmp+='\t\t</para>\n'
     else:
        tmp+='\t\t<para style="P3">Não há nenhum item</para>\n'

    return tmp


def presidente(lst_presidente):
    """ Gera o codigo rml da assinatura"""
    tmp=''
    tmp+='\t\t<para style="P3" spaceAfter="35">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P4"><b>' + str(lst_presidente) + '</b></para>\n'
    tmp+='\t\t<para style="P4">Presidente </para>\n'
    return tmp

def principal(cabecalho, rodape, sessao, imagem, inf_basicas_dic):
    """
    """

    #arquivoPdf=str(int(time.time()*100))+".pdf"
    arquivoPdf=str(inf_basicas_dic["cod_sessao_plen"])+"_pauta_expediente.pdf"

    tmp=''
    tmp+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp+='<document filename="relatorio.pdf">\n'
    tmp+='\t<template pageSize="(21cm, 29.7cm)" title="Pauta das Matérias do Expediente" author="OpenLegis" allowSplitting="20">\n'
    tmp+='\t\t<pageTemplate id="first">\n'
    tmp+='\t\t\t<pageGraphics>\n'
    tmp+=cabecalho(inf_basicas_dic,imagem)
    tmp+=rodape(rodape_dic)
    tmp+='\t\t\t</pageGraphics>\n'
    tmp+='\t\t\t<frame id="first" x1="3cm" y1="3cm" width="16cm" height="23cm"/>\n'
    tmp+='\t\t</pageTemplate>\n'
    tmp+='\t</template>\n'
    tmp+=paraStyle()
    tmp+='\t<story>\n'
    tmp+=inf_basicas(inf_basicas_dic)
    tmp+=materia_apresentada(lst_materia_apresentada)
    tmp+=pareceres(lst_pareceres)
    tmp+=indicacoes(lst_indicacoes)
    tmp+=requerimentos(lst_requerimentos)
    tmp+=mocoes(lst_mocoes)
    tmp+=outros(lst_outros)
    tmp+=presidente(lst_presidente)
    tmp+='\t</story>\n'
    tmp+='</document>\n'
    tmp_pdf=parseString(tmp)

#    if hasattr(context.temp_folder,arquivoPdf):
#        context.temp_folder.manage_delObjects(ids=arquivoPdf)
#    context.temp_folder.manage_addFile(arquivoPdf)
#    arq=context.temp_folder[arquivoPdf]
#    arq.manage_edit(title='Arquivo PDF temporario.',filedata=tmp_pdf,content_type='application/pdf')

#    return "/temp_folder/"+arquivoPdf


    if hasattr(context.sapl_documentos.pauta_sessao,arquivoPdf):
        context.sapl_documentos.pauta_sessao.manage_delObjects(ids=arquivoPdf)
    context.sapl_documentos.pauta_sessao.manage_addFile(arquivoPdf)
    arq=context.sapl_documentos.pauta_sessao[arquivoPdf]
    arq.manage_edit(title='Expediente',filedata=tmp_pdf,content_type='application/pdf')
   
    return "sapl_documentos/pauta_sessao/"+arquivoPdf

return principal(cabecalho, rodape, sessao, imagem, inf_basicas_dic)
