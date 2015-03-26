# -*- coding: utf-8 -*-
"""relatorio_ordem.py
   External method para gerar o arquivo rml da ordem do dia
   Autor: Leandro Gasparotto Valladares
   Empresa: Interlegis
   versão: 1.0
"""
import os
import App
from cStringIO import StringIO
import time


def cabecalho(arq,dic_cabecalho,dat_ordem):
	"""Gera o codigo rml do cabecalho"""
	arq.write('\t\t\t\t<image x="2.1cm" y="25.7cm" width="59" height="62" file="' + App.FindHomes.INSTANCE_HOME + '/brasao.gif"/>\n')
	arq.write('\t\t\t\t<lines>2cm 25cm 19cm 25cm</lines>\n')
	arq.write('\t\t\t\t<setFont name="Helvetica" size="16"/>\n')
	arq.write('\t\t\t\t<drawString x="5cm" y="27.2cm">' + dic_cabecalho['nom_casa'] + '</drawString>\n')
	arq.write('\t\t\t\t<setFont name="Helvetica" size="14"/>\n')
	arq.write('\t\t\t\t<drawString x="5cm" y="26.5cm">' + dic_cabecalho['nom_estado'] + '</drawString>\n')
	arq.write('\t\t\t\t<setFont name="Helvetica" size="14"/>\n')
	arq.write('\t\t\t\t<drawCentredString x="10.5cm" y="25.2cm">Relatório da Ordem do Dia ' + dat_ordem + '</drawCentredString>\n')


def rodape(arq,lst_rodape):
	"""Gera o codigo rml do rodape"""
	arq.write('\t\t\t\t<lines>2cm 3.2cm 19cm 3.2cm</lines>\n')
	arq.write('\t\t\t\t<setFont name="Helvetica" size="8"/>\n')
	arq.write('\t\t\t\t<drawString x="2cm" y="3.3cm">' + lst_rodape[2] + '</drawString>\n')
	arq.write('\t\t\t\t<drawString x="17.9cm" y="3.3cm">Página <pageNumber/></drawString>\n')
	arq.write('\t\t\t\t<drawCentredString x="10.5cm" y="2.7cm">' + lst_rodape[0] + '</drawCentredString>\n')
	arq.write('\t\t\t\t<drawCentredString x="10.5cm" y="2.3cm">' + lst_rodape[1] + '</drawCentredString>\n')
	
	
def paraStyle(arq):
	"""Gera o codigo rml que define o estilo dos paragrafos"""
	arq.write('\t<stylesheet>\n')
	arq.write('\t\t<blockTableStyle id="Standard_Outline">\n')
	arq.write('\t\t\t<blockAlignment value="LEFT"/>\n')
	arq.write('\t\t\t<blockValign value="TOP"/>\n')
	arq.write('\t\t</blockTableStyle>\n')
	arq.write('\t\t<initialize>\n')
	arq.write('\t\t\t<paraStyle name="all" alignment="justify"/>\n')
	arq.write('\t\t</initialize>\n')
	arq.write('\t\t<paraStyle name="P1" fontName="Helvetica-Bold" fontSize="10.0" leading="10" alignment="CENTER"/>\n')
	arq.write('\t\t<paraStyle name="P2" fontName="Helvetica" fontSize="10.0" leading="10" alignment="LEFT"/>\n')
	arq.write('\t</stylesheet>\n')


