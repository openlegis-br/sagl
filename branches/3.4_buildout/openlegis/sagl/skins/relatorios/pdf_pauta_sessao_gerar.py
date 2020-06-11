##parameters=rodape_dic, sessao='', imagem, inf_basicas_dic, lst_votacao, lst_expediente_materia
"""Script para geração do PDF das pautas das sessoes plenarias
   Autor Luciano De Fázio - 06/11/2012
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
    tmp+='\t\t\t\t<drawString x="6.7cm" y="28.1cm">' + dic_cabecalho['nom_casa'] + '</drawString>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica" size="11"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="27.6cm">' + 'Estado de ' + dic_cabecalho['nom_estado'] + '</drawString>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="12"/>\n'
    tmp+='\t\t\t\t<drawString x="2.2cm" y="24.6cm">Pauta da ' + str(inf_basicas_dic['num_sessao_plen']) + 'ª Sessão ' + str(inf_basicas_dic['nom_sessao']) + ' da ' + str(inf_basicas_dic['num_sessao_leg']) + 'ª Sessão Legislativa da ' + str(inf_basicas_dic['num_legislatura']) + 'ª Legislatura </drawString>\n'
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
    """
    """
    tmp=''
    tmp+='\t<stylesheet>\n'
    tmp+='\t\t<blockTableStyle id="repeater" spaceBefore="12">\n'
    tmp+='\t\t\t<lineStyle kind="OUTLINE" colorName="black" thickness="0.5"/>\n'
    tmp+='\t\t\t<lineStyle kind="GRID" colorName="gray" thickness="0.25"/>\n'
    tmp+='\t\t\t<blockFont name="Helvetica-Bold" size="8" leading="8" start="0,0" stop="-1,0"/>\n'
    tmp+='\t\t\t<blockBottomPadding length="1"/>\n'
    tmp+='\t\t\t<blockBackground colorName="silver" start="0,0" stop="-1,0"/>\n'
    tmp+='\t\t\t<lineStyle kind="LINEBELOW" colorName="black" start="0,0" stop="-1,0" thickness="0.5"/>\n'
    tmp+='\t\t\t<!--body section-->\n'
    tmp+='\t\t\t<blockFont name="Helvetica" size="8" leading="9" start="0,1" stop="-1,-1"/>\n'
    tmp+='\t\t\t<blockTopPadding length="1" start="0,1" stop="-1,-1"/>\n'
    tmp+='\t\t\t<blockAlignment value="LEFT" start="1,1" stop="-1,-1"/>\n'
    tmp+='\t\t\t<blockValign value="TOP"/>\n'
    tmp+='\t\t</blockTableStyle>\n'

    tmp+='\t\t<blockTableStyle id="votacao">\n'
    tmp+='\t\t\t<blockFont name="Helvetica" size="8" leading="9" start="0,0" stop="-1,0"/>\n'
    tmp+='\t\t\t<blockBackground colorName="silver" start="0,0" stop="3,0" />\n'
    tmp+='\t\t\t<lineStyle kind="GRID" colorName="silver" />\n'
    tmp+='\t\t\t<lineStyle kind="LINEBELOW" colorName="black" start="0,0" stop="-1,0" thickness="0.5"/>\n'
    tmp +='\t\t\t<blockAlignment value="LEFT"/>\n'
    tmp+='\t\t\t<blockValign value="TOP"/>\n'
    tmp+='\t\t</blockTableStyle>\n'
    tmp+='\t\t<initialize>\n'
    tmp+='\t\t\t<paraStyle name="all" alignment="justify"/>\n'
    tmp+='\t\t</initialize>\n'
    tmp+='\t\t<paraStyle name="style.Title" fontName="Helvetica" fontSize="11" leading="13" alignment="RIGHT"/>\n'
    tmp+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="12.0" textColor="silver" leading="14" spaceBefore="12" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="10.0" leading="10" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P3" fontName="Helvetica" fontSize="9" leading="10" spaceAfter="3" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P4" fontName="Helvetica" fontSize="8" leading="9" spaceAfter="3" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="texto_projeto" fontName="Helvetica" fontSize="12.0" leading="12" spaceAfter="10" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="numOrdem" alignment="CENTER"/>\n'
    tmp+='\t</stylesheet>\n'

    return tmp

def inf_basicas(inf_basicas_dic):
    """
    """
    tmp=""
    nom_sessao = inf_basicas_dic['nom_sessao']
    num_sessao_plen = inf_basicas_dic["num_sessao_plen"]
    num_sessao_leg = inf_basicas_dic["num_sessao_leg"]
    num_legislatura = inf_basicas_dic["num_legislatura"]
    dat_inicio_sessao = inf_basicas_dic["dat_inicio_sessao"]
    hr_inicio_sessao =  inf_basicas_dic["hr_inicio_sessao"]
    dat_fim_sessao = inf_basicas_dic["dat_fim_sessao"]
    hr_fim_sessao = inf_basicas_dic["hr_fim_sessao"]

    tmp+='\t\t<para style="P1">Informações Básicas</para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5"><b>Tipo da Sessão: </b> ' + nom_sessao + '</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5"><b>Abertura: </b> ' + dat_inicio_sessao + ' <b>- </b> ' + hr_inicio_sessao + '</para>\n'
 
    return tmp


def expediente_materia(lst_expediente_materia):
    """
    """
    tmp = ''
    tmp+='<para style="P1">Matérias do Expediente</para>\n\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='<blockTable style="repeater" repeatRows="1" colWidths="140, 230, 105">\n'
    tmp+='<tr><td >Matéria</td><td>Ementa</td><td>Situação</td></tr>\n'
    for expediente_materia in lst_expediente_materia:
        tmp+= '<tr><td><para style="P3"><b>' + str(expediente_materia['num_ordem']) + '</b> - ' + expediente_materia['id_materia'] + '</para>\n' + '<para style="P3"><b>Autor: </b>' + expediente_materia['nom_autor'] +'</para></td>\n'
        txt_ementa = expediente_materia['txt_ementa'].replace('&','')
        tmp+='<td><para style="P4">' + txt_ementa + '</para></td>\n'
        tmp+='<td><para style="P3">' + expediente_materia['des_situacao'] + '</para></td></tr>\n'

    tmp+='\t\t</blockTable>\n'
    return tmp

def votacao(lst_votacao):
    """
    """

    tmp = ''
    tmp+='<para style="P1">Ordem do Dia</para>\n\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='<blockTable style="repeater" repeatRows="1" colWidths="140, 230, 105">\n'
    tmp+='<tr><td >Matéria</td><td >Ementa</td><td>Situação</td></tr>\n'
    for votacao in lst_votacao:
        tmp+= '<tr><td><para style="P3"><b>' + str(votacao['num_ordem']) + '</b> - ' + votacao['id_materia'] + '</para>\n' + '<para style="P3"><b>Processo: </b>' + votacao['des_numeracao'] + '</para>\n' + '<para style="P3"><b>Turno: </b>' + votacao['des_turno'] + '</para>\n' + '<para style="P3"><b>Autor: </b>' + votacao['nom_autor'] + '</para></td>\n'
        txt_ementa = votacao['ordem_observacao'].replace('&','')
        tmp+='<td><para style="P4">' + votacao['ordem_observacao'] + '</para></td>\n'
        tmp+='<td><para style="P3">' + votacao['des_situacao'] + '</para></td></tr>\n'

    tmp+='\t\t</blockTable>\n'
    return tmp

def principal(cabecalho, rodape, sessao, imagem, inf_basicas_dic):
    """
    """

    arquivoPdf=str(int(time.time()*100))+".pdf"

    tmp=''
    tmp+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp+='<document filename="relatorio.pdf">\n'
    tmp+='\t<template pageSize="(21cm, 29.7cm)" title="Pauta da Sessao" author="OpenLegis" allowSplitting="20">\n'
    tmp+='\t\t<pageTemplate id="first">\n'
    tmp+='\t\t\t<pageGraphics>\n'
    tmp+=cabecalho(inf_basicas_dic,imagem)
    tmp+=rodape(rodape_dic)
    tmp+='\t\t\t</pageGraphics>\n'
    tmp+='\t\t\t<frame id="first" x1="3cm" y1="2cm" width="16cm" height="23cm"/>\n'
    tmp+='\t\t</pageTemplate>\n'
    tmp+='\t</template>\n'
    tmp+=paraStyle()
    tmp+='\t<story>\n'
    tmp+=inf_basicas(inf_basicas_dic)
    tmp+=expediente_materia(lst_expediente_materia)
    tmp+=votacao(lst_votacao)
    tmp+='\t</story>\n'
    tmp+='</document>\n'
    tmp_pdf=parseString(tmp)

    if hasattr(context.temp_folder,arquivoPdf):
        context.temp_folder.manage_delObjects(ids=arquivoPdf)
    context.temp_folder.manage_addFile(arquivoPdf)
    arq=context.temp_folder[arquivoPdf]
    arq.manage_edit(title='Arquivo PDF temporário.',filedata=tmp_pdf,content_type='application/pdf')

    return "/temp_folder/"+arquivoPdf

return principal(cabecalho, rodape, sessao, imagem, inf_basicas_dic)
