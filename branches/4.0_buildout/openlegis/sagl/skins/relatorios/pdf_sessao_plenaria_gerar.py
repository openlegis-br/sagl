##parameters=rodape_dic, imagem, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_expedientes, lst_expediente_materia, lst_oradores_expediente, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, sessao=''
"""Script para geração do PDF das sessoes plenarias
   Autor: Gustavo Lepri
   Atualizado por Luciano De Fázio - 22/03/2012
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
    tmp+='\t\t\t\t<setFont name="Helvetica" size="11"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="27.6cm">Estado de ' + str(inf_basicas_dic['nom_estado']) + '</drawString>\n'
    tmp+='\t\t\t\t<setFont name="Helvetica-Bold" size="14"/>\n'
    tmp+='\t\t\t\t<drawString x="6.7cm" y="28.1cm">' + str(inf_basicas_dic['nom_camara']) + '</drawString>\n'
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
    tmp+='\t\t<paraStyle name="P0" fontName="Helvetica-Bold" fontSize="12.0" leading="17" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P01" fontName="Helvetica" fontSize="10.0" leading="12" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="11.0" textColor="#333333" leading="14" spaceBefore="12" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P10" fontName="Helvetica-Bold" fontSize="10.0" textColor="#444444" leading="14" spaceBefore="12" alignment="LEFT"/>\n'
    tmp+='\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="10.0" leading="10" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P3" fontName="Helvetica" fontSize="9" leading="12" spaceAfter="7" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P4" fontName="Helvetica" fontSize="8" leading="9" spaceAfter="3" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="P5" fontName="Helvetica" fontSize="10.0" leading="12" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="P6" fontName="Helvetica" fontSize="11.0" leading="12" alignment="CENTER"/>\n'
    tmp+='\t\t<paraStyle name="texto_projeto" fontName="Helvetica" fontSize="12.0" leading="12" spaceAfter="10" alignment="JUSTIFY"/>\n'
    tmp+='\t\t<paraStyle name="numOrdem" alignment="CENTER"/>\n'
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
    tmp+='\t\t<para style="P0">' + str(inf_basicas_dic['num_sessao_plen']) + 'ª SESSÃO ' + str(inf_basicas_dic['nom_sessao']) + ' DA ' + str(inf_basicas_dic['num_legislatura']) + 'ª LEGISLATURA ' + '</para>\n'
    tmp+='\t\t<para style="P01">(Em '+ str(inf_basicas_dic["dia_sessao"])+')</para>\n'
    tmp+='\t\t<condPageBreak height="3cm"/>\n'     
    tmp+='\t\t<para style="P1"><i><u>1) ABERTURA</u></i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5"><b>Início: </b> ' + hr_inicio_sessao + ' horas</para>\n'
 
    return tmp


def mesa(lst_mesa):
    """
    
    """
    tmp=''
    tmp+='\t\t<para style="P10"><i>1.a) Mesa Diretora</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    for mesa in lst_mesa:
        tmp+='\t\t<para style="P2" spaceAfter="5"><b>'+ str(mesa['des_cargo']) +':</b> ' + str(mesa['nom_completo']) + '/' + str(mesa['sgl_partido']) +'</para>\n'
    return tmp

def presenca(lst_presenca_sessao):
    """
    
    """
    tmp = ''
    tmp+='\t\t<para style="P10"><i>1.b) Presença</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5">'+ lst_presenca_sessao +'</para>\n'
    return tmp

def materia_apresentada(lst_materia_apresentada):
    """
    """
    tmp = ''
    tmp+='\t\t<para style="P1"><i><u>2) PEQUENO EXPEDIENTE</u></i></para>\n\n'
    tmp+='\t\t<para style="P10"><i>2.a) Matérias Apresentadas</i></para>\n\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    for materia_apresentada in lst_materia_apresentada:
        tmp+= '<para style="P3"><b>'+ str(materia_apresentada['num_ordem']) + ' - ' + materia_apresentada['id_materia'] + ' - ' + materia_apresentada['nom_autor'] +' </b>- ' +materia_apresentada['txt_ementa'].replace('&','')+'</para>\n'

    return tmp

def expediente_materia(lst_expediente_materia):
    """
    """
    tmp = ''
    tmp+='\t\t<para style="P10"><i>2.b) Matérias Apreciadas</i></para>\n\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    for expediente_materia in lst_expediente_materia:
        tmp+= '<para style="P3"><b>'+ str(expediente_materia['num_ordem']) + ' - ' + expediente_materia['id_materia'] + ' - ' + expediente_materia['nom_autor'] +' </b>- ' +expediente_materia['txt_ementa'].replace('&','')+' ('+ expediente_materia['nom_resultado'] +')</para>\n'

    return tmp

def oradores_expediente(lst_oradores_expediente):
    """
    
    """
    tmp = ''
    tmp+='\t\t<para style="P10"><i>2.c) Oradores</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    for orador_expediente in lst_oradores_expediente:
        tmp+='\t\t<para style="P2" spaceAfter="5"><b>'+ str(orador_expediente['num_ordem']) +'</b> - ' + orador_expediente['nom_completo'] + '/' + str(orador_expediente['sgl_partido']) +'</para>\n'
    return tmp

def expedientes(lst_expedientes):
    """
    
    """
    tmp = ''
    tmp+='\t\t<para style="P10"><i>2.d) Expedientes Diversos</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    for expediente in lst_expedientes:
        tmp+='\t\t<para style="P3"><b>' + expediente['nom_expediente'] +': </b> <br />\n' + str(expediente['txt_expediente']) +'</para>\n'
        tmp+='\t\t<para style="P3">\n'
        tmp+='\t\t\t<font color="white">\n</font>\n'
        tmp+='\t\t</para>\n'
    return tmp

def presenca_ordem_dia(lst_presenca_ordem_dia):
    """
    
    """
    tmp = ''
    tmp+='<para style="P1"><i><u>3. ORDEM DO DIA</u></i></para>\n\n'
    tmp+='\t\t<para style="P10"><i>3.a) Presença</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5">'+ lst_presenca_ordem_dia +'</para>\n'
    return tmp

def votacao(lst_votacao):
    """
    """
    tmp = ''
    tmp+='<para style="P10"><i>3.b) Matérias Apreciadas</i></para>\n\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    for votacao in lst_votacao:
        tmp+= '<para style="P3"><b>'+ str(votacao['num_ordem']) + ' - ' + votacao['id_materia'] + ' - ' + votacao['nom_autor'] +' </b>- ' +votacao['txt_ementa'].replace('&','')+' ('+ votacao['nom_resultado'] +')</para>\n'

    return tmp

def presenca_expediente(lst_presenca_expediente):
    """
    
    """
    tmp = ''
    tmp+='<para style="P1"><i><u>4. GRANDE EXPEDIENTE</u></i></para>\n\n'
    tmp+='\t\t<para style="P10"><i>4.a) Presença</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5">'+ lst_presenca_expediente +'</para>\n'
    return tmp

def oradores(lst_oradores):
    """
    
    """
    tmp = ''
    tmp+='\t\t<para style="P10"><i>4.b) Oradores</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    for orador in lst_oradores:
        tmp+='\t\t<para style="P2" spaceAfter="5"><b>'+ str(orador['num_ordem']) +'</b> - ' + orador['nom_completo'] + '/' + str(orador['sgl_partido']) +'</para>\n'
    return tmp

def presenca_encerramento(lst_presenca_encerramento):
    """
    
    """
    tmp = ''
    tmp+='<para style="P1"><i><u>5. ENCERRAMENTO</u></i></para>\n\n'
    tmp+='\t\t<para style="P10"><i>5.a) Presença</i></para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5">'+ lst_presenca_encerramento +'</para>\n'
    tmp+='\t\t<para style="P2">\n'
    tmp+='\t\t\t<font color="white"> </font>\n'
    tmp+='\t\t</para>\n'
    tmp+='\t\t<para style="P2" spaceAfter="5"><i><b>Horário de encerramento: </b></i> ' + inf_basicas_dic["hr_fim_sessao"] + ' horas</para>\n'
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
    tmp+='\t\t<para style="P6"><b>' + str(lst_presidente) + '</b></para>\n'
    tmp+='\t\t<para style="P5">Presidente </para>\n'
    return tmp

def principal(cabecalho, rodape, sessao, imagem, inf_basicas_dic):
    """
    """

    arquivoPdf=str(int(time.time()*100))+".pdf"

    tmp=''
    tmp+='<?xml version="1.0" encoding="utf-8" standalone="no" ?>\n'
    tmp+='<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n'
    tmp+='<document filename="relatorio.pdf">\n'
    tmp+='\t<template pageSize="(21cm, 29.7cm)" title="Sessao Plenaria" author="Interlegis" allowSplitting="20">\n'
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
    tmp+=mesa(lst_mesa)
    tmp+=presenca(lst_presenca_sessao)
    tmp+=materia_apresentada(lst_materia_apresentada)
    tmp+=expediente_materia(lst_expediente_materia)
    tmp+=oradores_expediente(lst_oradores_expediente)
    tmp+=expedientes(lst_expedientes)
    tmp+=presenca_ordem_dia(lst_presenca_ordem_dia)
    tmp+=votacao(lst_votacao)
    tmp+=presenca_expediente(lst_presenca_expediente)
    tmp+=oradores(lst_oradores)
    tmp+=presenca_encerramento(lst_presenca_encerramento)
    tmp+=presidente(lst_presidente)
    tmp+='\t</story>\n'
    tmp+='</document>\n'
    tmp_pdf=parseString(tmp)

    if hasattr(context.temp_folder,arquivoPdf):
        context.temp_folder.manage_delObjects(ids=arquivoPdf)
    context.temp_folder.manage_addFile(arquivoPdf)
    arq=context.temp_folder[arquivoPdf]
    arq.manage_edit(title='Arquivo PDF temporario.',filedata=tmp_pdf,content_type='application/pdf')

    return "/temp_folder/"+arquivoPdf

return principal(cabecalho, rodape, sessao, imagem, inf_basicas_dic)