def pauta(arq,lst_pauta):
	"""Funcao que gera o codigo rml da pauta da ordem do dia"""
	contador = 0
	
	#inicio do bloco que contem os flowables
	arq.write('\t<story>\n')
	
	for dic in lst_pauta:
		contador = contador+1
		
		#espaco inicial
		arq.write('\t\t<para style="P2">\n')
		arq.write('\t\t\t<font color="white"> </font>\n')
		arq.write('\t\t</para>\n')
		arq.write('\t\t<para style="P2">\n')
		arq.write('\t\t\t<font color="white"> </font>\n')
		arq.write('\t\t</para>\n')
		
		#condicao para a quebra de pagina
		arq.write('\t\t<condPageBreak height="4cm"/>\n')
		
		#pauta
		if dic['num_ordem']!=None:
			arq.write('\t\t<para style="P1">Item nº ' + str(dic['num_ordem']) + '</para>')		
		if dic['id_materia']!=None:
			arq.write('\t\t<para style="P1">' + dic['id_materia'] + '</para>\n')
			arq.write('\t\t<para style="P1">\n')
			arq.write('\t\t\t<font color="white"> </font>\n')
			arq.write('\t\t</para>\n')						
		if dic['txt_ementa']!=None:
			arq.write('\t\t<para style="P2">' + dic['txt_ementa'].replace('&','&amp;') + '</para>\n')
			arq.write('\t\t<para style="P2">\n')
			arq.write('\t\t\t<font color="white"> </font>\n')
			arq.write('\t\t</para>\n')			
		if dic['des_turno']!=None:
			arq.write('\t\t<para style="P2"><b>Turno:</b> ' + dic['des_turno'] + '</para>\n')
		if dic['nom_autor']!=None:
			arq.write('\t\t<para style="P2"><b>Autor:</b> ' + dic['nom_autor'] + '</para>\n')
		if dic['des_situacao']!=None:
			arq.write('\t\t<para style="P2"><b>Situação:</b> ' + dic['des_situacao'] + '</para>\n')

		indice = 0
		for relator in dic['lst_relator']:
			indice = indice + 1
			if (relator != None):
				if (indice < 2):
					arq.write('\t\t<xpre style="P2"><b>Relator</b>: ' + relator + '</xpre>\n')
				else:
					arq.write('\t\t<pre style="P2">              ' + relator + '</pre>\n')
				
	arq.write('\t</story>\n')	
	return contador


def principal(dir_zope,sessao,imagem,dat_ordem,lst_pauta,dic_cabecalho,lst_rodape):
	"""
	Funcao principal que gera a estrutura global do arquivo rml contendo o relatorio de uma ordem do dia.
		ordem_dia_[data da ordem do dia do relatório].pdf
	Retorna:
	Parâmetros:
		dat_ordem => A data da ordem do dia.
		pauta	=> Uma lista de dicionários contendo a pauta da ordem do dia.
		cabecalho => Um dicionário contendo informações para o Cabeçalho do relatório, incluindo a imagem.
		rodapé	=> Uma lista contendo informações para o Rodapé do relatório.
	"""
	if sessao:
		arquivoPdf=App.FindHomes.CLIENT_HOME+"/tmp/"+sessao+".pdf"
		arquivoRml=App.FindHomes.CLIENT_HOME+"/tmp/"+sessao+".rml"
	else:
		arquivoPdf=App.FindHomes.CLIENT_HOME+"/tmp/"+time.strftime('%Y%m%d%H%M%S')+".pdf"
		arquivoRml=App.FindHomes.CLIENT_HOME+"/tmp/"+time.strftime('%Y%m%d%H%M%S')+".rml"
	
	arq = open(arquivoRml,'w')	
	arq.write('<?xml version="1.0" encoding="iso-8859-1" standalone="no" ?>\n')
	arq.write('<!DOCTYPE document SYSTEM "rml_1_0.dtd">\n')
	arq.write('<document filename="relatorio.pdf">\n')
	arq.write('\t<template pageSize="(21cm, 29.7cm)" title="Relatorio de Materias" author="Interlegis" allowSplitting="20">\n')
	arq.write('\t\t<pageTemplate id="first">\n')
	arq.write('\t\t\t<pageGraphics>\n')
	cabecalho(arq,dic_cabecalho,dat_ordem)
	rodape(arq,lst_rodape)
	arq.write('\t\t\t</pageGraphics>\n')
	arq.write('\t\t\t<frame id="first" x1="2cm" y1="4cm" width="17cm" height="21cm"/>\n')
	arq.write('\t\t</pageTemplate>\n')
	arq.write('\t</template>\n')
	paraStyle(arq)
	numero_de_pautas = pauta(arq,lst_pauta)
	arq.write('</document>\n')
	arq.close()

	os.system(App.FindHomes.INSTANCE_HOME + "/../trml2pdf/trml2pdf.py " + arquivoRml+ " >" + arquivoPdf)
	os.chmod(arquivoPdf,438)

	return arquivoPdf
