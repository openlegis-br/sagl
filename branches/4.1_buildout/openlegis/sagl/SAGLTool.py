# -*- coding: utf-8 -*-

import re
import os
import requests

import time

import hashlib
import pickle
from binascii import b2a_base64
from random import randrange

from lxml.builder import ElementMaker
from lxml import etree

from datetime import datetime
from DateTime import DateTime

from App.special_dtml import DTMLFile
from AccessControl.class_init import InitializeClass
from OFS.SimpleItem import SimpleItem

from Products.CMFCore.ActionProviderBase import ActionProviderBase
from Products.CMFCore.utils import UniqueObject

from zope.interface import Interface

from Products.CMFCore.utils import getToolByName

from PIL import Image

#imports para a geracao dos documentos
try:
    import urllib #py2
except ImportError:
    import urllib.request as urllib #py3
try:
    import urllib2 #py2
except ImportError:
    import urllib3 #py3
try:
    import StringIO #py2
except ImportError:
    from io import StringIO #py3
import cStringIO #py2
import uuid
from appy.pod.renderer import Renderer
from PyPDF4 import PdfFileWriter, PdfFileReader, PdfFileMerger
from PyPDF4.utils import PdfReadError
from pdfrw import PdfReader, PdfWriter, PageMerge
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128, qr
from reportlab.graphics.shapes import Drawing 
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.utils import ImageReader

#imports para assinatura digital
import sys
import six
import base64
from base64 import b64encode
from zlib import crc32
import simplejson as json

from restpki import *
from zope.testbrowser.browser import Browser
browser = Browser()

## Troca de senha
from AccessControl.SecurityInfo import ClassSecurityInfo

security = ClassSecurityInfo()

from AccessControl import Permissions
from AccessControl.Permission import addPermission
from AccessControl.SecurityInfo import ModuleSecurityInfo
from zope.deferredimport import deprecated
from zope.component import getUtility

security2 = ModuleSecurityInfo('Products.CMFCore.permissions')

security2.declarePublic('mailPassword')
mailPassword = 'Mail forgotten password'
addPermission(mailPassword, ('Anonymous', 'Manager',))

from Acquisition import aq_base


class ISAGLTool(Interface):
    """ Marker interface for SAGL Tool.
    """
    pass

