# -*- coding: utf-8 -*-

import re
import os

import time

import sha
import pickle
from binascii import b2a_base64
from random import randrange

from lxml.builder import ElementMaker
from lxml import etree

from datetime import datetime

from Globals import DTMLFile
from Globals import InitializeClass
from OFS.SimpleItem import SimpleItem

from Products.CMFCore.ActionProviderBase import ActionProviderBase
from Products.CMFCore.utils import UniqueObject

from zope.interface import Interface

from Products.CMFCore.utils import getToolByName

#imports para a geracao dos documentos
import urllib
import urllib2
import cStringIO
from appy.pod.renderer import Renderer
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from StringIO import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128, qr
from reportlab.graphics.shapes import Drawing 
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics import renderPDF

#imports para assinatura digital
import sys
import six
import base64
from base64 import b64encode
import simplejson as json

from lacunarestpki import *

from zope.testbrowser.browser import Browser
browser = Browser()

class ISAPLTool(Interface):
    """ Marker interface for SAPL Tool.
    """
    pass

class SAPLTool(UniqueObject, SimpleItem, ActionProviderBase):

    __implements__ = (ISAPLTool)

    id = 'portal_sapl'
    meta_type = 'SAPL Tool'

    XSI_NS = 'http://www.w3.org/2001/XMLSchema-instance'
    ns = {'lexml': 'http://www.lexml.gov.br/oai_lexml'}
    schema = {'oai_lexml': 'http://projeto.lexml.gov.br/esquemas/oai_lexml.xsd'}

    def verifica_esfera_federacao(self):
        ''' Funcao para verificar a esfera da federacao
        '''
        nome_camara = self.sapl_documentos.props_sapl.nom_casa
        camara = [u'Câmara','Camara','camara',u'camara']
        assembleia = [u'Assembléia','Assembleia','assembleia',u'assembléia']

        if [tipo for tipo in camara if nome_camara.startswith(tipo)]:
            return 'M'
        elif [tipo for tipo in assembleia if nome_camara.startswith(tipo)]:
            return 'E'
        else:
            return ''

    def monta_id(self,cod_norma):
        ''' Funcao que monta o id do objeto do LexML
        '''

        #consultas
        consulta = self.zsql.lexml_normas_juridicas_obter_zsql(cod_norma=cod_norma)
        if consulta:
            consulta = self.zsql.lexml_normas_juridicas_obter_zsql(cod_norma=cod_norma)[0]

            end_web_casa = self.sapl_documentos.props_sapl.end_web_casa
            sgl_casa = self.sapl_documentos.props_sapl.sgl_casa.lower()
            num = len(end_web_casa.split('.'))
            dominio = '.'.join(end_web_casa.split('.')[1:num])

            prefixo_oai = '%s.%s:sapl/' % (sgl_casa,dominio)
            numero_interno = consulta.num_norma
            tipo_norma = consulta.voc_lexml
            ano_norma = consulta.ano_norma

            identificador = '%s%s;%s;%s' % (prefixo_oai,tipo_norma,ano_norma,numero_interno)

            return identificador
        else:
            return None

    def monta_urn(self, cod_norma):
        ''' Funcao que monta a URN do LexML
        '''

        esfera = self.verifica_esfera_federacao()
        consulta = self.zsql.lexml_normas_juridicas_obter_zsql(cod_norma=cod_norma)
        if consulta:
            consulta = self.zsql.lexml_normas_juridicas_obter_zsql(cod_norma=cod_norma)[0]
            url = self.portal_url() + '/consultas/norma_juridica/norma_juridica_mostrar_proc?cod_norma=' + str(cod_norma)
            urn='urn:lex:br;'
            esferas = {'M':'municipal','E':'estadual'}

            localidade = self.zsql.localidade_obter_zsql(cod_localidade = self.sapl_documentos.props_sapl.cod_localidade)
            municipio = localidade[0].nom_localidade_pesq.lower()
            for i in re.findall('\s',municipio):
                municipio = municipio.replace(i, '.')

            if re.search( '\.de\.', municipio):
                municipio = [municipio.replace(i, '.') for i in re.findall( '\.de\.', municipio)][0]
            if re.search( '\.da\.', municipio):
                municipio = [municipio.replace(i, '.') for i in re.findall( '\.da\.', municipio)][0]
            if re.search( '\.das\.', municipio):
                municipio = [municipio.replace(i, '.') for i in re.findall( '\.das\.', municipio)][0]
            if re.search( '\.do\.', municipio):
                municipio = [municipio.replace(i, '.') for i in re.findall( '\.do\.', municipio)][0]
            if re.search( '\.dos\.', municipio):
                municipio = [municipio.replace(i, '.') for i in re.findall( '\.dos\.', municipio)][0]

            sigla_uf=localidade[0].sgl_uf
            uf = self.zsql.localidade_obter_zsql(sgl_uf=sigla_uf,tip_localidade='U')[0].nom_localidade_pesq.lower()
            for i in re.findall('\s',uf):
                uf = uf.replace(i, '.')

            if re.search( '\.de\.', uf):
                uf = [uf.replace(i, '.') for i in re.findall( '\.de\.', uf)][0]
            if re.search( '\.da\.', uf):
                uf = [uf.replace(i, '.') for i in re.findall( '\.da\.', uf)][0]
            if re.search( '\.das\.', uf):
                uf = [uf.replace(i, '.') for i in re.findall( '\.das\.', uf)][0]
            if re.search( '\.do\.', uf):
                uf = [uf.replace(i, '.') for i in re.findall( '\.do\.', uf)][0]
            if re.search( '\.dos\.', uf):
                uf = [uf.replace(i, '.') for i in re.findall( '\.dos\.', uf)][0]

            if self.verifica_esfera_federacao() == 'M':
                urn += uf + ';'
                urn += municipio + ':'
            elif self.verifica_esfera_federacao() == 'E':
                urn += uf + ':'

            if esfera == 'M':
                if consulta.voc_lexml == 'regimento.interno' or consulta.voc_lexml == 'resolucao':
                    urn += 'camara.municipal:'
                else:
                    urn += esferas[esfera] + ':'
            else:
                urn += esferas[esfera] + ':'

            urn += consulta.voc_lexml + ':'

            urn += self.pysc.port_to_iso_pysc(consulta.dat_norma) + ';'

            if consulta.voc_lexml == 'lei.organica' or consulta.voc_lexml == 'constituicao':
                urn += consulta.ano_norma
            else:
                urn += consulta.num_norma

            if consulta.dat_vigencia and consulta.dat_publicacao:
                urn += '@'
                urn += self.pysc.port_to_iso_pysc(consulta.dat_vigencia)
                urn += ';publicacao;'
                urn += self.pysc.port_to_iso_pysc(consulta.dat_publicacao)
            elif consulta.dat_publicacao:
                urn += '@'
                urn += 'inicio.vigencia;publicacao;' + self.pysc.port_to_iso_pysc(consulta.dat_publicacao)

            return urn
        else:
            return None

    def monta_xml(self,urn,cod_norma):
        #criacao do xml
        consulta = self.zsql.lexml_normas_juridicas_obter_zsql(cod_norma=cod_norma)
        publicador = self.zsql.lexml_publicador_obter_zsql()
        if consulta and publicador:
            consulta = self.zsql.lexml_normas_juridicas_obter_zsql(cod_norma=cod_norma)[0]
            publicador = self.zsql.lexml_publicador_obter_zsql()[0]

            url = self.portal_url() + '/consultas/norma_juridica/norma_juridica_mostrar_proc?cod_norma=' + str(cod_norma)

            E = ElementMaker()
            LEXML = ElementMaker(namespace=self.ns['lexml'],nsmap=self.ns)

            oai_lexml = LEXML.LexML()

            oai_lexml.attrib['{%s}schemaLocation' % self.XSI_NS] = '%s %s' % (
                'http://www.lexml.gov.br/oai_lexml',
                'http://projeto.lexml.gov.br/esquemas/oai_lexml.xsd')

            id_publicador = str(publicador.id_publicador)

            # montagem da epigrafe
            localidade = self.zsql.localidade_obter_zsql(cod_localidade = self.sapl_documentos.props_sapl.cod_localidade)[0].nom_localidade
            sigla_uf = self.zsql.localidade_obter_zsql(cod_localidade = self.sapl_documentos.props_sapl.cod_localidade)[0].sgl_uf
            if consulta.voc_lexml == 'lei.organica':
                epigrafe = u'%s de %s - %s, de %s' % (consulta.des_tipo_norma, localidade,sigla_uf, consulta.ano_norma)
            elif consulta.voc_lexml == 'constituicao':
                epigrafe = u'%s do Estado de %s, de %s' % (consulta.des_tipo_norma, localidade, consulta.ano_norma)
            else:
                epigrafe = u'%s n° %s,  de %s' % (consulta.des_tipo_norma, consulta.num_norma, self.pysc.data_converter_por_extenso_pysc(consulta.dat_norma))

            ementa = consulta.txt_ementa

            indexacao = consulta.txt_indexacao

            formato = 'text/html'
            id_documento = u'%s_%s' % (str(cod_norma), self.sapl_documentos.norma_juridica.nom_documento)
            if hasattr(self.sapl_documentos.norma_juridica,id_documento):
                arquivo = getattr(self.sapl_documentos.norma_juridica,id_documento)
                url_conteudo = arquivo.absolute_url()
                formato = arquivo.content_type
                if formato == 'application/octet-stream':
                    formato = 'application/msword'
                if formato == 'image/ipeg':
                    formato = 'image/jpeg'

            else:
                url_conteudo = self.portal_url() + '/consultas/norma_juridica/norma_juridica_mostrar_proc?cod_norma=' + str(cod_norma)

            item_conteudo = E.Item(url_conteudo,formato=formato, idPublicador=id_publicador,tipo='conteudo')
            oai_lexml.append(item_conteudo)

            item_metadado = E.Item(url,formato='text/html', idPublicador=id_publicador,tipo='metadado')
            oai_lexml.append(item_metadado)

            documento_individual = E.DocumentoIndividual(urn)
            oai_lexml.append(documento_individual)
            oai_lexml.append(E.Epigrafe(epigrafe))
            oai_lexml.append(E.Ementa(ementa))
            if indexacao:
                oai_lexml.append(E.Indexacao(indexacao))
            return etree.tostring(oai_lexml)
        else:
            return None

    def oai_query(self,
                  offset=0,
                  batch_size=20,
                  from_date=None,
                  until_date=None,
                  identifier=None):

        esfera = self.verifica_esfera_federacao()

        if batch_size < 0:
            batch_size = 0

        if until_date == None or until_date > datetime.now():
            until_date = datetime.now()

        if from_date is None:
            from_date = ''

        normas = self.zsql.lexml_normas_juridicas_obter_zsql(from_date=from_date,
            until_date=until_date,
            offset=offset,
            batch_size=batch_size,
            num_norma=identifier,
            tip_esfera_federacao=esfera)
        for norma in normas:
            resultado = {}
            cod_norma = norma.cod_norma
            identificador = self.monta_id(cod_norma)
            urn = self.monta_urn(cod_norma)
            xml_lexml = self.monta_xml(urn,cod_norma)

            resultado['tx_metadado_xml'] = xml_lexml
            resultado['cd_status'] = 'N'
            resultado['id'] = identificador
            resultado['when_modified'] = norma.timestamp
            resultado['deleted'] = 0
            if norma.ind_excluido == 1:
                resultado['deleted'] = 1
            yield {'record': resultado,
                   'metadata': resultado['tx_metadado_xml'],
            }

    def create_barcode(self, value):
        barcode = createBarcodeDrawing('Code128',
                                       value=str(value).zfill(7),
                                       barWidth=170,
                                       height=50,
                                       fontSize=2,
                                       humanReadable=True)
        data = b64encode(barcode.asString('png'))
        return data.decode('utf-8')

    def url(self):
        utool = getToolByName(self, 'portal_url')
        return utool.portal_url()

    def get_brasao(self):
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sapl.id_logo
        url = self.url() + '/sapl_documentos/props_sapl/logo_casa.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        brasao = open('/tmp/' + id_logo, 'rb')
        os.unlink('/tmp/' + id_logo)
        return brasao

    def ata_gerar_odt(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/ata.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.ata_sessao.manage_addFile(id=output_file_odt,file=data)
        #self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        #self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        #return data

    def ata_gerar_pdf(self, cod_sessao_plen):
        nom_arquivo_odt = "%s"%cod_sessao_plen+'_ata_sessao.odt'
    	nom_arquivo_pdf = "%s"%cod_sessao_plen+'_ata_sessao.pdf'
    	url = self.sapl_documentos.ata_sessao.absolute_url() + "/%s"%nom_arquivo_odt
    	odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    	output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    	renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    	renderer.run()
    	data = open(output_file_pdf, "rb").read()
    	for file in [output_file_pdf]:
    	    os.unlink(file)
    	    self.sapl_documentos.ata_sessao.manage_addFile(id=nom_arquivo_pdf,file=data)

    def iom_gerar_odt(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/iom.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_odt = "publicacao_iom.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def materia_apreciada_gerar_odt(self, inf_basicas_dic, lst_votacao):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/materia_apreciada.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "materia_apreciada.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def materia_apresentada_gerar_odt(self, inf_basicas_dic, lst_materia_apresentada):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/materia_apresentada.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_odt = "materia_apresentada.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()                                                                              
        data = open(output_file_odt, "rb").read()                 
        for file in [output_file_odt]:
            os.unlink(file)                                                                                                      
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data 

    def ordem_dia_gerar_odt(self, inf_basicas_dic, lst_pdiscussao, lst_sdiscussao, lst_discussao_unica, lst_presidente, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/ordem_dia.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.pauta_sessao.manage_addFile(id=output_file_odt,file=data)

    def ordem_dia_gerar_pdf(self, cod_sessao_plen):
        nom_arquivo_odt = "%s"%cod_sessao_plen+'_pauta_sessao.odt'
    	nom_arquivo_pdf = "%s"%cod_sessao_plen+'_pauta_sessao.pdf'
    	url = self.sapl_documentos.pauta_sessao.absolute_url() + "/%s"%nom_arquivo_odt
    	odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    	output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    	renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    	renderer.run()
    	data = open(output_file_pdf, "rb").read()
    	for file in [output_file_pdf]:
    	    os.unlink(file)
    	    self.sapl_documentos.pauta_sessao.manage_addFile(id=nom_arquivo_pdf,file=data)

    def oradores_gerar_odt(self, inf_basicas_dic, lst_oradores, lst_presidente, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/oradores.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.oradores_expediente.manage_addFile(id=output_file_odt,file=data)

    def oradores_gerar_pdf(self,cod_sessao_plen):
        nom_arquivo_odt = "%s"%cod_sessao_plen+'_oradores_expediente.odt'
        nom_arquivo_pdf = "%s"%cod_sessao_plen+'_oradores_expediente.pdf'
        url = self.sapl_documentos.oradores_expediente.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.oradores_expediente.manage_addFile(id=nom_arquivo_pdf,file=data)

    def expediente_gerar_odt(self, inf_basicas_dic, lst_indicacoes, lst_requerimentos, lst_mocoes, lst_oradores, lst_presidente, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/expediente.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()                                                                            
        data = open(output_file_odt, "rb").read()                 
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.pauta_sessao.manage_addFile(id=output_file_odt,file=data)

    def expediente_gerar_pdf(self, cod_sessao_plen):
        nom_arquivo_odt = "%s"%cod_sessao_plen+'_expediente.odt'
    	nom_arquivo_pdf = "%s"%cod_sessao_plen+'_expediente.pdf'
    	url = self.sapl_documentos.pauta_sessao.absolute_url() + "/%s"%nom_arquivo_odt
    	odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    	output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    	renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    	renderer.run()
    	data = open(output_file_pdf, "rb").read()
    	for file in [output_file_pdf]:
    	    os.unlink(file)
    	    self.sapl_documentos.pauta_sessao.manage_addFile(id=nom_arquivo_pdf,file=data)

    def resumo_gerar_odt(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/resumo.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "resumo_sessao.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def doc_acessorio_gerar_odt(self, inf_basicas_dic, nom_arquivo, des_tipo_documento, nom_documento, txt_ementa, dat_documento, data_documento, nom_autor, materia_vinculada, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.documento_acessorio.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.materia_odt.manage_addFile(id=nom_arquivo,file=data)

    def doc_acessorio_gerar_pdf(self, cod_documento):
        nom_arquivo_odt = "%s"%cod_documento+'.odt'
        nom_arquivo_pdf = "%s"%cod_documento+'.pdf'
        url = self.sapl_documentos.materia_odt.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()                 
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.materia.manage_addFile(id=nom_arquivo_pdf,file=data)

    def oficio_ind_gerar_odt(self, inf_basicas_dic, lst_indicacao, lst_presidente):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/oficio_indicacao.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "oficio_indicacao.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def emenda_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.emenda.manage_addFile(id=nom_arquivo,file=data)

    def emenda_gerar_pdf(self,cod_emenda):
        nom_arquivo_odt = "%s"%cod_emenda+'_emenda.odt'
        nom_arquivo_pdf = "%s"%cod_emenda+'_emenda.pdf'
        url = self.sapl_documentos.emenda.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()                 
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.emenda.manage_addFile(id=nom_arquivo_pdf,file=data)

    def materia_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.materia_odt.manage_addFile(id=nom_arquivo,file=data)

    def materia_gerar_pdf(self, cod_materia):
        nom_arquivo_odt = "%s"%cod_materia+'_texto_integral.odt'
        nom_arquivo_pdf1 = "%s"%cod_materia+'_texto_integral.pdf'
        url = self.sapl_documentos.materia_odt.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.materia.manage_addFile(id=nom_arquivo_pdf1, file=data)

    def redacao_final_gerar_pdf(self, cod_materia):
        nom_arquivo_odt = "%s"%cod_materia+'_redacao_final.odt'
        nom_arquivo_pdf1 = "%s"%cod_materia+'_redacao_final.pdf'
        url = self.sapl_documentos.materia_odt.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.materia.manage_addFile(id=nom_arquivo_pdf1, file=data)

    def norma_gerar_odt(self, inf_basicas_dic, nom_arquivo, des_tipo_norma, num_norma, ano_norma, dat_norma, data_norma, txt_ementa, modelo_norma):
        url = self.sapl_documentos.modelo.norma.absolute_url() + "/%s" % modelo_norma
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.norma_juridica.manage_addFile(id=nom_arquivo,file=data)

    def norma_gerar_pdf(self, cod_norma):
        nom_arquivo_odt = "%s"%cod_norma+'_texto_integral.odt'
        nom_arquivo_pdf1 = "%s"%cod_norma+'_texto_consolidado.pdf'
        url = self.sapl_documentos.norma_juridica.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.norma_juridica.manage_addFile(id=nom_arquivo_pdf1, file=data)

    def oficio_gerar_odt(self, inf_basicas_dic, nom_arquivo, sgl_tipo_documento, num_documento, ano_documento, txt_ementa, dat_documento, dia_documento, nom_autor, modelo_documento):
        url = self.sapl_documentos.modelo.documento_administrativo.absolute_url() + "/%s" % modelo_documento
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.administrativo.manage_addFile(id=nom_arquivo,file=data)

    def oficio_gerar_pdf(self, cod_documento):
        nom_arquivo_odt = "%s"%cod_documento+'_texto_integral.odt'
        nom_arquivo_pdf1 = "%s"%cod_documento+'_texto_integral.pdf'
        url = self.sapl_documentos.administrativo.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.administrativo.manage_addFile(id=nom_arquivo_pdf1, file=data)

    def parecer_gerar_odt(self, inf_basicas_dic, nom_arquivo, nom_comissao, materia, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao):
        url = self.sapl_documentos.modelo.materia.parecer.absolute_url() + "/parecer.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.parecer_comissao.manage_addFile(id=nom_arquivo,file=data)

    def parecer_gerar_pdf(self, cod_parecer):
        nom_arquivo_odt = "%s"%cod_parecer+'_parecer.odt'
        nom_arquivo_pdf1 = "%s"%cod_parecer+'_parecer.pdf'
        url = self.sapl_documentos.parecer_comissao.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.parecer_comissao.manage_addFile(id=nom_arquivo_pdf1, file=data)

    def proposicao_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/%s"%modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.proposicao.manage_addFile(id=nom_arquivo,file=data)

    def proposicao_gerar_pdf(self, cod_proposicao):
        nom_arquivo_odt = "%s"%cod_proposicao+'.odt'
        nom_arquivo_pdf1 = "%s"%cod_proposicao+'.pdf'
        url = self.sapl_documentos.proposicao.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.proposicao.manage_addFile(id=nom_arquivo_pdf1, file=data)

    def substitutivo_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/%s"%modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        # atribui o brasao no locals
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.substitutivo.manage_addFile(id=nom_arquivo,file=data)

    def substitutivo_gerar_pdf(self,cod_substitutivo):
        nom_arquivo_odt = "%s"%cod_substitutivo+'_substitutivo.odt'
        nom_arquivo_pdf = "%s"%cod_substitutivo+'_substitutivo.pdf'
        url = self.sapl_documentos.substitutivo.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()                 
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.substitutivo.manage_addFile(id=nom_arquivo_pdf,file=data)

    def protocolo_barcode(self,cod_protocolo):
        sgl_casa = self.sapl_documentos.props_sapl.sgl_casa
        for protocolo in self.zsql.protocolo_obter_zsql(cod_protocolo=cod_protocolo):
          string = str(protocolo.cod_protocolo).zfill(7)
          texto = 'PROT-'+ str(sgl_casa)+' '+ str(protocolo.num_protocolo)+'/'+str(protocolo.ano_protocolo)
          data = self.pysc.iso_to_port_pysc(protocolo.dat_protocolo)+' - '+protocolo.hor_protocolo[0:2]+':'+protocolo.hor_protocolo[3:5]
          pdf_protocolo = self.sapl_documentos.protocolo.absolute_url() + "/" +  str(cod_protocolo) + "_protocolo.pdf"
          nom_pdf_protocolo = str(cod_protocolo) + "_protocolo.pdf"
        pdfmetrics.registerFont(TTFont('Courier_Bold', '/usr/share/fonts/truetype/msttcorefonts/Courier_New_Bold.ttf'))
        x_var=169
        y_var=285
        packet = os.path.normpath('temp.pdf')
        slab = canvas.Canvas(packet, pagesize=A4)
        slab.setFillColorRGB(0,0,0) 
        barcode = barcode128 = code128.Code128(string,barWidth=.34*mm,barHeight=7*mm)
        barcode.drawOn(slab, x_var*mm , y_var*mm)
        slab.setFont("Courier_Bold", 8)
        slab.drawString(497, 801, texto)
        slab.drawString(497, 794, data)
        slab.save()
        barcode_pdf = open(packet, 'rb')
        new_pdf = PdfFileReader(barcode_pdf)
        pdf_file = '%s' % (cod_protocolo) + "_protocolo.pdf"
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        url = self.url() + '/sapl_documentos/protocolo/' + pdf_file
        opener = urllib.urlopen(url)
        f = open('/tmp/' + pdf_file, 'wb').write(opener.read())
        existing_pdf = PdfFileReader(file('/tmp/'+nom_pdf_protocolo, "rb"))
        output = PdfFileWriter()
        for item in range(existing_pdf.getNumPages()):
          pages = existing_pdf.getPage(item)
          page1 = existing_pdf.getPage(0)
          pages.mergePage(new_pdf.getPage(0))
          output.addPage(pages)
        outputStream = file(os.path.normpath(nom_pdf_protocolo), "wb")
        output.write(outputStream)
        outputStream.close()
        data = open(nom_pdf_protocolo, "rb").read()              
        for item in [outputStream]:
          if nom_pdf_protocolo in self.sapl_documentos.protocolo:
            documento = getattr(self.sapl_documentos.protocolo,nom_pdf_protocolo)
            documento.manage_upload(file=data)
        os.unlink('/tmp/'+nom_pdf_protocolo)
        os.unlink(packet)
        os.unlink(nom_pdf_protocolo)

    def processo_eletronico_gerar_pdf(self,cod_materia):
        if cod_materia.isdigit():
           cod_materia = cod_materia
        else:
           cod_materia = self.pysc.b64decode_pysc(codigo=str(cod_materia))
        writer = PdfFileWriter()
        merger = PdfFileMerger()
        for materia in self.zsql.materia_obter_zsql(cod_materia=cod_materia):
           nom_arquivo_pdf = materia.sgl_tipo_materia + "-" +str(materia.num_ident_basica) + "-" + str(materia.ano_ident_basica) + '_processo_eletronico.pdf'
        proposicao = self.zsql.proposicao_obter_zsql(ind_mat_ou_doc='M',cod_mat_ou_doc=cod_materia,ind_excluido=0)
        if proposicao:
           cod_proposicao = proposicao[0].cod_proposicao
           pdf_proposicao = self.sapl_documentos.proposicao.absolute_url() + "/" +  str(cod_proposicao) + "_signed.pdf"
           texto_materia = cStringIO.StringIO(urllib.urlopen(pdf_proposicao).read())
           merger.append(texto_materia)
        else:
           if hasattr(self.sapl_documentos.materia, str(cod_materia) + '_texto_integral.pdf'):
              pdf_materia = self.sapl_documentos.materia.absolute_url()+ "/" + cod_materia + "_texto_integral.pdf"
              texto_materia = cStringIO.StringIO(urllib.urlopen(pdf_materia).read())
              merger.append(texto_materia)

        lst_mat_anexadas = []
        for anexada in self.zsql.anexada_obter_zsql(cod_materia_principal=cod_materia,ind_excluido=0):
           dic_mat = {}
           if hasattr(self.sapl_documentos.materia, str(anexada.cod_materia_anexada) + '_texto_integral.pdf'):
              dic_mat['pdf_anexada'] = self.sapl_documentos.materia.absolute_url()+ "/" + str(anexada.cod_materia_anexada) + "_texto_integral.pdf"
           lst_mat_anexadas.append(dic_mat)
           if hasattr(self.sapl_documentos.materia, str(anexada.cod_materia_anexada) + '_texto_integral.pdf'):
              for dic_mat in lst_mat_anexadas:
                 texto_anexada = cStringIO.StringIO(urllib.urlopen(dic_mat['pdf_anexada']).read())
                 merger.append(texto_anexada)

        lst_emendas = []
        for emenda in self.zsql.emenda_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
           dic_emendas = {}
           if hasattr(self.sapl_documentos.emenda, str(emenda.cod_emenda) + '_emenda.pdf'):
              dic_emendas['pdf_emenda'] = self.sapl_documentos.emenda.absolute_url()+ "/" + str(emenda.cod_emenda) + "_emenda.pdf"
           lst_emendas.append(dic_emendas)
           if hasattr(self.sapl_documentos.emenda, str(emenda.cod_emenda) + '_emenda.pdf'):
              for dic_emendas in lst_emendas:
                 texto_emenda = cStringIO.StringIO(urllib.urlopen(dic_emendas['pdf_emenda']).read())
                 merger.append(texto_emenda)

        lst_substitutivos = []
        for substitutivo in self.zsql.substitutivo_obter_zsql(cod_materia=cod_materia):
           dic_substitutivos = {}
           if hasattr(self.sapl_documentos.substitutivo, str(substitutivo.cod_substitutivo) + '_substitutivo.pdf'):
              dic_substitutivos['pdf_substitutivo'] = self.sapl_documentos.substitutivo.absolute_url()+ "/" + str(substitutivo.cod_substitutivo) + "_substitutivo.pdf"
           lst_substitutivos.append(dic_substitutivos)
           if hasattr(self.sapl_documentos.substitutivo, str(substitutivo.cod_substitutivo) + '_substitutivo.pdf'):
              for dic_substitutivos in lst_substitutivos:
                 texto_substitutivo = cStringIO.StringIO(urllib.urlopen(dic_substitutivos['pdf_substitutivo']).read())
                 merger.append(texto_substitutivo)

        #lst_relatorias = []
        #for relatoria in self.zsql.relatoria_obter_zsql(cod_materia = cod_materia,ind_excluido=0):
        #   dic_comissao={}
        #   if hasattr(self.sapl_documentos.parecer_comissao, str(relatoria.cod_relatoria) + '_parecer.pdf'):
        #      dic_comissao['pdf_relatoria'] = self.sapl_documentos.parecer_comissao.absolute_url()+ "/" + relatoria.cod_relatoria + "_parecer.pdf"
        #   lst_relatorias.append(dic_comissao)
        #   if hasattr(self.sapl_documentos.parecer_comissao, str(relatoria.cod_relatoria) + '_parecer.pdf'):
        #      for dic_comissao in lst_relatorias:
        #         texto_relatoria = cStringIO.StringIO(urllib.urlopen(dic_comissao['pdf_relatoria']).read())
        #         merger.append(texto_relatoria)

        lst_acessorios = []
        for documento in self.zsql.documento_acessorio_obter_zsql(cod_materia = cod_materia,ind_excluido=0):
           proposicao = self.zsql.proposicao_obter_zsql(ind_mat_ou_doc='D',cod_mat_ou_doc=documento.cod_documento,ind_excluido=0)
           if proposicao:
              cod_proposicao = proposicao[0].cod_proposicao
              pdf_proposicao = self.sapl_documentos.proposicao.absolute_url() + "/" +  str(cod_proposicao) + "_signed.pdf"
              texto_documento = cStringIO.StringIO(urllib.urlopen(pdf_proposicao).read())
              merger.append(texto_documento)
           else:
              dic_dados={}
              if hasattr(self.sapl_documentos.materia, str(documento.cod_documento) + '.pdf'):
                 dic_dados['pdf_documento'] = self.sapl_documentos.materia.absolute_url()+ "/" + documento.cod_documento + ".pdf"
              lst_acessorios.append(dic_dados)
              if hasattr(self.sapl_documentos.materia, str(documento.cod_documento) + '.pdf'):
                 for dic_dados in lst_acessorios:
                   texto_documento = cStringIO.StringIO(urllib.urlopen(dic_dados['pdf_documento']).read())
                   merger.append(texto_documento)

        lst_tramitacoes = []
        for tramitacao in self.zsql.tramitacao_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
           dic_tramitacoes={}
           if hasattr(self.sapl_documentos.materia.tramitacao, str(tramitacao.cod_tramitacao) + '_tram_signed.pdf'):
              dic_tramitacoes['pdf_tramitacao'] = self.sapl_documentos.materia.tramitacao.absolute_url()+ "/" + tramitacao.cod_tramitacao + "_tram_signed.pdf"
           #   lst_tramitacoes.append(dic_tramitacoes)
           elif hasattr(self.sapl_documentos.materia.tramitacao, str(tramitacao.cod_tramitacao) + '_tram.pdf'):
              dic_tramitacoes['pdf_tramitacao'] = self.sapl_documentos.materia.tramitacao.absolute_url()+ "/" + tramitacao.cod_tramitacao + "_tram.pdf"
              lst_tramitacoes.append(dic_tramitacoes)
           #if hasattr(self.sapl_documentos.materia.tramitacao, str(tramitacao.cod_tramitacao) + '_tram_signed.pdf') or hasattr(self.sapl_documentos.materia.tramitacao, str(tramitacao.cod_tramitacao) + '_tram.pdf'):
        for dic_tramitacoes in lst_tramitacoes:
           texto_tramitacao = cStringIO.StringIO(urllib.urlopen(dic_tramitacoes['pdf_tramitacao']).read())
           merger.append(texto_tramitacao)

        output_file_pdf = os.path.normpath(nom_arquivo_pdf)
        f = open(output_file_pdf, "wb")
        merger.write(f)
        f.close()
        readin = open(output_file_pdf, 'r' )
        contents = readin.read()
        for file in [output_file_pdf]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/pdf'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="processo_eletronico.pdf"'
        return contents

    def proposicao_autuar(self,cod_proposicao):
        nom_pdf_proposicao = str(cod_proposicao) + "_signed.pdf"
        pdf_proposicao = self.sapl_documentos.proposicao.absolute_url() + "/" +  nom_pdf_proposicao
        nom_pdf_proposicao = str(cod_proposicao) + "_signed.pdf"
        for proposicao in self.zsql.proposicao_obter_zsql(cod_proposicao=cod_proposicao):
          for tipo_proposicao in self.zsql.tipo_proposicao_obter_zsql(tip_proposicao=proposicao.tip_proposicao):
            if tipo_proposicao.ind_mat_ou_doc == "M":
              for materia in self.zsql.materia_obter_zsql(cod_materia=proposicao.cod_mat_ou_doc):
                string = str(materia.cod_materia).zfill(11)
                num_proposicao = proposicao.cod_proposicao
                cod_materia = materia.cod_materia
                nom_autor = proposicao.nom_autor
                texto = str(materia.des_tipo_materia.upper())+' Nº '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
                validacao = 'Código: ' + self.pysc.proposicao_calcular_checksum_pysc(cod_proposicao)
                nom_pdf_saida = str(materia.cod_materia) + "_texto_integral.pdf"
            elif tipo_proposicao.ind_mat_ou_doc == "D":
              for documento in self.zsql.documento_acessorio_obter_zsql(cod_documento=proposicao.cod_mat_ou_doc):
                string = str(documento.cod_documento).zfill(11)
                num_proposicao = proposicao.cod_proposicao
                cod_materia = documento.cod_materia
                nom_autor = proposicao.nom_autor
                texto = str(documento.des_tipo_documento.upper())
                validacao = 'Código: ' + self.pysc.proposicao_calcular_checksum_pysc(cod_proposicao)
                nom_pdf_saida = str(documento.cod_documento) + ".pdf"
        mensagem1 = texto + ' - Este documento é cópia do original assinado digitalmente por '+nom_autor+'.'
        mensagem2 = 'Para conferir o original, utilize um leitor QR Code ou acesse ' + self.url()+'/consultas/proposicao'+' e informe o número '+ num_proposicao+'.'
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        x_var=27
        y_var=210
        packet = os.path.normpath('temp.pdf')
        slab = canvas.Canvas(packet, pagesize=A4)
        slab.setFillColorRGB(0,0,0)
        qr_code = qr.QrCodeWidget(self.url()+'/consultas/materia/materia_mostrar_proc?cod_materia='+str(cod_materia))
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(100, 100, transform=[100./width,0,0,100./height,0,0])
        d.add(qr_code)
        renderPDF.draw(d, slab,  x_var*mm, y_var*mm)
        slab.setFont("Arial_Bold", 12)
        slab.drawString(185, 675, texto)
        slab.setFont("Arial", 9)
        slab.drawString(185, 662, validacao)
        slab.save()
        barcode_pdf = open(packet, 'rb')
        new_pdf = PdfFileReader(barcode_pdf)

        packet1 = os.path.normpath('temp1.pdf')
        c = canvas.Canvas(packet1, pagesize=A4)
        c.setFillColorRGB(0,0,0)
        c.rotate(90)
        c.setFont("Arial", 9)
        c.drawString(10, -578, mensagem1)
        c.drawString(10, -590, mensagem2)
        c.save()
        texto_pdf = open(packet1, 'rb')
        new_pdf1 = PdfFileReader(texto_pdf)

        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        url = self.url() + '/sapl_documentos/proposicao/' + nom_pdf_proposicao
        opener = urllib.urlopen(url)
        f = open('/tmp/' + nom_pdf_proposicao, 'wb').write(opener.read())
        existing_pdf = PdfFileReader(file('/tmp/' + nom_pdf_proposicao, "rb"))
        output = PdfFileWriter()
        for item in range(existing_pdf.getNumPages()):
          pages = existing_pdf.getPage(item)
          page1 = existing_pdf.getPage(0)
          page1.mergePage(new_pdf.getPage(0))
          pages.mergePage(new_pdf1.getPage(0))
          output.addPage(pages)
        outputStream = file(os.path.normpath(nom_pdf_proposicao), "wb")
        output.write(outputStream)
        outputStream.close()
        data = open(nom_pdf_proposicao, "rb").read()              
        for item in [outputStream]:
          if nom_pdf_saida in self.sapl_documentos.materia:
            documento = getattr(self.sapl_documentos.materia,nom_pdf_saida)
            documento.manage_upload(file=data)
          else:
            self.sapl_documentos.materia.manage_addFile(id=nom_pdf_saida,file=data)
        os.unlink('/tmp/'+nom_pdf_proposicao)
        os.unlink(packet)
        os.unlink(packet1)
        os.unlink(nom_pdf_proposicao)

    def restpki_client(self):
        restpki_url = 'https://pki.rest/'
        restpki_access_token = self.sapl_documentos.props_sapl.restpki_access_token            
        restpki_client = RestPkiClient(restpki_url, restpki_access_token)
        return restpki_client

    def pades_signature(self, cod_proposicao):
        pdf_file = '%s' % (cod_proposicao) + ".pdf"

        # Read the PDF path
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        url = self.url() + '/sapl_documentos/proposicao/' + pdf_file
        opener = urllib.urlopen(url)
        f = open('/tmp/' + pdf_file, 'wb').write(opener.read())
        tmp_path = '/tmp'
        pdf_tmp = pdf_file
        pdf_path = '%s/%s' % (tmp_path, pdf_file)

        # Read the PDF stamp image
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sapl.id_logo
        url = self.url() + '/sapl_documentos/props_sapl/logo_casa.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        f = open('/tmp/' + id_logo, 'rb')
        pdf_stamp = f.read()
        f.close()

        signature_starter = PadesSignatureStarter(self.restpki_client())
        signature_starter.set_pdf_path(pdf_path)
        signature_starter.signature_policy_id = StandardSignaturePolicies.PADES_BASIC
        signature_starter.security_context_id = StandardSecurityContexts.PKI_BRAZIL
        signature_starter.visual_representation = ({
            'text': {
                # The tags {{signerName}} and {{signerNationalId}} will be substituted according to the user's
                # certificate
                # signerName -> full name of the signer
                # signerNationalId -> if the certificate is ICP-Brasil, contains the signer's CPF
                'text': 'Assinado por {{signerName}} - {{signerNationalId}}',
                # Specify that the signing time should also be rendered
                'includeSigningTime': True,
                # Optionally set the horizontal alignment of the text ('Left' or 'Right'), if not set the default is
                # Left
                'horizontalAlign': 'Left'
            },

            'image': {
                # We'll use as background the image that we've read above
                'resource': {
                    'content': base64.b64encode(pdf_stamp),
                    'mimeType': 'image/png'
                },
                # Opacity is an integer from 0 to 100 (0 is completely transparent, 100 is completely opaque).
                'opacity': 40,
                # Align the image to the right
                'horizontalAlign': 'Right'
            },

            'position': self.get_visual_representation_position(1)
        })

        token = signature_starter.start_with_webpki()
 
        return token, pdf_path, cod_proposicao

    def pades_cosignature(self, cod_proposicao):
        pdf_file_signed = '%s' % (cod_proposicao) + "_signed.pdf"
        
        # Read the PDF path
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        url = self.url() + '/sapl_documentos/proposicao/' + pdf_file_signed
        opener = urllib.urlopen(url)
        f = open('/tmp/' + pdf_file_signed, 'wb').write(opener.read())
        tmp_path = '/tmp'
        pdf_tmp = pdf_file_signed
        pdf_path = '%s/%s' % (tmp_path, pdf_file_signed)

        # Read the PDF stamp image
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sapl.id_logo
        url = self.url() + '/sapl_documentos/props_sapl/logo_casa.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        f = open('/tmp/' + id_logo, 'rb')
        pdf_stamp = f.read()
        f.close()

        signature_starter = PadesSignatureStarter(self.restpki_client())
        signature_starter.set_pdf_path(pdf_path)
        signature_starter.signature_policy_id = StandardSignaturePolicies.PADES_BASIC
        signature_starter.security_context_id = StandardSecurityContexts.PKI_BRAZIL
        signature_starter.visual_representation = ({
            'text': {
                # The tags {{signerName}} and {{signerNationalId}} will be substituted according to the user's
                # certificate
                # signerName -> full name of the signer
                # signerNationalId -> if the certificate is ICP-Brasil, contains the signer's CPF
                'text': 'Assinado por {{signerName}} - {{signerNationalId}}',
                # Specify that the signing time should also be rendered
                'includeSigningTime': True,
                # Optionally set the horizontal alignment of the text ('Left' or 'Right'), if not set the default is
                # Left
                'horizontalAlign': 'Left'
            },

            'image': {
                # We'll use as background the image that we've read above
                'resource': {
                    'content': base64.b64encode(pdf_stamp),
                    'mimeType': 'image/png'
                },
                # Opacity is an integer from 0 to 100 (0 is completely transparent, 100 is completely opaque).
                'opacity': 40,
                # Align the image to the right
                'horizontalAlign': 'Right'
            },

            'position': self.get_visual_representation_position(2)
        })

        token = signature_starter.start_with_webpki()
 
        return token, pdf_path, cod_proposicao

    def pades_signature_action(self, token, cod_proposicao):
        # Get the token for this signature (rendered in a hidden input field, see pades-signature.html template)
        token = token
        cod_proposicao = cod_proposicao

        # Instantiate the PadesSignatureFinisher class, responsible for completing the signature process
        signature_finisher = PadesSignatureFinisher(self.restpki_client())

        # Set the token
        signature_finisher.token = token

        # Call the finish() method, which finalizes the signature process and returns the signed PDF
        signature_finisher.finish()

        # Get information about the certificate used by the user to sign the file. This method must only be called after
        # calling the finish() method.
        signer_cert = signature_finisher.certificate

        # At this point, you'd typically store the signed PDF on your database.
        filename = "%s"%cod_proposicao+'_signed.pdf'
        old_filename = "%s"%cod_proposicao+'.pdf'

        tmp_path = "/tmp"

        signature_finisher.write_signed_pdf(os.path.join(tmp_path, filename))

        signature_finisher.write_signed_pdf(filename)

        data = open('/tmp/' + filename, "rb").read()

        for file in [filename]:
            self.sapl_documentos.proposicao.manage_delObjects(ids=old_filename)
            os.unlink(file)
            if filename in self.sapl_documentos.proposicao:
              documento = getattr(self.sapl_documentos.proposicao,filename)
              documento.manage_upload(file=data)
            else:
              self.sapl_documentos.proposicao.manage_addFile(id=filename,file=data)

        for item in signer_cert:
           subjectName = signer_cert['subjectName']
           commonName = subjectName['commonName']
           email = signer_cert['emailAddress']
           pkiBrazil = signer_cert['pkiBrazil']
           certificateType = pkiBrazil['certificateType']
           cpf = pkiBrazil['cpf']
           responsavel = pkiBrazil['responsavel']

        return signer_cert, commonName, email, certificateType, cpf, responsavel, filename

    def tramitacao_signature(self, cod_tramitacao):
        pdf_file = '%s' % (cod_tramitacao) + "_tram.pdf"

        # Read the PDF path
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        url = self.url() + '/sapl_documentos/materia/tramitacao/' + pdf_file
        opener = urllib.urlopen(url)
        f = open('/tmp/' + pdf_file, 'wb').write(opener.read())
        tmp_path = '/tmp'
        pdf_tmp = pdf_file
        pdf_path = '%s/%s' % (tmp_path, pdf_file)

        # Read the PDF stamp image
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sapl.id_logo
        url = self.url() + '/sapl_documentos/props_sapl/logo_casa.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        f = open('/tmp/' + id_logo, 'rb')
        pdf_stamp = f.read()
        f.close()

        signature_starter = PadesSignatureStarter(self.restpki_client())
        signature_starter.set_pdf_path(pdf_path)
        signature_starter.signature_policy_id = StandardSignaturePolicies.PADES_BASIC
        signature_starter.security_context_id = StandardSecurityContexts.PKI_BRAZIL
        signature_starter.visual_representation = ({
            'text': {
                # The tags {{signerName}} and {{signerNationalId}} will be substituted according to the user's
                # certificate
                # signerName -> full name of the signer
                # signerNationalId -> if the certificate is ICP-Brasil, contains the signer's CPF
                'text': 'Assinado por {{signerName}} - {{signerNationalId}}',
                # Specify that the signing time should also be rendered
                'includeSigningTime': True,
                # Optionally set the horizontal alignment of the text ('Left' or 'Right'), if not set the default is
                # Left
                'horizontalAlign': 'Left'
            },

            'image': {
                # We'll use as background the image that we've read above
                'resource': {
                    'content': base64.b64encode(pdf_stamp),
                    'mimeType': 'image/png'
                },
                # Opacity is an integer from 0 to 100 (0 is completely transparent, 100 is completely opaque).
                'opacity': 40,
                # Align the image to the right
                'horizontalAlign': 'Right'
            },

            'position': self.get_visual_representation_position(2)
        })

        token = signature_starter.start_with_webpki()
 
        return token, pdf_path, cod_tramitacao

    def tramitacao_signature_action(self, token, cod_tramitacao):
        # Get the token for this signature (rendered in a hidden input field, see pades-signature.html template)
        token = token
        cod_tramitacao = cod_tramitacao

        # Instantiate the PadesSignatureFinisher class, responsible for completing the signature process
        signature_finisher = PadesSignatureFinisher(self.restpki_client())

        # Set the token
        signature_finisher.token = token

        # Call the finish() method, which finalizes the signature process and returns the signed PDF
        signature_finisher.finish()

        # Get information about the certificate used by the user to sign the file. This method must only be called after
        # calling the finish() method.
        signer_cert = signature_finisher.certificate

        # At this point, you'd typically store the signed PDF on your database.
        old_filename = "%s"%cod_tramitacao+'_tram.pdf'
        filename = "%s"%cod_tramitacao+'_tram_signed.pdf'

        tmp_path = "/tmp"

        signature_finisher.write_signed_pdf(os.path.join(tmp_path, filename))

        signature_finisher.write_signed_pdf(filename)

        data = open('/tmp/' + filename, "rb").read()

        for file in [filename]:
            self.sapl_documentos.materia.tramitacao.manage_delObjects(ids=old_filename)
            os.unlink(file)
            if filename in self.sapl_documentos.materia.tramitacao:
              documento = getattr(self.sapl_documentos.materia.tramitacao,filename)
              documento.manage_upload(file=data)
            else:
              self.sapl_documentos.materia.tramitacao.manage_addFile(id=filename,file=data)

        for item in signer_cert:
           subjectName = signer_cert['subjectName']
           commonName = subjectName['commonName']
           email = signer_cert['emailAddress']
           pkiBrazil = signer_cert['pkiBrazil']
           certificateType = pkiBrazil['certificateType']
           cpf = pkiBrazil['cpf']
           responsavel = pkiBrazil['responsavel']

        return signer_cert, commonName, email, certificateType, cpf, responsavel, filename

    def get_visual_representation_position(self, sample_number):
        if sample_number == 1:
            # Example #1: automatic positioning on footnote. This will insert the signature, and future signatures,
            # ordered as a footnote of the last page of the document
            return PadesVisualPositioningPresets.get_footnote(self.restpki_client())
        elif sample_number == 2:
            # Example #2: get the footnote positioning preset and customize it
            visual_position = PadesVisualPositioningPresets.get_footnote(self.restpki_client())
            visual_position['auto']['container']['left'] = 2.54
            visual_position['auto']['container']['bottom'] = 2.54
            visual_position['auto']['container']['right'] = 2.54
            return visual_position
        elif sample_number == 3:
            # Example #3: automatic positioning on new page. This will insert the signature, and future signatures,
            # in a new page appended to the end of the document.
            return PadesVisualPositioningPresets.get_new_page(self.restpki_client())
        elif sample_number == 4:
            # Example #4: get the "new page" positioning preset and customize it
            visual_position = PadesVisualPositioningPresets.get_new_page(self.restpki_client())
            visual_position['auto']['container']['left'] = 2.54
            visual_position['auto']['container']['top'] = 2.54
            visual_position['auto']['container']['right'] = 2.54
            visual_position['auto']['signatureRectangleSize']['width'] = 5
            visual_position['auto']['signatureRectangleSize']['height'] = 3
            return visual_position
        elif sample_number == 5:
            # Example #5: manual positioning
            return {
                'pageNumber': 0,
                # zero means the signature will be placed on a new page appended to the end of the document
                'measurementUnits': 'Centimeters',
                # define a manual position of 5cm x 3cm, positioned at 1 inch from the left and bottom margins
                'manual': {
                    'left': 2.54,
                    'bottom': 2.54,
                    'width': 5,
                    'height': 3
                }
            }
        elif sample_number == 6:
            # Example #6: custom auto positioning
            return {
                'pageNumber': -1,
                # negative values represent pages counted from the end of the document (-1 is last page)
                'measurementUnits': 'Centimeters',
                'auto': {
                    # Specification of the container where the signatures will be placed, one after the other
                    'container': {
                        # Specifying left and right (but no width) results in a variable-width container with the given
                        # margins
                        'left': 2.54,
                        'right': 2.54,
                        # Specifying bottom and height (but no top) results in a bottom-aligned fixed-height container
                        'bottom': 2.54,
                        'height': 12.31
                    },
                    # Specification of the size of each signature rectangle
                    'signatureRectangleSize': {
                        'width': 5,
                        'height': 3
                    },
                    # The signatures will be placed in the container side by side. If there's no room left, the
                    # signatures will "wrap" to the next row. The value below specifies the vertical distance between
                    # rows
                    'rowSpacing': 1
                }
            }
        else:
            return None

InitializeClass(SAPLTool)