class SAGLTool(UniqueObject, SimpleItem, ActionProviderBase):

    __implements__ = (ISAGLTool)

    id = 'portal_sagl'
    meta_type = 'SAGL Tool'

    XSI_NS = 'http://www.w3.org/2001/XMLSchema-instance'
    ns = {'lexml': 'http://www.lexml.gov.br/oai_lexml'}
    schema = {'oai_lexml': 'http://projeto.lexml.gov.br/esquemas/oai_lexml.xsd'}

    def verifica_esfera_federacao(self):
        ''' Funcao para verificar a esfera da federacao
        '''
        nome_camara = self.sapl_documentos.props_sagl.nom_casa
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

            end_web_casa = self.sapl_documentos.props_sagl.end_web_casa
            sgl_casa = self.sapl_documentos.props_sagl.sgl_casa.lower()
            num = len(end_web_casa.split('.'))
            dominio = '.'.join(end_web_casa.split('.')[1:num])

            prefixo_oai = '%s.%s:sagl/' % (sgl_casa,dominio)
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

            localidade = self.zsql.localidade_obter_zsql(cod_localidade = self.sapl_documentos.props_sagl.cod_localidade)
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
            localidade = self.zsql.localidade_obter_zsql(cod_localidade = self.sapl_documentos.props_sagl.cod_localidade)[0].nom_localidade
            sigla_uf = self.zsql.localidade_obter_zsql(cod_localidade = self.sapl_documentos.props_sagl.cod_localidade)[0].sgl_uf
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

    def resize_and_crop(self,cod_parlamentar):
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        image_file = '%s' % (cod_parlamentar) + "_foto_parlamentar"
        url = self.url() + '/sapl_documentos/parlamentar/fotos/' + image_file
        opener = urllib.urlopen(url)
        img_path = open('/tmp/' + image_file, 'wb').write(opener.read())
        foto_parlamentar = str(cod_parlamentar) + "_foto_parlamentar.jpg"
        modified_path = '/tmp/' + str(cod_parlamentar) + "_foto_parlamentar.jpg"
        crop_type='top'
        size = (350, 380)
        img = Image.open('/tmp/' + image_file)
        img = img.convert('RGB')
        img_ratio = img.size[0] / float(img.size[1])
        ratio = size[0] / float(size[1])
        if ratio > img_ratio:
            img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))),
                Image.ANTIALIAS)
            if crop_type == 'top':
                box = (0, 0, img.size[0], size[1])
            elif crop_type == 'middle':
                box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0],
                    int(round((img.size[1] + size[1]) / 2)))
            elif crop_type == 'bottom':
                box = (0, img.size[1] - size[1], img.size[0], img.size[1])
            else :
                raise ValueError('ERROR: invalid value for crop_type')
            img = img.crop(box)
        elif ratio < img_ratio:
            img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]),
                Image.ANTIALIAS)
            if crop_type == 'top':
                box = (0, 0, size[0], img.size[1])
            elif crop_type == 'middle':
                box = (int(round((img.size[0] - size[0]) / 2)), 0,
                    int(round((img.size[0] + size[0]) / 2)), img.size[1])
            elif crop_type == 'bottom':
                box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
            else :
                raise ValueError('ERROR: invalid value for crop_type')
            img = img.crop(box)
        else :
            img = img.resize((size[0], size[1]),
                Image.ANTIALIAS)

        img.save(modified_path)
        data = open(modified_path, "rb").read()
        foto = getattr(self.sapl_documentos.parlamentar.fotos,image_file)
        foto.manage_upload(file=data)
        os.unlink('/tmp/'+image_file)
        os.unlink('/tmp/'+foto_parlamentar)

    def get_brasao(self):
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sagl.id_logo
        if hasattr(self.sapl_documentos.props_sagl, id_logo):
           url = self.url() + '/sapl_documentos/props_sagl/' + id_logo
        else:
           url = self.url() + '/imagens/brasao.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        brasao = open('/tmp/' + id_logo, 'rb')
        os.unlink('/tmp/' + id_logo)
        return brasao

    def ata_gerar_odt(self, ata_dic, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/ata.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.ata_sessao.manage_addFile(id=output_file_odt,file=data)

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

    def ata_comissao_gerar_odt(self, ata_dic, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/ata_comissao.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.reuniao_comissao.manage_addFile(id=output_file_odt,file=data)

    def ata_comissao_gerar_pdf(self, cod_reuniao):
        nom_arquivo_odt = "%s"%cod_reuniao+'_ata.odt'
        nom_arquivo_pdf = "%s"%cod_reuniao+'_ata.pdf'
        url = self.sapl_documentos.reuniao_comissao.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.reuniao_comissao.manage_addFile(id=nom_arquivo_pdf,file=data)


    def iom_gerar_odt(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/iom.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'        
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
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
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
            if nom_arquivo_pdf in self.sapl_documentos.pauta_sessao:
              documento = getattr(self.sapl_documentos.pauta_sessao,nom_arquivo_pdf)
              documento.manage_upload(file=data)
            else:
              self.sapl_documentos.pauta_sessao.manage_addFile(id=nom_arquivo_pdf,file=data)
            os.unlink(file)

    def pdf_completo(self, cod_sessao_plen):
        writer = PdfWriter()
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        for pauta in self.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen):
          nom_arquivo_pdf = "%s"%cod_sessao_plen+'_pauta_completa.pdf'
          nom_pdf_amigavel = str(pauta.num_sessao_plen)+'-sessao-'+ str(pauta.dat_inicio)+'-pauta_completa.pdf'
          nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
          if hasattr(self.sapl_documentos.pauta_sessao, str(cod_sessao_plen) + '_pauta_sessao.pdf'):
             arq = getattr(self.sapl_documentos.pauta_sessao, str(cod_sessao_plen) + '_pauta_sessao.pdf')
             arquivo = cStringIO.StringIO(str(arq.data))
             texto_pauta = PdfReader(arquivo, decompress=False).pages
             writer.addpages(texto_pauta)
          lst_materia = []
          for materia in self.zsql.ordem_dia_obter_zsql(cod_sessao_plen=pauta.cod_sessao_plen,ind_excluido=0):
              if materia.cod_materia != None and materia.cod_materia != '':
                 cod_materia = int(materia.cod_materia)
                 lst_materia.append(cod_materia)
          lst_materia = [i for n, i in enumerate(lst_materia) if i not in lst_materia[n + 1:]]
          for cod_materia in lst_materia:
              if hasattr(self.sapl_documentos.materia, str(cod_materia) + '_redacao_final.pdf'):
                 arq = getattr(self.sapl_documentos.materia, str(cod_materia) + '_redacao_final.pdf')
                 arquivo = cStringIO.StringIO(str(arq.data))
                 texto_redacao = PdfReader(arquivo, decompress=False).pages
                 writer.addpages(texto_redacao)
              elif hasattr(self.sapl_documentos.materia, str(cod_materia) + '_texto_integral.pdf'):
                   arq = getattr(self.sapl_documentos.materia, str(cod_materia) + '_texto_integral.pdf')
                   arquivo = cStringIO.StringIO(str(arq.data))
                   texto_materia = PdfReader(arquivo, decompress=False).pages
                   writer.addpages(texto_materia)
                   for anexada in self.zsql.anexada_obter_zsql(cod_materia_principal=cod_materia,ind_excluido=0):
                       anexada = anexada.cod_materia_anexada
                       if hasattr(self.sapl_documentos.materia, str(anexada) + '_texto_integral.pdf'):
                          arq = getattr(self.sapl_documentos.materia, str(anexada) + '_texto_integral.pdf')
                          arquivo = cStringIO.StringIO(str(arq.data))
                          texto_anexada = PdfReader(arquivo, decompress=False).pages
                          writer.addpages(texto_anexada)
                   for subst in self.zsql.substitutivo_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
                       substitutivo = subst.cod_substitutivo
                       if hasattr(self.sapl_documentos.substitutivo, str(substitutivo) + '_substitutivo.pdf'):
                          arq = getattr(self.sapl_documentos.substitutivo, str(substitutivo) + '_substitutivo.pdf')
                          arquivo = cStringIO.StringIO(str(arq.data))
                          texto_substitutivo = PdfReader(arquivo, decompress=False).pages
                          writer.addpages(texto_substitutivo)
                   for eme in self.zsql.emenda_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
                       emenda = eme.cod_emenda
                       if hasattr(self.sapl_documentos.emenda, str(emenda) + '_emenda.pdf'):
                          arq = getattr(self.sapl_documentos.emenda, str(emenda) + '_emenda.pdf')
                          arquivo = cStringIO.StringIO(str(arq.data))
                          texto_emenda = PdfReader(arquivo, decompress=False).pages
                          writer.addpages(texto_emenda)
                   for relat in self.zsql.relatoria_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
                       relatoria = relat.cod_relatoria
                       if hasattr(self.sapl_documentos.parecer_comissao, str(relatoria) + '_parecer.pdf'):
                          arq = getattr(self.sapl_documentos.parecer_comissao, str(relatoria) + '_parecer.pdf')
                          arquivo = cStringIO.StringIO(str(arq.data))
                          texto_parecer = PdfReader(arquivo, decompress=False).pages
                          writer.addpages(texto_parecer)
          output_file_pdf = cStringIO.StringIO()
          writer.write(output_file_pdf)
          output_file_pdf.seek(0)
          existing_pdf = PdfFileReader(output_file_pdf, strict=False)
          numPages = existing_pdf.getNumPages()
          # cria novo PDF
          packet = cStringIO.StringIO()
          can = canvas.Canvas(packet)
          for page_num, i in enumerate(range(numPages), start=1):
              page = existing_pdf.getPage(i)
              pwidth = self.getPageSizeW(page)
              pheight = self.getPageSizeH(page)
              can.setPageSize((pwidth, pheight))
              can.setFillColorRGB(0,0,0)
              # Numero de pagina
              num_pagina = "fls. %s/%s" % (page_num, numPages)
              can.saveState()
              can.setFont('Arial', 9)
              can.drawCentredString(pwidth-45, pheight-60, num_pagina)
              can.restoreState()
              can.showPage()
          can.save()
          packet.seek(0)
          new_pdf = PdfFileReader(packet)
          # Mescla arquivos
          output = PdfFileWriter()
          for page in range(existing_pdf.getNumPages()):
              pdf_page = existing_pdf.getPage(page)
              # numeração de páginas
              for wm in range(new_pdf.getNumPages()):
                  watermark_page = new_pdf.getPage(wm)
                  if page == wm:
                     pdf_page.mergePage(watermark_page)
              output.addPage(pdf_page)
          outputStream = cStringIO.StringIO()
          self.temp_folder.manage_addFile(nom_arquivo_pdf)
          output.write(outputStream)
          arq=self.temp_folder[nom_arquivo_pdf]
          arq.manage_edit(title=nom_pdf_amigavel,filedata=outputStream.getvalue(),content_type='application/pdf')
          tmp_copy = self.temp_folder.manage_copyObjects(ids=nom_arquivo_pdf)
          if nom_arquivo_pdf in self.sapl_documentos.pauta_sessao:
             self.sapl_documentos.pauta_sessao.manage_delObjects(nom_arquivo_pdf)
          tmp_id = self.sapl_documentos.pauta_sessao.manage_pasteObjects(tmp_copy)[0]['new_id']
          arq = getattr(self.temp_folder,nom_arquivo_pdf)
          self.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
          self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)
          self.temp_folder.manage_delObjects(nom_arquivo_pdf)
          return arq

    def pdf_expediente_completo(self, cod_sessao_plen):
        writer = PdfWriter()
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        for pauta in self.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen):
          nom_pdf_amigavel = str(pauta.num_sessao_plen)+'-sessao-'+ str(pauta.dat_inicio)+'-expediente_completo.pdf'
          nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
          if hasattr(self.sapl_documentos.pauta_sessao, str(cod_sessao_plen) + '_pauta_expediente.pdf'):
             arq = getattr(self.sapl_documentos.pauta_sessao, str(cod_sessao_plen) + '_pauta_expediente.pdf')
             arquivo = cStringIO.StringIO(str(arq.data))
             texto_pauta = PdfReader(arquivo, decompress=False).pages
             writer.addpages(texto_pauta)
          for item in self.zsql.materia_apresentada_sessao_obter_zsql(cod_sessao_plen = pauta.cod_sessao_plen, ind_excluido = 0):
              if item.cod_materia != None:
                 if hasattr(self.sapl_documentos.materia, str(item.cod_materia) + '_texto_integral.pdf'):
                    arq = getattr(self.sapl_documentos.materia, str(item.cod_materia) + '_texto_integral.pdf')
                    arquivo = cStringIO.StringIO(str(arq.data))
                    texto_materia = PdfReader(arquivo, decompress=False).pages
                    writer.addpages(texto_materia)
              elif item.cod_emenda != None:
                   if hasattr(self.sapl_documentos.emenda, str(item.cod_emenda) + '_emenda.pdf'):
                      arq = getattr(self.sapl_documentos.emenda, str(item.cod_emenda) + '_emenda.pdf')
                      arquivo = cStringIO.StringIO(str(arq.data))
                      texto_emenda = PdfReader(arquivo, decompress=False).pages
                      writer.addpages(texto_emenda)
              elif item.cod_substitutivo != None:
                   if hasattr(self.sapl_documentos.substitutivo, str(item.cod_substitutivo) + '_substitutivo.pdf'):
                      arq = getattr(self.sapl_documentos.substitutivo, str(item.cod_substitutivo) + '_substitutivo.pdf')
                      arquivo = cStringIO.StringIO(str(arq.data))
                      texto_substitutivo = PdfReader(arquivo, decompress=False).pages
                      writer.addpages(texto_substitutivo)
              elif item.cod_parecer != None:
                   if hasattr(self.sapl_documentos.parecer_comissao, str(item.cod_parecer) + '_parecer.pdf'):
                      arq = getattr(self.sapl_documentos.parecer_comissao, str(item.cod_parecer) + '_parecer.pdf')
                      arquivo = cStringIO.StringIO(str(arq.data))
                      texto_parecer = PdfReader(arquivo, decompress=False).pages
                      writer.addpages(texto_parecer)
              elif item.cod_documento != None:
                   if hasattr(self.sapl_documentos.administrativo, str(item.cod_documento) + '_texto_integral.pdf'):
                      arq = getattr(self.sapl_documentos.administrativo, str(item.cod_documento) + '_texto_integral.pdf')
                      arquivo = cStringIO.StringIO(str(arq.data))
                      texto_documento = PdfReader(arquivo, decompress=False).pages
                      writer.addpages(texto_documento)
          for item in self.zsql.expediente_materia_obter_zsql(cod_sessao_plen = pauta.cod_sessao_plen, ind_excluido = 0):
              if item.cod_materia != None:
                 if hasattr(self.sapl_documentos.materia, str(item.cod_materia) + '_texto_integral.pdf'):
                    arq = getattr(self.sapl_documentos.materia, str(item.cod_materia) + '_texto_integral.pdf')
                    arquivo = cStringIO.StringIO(str(arq.data))
                    texto_materia = PdfReader(arquivo, decompress=False).pages
                    writer.addpages(texto_materia)
              elif item.cod_parecer != None:
                   if hasattr(self.sapl_documentos.parecer_comissao, str(item.cod_parecer) + '_parecer.pdf'):
                      arq = getattr(self.sapl_documentos.parecer_comissao, str(item.cod_parecer) + '_parecer.pdf')
                      arquivo = cStringIO.StringIO(str(arq.data))
                      texto_parecer = PdfReader(arquivo, decompress=False).pages
                      writer.addpages(texto_parecer)
          output_file_pdf = cStringIO.StringIO()
          writer.write(output_file_pdf)
          output_file_pdf.seek(0)
          existing_pdf = PdfFileReader(output_file_pdf, strict=False)
          numPages = existing_pdf.getNumPages()
          # cria novo PDF
          packet = cStringIO.StringIO()
          can = canvas.Canvas(packet)
          for page_num, i in enumerate(range(numPages), start=1):
              page = existing_pdf.getPage(i)
              pwidth = self.getPageSizeW(page)
              pheight = self.getPageSizeH(page)
              can.setPageSize((pwidth, pheight))
              can.setFillColorRGB(0,0,0)
              # Numero de pagina
              num_pagina = "fls. %s/%s" % (page_num, numPages)
              can.saveState()
              can.setFont('Arial', 9)
              can.drawCentredString(pwidth-45, pheight-60, num_pagina)
              can.restoreState()
              can.showPage()
          can.save()
          packet.seek(0)
          new_pdf = PdfFileReader(packet)
          # Mescla arquivos
          output = PdfFileWriter()
          for page in range(existing_pdf.getNumPages()):
              pdf_page = existing_pdf.getPage(page)
              # numeração de páginas
              for wm in range(new_pdf.getNumPages()):
                  watermark_page = new_pdf.getPage(wm)
                  if page == wm:
                     pdf_page.mergePage(watermark_page)
              output.addPage(pdf_page)
          outputStream = cStringIO.StringIO()
          self.temp_folder.manage_addFile(nom_pdf_amigavel)
          output.write(outputStream)
          arq=self.temp_folder[nom_pdf_amigavel]
          arq.manage_edit(title=nom_pdf_amigavel,filedata=outputStream.getvalue(),content_type='application/pdf')
          arq = getattr(self.temp_folder,nom_pdf_amigavel)
          self.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
          self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)
          self.temp_folder.manage_delObjects(nom_pdf_amigavel)
          return arq

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

    def resumo_gerar_odt(self, resumo_dic, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/resumo.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def resumo_tramitacao_gerar_odt(self, inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_proposicao, des_tipo_materia, nom_autor, txt_ementa, regime_tramitacao, nom_arquivo):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/resumo-tramitacao.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
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

    def oficio_req_gerar_odt(self, inf_basicas_dic, lst_requerimento, lst_presidente):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/oficio_requerimento.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "oficio_requerimento.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def emenda_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.emenda.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
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

    def capa_processo_gerar_odt(self, capa_dic):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/capa_processo.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % capa_dic['nom_arquivo_odt']
        output_file_pdf = "%s" % capa_dic['nom_arquivo_pdf']
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        odtFile = cStringIO.StringIO(data)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        self.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
        self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %output_file_pdf)
        for file in [output_file_odt]:
            os.unlink(file)
        for file in [output_file_pdf]:
            os.unlink(file)
        return data

    def capa_processo_adm_gerar_odt(self, capa_dic):
        url = self.sapl_documentos.modelo.documento_administrativo.absolute_url() + "/capa_processo_adm.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % capa_dic['nom_arquivo_odt']
        output_file_pdf = "%s" % capa_dic['nom_arquivo_pdf']
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        odtFile = cStringIO.StringIO(data)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        self.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
        self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %output_file_pdf)
        for file in [output_file_odt]:
            os.unlink(file)
        for file in [output_file_pdf]:
            os.unlink(file)
        return data

    def materia_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
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

    def materias_expediente_gerar_ods(self, relatorio_dic, total_assuntos, parlamentares, nom_arquivo):
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/relatorio-expediente.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

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
        exec 'brasao = brasao_file'
        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.norma_juridica.manage_addFile(id=nom_arquivo,file=data)

    def norma_gerar_pdf(self, cod_norma, tipo_texto):
        nom_arquivo_odt = "%s"%cod_norma+'_texto_integral.odt'
        if tipo_texto == 'compilado':
           nom_arquivo_pdf1 = "%s"%cod_norma+'_texto_consolidado.pdf'
        elif tipo_texto == 'integral':
           nom_arquivo_pdf1 = "%s"%cod_norma+'_texto_integral.pdf'
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
        arquivo = getattr(self.sapl_documentos.administrativo, nom_arquivo_odt)
        odtFile = cStringIO.StringIO(str(arquivo.data))
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.administrativo.manage_addFile(id=nom_arquivo_pdf1, file=data)

    def tramitacao_documento_juntar(self,cod_tramitacao):
        merger = PdfWriter()
        arquivoPdf=str(cod_tramitacao)+"_tram.pdf"
        arquivoPdfAnexo=str(cod_tramitacao)+"_tram_anexo1.pdf"
        arquivoFinal=str(cod_tramitacao)+".pdf"
        if hasattr(self.sapl_documentos.administrativo.tramitacao,arquivoPdf):
           arq = getattr(self.sapl_documentos.administrativo.tramitacao, arquivoPdf)
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_tram = PdfReader(arquivo, decompress=False).pages
           merger.addpages(texto_tram)
        if hasattr(self.sapl_documentos.administrativo.tramitacao,arquivoPdfAnexo):
           arq = getattr(self.sapl_documentos.administrativo.tramitacao, arquivoPdfAnexo)
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_anexo = PdfReader(arquivo, decompress=False).pages
           merger.addpages(texto_anexo)
           self.sapl_documentos.administrativo.tramitacao.manage_delObjects(arquivoPdfAnexo)
        outputStream = cStringIO.StringIO()
        self.temp_folder.manage_addFile(arquivoPdf)
        merger.write(outputStream)
        arq=self.temp_folder[arquivoPdf]
        arq.manage_edit(title=arquivoPdf,filedata=outputStream.getvalue(),content_type='application/pdf')
        tmp_copy = self.temp_folder.manage_copyObjects(ids=arquivoPdf)
        if arquivoPdf in self.sapl_documentos.administrativo.tramitacao:
           self.sapl_documentos.administrativo.tramitacao.manage_delObjects(arquivoPdf)
           tmp_id = self.sapl_documentos.administrativo.tramitacao.manage_pasteObjects(tmp_copy)[0]['new_id']
           self.sapl_documentos.administrativo.tramitacao.manage_renameObjects(ids=list([tmp_id]), new_ids=list([arquivoPdf]))
        self.temp_folder.manage_delObjects(arquivoPdf)

    def tramitacao_materia_juntar(self,cod_tramitacao):
        merger = PdfWriter()
        arquivoPdf=str(cod_tramitacao)+"_tram.pdf"
        arquivoPdfAnexo=str(cod_tramitacao)+"_tram_anexo1.pdf"
        arquivoFinal=str(cod_tramitacao)+".pdf"
        if hasattr(self.sapl_documentos.materia.tramitacao,arquivoPdf):
           arq = getattr(self.sapl_documentos.materia.tramitacao, arquivoPdf)
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_tram = PdfReader(arquivo, decompress=False).pages
           merger.addpages(texto_tram)
        if hasattr(self.sapl_documentos.materia.tramitacao,arquivoPdfAnexo):
           arq = getattr(self.sapl_documentos.materia.tramitacao, arquivoPdfAnexo)
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_anexo = PdfReader(arquivo, decompress=False).pages
           merger.addpages(texto_anexo)
           self.sapl_documentos.materia.tramitacao.manage_delObjects(arquivoPdfAnexo)
        outputStream = cStringIO.StringIO()
        self.temp_folder.manage_addFile(arquivoPdf)
        merger.write(outputStream)
        arq=self.temp_folder[arquivoPdf]
        arq.manage_edit(title=arquivoPdf,filedata=outputStream.getvalue(),content_type='application/pdf')
        tmp_copy = self.temp_folder.manage_copyObjects(ids=arquivoPdf)
        if arquivoPdf in self.sapl_documentos.materia.tramitacao:
           self.sapl_documentos.materia.tramitacao.manage_delObjects(arquivoPdf)
           tmp_id = self.sapl_documentos.materia.tramitacao.manage_pasteObjects(tmp_copy)[0]['new_id']
           self.sapl_documentos.materia.tramitacao.manage_renameObjects(ids=list([tmp_id]),new_ids=list([arquivoPdf]))
        self.temp_folder.manage_delObjects(arquivoPdf)

    def documento_assinado_imprimir(self,cod_documento):
        nom_pdf_documento = str(cod_documento) + "_texto_integral_signed.pdf"
        for documento in self.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
          string = self.pysc.b64encode_pysc(codigo=str(documento.cod_documento))
          num_documento = documento.num_documento
          nom_autor = documento.txt_interessado
          for tipo_documento in self.zsql.tipo_documento_administrativo_obter_zsql(tip_documento=documento.tip_documento):
            texto = str(tipo_documento.des_tipo_documento.decode('utf-8').upper())+' Nº '+ str(documento.num_documento)+'/'+str(documento.ano_documento)
            nom_pdf_amigavel = str(tipo_documento.sgl_tipo_documento)+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+".pdf"
        mensagem1 = texto + ' - Esta é uma cópia do original assinado digitalmente por '+nom_autor+'.'
        mensagem2 = 'Para validar o documento, leia o código QR ou acesse ' + self.url()+'/conferir_assinatura'+' e informe o código '+ string + '.'
        mensagem = mensagem1 + '\n' + mensagem2
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        validacao = ''
        arq = getattr(self.sapl_documentos.administrativo, nom_pdf_documento)
        arquivo = cStringIO.StringIO(str(arq.data))
        existing_pdf = PdfFileReader(arquivo, strict=False)
        numPages = existing_pdf.getNumPages()
        # cria novo PDF
        packet = StringIO.StringIO()
        can = canvas.Canvas(packet)
        for page_num, i in enumerate(range(numPages), start=1):
            page = existing_pdf.getPage(i)
            pwidth = self.getPageSizeW(page)
            pheight = self.getPageSizeH(page)
            can.setPageSize((pwidth, pheight))
            can.setFillColorRGB(0,0,0) 
            # QRCode
            qr_code = qr.QrCodeWidget(self.url()+'/conferir_assinatura_proc?txt_codigo_verificacao='+str(string))
            bounds = qr_code.getBounds()
            width = bounds[2] - bounds[0]
            height = bounds[3] - bounds[1]
            d = Drawing(55, 55, transform=[55./width,0,0,55./height,0,0])
            d.add(qr_code)
            x = 59
            renderPDF.draw(d, can,  pwidth-59, 13)
            # Margem direita
            d = Drawing(10, 5)
            lab = Label()
            lab.setOrigin(0,250)
            lab.angle = 90
            lab.fontName = 'Arial'
            lab.fontSize = 7
            lab.textAnchor = 'start'
            lab.boxAnchor = 'n'
            lab.setText(mensagem)
            d.add(lab)
            renderPDF.draw(d, can, pwidth-24, 160)
            # Numero de pagina
            footer_text = "Pag. %s/%s" % (page_num, numPages)
            can.saveState()
            can.setFont('Arial', 8)
            can.drawCentredString(pwidth-30, 10, footer_text)
            can.restoreState()
            can.showPage()
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # Mescla arquivos
        output = PdfFileWriter()
        for page in range(existing_pdf.getNumPages()):
            pdf_page = existing_pdf.getPage(page)
            # qrcode e margem direita em todas as páginas
            for wm in range(new_pdf.getNumPages()):
                watermark_page = new_pdf.getPage(wm)
                if page == wm:
                   pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = cStringIO.StringIO()
        self.temp_folder.manage_addFile(nom_pdf_amigavel)
        output.write(outputStream)
        arq=self.temp_folder[nom_pdf_amigavel]
        arq.manage_edit(title=nom_pdf_amigavel,filedata=outputStream.getvalue(),content_type='application/pdf')
        arq = getattr(self.temp_folder,nom_pdf_amigavel)
        self.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
        self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)
        self.temp_folder.manage_delObjects(nom_pdf_amigavel)
        return arq

    # obter altura da pagina
    def getPageSizeH(self, p):
        h = int(p.mediaBox.getHeight())
        return h

    # obter largura da pagina
    def getPageSizeW(self, p):
        w = int(p.mediaBox.getWidth())
        return w

    def parecer_gerar_odt(self, inf_basicas_dic, nom_arquivo, nom_comissao, materia_vinculada, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.parecer.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
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

    def peticao_gerar_odt(self, inf_basicas_dic, nom_arquivo, modelo_path):
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        modelo = portal.unrestrictedTraverse(modelo_path)
        template_file = cStringIO.StringIO(str(modelo.data))
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.peticao.manage_addFile(id=nom_arquivo,file=data)
        odt = getattr(self.sapl_documentos.peticao, nom_arquivo)
        odt.manage_permission('View', roles=['Manager','Owner'], acquire=0)

    def peticao_gerar_pdf(self, cod_peticao):
        nom_arquivo_odt = "%s"%cod_peticao+'.odt'
        nom_arquivo_pdf1 = "%s"%cod_peticao+'.pdf'
        arquivo = getattr(self.sapl_documentos.peticao, nom_arquivo_odt)
        odtFile = cStringIO.StringIO(str(arquivo.data))
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.peticao.manage_addFile(id=nom_arquivo_pdf1, file=data)
        pdf = getattr(self.sapl_documentos.peticao, nom_arquivo_pdf1)
        pdf.manage_permission('View', roles=['Manager','Authenticated'], acquire=0)


    def proposicao_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao, modelo_path):
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        if inf_basicas_dic['des_tipo_proposicao'] == 'Parecer' or inf_basicas_dic['des_tipo_proposicao'] == 'Parecer de Comissão':
           materia = inf_basicas_dic['id_materia']
           nom_comissao = inf_basicas_dic['nom_comissao']
           data_parecer = inf_basicas_dic['data_parecer']
           nom_relator = inf_basicas_dic['nom_relator']
           lst_composicao = []
        modelo = portal.unrestrictedTraverse(modelo_path)
        template_file = cStringIO.StringIO(str(modelo.data))
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.proposicao.manage_addFile(id=nom_arquivo,file=data)

    def proposicao_gerar_pdf(self, cod_proposicao):
        writer = PdfFileWriter()
        merger = PdfWriter()
        nom_arquivo_odt = "%s"%cod_proposicao+'.odt'
        nom_arquivo_pdf1 = "%s"%cod_proposicao+'.pdf'
        arquivo = getattr(self.sapl_documentos.proposicao, nom_arquivo_odt)
        odtFile = cStringIO.StringIO(str(arquivo.data))
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        texto_pdf = PdfReader(os.path.normpath(nom_arquivo_pdf1), decompress=False).pages
        merger.addpages(texto_pdf)
        os.unlink(output_file_pdf)

        lst_anexos = []
        for anexo in self.pysc.anexo_proposicao_pysc(cod_proposicao,listar=True):
            arq = getattr(self.sapl_documentos.proposicao, anexo)
            arquivo = cStringIO.StringIO(str(arq.data))
            texto_anexo = PdfReader(arquivo, decompress=False).pages
            merger.addpages(texto_anexo)

        final_output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        merger.write(final_output_file_pdf)
        readin = open(final_output_file_pdf, "r")
        contents = readin.read()
        for file in [final_output_file_pdf]:
            os.unlink(file)
            self.sapl_documentos.proposicao.manage_addFile(id=nom_arquivo_pdf1, file=contents)

    def substitutivo_gerar_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        url = self.sapl_documentos.modelo.materia.substitutivo.absolute_url() + "/%s"%modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.substitutivo.manage_addFile(id=nom_arquivo,file=data)

    def pessoas_exportar(self, pessoas):
        url = self.sapl_documentos.modelo.absolute_url() + "/planilha-visitantes.ods"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()
        exec 'brasao = brasao_file'
        output_file_ods = "contatos.ods"
        renderer = Renderer(template_file, locals(), output_file_ods, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_ods, "rb").read()
        for file in [output_file_ods]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'vnd.oasis.opendocument.spreadsheet'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_ods
        return data

    def eleitores_exportar(self, eleitores):
        url = self.sapl_documentos.modelo.absolute_url() + "/planilha-eleitores.ods"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_ods = "eleitores.ods"
        renderer = Renderer(template_file, locals(), output_file_ods, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_ods, "rb").read()
        for file in [output_file_ods]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'vnd.oasis.opendocument.spreadsheet'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_ods
        return data

    def materias_exportar(self, materias):
        url = self.sapl_documentos.modelo.absolute_url() + "/planilha-materias.ods"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_ods = "materias.ods"
        renderer = Renderer(template_file, locals(), output_file_ods, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_ods, "rb").read()
        for file in [output_file_ods]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'vnd.oasis.opendocument.spreadsheet'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_ods
        return data

    def normas_exportar(self, normas):
        url = self.sapl_documentos.modelo.absolute_url() + "/planilha-normas.ods"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_ods = "normas.ods"
        renderer = Renderer(template_file, locals(), output_file_ods, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
        renderer.run()
        data = open(output_file_ods, "rb").read()
        for file in [output_file_ods]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'vnd.oasis.opendocument.spreadsheet'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_ods
        return data

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
        sgl_casa = self.sapl_documentos.props_sagl.sgl_casa
        for protocolo in self.zsql.protocolo_obter_zsql(cod_protocolo=cod_protocolo):
          string = str(protocolo.cod_protocolo).zfill(7)
          texto = 'PROT-'+ str(sgl_casa) + ' ' + str(protocolo.num_protocolo)+'/'+str(protocolo.ano_protocolo)
          data = self.pysc.iso_to_port_pysc(protocolo.dat_protocolo)+' - '+protocolo.hor_protocolo[0:2] + ':' + protocolo.hor_protocolo[3:5]
          des_tipo_materia=""
          num_materia = ""
          materia_principal = ""
          if protocolo.tip_processo==1:
             if protocolo.tip_natureza_materia == 1:
                for materia in self.zsql.materia_obter_zsql(num_protocolo=protocolo.num_protocolo,ano_ident_basica=protocolo.ano_protocolo):
                    des_tipo_materia = materia.des_tipo_materia
                    num_materia=materia.sgl_tipo_materia+' '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
             elif protocolo.tip_natureza_materia == 2:
                  for materia in self.zsql.materia_obter_zsql(cod_materia=protocolo.cod_materia_principal):
                      materia_principal = ' - ' + materia.sgl_tipo_materia+' '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
                  for tipo in self.zsql.tipo_materia_legislativa_obter_zsql(tip_materia=protocolo.tip_materia,tip_natureza='A'):
                      if tipo.des_tipo_materia == 'Emenda':
                         for emenda in self.zsql.emenda_obter_zsql(num_protocolo=protocolo.num_protocolo, cod_materia=protocolo.cod_materia_principal):
                             num_materia = 'EME' + ' ' +str(emenda.num_emenda) + str(materia_principal)
                      elif tipo.des_tipo_materia == 'Substitutivo':
                           for substitutivo in self.zsql.substitutivo_obter_zsql(num_protocolo=protocolo.num_protocolo, cod_materia=protocolo.cod_materia_principal):
                               num_materia = 'SUB ' +str(substitutivo.num_substitutivo) + str(materia_principal)
             elif protocolo.tip_natureza_materia == 3:
                  for materia in self.zsql.materia_obter_zsql(cod_materia=protocolo.cod_materia_principal):
                      materia_principal = ' - ' + materia.sgl_tipo_materia+' '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
                  for documento in self.zsql.documento_acessorio_obter_zsql(num_protocolo=protocolo.num_protocolo, cod_materia=protocolo.cod_materia_principal):
                      num_materia = documento.des_tipo_documento + str(materia_principal)
             elif protocolo.tip_natureza_materia == 4:
                  for materia in self.zsql.materia_obter_zsql(cod_materia=protocolo.cod_materia_principal):
                      materia_principal = ' - ' + materia.sgl_tipo_materia+' '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
                  for autor in self.zsql.autor_obter_zsql(cod_autor=protocolo.cod_autor):
                      for comissao in self.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao):
                          sgl_comissao = comissao.sgl_comissao
                  for parecer in self.zsql.relatoria_obter_zsql(num_protocolo=protocolo.num_protocolo, cod_materia=protocolo.cod_materia_principal):
                      materia_principal = 'PAR ' + sgl_comissao +' ' + str(parecer.num_parecer)+'/'+str(parecer.ano_parecer) + str(materia_principal)
          elif protocolo.tip_processo==0:
               for documento in self.zsql.documento_administrativo_obter_zsql(num_protocolo=protocolo.num_protocolo, ano_documento=protocolo.ano_protocolo):
                   num_materia = documento.sgl_tipo_documento+' '+str(documento.num_documento)+'/'+str(documento.ano_documento)

        pdf_protocolo = self.sapl_documentos.protocolo.absolute_url() + "/" +  str(cod_protocolo) + "_protocolo.pdf"
        nom_pdf_protocolo = str(cod_protocolo) + "_protocolo.pdf"
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Courier_Bold', '/usr/share/fonts/truetype/msttcorefonts/Courier_New_Bold.ttf'))
        x_var=165
        y_var=288
        packet = os.path.normpath('temp.pdf')
        slab = canvas.Canvas(packet, pagesize=A4)
        slab.setFillColorRGB(0,0,0) 
        barcode = barcode128 = code128.Code128(string,barWidth=.34*mm,barHeight=6*mm)
        barcode.drawOn(slab, x_var*mm , y_var*mm)
        slab.setFont("Arial_Bold", 7)
        slab.drawString(485, 809, texto)
        slab.drawString(485, 802, data)
        slab.drawString(485, 795, num_materia)
        slab.save()
        barcode_pdf = open(packet, 'rb')
        new_pdf = PdfReader(barcode_pdf)
        pdf_file = '%s' % (cod_protocolo) + "_protocolo.pdf"
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        url = self.url() + '/sapl_documentos/protocolo/' + pdf_file
        opener = urllib.urlopen(url)
        f = open('/tmp/' + pdf_file, 'wb').write(opener.read())
        existing_pdf = PdfReader(file('/tmp/'+nom_pdf_protocolo, "rb"))
        barcode = PageMerge().add(new_pdf.pages[0])[0]
        for page in existing_pdf.pages:
          PageMerge(page).add(barcode).render()
        outputStream = '/tmp/' + nom_pdf_protocolo
        PdfWriter(outputStream, trailer=existing_pdf).write()
        data = open('/tmp/' + nom_pdf_protocolo, 'rb').read() 
        for item in [outputStream]:
          if nom_pdf_protocolo in self.sapl_documentos.protocolo:
            documento = getattr(self.sapl_documentos.protocolo,nom_pdf_protocolo)
            documento.manage_upload(file=data)
          else:
            self.sapl_documentos.protocolo.manage_addFile(id=nom_pdf_protocolo,file=data)
        os.unlink('/tmp/'+nom_pdf_protocolo)
        os.unlink(packet)

    def processo_adm_gerar_pdf(self, cod_documento):
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        writer = PdfFileWriter()
        merger = PdfFileMerger(strict=False)
        for documento in self.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
           nom_pdf_amigavel = documento.sgl_tipo_documento+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+'.pdf'
           id_processo = documento.sgl_tipo_documento+' '+str(documento.num_documento)+'/'+str(documento.ano_documento)
        nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        capa = cStringIO.StringIO(self.modelo_proposicao.capa_processo_adm(cod_documento=cod_documento))
        texto_capa = PdfFileReader(capa)
        merger.append(texto_capa)
        if hasattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf'):
           arq = getattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf')
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_documento = PdfFileReader(arquivo)
           merger.append(texto_documento)
        elif hasattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf'):
           arq = getattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf')
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_documento = PdfFileReader(arquivo)
           merger.append(texto_documento)
        anexos = []
        for docvinculado in self.zsql.documento_administrativo_vinculado_obter_zsql(cod_documento_vinculante=documento.cod_documento, ind_excluido=0):
           if hasattr(self.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf'):
              dic_anexo = {}
              dic_anexo["data"] = DateTime(docvinculado.dat_documento_vinculado, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
              if docvinculado.num_protocolo_vinculado != '' and docvinculado.num_protocolo_vinculado != None:
                 for protocolo in self.zsql.protocolo_obter_zsql(num_protocolo=docvinculado.num_protocolo_vinculado, ano_protocolo=docvinculado.ano_documento_vinculado):
                     dic_anexo["data"] = DateTime(protocolo.dat_timestamp, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
              dic_anexo["arquivo"] = getattr(self.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf')
              dic_anexo["id"] = getattr(self.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf').absolute_url()
              anexos.append(dic_anexo)
           elif hasattr(self.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf'):
              dic_anexo = {}
              dic_anexo["data"] = DateTime(docvinculado.dat_documento_vinculado, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
              if docvinculado.num_protocolo_vinculado != '' and docvinculado.num_protocolo_vinculado != None:
                 for protocolo in self.zsql.protocolo_obter_zsql(num_protocolo=docvinculado.num_protocolo_vinculado, ano_protocolo=docvinculado.ano_documento_vinculado):
                     dic_anexo["data"] = DateTime(protocolo.dat_timestamp, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
              dic_anexo["arquivo"] = getattr(self.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf')
              dic_anexo["id"] = getattr(self.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf').absolute_url()
              anexos.append(dic_anexo)
        for docadm in self.zsql.documento_acessorio_administrativo_obter_zsql(cod_documento=documento.cod_documento, ind_excluido=0):
           if hasattr(self.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf'):
              dic_anexo = {}
              dic_anexo["data"] = DateTime(docadm.dat_documento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
              dic_anexo["arquivo"] = getattr(self.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf')
              dic_anexo["id"] = getattr(self.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf').absolute_url()
              anexos.append(dic_anexo)
        for tram in self.zsql.tramitacao_administrativo_obter_zsql(cod_documento=documento.cod_documento, rd_ordem='1', ind_excluido=0):
            if hasattr(self.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf').absolute_url()
               anexos.append(dic_anexo)
            elif hasattr(self.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf').absolute_url()
               anexos.append(dic_anexo)
        anexos.sort(key=lambda dic: dic['data'])
        for dic in anexos:
            arquivo_doc = cStringIO.StringIO(str(dic['arquivo'].data))
            try:
               texto_anexo = PdfFileReader(arquivo_doc, strict=False)
            except:
               msg = msg = 'O arquivo "' + str(dic['id']) + '" não é um documento PDF válido.'
               raise ValueError(msg)
            else:
               merger.append(texto_anexo)
        output_file_pdf = cStringIO.StringIO()
        merger.write(output_file_pdf)
        merger.close()

        output_file_pdf.seek(0)
        existing_pdf = PdfFileReader(output_file_pdf, strict=False)
        numPages = existing_pdf.getNumPages()
        # cria novo PDF
        packet = cStringIO.StringIO()
        can = canvas.Canvas(packet)
        for page_num, i in enumerate(range(numPages), start=1):
            page = existing_pdf.getPage(i)
            pwidth = self.getPageSizeW(page)
            pheight = self.getPageSizeH(page)
            can.setPageSize((pwidth, pheight))
            can.setFillColorRGB(0,0,0)
            # Numero de pagina
            num_pagina = "fls. %s/%s" % (page_num, numPages)
            can.saveState()
            can.setFont('Arial', 9)
            can.drawCentredString(pwidth-45, pheight-60, id_processo)
            can.setFont('Arial_Bold', 9)
            can.drawCentredString(pwidth-45, pheight-72, num_pagina)
            can.restoreState()
            can.showPage()
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # Mescla arquivos
        output = PdfFileWriter()
        for page in range(existing_pdf.getNumPages()):
            pdf_page = existing_pdf.getPage(page)
            # numeração de páginas
            for wm in range(new_pdf.getNumPages()):
                watermark_page = new_pdf.getPage(wm)
                if page == wm:
                   pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = cStringIO.StringIO()
        self.temp_folder.manage_addFile(nom_pdf_amigavel)
        output.write(outputStream)
        arq=self.temp_folder[nom_pdf_amigavel]
        arq.manage_edit(title=nom_pdf_amigavel,filedata=outputStream.getvalue(),content_type='application/pdf')
        arq = getattr(self.temp_folder,nom_pdf_amigavel)
        self.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
        self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)
        self.temp_folder.manage_delObjects(nom_pdf_amigavel)
        return arq

    def processo_eletronico_gerar_pdf(self, cod_materia):
        utool = getToolByName(self, 'portal_url')
        writer = PdfFileWriter()
        merger = PdfFileMerger(strict=False)
        portal = utool.getPortalObject()
        if cod_materia.isdigit():
           cod_materia = cod_materia
        else:
           cod_materia = self.pysc.b64decode_pysc(codigo=str(cod_materia))
        for materia in self.zsql.materia_obter_zsql(cod_materia=cod_materia):
           nom_pdf_amigavel = materia.sgl_tipo_materia+'-'+str(materia.num_ident_basica)+'-'+str(materia.ano_ident_basica)+'.pdf'
           nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
           id_processo = materia.sgl_tipo_materia+' '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        capa = cStringIO.StringIO(self.modelo_proposicao.capa_processo(cod_materia=cod_materia))
        texto_capa = PdfFileReader(capa)
        merger.append(texto_capa)
        if hasattr(self.sapl_documentos.materia, str(cod_materia) + '_texto_integral.pdf'):
           arq = getattr(self.sapl_documentos.materia, str(cod_materia) + '_texto_integral.pdf')
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_materia = PdfFileReader(arquivo)
           merger.append(texto_materia)
        anexos = []
        for substitutivo in self.zsql.substitutivo_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
            if hasattr(self.sapl_documentos.substitutivo, str(substitutivo.cod_substitutivo) + '_substitutivo.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(substitutivo.dat_apresentacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.substitutivo, str(substitutivo.cod_substitutivo) + '_substitutivo.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.substitutivo, str(substitutivo.cod_substitutivo) + '_substitutivo.pdf').absolute_url()
               anexos.append(dic_anexo)
        for eme in self.zsql.emenda_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
            if hasattr(self.sapl_documentos.emenda, str(eme.cod_emenda) + '_emenda.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(eme.dat_apresentacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.emenda, str(eme.cod_emenda) + '_emenda.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.emenda, str(eme.cod_emenda) + '_emenda.pdf').absolute_url()
               anexos.append(dic_anexo)
        for relat in self.zsql.relatoria_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
            if hasattr(self.sapl_documentos.parecer_comissao, str(relat.cod_relatoria) + '_parecer.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(relat.dat_destit_relator, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               for proposicao in self.zsql.proposicao_obter_zsql(cod_parecer=relat.cod_relatoria):
                   dic_anexo["data"] = DateTime(proposicao.dat_recebimento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.parecer_comissao, str(relat.cod_relatoria) + '_parecer.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.parecer_comissao, str(relat.cod_relatoria) + '_parecer.pdf').absolute_url()
               anexos.append(dic_anexo)
        for anexada in self.zsql.anexada_obter_zsql(cod_materia_principal=cod_materia,ind_excluido=0):
            if hasattr(self.sapl_documentos.materia, str(anexada.cod_materia_anexada) + '_texto_integral.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(anexada.dat_anexacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.materia, str(anexada.cod_materia_anexada) + '_texto_integral.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.materia, str(anexada.cod_materia_anexada) + '_texto_integral.pdf').absolute_url()
               anexos.append(dic_anexo)
        for docadm in self.zsql.documento_administrativo_materia_obter_zsql(cod_materia=cod_materia, ind_excluido=0):
            if hasattr(self.sapl_documentos.administrativo, str(docadm.cod_documento) + '_texto_integral.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(docadm.data_documento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.administrativo, str(docadm.cod_documento) + '_texto_integral.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.administrativo, str(docadm.cod_documento) + '_texto_integral.pdf').absolute_url()
               anexos.append(dic_anexo)
        for documento in self.zsql.documento_acessorio_obter_zsql(cod_materia = cod_materia, ind_excluido=0):
            if hasattr(self.sapl_documentos.materia, str(documento.cod_documento) + '.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(documento.dat_documento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.materia, str(documento.cod_documento) + '.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.materia, str(documento.cod_documento) + '.pdf').absolute_url()
               anexos.append(dic_anexo)
        for tram in self.zsql.tramitacao_obter_zsql(cod_materia=cod_materia, rd_ordem='1', ind_excluido=0):
            if hasattr(self.sapl_documentos.materia.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.materia.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.materia.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf').absolute_url()
               anexos.append(dic_anexo)
            elif hasattr(self.sapl_documentos.materia.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.materia.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.materia.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf').absolute_url()
               anexos.append(dic_anexo)
        for norma in self.zsql.materia_buscar_norma_juridica_zsql(cod_materia = cod_materia):
            if hasattr(self.sapl_documentos.norma_juridica, str(norma.cod_norma) + '_texto_integral.pdf'):
               dic_anexo = {}
               dic_anexo["data"] = DateTime(norma.dat_norma, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
               dic_anexo["arquivo"] = getattr(self.sapl_documentos.norma_juridica, str(norma.cod_norma) + '_texto_integral.pdf')
               dic_anexo["id"] = getattr(self.sapl_documentos.norma_juridica, str(norma.cod_norma) + '_texto_integral.pdf').absolute_url()
               anexos.append(dic_anexo)
        anexos.sort(key=lambda dic: dic['data'])
        for dic in anexos:
            arquivo_doc = cStringIO.StringIO(str(dic['arquivo'].data))
            try:
               texto_anexo = PdfFileReader(arquivo_doc, strict=False)
            except:
               msg = 'O arquivo "' + str(dic['id']) + '" não é um documento PDF válido.'
               raise ValueError(msg)
            else:
               merger.append(texto_anexo)
        output_file_pdf = cStringIO.StringIO()
        merger.write(output_file_pdf)
        merger.close()

        output_file_pdf.seek(0)
        existing_pdf = PdfFileReader(output_file_pdf, strict=False)
        numPages = existing_pdf.getNumPages()
        # cria novo PDF
        packet = cStringIO.StringIO()
        can = canvas.Canvas(packet)
        for page_num, i in enumerate(range(numPages), start=1):
            page = existing_pdf.getPage(i)
            pwidth = self.getPageSizeW(page)
            pheight = self.getPageSizeH(page)
            can.setPageSize((pwidth, pheight))
            can.setFillColorRGB(0,0,0)
            # Numero de pagina
            num_pagina = "fls. %s/%s" % (page_num, numPages)
            can.saveState()
            can.setFont('Arial', 9)
            can.drawCentredString(pwidth-45, pheight-60, id_processo)
            can.setFont('Arial_Bold', 9)
            can.drawCentredString(pwidth-45, pheight-72, num_pagina)
            can.restoreState()
            can.showPage()
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # Mescla arquivos
        output = PdfFileWriter()
        for page in range(existing_pdf.getNumPages()):
            pdf_page = existing_pdf.getPage(page)
            # numeração de páginas
            for wm in range(new_pdf.getNumPages()):
                watermark_page = new_pdf.getPage(wm)
                if page == wm:
                   pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = cStringIO.StringIO()
        self.temp_folder.manage_addFile(nom_pdf_amigavel)
        output.write(outputStream)
        arq=self.temp_folder[nom_pdf_amigavel]
        arq.manage_edit(title=nom_pdf_amigavel,filedata=outputStream.getvalue(),content_type='application/pdf')
        arq = getattr(self.temp_folder,nom_pdf_amigavel)
        self.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
        self.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)
        self.temp_folder.manage_delObjects(nom_pdf_amigavel)
        return arq

    def proposicao_autuar(self,cod_proposicao):
        nom_pdf_proposicao = str(cod_proposicao) + "_signed.pdf"
        pdf_proposicao = self.sapl_documentos.proposicao.absolute_url() + "/" +  nom_pdf_proposicao
        for proposicao in self.zsql.proposicao_obter_zsql(cod_proposicao=cod_proposicao):
          num_proposicao = proposicao.cod_proposicao
          nom_autor = proposicao.nom_autor
          cod_validacao_doc = ''
          outros = ''
          qtde_assinaturas = []
          for validacao in self.zsql.assinatura_documento_obter_zsql(codigo=cod_proposicao,tipo_doc='proposicao',ind_assinado=1):
            qtde_assinaturas.append(validacao.cod_usuario)
            if validacao.ind_prim_assinatura == 1:
               nom_autor = validacao.nom_completo
            cod_validacao_doc = str(self.cadastros.assinatura.format_verification_code(code=validacao.cod_assinatura_doc))
          if len(qtde_assinaturas) == 2:
             outros = " e outro"
          elif len(qtde_assinaturas) > 2:
             outros = " e outros"
          info_protocolo = '- Recebido em ' + proposicao.dat_recebimento + ' - '
          tipo_proposicao = proposicao.des_tipo_proposicao
          nome_autor = ''
          #if tipo_proposicao != 'Indicação' and tipo_proposicao !='Moção'  and tipo_proposicao != 'Requerimento' and tipo_proposicao != 'Requerimento ao Plenário' and tipo_proposicao != 'Requerimento à Presidência' and tipo_proposicao != 'Mensagem Aditiva':
          #    nome_autor = '(' + nom_autor + ')'
          if proposicao.ind_mat_ou_doc == "M":
            for materia in self.zsql.materia_obter_zsql(cod_materia=proposicao.cod_mat_ou_doc):
              if materia.num_protocolo != None and materia.num_protocolo != '':
                 for protocolo in self.zsql.protocolo_obter_zsql(num_protocolo=materia.num_protocolo, ano_protocolo=materia.ano_ident_basica):
                     info_protocolo = ' - Protocolo nº ' + str(protocolo.num_protocolo) + '/' + str(protocolo.ano_protocolo) + ' recebido em ' + self.pysc.iso_to_port_pysc(protocolo.dat_protocolo) + ' ' + protocolo.hor_protocolo + ' - '
              texto = str(materia.des_tipo_materia.decode('utf-8').upper())+' Nº '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
              storage_path = self.sapl_documentos.materia
              nom_pdf_saida = str(materia.cod_materia) + "_texto_integral.pdf"
          elif proposicao.ind_mat_ou_doc=='D' and (proposicao.des_tipo_proposicao!='Emenda' and proposicao.des_tipo_proposicao!='Mensagem Aditiva' and proposicao.des_tipo_proposicao!='Substitutivo' and proposicao.des_tipo_proposicao!='Parecer' and proposicao.des_tipo_proposicao!='Parecer de Comissão'):
            for documento in self.zsql.documento_acessorio_obter_zsql(cod_documento=proposicao.cod_mat_ou_doc):
              for materia in self.zsql.materia_obter_zsql(cod_materia=documento.cod_materia):
                  materia = str(materia.sgl_tipo_materia)+' Nº '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
              info_protocolo = '- Recebido em ' + proposicao.dat_recebimento + ' - '
              texto = str(documento.des_tipo_documento.decode('utf-8').upper())+' - ' + str(materia)
              storage_path = self.sapl_documentos.materia
              nom_pdf_saida = str(documento.cod_documento) + ".pdf"
          elif proposicao.ind_mat_ou_doc=='D' and (proposicao.des_tipo_proposicao=='Emenda' or proposicao.des_tipo_proposicao=='Mensagem Aditiva'):
            for emenda in self.zsql.emenda_obter_zsql(cod_emenda=proposicao.cod_emenda):
              for materia in self.zsql.materia_obter_zsql(cod_materia=emenda.cod_materia):
                  materia = str(materia.sgl_tipo_materia)+' Nº '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
              info_protocolo = '- Recebida em ' + proposicao.dat_recebimento + ' - '
              texto = 'EMENDA ' + str(emenda.des_tipo_emenda.decode('utf-8').upper())+' Nº '+ str(emenda.num_emenda) + ' AO ' + str(materia)
              storage_path = self.sapl_documentos.emenda
              nom_pdf_saida = str(emenda.cod_emenda) + "_emenda.pdf"
          elif proposicao.ind_mat_ou_doc=='D' and (proposicao.des_tipo_proposicao=='Substitutivo'):
            for substitutivo in self.zsql.substitutivo_obter_zsql(cod_substitutivo=proposicao.cod_substitutivo):
              for materia in self.zsql.materia_obter_zsql(cod_materia=substitutivo.cod_materia):
                  materia = str(materia.sgl_tipo_materia)+' Nº '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
              texto = 'SUBSTITUTIVO' + ' Nº '+ str(substitutivo.num_substitutivo) + ' AO ' + str(materia)
              storage_path = self.sapl_documentos.substitutivo
              nom_pdf_saida = str(substitutivo.cod_substitutivo) + "_substitutivo.pdf"
          elif proposicao.ind_mat_ou_doc=='D' and (proposicao.des_tipo_proposicao=='Parecer' or proposicao.des_tipo_proposicao=='Parecer de Comissão'):
            for relatoria in self.zsql.relatoria_obter_zsql(cod_relatoria=proposicao.cod_parecer, ind_excluido=0): 
              for comissao in self.zsql.comissao_obter_zsql(cod_comissao=relatoria.cod_comissao):
                  sgl_comissao = comissao.sgl_comissao
              for materia in self.zsql.materia_obter_zsql(cod_materia=proposicao.cod_mat_ou_doc):
                  materia = str(materia.sgl_tipo_materia)+' Nº '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
              texto = 'PARECER ' + sgl_comissao + ' Nº '+ str(relatoria.num_parecer) + '/' +str(relatoria.ano_parecer) + ' AO ' + str(materia)
              storage_path = self.sapl_documentos.parecer_comissao
              nom_pdf_saida = str(relatoria.cod_relatoria) + "_parecer.pdf"

        if self.sapl_documentos.props_sagl.restpki_access_token!='':
           mensagem1 = texto + info_protocolo + 'Esta é uma cópia do original assinado digitalmente por ' + nom_autor + outros
           mensagem2 = 'Para validar o documento, leia o código QR ou acesse ' + self.url()+'/conferir_assinatura'+' e informe o código '+ cod_validacao_doc + '.'
        else:
           mensagem1 = ''
           mensagem2 = ''
        mensagem = mensagem1 + '\n' + mensagem2
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Italic', '/usr/share/fonts/truetype/msttcorefonts/Arial_Italic.ttf'))
        pdfmetrics.registerFont(TTFont('Times_New_Roman', '/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf'))
        pdfmetrics.registerFont(TTFont('Times_New_Roman_Bold', '/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman_Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Times_New_Roman_Italic', '/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman_Italic.ttf'))
        arq = getattr(self.sapl_documentos.proposicao, nom_pdf_proposicao)
        arquivo = cStringIO.StringIO(str(arq.data))
        existing_pdf = PdfFileReader(arquivo, strict=False)
        numPages = existing_pdf.getNumPages()

        # cria novo PDF
        packet = StringIO.StringIO()
        can = canvas.Canvas(packet)
        for page_num, i in enumerate(range(numPages), start=1):
            page = existing_pdf.getPage(i)
            pwidth = self.getPageSizeW(page)
            pheight = self.getPageSizeH(page)
            can.setPageSize((pwidth, pheight))
            can.setFillColorRGB(0,0,0)
            # QRCode
            qr_code = qr.QrCodeWidget(self.url()+'/conferir_assinatura_proc?txt_codigo_verificacao='+str(cod_validacao_doc))
            bounds = qr_code.getBounds()
            width = bounds[2] - bounds[0]
            height = bounds[3] - bounds[1]
            d = Drawing(55, 55, transform=[55./width,0,0,55./height,0,0])
            d.add(qr_code)
            x = 59
            renderPDF.draw(d, can,  pwidth-59, 13)
            # Margem direita
            d = Drawing(10, 5)
            lab = Label()
            lab.setOrigin(0,250)
            lab.angle = 90
            lab.fontName = 'Arial'
            lab.fontSize = 7
            lab.textAnchor = 'start'
            lab.boxAnchor = 'n'
            lab.setText(mensagem)
            d.add(lab)
            renderPDF.draw(d, can, pwidth-24, 160)
            # Numero de pagina
            footer_text = "Pag. %s/%s" % (page_num, numPages)
            can.saveState()
            can.setFont('Arial', 8)
            can.drawCentredString(pwidth-30, 10, footer_text)
            can.restoreState()
            can.showPage()
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # Numero do documento
        packet2 = StringIO.StringIO()
        d = canvas.Canvas(packet2, pagesize=A4)
        d.setFillColorRGB(0,0,0)
        d.setFont("Arial_Bold", 13)
        # alinhamento a esquerda
        #d.drawString(85, 700, texto)
        # alinhamento centralizado
        d.drawCentredString(pwidth/2, 700, texto)
        # nome autor abaixo da numeracao
        d.setFont("Arial_Italic", 10)
        #d.drawCentredString(pwidth/2, 688, nome_autor)
        d.save()
        packet2.seek(0)
        new_pdf2 = PdfFileReader(packet2)
        # Mescla arquivos
        output = PdfFileWriter()
        for page in range(existing_pdf.getNumPages()):
            pdf_page = existing_pdf.getPage(page)
            # numeração documento na primeira pagina
            if tipo_proposicao != 'Parecer' and tipo_proposicao != 'Parecer de Comissão' and page == 0:
               pdf_page.mergePage(new_pdf2.getPage(0))
            # qrcode e margem direita em todas as páginas
            if self.sapl_documentos.props_sagl.restpki_access_token != '' and cod_validacao_doc != '':
               for wm in range(new_pdf.getNumPages()):
                   watermark_page = new_pdf.getPage(wm)
                   if page == wm:
                      pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = cStringIO.StringIO()
        output.write(outputStream)
        if nom_pdf_saida in storage_path:
           storage_path.manage_delObjects(nom_pdf_saida)
           storage_path.manage_addFile(nom_pdf_saida)
           arq=storage_path[nom_pdf_saida]
           arq.manage_edit(title=nom_pdf_saida,filedata=outputStream.getvalue(),content_type='application/pdf')
        else:
           storage_path.manage_addFile(nom_pdf_saida)
           arq=storage_path[nom_pdf_saida]
           arq.manage_edit(title=nom_pdf_saida,filedata=outputStream.getvalue(),content_type='application/pdf')

    def peticao_autuar(self,cod_peticao):
        for peticao in self.zsql.peticao_obter_zsql(cod_peticao=cod_peticao):
            cod_validacao_doc = ''
            nom_autor = ''
            outros = ''
            qtde_assinaturas = []
            if self.zsql.assinatura_documento_obter_zsql(tipo_doc='peticao', codigo=peticao.cod_peticao, ind_assinado=1):
               for validacao in self.zsql.assinatura_documento_obter_zsql(tipo_doc='peticao', codigo=peticao.cod_peticao, ind_assinado=1):
                   nom_pdf_peticao = str(validacao.cod_assinatura_doc) + ".pdf"
                   pdf_peticao = self.sapl_documentos.documentos_assinados.absolute_url() + "/" +  nom_pdf_peticao
                   qtde_assinaturas.append(validacao.cod_usuario)
                   if validacao.ind_prim_assinatura == 1:
                      nom_autor = validacao.nom_completo
                   cod_validacao_doc = str(self.cadastros.assinatura.format_verification_code(code=validacao.cod_assinatura_doc))
            else:
               nom_pdf_peticao = str(cod_peticao) + ".pdf"
               pdf_peticao = self.sapl_documentos.peticao.absolute_url() + "/" +  nom_pdf_peticao
               for usuario in self.zsql.usuario_obter_zsql(cod_usuario=peticao.cod_usuario):
                   qtde_assinaturas.append(usuario.cod_usuario)
                   nom_autor = usuario.nom_completo
                   cod_validacao_doc = ''
            if len(qtde_assinaturas) == 2:
               outros = " e outro"
            elif len(qtde_assinaturas) > 2:
               outros = " e outros"
            info_protocolo = '- Recebido em ' + peticao.dat_recebimento + ' - '
            tipo_tipo_peticionamento = peticao.des_tipo_peticionamento
            if peticao.ind_doc_adm == "1":
               for documento in self.zsql.documento_administrativo_obter_zsql(cod_documento=peticao.cod_documento):
                   for protocolo in self.zsql.protocolo_obter_zsql(num_protocolo=documento.num_protocolo, ano_protocolo=documento.ano_documento):
                       info_protocolo = ' - Protocolo nº ' + str(protocolo.num_protocolo) + '/' + str(protocolo.ano_protocolo) + ' recebido em ' + self.pysc.iso_to_port_pysc(protocolo.dat_protocolo) + ' ' + protocolo.hor_protocolo + ' - '
                   texto = str(documento.des_tipo_documento.decode('utf-8').upper())+' Nº '+ str(documento.num_documento)+ '/' +str(documento.ano_documento)
                   storage_path = self.sapl_documentos.administrativo
                   nom_pdf_saida = str(documento.cod_documento) + "_texto_integral.pdf"
                   caminho = '/sapl_documentos/administrativo/'
            elif peticao.ind_doc_materia == "1":
               for documento in self.zsql.documento_acessorio_obter_zsql(cod_documento=peticao.cod_doc_acessorio):
                   texto = str(documento.des_tipo_documento.decode('utf-8').upper())+' - ' + str(materia)
                   storage_path = self.sapl_documentos.materia
                   nom_pdf_saida = str(documento.cod_documento) + ".pdf"
                   caminho = '/sapl_documentos/materia/'
            elif peticao.ind_norma == "1":
               storage_path = self.sapl_documentos.norma_juridica
               for norma in self.zsql.norma_juridica_obter_zsql(cod_norma=peticao.cod_norma):
                   texto = str(norma.des_tipo_norma.decode('utf-8').upper())+' Nº '+ str(norma.num_norma) + '/' + str(norma.ano_norma)
                   nom_pdf_saida = str(norma.cod_norma) + "_texto_integral.pdf"
                   caminho = '/sapl_documentos/norma_juridica/'
        if cod_validacao_doc != '':
           mensagem1 = texto + info_protocolo + 'Esta é uma cópia do original assinado digitalmente por ' + nom_autor + outros
           mensagem2 = 'Para validar o documento, leia o código QR ou acesse ' + self.url()+'/conferir_assinatura'+' e informe o código '+ cod_validacao_doc + '.'
        else:
           mensagem1 = texto + info_protocolo + 'Documento assinado com usuário e senha por ' + nom_autor
           mensagem2 = ''
        mensagem = mensagem1 + '\n' + mensagem2
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))

        if cod_validacao_doc != '':
           arq = getattr(self.sapl_documentos.documentos_assinados, nom_pdf_peticao)
        else:
           arq = getattr(self.sapl_documentos.peticao, nom_pdf_peticao)

        arquivo = cStringIO.StringIO(str(arq.data))
        existing_pdf = PdfFileReader(arquivo, strict=False)
        numPages = existing_pdf.getNumPages()

        # cria novo PDF
        packet = StringIO.StringIO()
        can = canvas.Canvas(packet)
        for page_num, i in enumerate(range(numPages), start=1):
            page = existing_pdf.getPage(i)
            pwidth = self.getPageSizeW(page)
            pheight = self.getPageSizeH(page)
            can.setPageSize((pwidth, pheight))
            can.setFillColorRGB(0,0,0)
            # QRCode
            if cod_validacao_doc != '':
               qr_code = qr.QrCodeWidget(self.url()+'/conferir_assinatura_proc?txt_codigo_verificacao='+str(cod_validacao_doc))
            else:
               qr_code = qr.QrCodeWidget(self.url() + str(caminho) + str(nom_pdf_saida))
            bounds = qr_code.getBounds()
            width = bounds[2] - bounds[0]
            height = bounds[3] - bounds[1]
            d = Drawing(55, 55, transform=[55./width,0,0,55./height,0,0])
            d.add(qr_code)
            x = 59
            renderPDF.draw(d, can,  pwidth-59, 13)
            # Margem direita
            d = Drawing(10, 5)
            lab = Label()
            lab.setOrigin(0,250)
            lab.angle = 90
            lab.fontName = 'Arial'
            lab.fontSize = 7
            lab.textAnchor = 'start'
            lab.boxAnchor = 'n'
            lab.setText(mensagem)
            d.add(lab)
            renderPDF.draw(d, can, pwidth-24, 160)
            # Numero de pagina
            footer_text = "Pag. %s/%s" % (page_num, numPages)
            can.saveState()
            can.setFont('Arial', 8)
            can.drawCentredString(pwidth-30, 10, footer_text)
            can.restoreState()
            can.showPage()
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # Numero do documento
        packet2 = StringIO.StringIO()
        d = canvas.Canvas(packet2, pagesize=A4)
        d.setFillColorRGB(0,0,0)
        d.setFont("Arial_Bold", 13)
        # alinhamento a esquerda
        #d.drawString(85, 700, texto)
        # alinhamento centralizado
        d.drawCentredString(pwidth/2, 700, texto)
        d.save()
        packet2.seek(0)
        new_pdf2 = PdfFileReader(packet2)
        # Mescla arquivos
        output = PdfFileWriter()
        for page in range(existing_pdf.getNumPages()):
            pdf_page = existing_pdf.getPage(page)
            # numeração documento na primeira pagina
            if peticao.ind_doc_adm == '1' and page == 0:
               pdf_page.mergePage(new_pdf2.getPage(0))
            # qrcode e margem direita em todas as páginas
            for wm in range(new_pdf.getNumPages()):
                watermark_page = new_pdf.getPage(wm)
                if page == wm:
                   pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = cStringIO.StringIO()
        output.write(outputStream)
        if nom_pdf_saida in storage_path:
           storage_path.manage_delObjects(nom_pdf_saida)
           storage_path.manage_addFile(nom_pdf_saida)
           arq=storage_path[nom_pdf_saida]
           arq.manage_edit(title=nom_pdf_saida,filedata=outputStream.getvalue(),content_type='application/pdf')
           arq.manage_permission('View', roles=['Manager','Authenticated'], acquire=0)
        else:
           storage_path.manage_addFile(nom_pdf_saida)
           arq=storage_path[nom_pdf_saida]
           arq.manage_edit(title=nom_pdf_saida,filedata=outputStream.getvalue(),content_type='application/pdf')
           arq.manage_permission('View', roles=['Manager','Authenticated'], acquire=0)

        if peticao.ind_norma == "1":
           arq=storage_path[nom_pdf_saida]
           arq.manage_permission('View', roles=['Anonymoys'], acquire=1)
           self.sapl_documentos.norma_juridica.Catalog.atualizarCatalogo(cod_norma=peticao.cod_norma)

    def restpki_client(self):
        restpki_url = 'https://restpkiol.azurewebsites.net/'
        #restpki_url = 'https://pki.rest/'
        restpki_access_token = self.sapl_documentos.props_sagl.restpki_access_token
        restpki_client = RestPkiClient(restpki_url, restpki_access_token)
        return restpki_client

    def get_file_tosign(self, codigo, tipo_doc):
        for storage in self.zsql.assinatura_storage_obter_zsql(tip_documento=tipo_doc):
            tipo_doc = storage.tip_documento
            if tipo_doc == 'proposicao':
               storage_path = self.sapl_documentos.proposicao
               pdf_location = storage.pdf_location
               pdf_signed = str(pdf_location) + str(codigo) + str(storage.pdf_signed)
               nom_arquivo_assinado = str(codigo) + str(storage.pdf_signed)
               pdf_file = str(pdf_location) + str(codigo) + str(storage.pdf_file)
               nom_arquivo = str(codigo) + str(storage.pdf_file)
            else:
               for item in self.zsql.assinatura_documento_obter_zsql(codigo=codigo, tipo_doc=tipo_doc, ind_assinado=1):
                   if len([item]) >= 1:
                      storage_path = self.sapl_documentos.documentos_assinados
                      pdf_location = 'sapl_documentos/documentos_assinados/'
                      pdf_signed = str(pdf_location) + str(item.cod_assinatura_doc) + '.pdf'
                      nom_arquivo_assinado = str(item.cod_assinatura_doc) + '.pdf'
                      pdf_file = str(pdf_location) + str(item.cod_assinatura_doc) + '.pdf'
                      nom_arquivo = str(item.cod_assinatura_doc) + '.pdf'
                      break
               else:
                   # local de armazenamento
                   if tipo_doc == 'materia' or tipo_doc == 'doc_acessorio' or tipo_doc == 'redacao_final':
                      storage_path = self.sapl_documentos.materia
                   elif tipo_doc == 'emenda':
                      storage_path = self.sapl_documentos.emenda
                   elif tipo_doc == 'substitutivo':
                      storage_path = self.sapl_documentos.substitutivo
                   elif tipo_doc == 'tramitacao':
                      storage_path = self.sapl_documentos.materia.tramitacao
                   elif tipo_doc == 'parecer_comissao':
                      storage_path = self.sapl_documentos.parecer_comissao
                   elif tipo_doc == 'pauta':
                      storage_path = self.sapl_documentos.pauta_sessao
                   elif tipo_doc == 'ata':
                      storage_path = self.sapl_documentos.ata_sessao
                   elif tipo_doc == 'norma':
                      storage_path = self.sapl_documentos.norma_juridica
                   elif tipo_doc == 'documento' or tipo_doc == 'doc_acessorio_adm':
                      storage_path = self.sapl_documentos.administrativo
                   elif tipo_doc == 'tramitacao_adm':
                      storage_path = self.sapl_documentos.administrativo.tramitacao
                   elif tipo_doc == 'protocolo':
                      storage_path = self.sapl_documentos.protocolo
                   elif tipo_doc == 'peticao':
                      storage_path = self.sapl_documentos.peticao
                   elif tipo_doc == 'pauta_comissao':
                      storage_path = self.sapl_documentos.reuniao_comissao
                   elif tipo_doc == 'ata_comissao':
                      storage_path = self.sapl_documentos.reuniao_comissao
                   elif tipo_doc == 'documento_comissao':
                      storage_path = self.sapl_documentos.documento_comissao
                   pdf_location = storage.pdf_location
                   pdf_signed = str(pdf_location) + str(codigo) + str(storage.pdf_signed)
                   nom_arquivo_assinado = str(codigo) + str(storage.pdf_signed)
                   pdf_file = str(pdf_location) + str(codigo) + str(storage.pdf_file)
                   nom_arquivo = str(codigo) + str(storage.pdf_file)
        try:
           arquivo = self.restrictedTraverse(pdf_signed)
           pdf_tosign = nom_arquivo_assinado
        except:
           arquivo = self.restrictedTraverse(pdf_file)
           pdf_tosign = nom_arquivo

        x = crc32(str(arquivo))

        if (x>=0):
           crc_arquivo= str(x)
        else:
           crc_arquivo= str(-1 * x)

        return pdf_tosign, storage_path, crc_arquivo

    def pades_signature(self, codigo, tipo_doc, cod_usuario, qtde_assinaturas):
        # get file to sign
        pdf_tosign, storage_path, crc_arquivo = self.get_file_tosign(codigo, tipo_doc)
        arq = getattr(storage_path, pdf_tosign)
        arquivo = cStringIO.StringIO(str(arq.data))
        arquivo.seek(0)
        pdf_path = ''
        pdf_stream = str(arq.data)

        # Read the PDF stamp image
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sagl.id_logo
        if hasattr(self.sapl_documentos.props_sagl, id_logo):
           url = self.url() + '/sapl_documentos/props_sagl/' + id_logo
        else:
           url = self.url() + '/imagens/brasao.gif'
        pdf_stamp = urllib.urlopen(url).read()

        signature_starter = PadesSignatureStarter(self.restpki_client())
        signature_starter.set_pdf_stream(pdf_stream)

        signature_starter.signature_policy_id = StandardSignaturePolicies.PADES_BASIC
        signature_starter.security_context_id = StandardSecurityContexts.PKI_BRAZIL
        if int(qtde_assinaturas) <= 3:
           signature_starter.visual_representation = ({
               'text': {
                   'text': 'Assinado digitalmente por {{signerName}}',
                   'includeSigningTime': True,
                   'horizontalAlign': 'Left'
               },
               'image': {
                   'resource': {
                       'content': base64.b64encode(pdf_stamp),
                       'mimeType': 'image/png'
                   },
                   'opacity': 40,
                   'horizontalAlign': 'Right'
               },
               'position': self.get_visual_representation_position(2)
           })
        elif int(qtde_assinaturas) > 3:
           signature_starter.visual_representation = ({
               'text': {
                   'text': 'Assinado digitalmente por {{signerName}}',
                   'includeSigningTime': True,
                   'horizontalAlign': 'Left'
               },
               'image': {
                   'resource': {
                       'content': base64.b64encode(pdf_stamp),
                       'mimeType': 'image/png'
                   },
                   'opacity': 40,
                   'horizontalAlign': 'Right'
               },
               'position': self.get_visual_representation_position(4)
           })

        token = signature_starter.start_with_webpki()

        tokenjs = json.dumps(token)

        return token, pdf_path, crc_arquivo, codigo, tipo_doc, cod_usuario, tokenjs

    def pades_signature_action(self, token, codigo, tipo_doc, cod_usuario, crc_arquivo_original):
        # checking if file was changed
        pdf_tosign, storage_path, crc_arquivo = self.get_file_tosign(codigo, tipo_doc)
        if str(crc_arquivo_original) != str(crc_arquivo):
           msg = 'O arquivo foi modificado durante o procedimento de assinatura! Tente novamente.'
           raise ValueError(msg)

        # Get the token for this signature (rendered in a hidden input field)
        token = token
        codigo = codigo
        tipo_doc = tipo_doc
        cod_usuario = cod_usuario

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
        cod_assinatura_doc = ''
        for item in self.zsql.assinatura_documento_obter_zsql(codigo=codigo, tipo_doc=tipo_doc):
            cod_assinatura_doc = str(item.cod_assinatura_doc)
            self.zsql.assinatura_documento_registrar_zsql(cod_assinatura_doc=item.cod_assinatura_doc, cod_usuario=cod_usuario)
            break
        else:
            cod_assinatura_doc = str(self.cadastros.assinatura.generate_verification_code())
            self.zsql.assinatura_documento_incluir_zsql(cod_assinatura_doc=cod_assinatura_doc, codigo=codigo,tipo_doc=tipo_doc, cod_usuario=cod_usuario, ind_prim_assinatura=1)
            self.zsql.assinatura_documento_registrar_zsql(cod_assinatura_doc=cod_assinatura_doc, cod_usuario=cod_usuario)

        if tipo_doc == 'proposicao':
           storage_path = self.sapl_documentos.proposicao
           for storage in self.zsql.assinatura_storage_obter_zsql(tip_documento=tipo_doc):
               filename = str(codigo) + str(storage.pdf_signed)
               old_filename = str(codigo) + str(storage.pdf_file)
        else:
           storage_path = self.sapl_documentos.documentos_assinados
           for storage in self.zsql.assinatura_storage_obter_zsql(tip_documento=tipo_doc):
               filename = str(cod_assinatura_doc) + '.pdf'
               old_filename = str(codigo) + str(storage.pdf_file)

        file_hash = str(uuid.uuid4().hex) + '.pdf'

        self.temp_folder.manage_addFile(file_hash)
        arq=self.temp_folder[file_hash]
        f = signature_finisher.stream_signed_pdf()
        arq.manage_edit(title=file_hash,filedata=f.getvalue(),content_type='application/pdf')

        if tipo_doc != 'proposicao' and tipo_doc != 'peticao':
           self.margem_direita(codigo, tipo_doc, cod_assinatura_doc, cod_usuario, file_hash)

        if hasattr(storage_path,filename):
           storage_path.manage_delObjects(filename)
           tmp_copy = self.temp_folder.manage_copyObjects(ids=file_hash)
           tmp_id = storage_path.manage_pasteObjects(tmp_copy)[0]['new_id']
           storage_path.manage_renameObjects(ids=list([tmp_id]),new_ids=list([filename]))
           self.temp_folder.manage_delObjects(file_hash)
        else:
           tmp_copy = self.temp_folder.manage_copyObjects(ids=file_hash)
           tmp_id = storage_path.manage_pasteObjects(tmp_copy)[0]['new_id']
           storage_path.manage_renameObjects(ids=list([tmp_id]),new_ids=list([filename]))
           self.temp_folder.manage_delObjects(file_hash)

        for item in signer_cert:
           subjectName = signer_cert['subjectName']
           commonName = subjectName['commonName']
           email = signer_cert['emailAddress']
           pkiBrazil = signer_cert['pkiBrazil']
           certificateType = pkiBrazil['certificateType']
           cpf = pkiBrazil['cpf']
           responsavel = pkiBrazil['responsavel']

        filenamejs = json.dumps(filename)

        return signer_cert, commonName, email, certificateType, cpf, responsavel, file_hash, filenamejs

    def get_visual_representation_position(self, sample_number):
        if sample_number == 1:
            # Example #1: automatic positioning on footnote. This will insert the signature, and future signatures,
            # ordered as a footnote of the last page of the document
            return PadesVisualPositioningPresets.get_footnote(self.restpki_client())
        elif sample_number == 2:
            # Example #2: get the footnote positioning preset and customize it
            visual_position = PadesVisualPositioningPresets.get_footnote(self.restpki_client())
            visual_position['auto']['container']['left'] = 3
            visual_position['auto']['container']['bottom'] = 2
            visual_position['auto']['container']['right'] = 3
            return visual_position
        elif sample_number == 3:
            # Example #3: automatic positioning on new page. This will insert the signature, and future signatures,
            # in a new page appended to the end of the document.
            return PadesVisualPositioningPresets.get_new_page(self.restpki_client())
        elif sample_number == 4:
            # Example #4: get the "new page" positioning preset and customize it
            visual_position = PadesVisualPositioningPresets.get_new_page(self.restpki_client())
            visual_position['auto']['container']['left'] = 3
            visual_position['auto']['container']['top'] = 2
            visual_position['auto']['container']['bottom'] = 2
            visual_position['auto']['container']['right'] = 3
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
                    'bottom': 1.54,
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
                        'top': 1.54,
                        'height': 3
                    },
                    # Specification of the size of each signature rectangle
                    #'signatureRectangleSize': {
                    #    'width': 5,
                    #    'height': 3
                    #},
                    # The signatures will be placed in the container side by side. If there's no room left, the
                    # signatures will "wrap" to the next row. The value below specifies the vertical distance between
                    # rows
                    'rowSpacing': 1
                }
            }
        else:
            return None

    def margem_direita(self, codigo, tipo_doc, cod_assinatura_doc, cod_usuario, file_hash):

        for storage in self.zsql.assinatura_storage_obter_zsql(tip_documento=tipo_doc):
            nom_pdf_assinado = str(cod_assinatura_doc) + '.pdf'
            nom_pdf_documento = str(codigo) + str(storage.pdf_file)

        outros = ''
        qtde_assinaturas = []
        for validacao in self.zsql.assinatura_documento_obter_zsql(cod_assinatura_doc=cod_assinatura_doc, ind_assinado=1):
            qtde_assinaturas.append(validacao.cod_usuario)
            if validacao.ind_prim_assinatura == 1:
               nom_autor = validacao.nom_completo
               cod_validacao_doc = str(self.cadastros.assinatura.format_verification_code(code=validacao.cod_assinatura_doc))
        else:
            for usuario in self.zsql.usuario_obter_zsql(cod_usuario=cod_usuario):
                nom_autor = usuario.nom_completo
                break
        if len(qtde_assinaturas) == 2:
           outros = " e outro"
        elif len(qtde_assinaturas) > 2:
           outros = " e outros"

        string = str(self.cadastros.assinatura.format_verification_code(cod_assinatura_doc))

        # Variáveis para obtenção de dados e local de armazenamento por tipo de documento

        if tipo_doc == 'materia' or tipo_doc == 'doc_acessorio' or tipo_doc == 'redacao_final':
           storage_path = self.sapl_documentos.materia
           if tipo_doc == 'materia' or tipo_doc == 'redacao_final':
              for metodo in self.zsql.materia_obter_zsql(cod_materia=codigo):
                  num_documento = metodo.num_ident_basica
                  if tipo_doc == 'materia':
                     texto = str(metodo.des_tipo_materia.decode('utf-8').upper())+' Nº '+ str(metodo.num_ident_basica) + '/' + str(metodo.ano_ident_basica)
                  elif tipo_doc == 'redacao_final':
                     texto = 'REDAÇÃO FINAL - ' + str(metodo.sgl_tipo_materia)+' Nº '+ str(metodo.num_ident_basica) + '/' + str(metodo.ano_ident_basica)
           elif tipo_doc == 'doc_acessorio':
              for metodo in self.zsql.documento_acessorio_obter_zsql(cod_documento=codigo):
                  for materia in self.zsql.materia_obter_zsql(cod_materia=metodo.cod_materia):
                      materia = str(materia.sgl_tipo_materia)+' '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
              texto = str(metodo.nom_documento) + ' - ' + str(materia)
        elif tipo_doc == 'emenda':
           storage_path = self.sapl_documentos.emenda
           for metodo in self.zsql.emenda_obter_zsql(cod_emenda=codigp):
               for materia in self.zsql.materia_obter_zsql(cod_materia=metodo.cod_materia):
                   materia = str(materia.sgl_tipo_materia)+' '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
               texto = 'EMENDA' + str(metodo.des_tipo_emenda())+' Nº '+ str(metodo.num_emenda) + ' - ' + str(materia)
        elif tipo_doc == 'substitutivo':
           storage_path = self.sapl_documentos.substitutivo
           for metodo in self.zsql.substitutivo_obter_zsql(cod_substitutivo=codigo):
               for materia in self.zsql.materia_obter_zsql(cod_materia=metodo.cod_materia):
                   materia = str(materia.sgl_tipo_materia)+' '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
               texto = 'SUBSTITUTIVO Nº '+ str(metodo.num_substitutivo) + ' - ' + str(materia)
        elif tipo_doc == 'tramitacao':
           storage_path = self.sapl_documentos.materia.tramitacao
           for metodo in self.zsql.tramitacao_obter_zsql(cod_tramitacao=codigo):
               materia = str(metodo.sgl_tipo_materia)+' '+ str(metodo.num_ident_basica)+'/'+str(metodo.ano_ident_basica)
           texto = 'TRAMITAÇÃO Nº '+ str(metodo.cod_tramitacao) + ' - ' + str(materia)
        elif tipo_doc == 'parecer_comissao':
           storage_path = self.sapl_documentos.parecer_comissao
           for metodo in self.zsql.relatoria_obter_zsql(cod_relatoria=codigo):
               for materia in self.zsql.materia_obter_zsql(cod_materia=metodo.cod_materia):
                   materia = str(materia.sgl_tipo_materia)+' '+ str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
           texto = 'PARECER Nº '+ str(metodo.num_ordem) + ' - ' + str(materia)
        elif tipo_doc == 'pauta':
           storage_path = self.sapl_documentos.pauta_sessao
           for metodo in self.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=codigo):
               for tipo in self.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=metodo.tip_sessao):
                   sessao = str(metodo.num_sessao_plen) +  'ª Sessão ' + str(tipo.nom_sessao)+' - '+ str(metodo.dat_inicio_sessao)
           texto = 'PAUTA' + ' - ' + str(sessao)
        elif tipo_doc == 'ata':
           storage_path = self.sapl_documentos.ata_sessao
           for metodo in self.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=codigo):
               for tipo in self.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=metodo.tip_sessao):
                   sessao = str(metodo.num_sessao_plen) +  'ª Sessão ' + str(tipo.nom_sessao)+' - '+ str(metodo.dat_inicio_sessao)
           texto = 'ATA' + ' - ' + str(sessao)
        elif tipo_doc == 'norma':
           storage_path = self.sapl_documentos.norma_juridica
           for metodo in self.zsql.norma_juridica_obter_zsql(cod_norma=codigo):
               texto = str(metodo.des_tipo_norma.decode('utf-8').upper())+' Nº '+ str(metodo.num_norma) + '/' + str(metodo.ano_norma)
        elif tipo_doc == 'documento' or tipo_doc == 'doc_acessorio_adm':
           storage_path = self.sapl_documentos.administrativo
           if tipo_doc == 'documento':
              for metodo in self.zsql.documento_administrativo_obter_zsql(cod_documento=codigo):
                  num_documento = metodo.num_documento
              texto = str(metodo.des_tipo_documento.decode('utf-8').upper())+' Nº '+ str(metodo.num_documento)+ '/' +str(metodo.ano_documento)
           elif tipo_doc == 'doc_acessorio_adm':
              for metodo in self.zsql.documento_acessorio_administrativo_obter_zsql(cod_documento_acessorio=codigo):
                  for documento in self.zsql.documento_administrativo_obter_zsql(cod_documento=metodo.cod_documento):
                      documento = str(documento.sgl_tipo_documento) +' '+ str(documento.num_documento)+'/'+str(documento.ano_documento)
              texto = 'Acessório' + ' - ' + str(documento)
        elif tipo_doc == 'tramitacao_adm':
           storage_path = self.sapl_documentos.administrativo.tramitacao
           for metodo in self.zsql.tramitacao_administrativo_obter_zsql(cod_tramitacao=codigo):
               documento = str(metodo.sgl_tipo_documento)+' '+ str(metodo.num_documento)+'/'+str(metodo.ano_documento)
           texto = 'TRAMITAÇÃO Nº '+ str(metodo.cod_tramitacao) + ' - ' + str(documento)
        elif tipo_doc == 'proposicao':
           storage_path = self.sapl_documentos.proposicao
           for metodo in self.zsql.proposicao_obter_zsql(cod_proposicao=codigo):
               texto = str(metodo.des_tipo_proposicao.decode('utf-8').upper())+' Nº '+ str(metodo.cod_proposicao)
        elif tipo_doc == 'protocolo':
           storage_path = self.sapl_documentos.protocolo
           for metodo in self.zsql.protocolo_obter_zsql(cod_protocolo=codigo):
               texto = 'PROTOCOLO Nº '+ str(metodo.num_protocolo)+'/'+ str(metodo.ano_protocolo)
        elif tipo_doc == 'peticao':
           storage_path = self.sapl_documentos.peticao
           texto = 'PETIÇÃO ELETRÔNICA'
        elif tipo_doc == 'pauta_comissao':
           storage_path = self.sapl_documentos.reuniao_comissao
           for metodo in self.zsql.reuniao_comissao_obter_zsql(cod_reuniao=codigo):
               for comissao in self.zsql.comissao_obter_zsql(cod_comissao=metodo.cod_comissao):
                   texto = 'PAUTA - ' + metodo.num_reuniao + 'ª Reunião da ' + comissao.sgl_comissao + ', em ' + metodo.dat_inicio_reuniao
        elif tipo_doc == 'ata_comissao':
           storage_path = self.sapl_documentos.reuniao_comissao
           for metodo in self.zsql.reuniao_comissao_obter_zsql(cod_reuniao=codigo):
               for comissao in self.zsql.comissao_obter_zsql(cod_comissao=metodo.cod_comissao):
                   texto = 'ATA - ' + metodo.num_reuniao + 'ª Reunião da ' + comissao.sgl_comissao + ', em ' + metodo.dat_inicio_reuniao
        elif tipo_doc == 'documento_comissao':
           storage_path = self.sapl_documentos.documento_comissao
           for metodo in self.zsql.documento_comissao_obter_zsql(cod_documento=codigo):
               for comissao in self.zsql.comissao_obter_zsql(cod_comissao=metodo.cod_comissao):
                   texto = metodo.txt_descricao + ' - ' + comissao.sgl_comissao

        mensagem1 = texto + ' - Esta é uma cópia do original assinado digitalmente por ' + nom_autor + outros + '.'
        mensagem2 = 'Para validar o documento, leia o código QR ou acesse ' + self.url()+'/conferir_assinatura'+' e informe o código '+ string
        mensagem = mensagem1 + '\n' + mensagem2
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        arq = getattr(self.temp_folder, file_hash)
        arquivo = cStringIO.StringIO(str(arq.data))
        existing_pdf = PdfFileReader(arquivo, strict=False)
        numPages = existing_pdf.getNumPages()
        # cria novo PDF
        packet = StringIO.StringIO()
        can = canvas.Canvas(packet)
        for page_num, i in enumerate(range(numPages), start=1):
            page = existing_pdf.getPage(i)
            pwidth = self.getPageSizeW(page)
            pheight = self.getPageSizeH(page)
            can.setPageSize((pwidth, pheight))
            can.setFillColorRGB(0,0,0)
            # QRCode
            qr_code = qr.QrCodeWidget(self.url()+'/conferir_assinatura_proc?txt_codigo_verificacao='+str(string))
            bounds = qr_code.getBounds()
            width = bounds[2] - bounds[0]
            height = bounds[3] - bounds[1]
            d = Drawing(55, 55, transform=[55./width,0,0,55./height,0,0])
            d.add(qr_code)
            x = 59
            renderPDF.draw(d, can,  pwidth-59, 13)
            # Margem direita
            d = Drawing(10, 5)
            lab = Label()
            lab.setOrigin(0,250)
            lab.angle = 90
            lab.fontName = 'Arial'
            lab.fontSize = 7
            lab.textAnchor = 'start'
            lab.boxAnchor = 'n'
            lab.setText(mensagem)
            d.add(lab)
            renderPDF.draw(d, can, pwidth-24, 160)
            # Numero de pagina
            footer_text = "Pag. %s/%s" % (page_num, numPages)
            can.saveState()
            can.setFont('Arial', 8)
            can.drawCentredString(pwidth-30, 10, footer_text)
            can.restoreState()
            can.showPage()
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # Mescla arquivos
        output = PdfFileWriter()
        for page in range(existing_pdf.getNumPages()):
            pdf_page = existing_pdf.getPage(page)
            # qrcode e margem direita em todas as páginas
            for wm in range(new_pdf.getNumPages()):
                watermark_page = new_pdf.getPage(wm)
                if page == wm:
                   pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = cStringIO.StringIO()
        output.write(outputStream)

        if hasattr(storage_path,nom_pdf_documento):
           storage_path.manage_delObjects(nom_pdf_documento)
           storage_path.manage_addFile(nom_pdf_documento)
           arq=storage_path[nom_pdf_documento]
           arq.manage_edit(title=nom_pdf_documento,filedata=outputStream.getvalue(),content_type='application/pdf')
        else:
           storage_path.manage_addFile(nom_pdf_documento)
           arq=storage_path[nom_pdf_documento]
           arq.manage_edit(title=nom_pdf_documento,filedata=outputStream.getvalue(),content_type='application/pdf')

        if tipo_doc == 'parecer_comissao':
           for relat in self.zsql.relatoria_obter_zsql(cod_relatoria=codigo):
               nom_arquivo_pdf = "%s"%relat.cod_relatoria+'_parecer.pdf'
               if relat.tip_fim_relatoria == '6' and hasattr(self.sapl_documentos.parecer_comissao, nom_arquivo_pdf):
                  pdf = getattr(self.sapl_documentos.parecer_comissao, nom_arquivo_pdf)
                  pdf.manage_permission('View', roles=['Manager','Authenticated'], acquire=0)

        if tipo_doc == 'doc_acessorio':
           for documento in self.zsql.documento_acessorio_obter_zsql(cod_documento=codigo):
               nom_arquivo_pdf = "%s"%documento.cod_documento+'.pdf'
               if documento.ind_publico == '0' and hasattr(self.sapl_documentos.materia, nom_arquivo_pdf):
                  pdf = getattr(self.sapl_documentos.materia, nom_arquivo_pdf)
                  pdf.manage_permission('View', roles=['Manager','Authenticated'], acquire=0)

        if tipo_doc == 'documento':
           for documento in self.zsql.documento_administrativo_obter_zsql(cod_documento=codigo):
               nom_arquivo_pdf = "%s"%documento.cod_documento+'_texto_integral.pdf'
               if documento.ind_publico == '1' and hasattr(self.sapl_documentos.administrativo, nom_arquivo_pdf):
                  pdf = getattr(self.sapl_documentos.administrativo, nom_arquivo_pdf)
                  pdf.manage_permission('View', roles=['Anonymous'], acquire=0)

        return 'ok'


    def assinar_proposicao(self, cod_proposicao):
        storage_path = self.sapl_documentos.proposicao
        for proposicao in self.zsql.proposicao_obter_zsql(cod_proposicao=cod_proposicao):
            string = self.pysc.proposicao_calcular_checksum_pysc(proposicao.cod_proposicao, senha=1)
            nom_autor = proposicao.nom_autor
            pdf_proposicao = str(proposicao.cod_proposicao) + '.pdf'
            pdf_assinado = str(proposicao.cod_proposicao) + '_signed.pdf'
            texto = 'Proposição eletrônica ' + string
        mensagem1 = 'Documento assinado digitalmente com usuário e senha por ' + nom_autor + '.'
        mensagem2 = texto + ', Para verificação de autenticidade utilize o QR Code exibido no rodapé.'
        mensagem = mensagem1 + '\n' + mensagem2
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        arq = getattr(storage_path, pdf_proposicao)
        arquivo = cStringIO.StringIO(str(arq.data))
        existing_pdf = PdfFileReader(arquivo, strict=False)
        numPages = existing_pdf.getNumPages()
        # cria novo PDF
        packet = StringIO.StringIO()
        can = canvas.Canvas(packet)
        for page_num, i in enumerate(range(numPages), start=1):
            page = existing_pdf.getPage(i)
            pwidth = self.getPageSizeW(page)
            pheight = self.getPageSizeH(page)
            can.setPageSize((pwidth, pheight))
            can.setFillColorRGB(0,0,0)
            # QRCode
            qr_code = qr.QrCodeWidget(self.url() + '/sapl_documentos/proposicao/' + cod_proposicao + '_signed.pdf')
            bounds = qr_code.getBounds()
            width = bounds[2] - bounds[0]
            height = bounds[3] - bounds[1]
            d = Drawing(55, 55, transform=[55./width,0,0,55./height,0,0])
            d.add(qr_code)
            x = 59
            renderPDF.draw(d, can,  pwidth-59, 13)
            # Margem direita
            d = Drawing(10, 5)
            lab = Label()
            lab.setOrigin(0,250)
            lab.angle = 90
            lab.fontName = 'Arial'
            lab.fontSize = 7
            lab.textAnchor = 'start'
            lab.boxAnchor = 'n'
            lab.setText(mensagem)
            d.add(lab)
            renderPDF.draw(d, can, pwidth-24, 160)
            # Numero de pagina
            footer_text = "Pag. %s/%s" % (page_num, numPages)
            can.saveState()
            can.setFont('Arial', 8)
            can.drawCentredString(pwidth-30, 10, footer_text)
            can.restoreState()
            can.showPage()
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # Mescla arquivos
        output = PdfFileWriter()
        for page in range(existing_pdf.getNumPages()):
            pdf_page = existing_pdf.getPage(page)
            # qrcode e margem direita em todas as páginas
            for wm in range(new_pdf.getNumPages()):
                watermark_page = new_pdf.getPage(wm)
                if page == wm:
                   pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = cStringIO.StringIO()
        output.write(outputStream)
        if hasattr(storage_path,pdf_assinado):
           storage_path.manage_delObjects(pdf_assinado)
           storage_path.manage_addFile(pdf_assinado)
           output.write(outputStream)
           arq=storage_path[pdf_assinado]
           arq.manage_edit(title=pdf_assinado,filedata=outputStream.getvalue(),content_type='application/pdf')
        else:
           storage_path.manage_addFile(pdf_assinado)
           output.write(outputStream)
           arq=storage_path[pdf_assinado]
           arq.manage_edit(title=pdf_assinado,filedata=outputStream.getvalue(),content_type='application/pdf')
        redirect_url = self.portal_url()+'/cadastros/proposicao/proposicao_mostrar_proc?cod_proposicao=' + cod_proposicao
        REQUEST = self.REQUEST
        RESPONSE = REQUEST.RESPONSE
        RESPONSE.redirect(redirect_url)

    def requerimento_aprovar(self, cod_sessao_plen, nom_resultado, cod_materia):

        if hasattr(self.sapl_documentos.props_sagl, 'logo_carimbo.png'):
           logo = ImageReader(self.portal_url() + '/sapl_documentos/props_sagl/logo_carimbo.png')
        elif hasattr(self.sapl_documentos.props_sagl, 'logo_casa.gif'):
           logo = ImageReader(self.portal_url() + '/sapl_documentos/props_sagl/logo_casa.gif')
        else:
           logo = ImageReader(self.portal_url() + '/imagens/brasao.gif')

        nom_presidente = ''
        # obtem dados da sessao
        if cod_sessao_plen != '0':
           for item in self.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen):
               for tipo in self.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=item.tip_sessao):
                   id_sessao = str(item.num_sessao_plen) + 'ª Sessão ' + tipo.nom_sessao + ' - '
               data = item.dat_inicio_sessao
               data1 = self.pysc.data_converter_pysc(data)
               num_legislatura = item.num_legislatura
           for composicao in self.zsql.composicao_mesa_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen, cod_cargo=1, ind_excluido=0):
               for parlamentar in self.zsql.parlamentar_obter_zsql(cod_parlamentar=composicao.cod_parlamentar):
                   nom_presidente = str(parlamentar.nom_parlamentar.decode('utf-8').upper())
           if nom_presidente == '':
              data = DateTime().strftime('%d/%m/%Y')
              data1 = self.pysc.data_converter_pysc(data)
              for sleg in self.zsql.periodo_comp_mesa_obter_zsql(data=data1):
                  for cod_presidente in self.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp, cod_cargo=1):
                      for presidencia in self.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
                          nom_presidente = str(presidencia.nom_parlamentar.decode('utf-8').upper())
        else:
           id_sessao = ""
           data = DateTime().strftime('%d/%m/%Y')
           data1 = self.pysc.data_converter_pysc(data)
           for sleg in self.zsql.periodo_comp_mesa_obter_zsql(data=data1):
               for cod_presidente in self.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp, cod_cargo=1):
                   for presidencia in self.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
                       nom_presidente = str(presidencia.nom_parlamentar.decode('utf-8').upper())

        # prepara carimbo
        packet = StringIO.StringIO()
        can = canvas.Canvas(packet)
        can.drawImage(logo, 490, 715,  width=50, height=50, mask='auto')
        texto = "%s" % (str(nom_resultado.decode('utf-8').upper()))
        sessao = "%s%s" % (id_sessao, data)
        presidente = "%s " % (nom_presidente)
        cargo = "Presidente"
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        can.setFont('Arial_Bold', 10)
        can.drawString(400, 750, texto)
        can.setFont('Arial', 9)
        can.drawString(400, 740, sessao)
        can.drawString(400, 730, presidente)
        can.drawString(400, 720, cargo)
        can.showPage()
        can.save()
        new_pdf = PdfFileReader(packet)
        output = PdfFileWriter()
        # adiciona carimbo aos documentos
        for materia in self.zsql.materia_obter_zsql(cod_materia=cod_materia):
            storage_path = self.sapl_documentos.materia
            nom_pdf_saida = str(materia.cod_materia) + "_texto_integral.pdf"
            if hasattr(storage_path, nom_pdf_saida):
               arq = getattr(storage_path, nom_pdf_saida)
               arquivo = cStringIO.StringIO(str(arq.data))
               existing_pdf = PdfFileReader(arquivo, strict=False)
               try:
                  existing_pdf = PdfFileReader(arquivo, strict=False)
                  numPages = existing_pdf.getNumPages()
                  # Mescla canvas
                  for page in range(existing_pdf.getNumPages()):
                      page_pdf = existing_pdf.getPage(page)
                      # carimbo na primeira pagina
                      if page == 0:
                         page_pdf.mergePage(new_pdf.getPage(0))
                      output.addPage(page_pdf)
                  outputStream = cStringIO.StringIO()
                  output.write(outputStream)
                  if hasattr(storage_path, nom_pdf_saida):
                     storage_path.manage_delObjects(nom_pdf_saida)
                     storage_path.manage_addFile(nom_pdf_saida)
                     arq=storage_path[nom_pdf_saida]
                     arq.manage_edit(title=nom_pdf_saida, filedata=outputStream.getvalue(), content_type='application/pdf')
                  else:
                     storage_path.manage_addFile(nom_pdf_saida)
                     arq=storage_path[nom_pdf_saida]
                     arq.manage_edit(title=nom_pdf_saida, filedata=outputStream.getvalue(), content_type='application/pdf')
               except:
                  pass

    def _getValidEmailAddress(self, member):
        email = None
        for usuario in self.zsql.usuario_obter_zsql(col_username=member):
            email = usuario.end_email

        return email

    security.declarePublic( 'mailPassword' )
    def mailPassword(self, forgotten_userid, REQUEST):
        membership = getToolByName(self, 'portal_membership')
        member = membership.getMemberById(forgotten_userid)

        if member is None:
            msg = 'Usuário não encontrado'
            raise ValueError(msg)

        email = self._getValidEmailAddress(member)

        if email is None or email == '':
           msg = 'Endereço de email não cadastrado'
           raise ValueError(msg)

        method = self.pysc.password_email
        kw = {'email': email, 'member': member, 'password': member.getPassword()}

        if getattr(aq_base(method), 'isDocTemp', 0):
            mail_text = method(self, REQUEST, **kw)
        else:
            mail_text = method(**kw)

        host = self.MailHost

        host.send( mail_text )

        return self.generico.mail_password_response( self, REQUEST )

    def create_payload(self, cod_materia):

        data = {}
        for materia in self.zsql.materia_obter_zsql(cod_materia=cod_materia, ind_excluido=0):
            data['codmateria'] = materia.cod_materia
            data['tipo'] = materia.des_tipo_materia
            data['numero'] = materia.num_ident_basica
            data['ano'] = materia.ano_ident_basica
            data['ementa'] = materia.txt_ementa
            data['autoria'] = ''
            autores = self.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia, ind_excluido=0)
            fields = autores.data_dictionary().keys()
            lista_autor = []
            for autor in autores:
                for field in fields:
                    nome_autor = autor['nom_autor_join']
                lista_autor.append(nome_autor)
            data['autoria'] = ', '.join(['%s' % (value) for (value) in lista_autor])
            data['linkarquivo'] = ''
            if hasattr(self.sapl_documentos.materia, str(materia.cod_materia) + '_texto_integral.pdf'):
               data['linkarquivo'] = self.portal_url() + '/sapl_documentos/materia/' + str(materia.cod_materia) + '_texto_integral.pdf'
            data['casalegislativa'] = self.sapl_documentos.props_sagl.nom_casa

        serialized = json.dumps(data, sort_keys=True, indent=3)

        return json.loads(serialized)


    def protocolo_prefeitura(self, cod_materia):

        API_ENDPOINT = ''
        API_USER = ''
        API_PASSWORD = ''
        session = requests.Session()
        session.auth = (API_USER, API_PASSWORD)
        auth = session.post(API_ENDPOINT)
        response = session.post(API_ENDPOINT, data=self.create_payload(cod_materia))

        if (response.status_code == 200):
            r = response.json()
            protocolo = r[0]['numero_protocolo']
            data = DateTime(r[0]['criado_em']).strftime('%d/%m/%Y às %H:%M:%S')
            return 'Protocolado na Prefeitura Municipal sob nº ' + str(protocolo) + ' em ' + str(data)
        else:
            r = response.json()
            msg = r[0]['Detail'] + 'Houve um erro ao enviar a matéria para a Prefeitura. Código da matéria: ' + cod_materia
            raise ValueError(msg)


    def cep_buscar(self, numcep):

        url = 'https://brasilapi.com.br/api/cep/v2/%s'%numcep
        resposta = requests.get(url)
        dic_requisicao = resposta.json()
        cepArray=[]
        if 'errors' not in dic_requisicao:
           cepDict = {}
           cepDict['logradouro'] = dic_requisicao['street']
           cepDict['bairro'] = dic_requisicao['neighborhood']
           cepDict['cidade'] = dic_requisicao['city']
           cepDict['estado'] = dic_requisicao['state']
           cepArray.append(cepDict)
           return json.dumps(cepDict)


InitializeClass(SAGLTool)
