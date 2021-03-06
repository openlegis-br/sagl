# -*- coding: utf-8 -*-

import re
import os
import requests

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

from PIL import Image

#imports para a geracao dos documentos
import uuid
import urllib
import urllib2
import cStringIO
import StringIO
from appy.pod.renderer import Renderer
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
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
          self.temp_folder.manage_delObjects(ids=nom_arquivo_pdf)
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
          self.temp_folder.manage_delObjects(ids=nom_pdf_amigavel)
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

    def capa_processo_gerar_odt(self, inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_proposicao, des_tipo_materia, nom_autor, txt_ementa, regime_tramitacao, nom_arquivo):
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/capa_processo.odt"
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

    def capa_processo_adm_gerar_odt(self, inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_documento, des_tipo_documento, txt_interessado, txt_assunto, nom_arquivo):
        url = self.sapl_documentos.modelo.documento_administrativo.absolute_url() + "/capa_processo_adm.odt"
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
           self.sapl_documentos.administrativo.tramitacao.manage_delObjects(ids=arquivoPdfAnexo)
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
        self.temp_folder.manage_delObjects(ids=arquivoPdf)

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
           self.sapl_documentos.materia.tramitacao.manage_delObjects(ids=arquivoPdfAnexo)
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
        self.temp_folder.manage_delObjects(ids=arquivoPdf)

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
        self.temp_folder.manage_delObjects(ids=nom_pdf_amigavel)
        return arq

    # obter altura da pagina
    def getPageSizeH(self, p):
        h = int(p.mediaBox.getHeight())
        return h

    # obter largura da pagina
    def getPageSizeW(self, p):
        w = int(p.mediaBox.getWidth())
        return w

    def parecer_gerar_odt(self, inf_basicas_dic, nom_arquivo, nom_comissao, materia, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao):
        url = self.sapl_documentos.modelo.materia.parecer.absolute_url() + "/parecer.odt"
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

    def processo_adm_gerar_pdf(self,cod_documento):
        writer = PdfWriter()
        for documento in self.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
           nom_pdf_amigavel = documento.sgl_tipo_documento+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+'.pdf'
           id_processo = documento.sgl_tipo_documento+' '+str(documento.num_documento)+'/'+str(documento.ano_documento)
        nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        if hasattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf'):
           arq = getattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf')
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_documento = PdfReader(arquivo, decompress=False).pages
           writer.addpages(texto_documento)
        elif hasattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf'):
           arq = getattr(self.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf')
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_documento = PdfReader(arquivo, decompress=False).pages
           writer.addpages(texto_documento)
        for docadm in self.zsql.documento_acessorio_administrativo_obter_zsql(cod_documento=cod_documento,ind_excluido=0):
           cod_documento_acessorio = docadm.cod_documento_acessorio
           if hasattr(self.sapl_documentos.administrativo, str(cod_documento_acessorio) + '.pdf'):
              doc = getattr(self.sapl_documentos.administrativo, str(cod_documento_acessorio) + '.pdf')
              arquivo_doc = cStringIO.StringIO(str(doc.data))
              texto_doc = PdfReader(arquivo_doc, decompress=False).pages
              writer.addpages(texto_doc)
        for tram in self.zsql.tramitacao_administrativo_obter_zsql(cod_documento=cod_documento,rd_ordem='1',ind_excluido=0):
            tramitacao = tram.cod_tramitacao
            if hasattr(self.sapl_documentos.administrativo.tramitacao, str(tramitacao) + '_tram.pdf'):
               tram = getattr(self.sapl_documentos.administrativo.tramitacao, str(tramitacao) + '_tram.pdf')
               existe_arquivo = 1
            elif hasattr(self.sapl_documentos.administrativo.tramitacao, str(tramitacao) + '_tram_signed.pdf'):
               tram = getattr(self.sapl_documentos.administrativo.tramitacao, str(tramitacao) + '_tram_signed.pdf')
               existe_arquivo = 1
            else:
               existe_arquivo = 0
            if existe_arquivo == 1:
               arquivo_tram = cStringIO.StringIO(str(tram.data))
               texto_tramitacao = PdfReader(arquivo_tram).pages
               writer.addpages(texto_tramitacao)
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
        self.temp_folder.manage_delObjects(ids=nom_pdf_amigavel)
        return arq

    def processo_eletronico_gerar_pdf(self,cod_materia):
        if cod_materia.isdigit():
           cod_materia = cod_materia
        else:
           cod_materia = self.pysc.b64decode_pysc(codigo=str(cod_materia))     
        for materia in self.zsql.materia_obter_zsql(cod_materia=cod_materia):
           nom_pdf_amigavel = materia.sgl_tipo_materia+'-'+str(materia.num_ident_basica)+'-'+str(materia.ano_ident_basica)+'.pdf'
           nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
           id_processo = materia.sgl_tipo_materia+' '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)
        writer = PdfWriter()
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
        if hasattr(self.sapl_documentos.materia, str(cod_materia) + '_texto_integral.pdf'):
           arq = getattr(self.sapl_documentos.materia, str(cod_materia) + '_texto_integral.pdf')
           arquivo = cStringIO.StringIO(str(arq.data))
           texto_materia = PdfReader(arquivo, decompress=False).pages
           writer.addpages(texto_materia)
        for substitutivo in self.zsql.substitutivo_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
            subst = substitutivo.cod_substitutivo
            if hasattr(self.sapl_documentos.substitutivo, str(subst) + '_substitutivo.pdf'):
               subst = getattr(self.sapl_documentos.substitutivo, str(subst) + '_substitutivo.pdf')
               arquivo_subst = cStringIO.StringIO(str(subst.data))
               texto_subst = PdfReader(arquivo_subst).pages
               writer.addpages(texto_subst)
        for eme in self.zsql.emenda_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
            emenda = eme.cod_emenda
            if hasattr(self.sapl_documentos.emenda, str(emenda) + '_emenda.pdf'):
               pdf_emenda = getattr(self.sapl_documentos.emenda, str(emenda) + '_emenda.pdf')
               arquivo_emenda = cStringIO.StringIO(str(pdf_emenda.data))
               texto_emenda = PdfReader(arquivo_emenda).pages
               writer.addpages(texto_emenda)
        for relat in self.zsql.relatoria_obter_zsql(cod_materia=cod_materia,ind_excluido=0):
            relatoria = relat.cod_relatoria
            if hasattr(self.sapl_documentos.parecer_comissao, str(relatoria) + '_parecer.pdf'):
               pdf_relatoria = getattr(self.sapl_documentos.parecer_comissao, str(relatoria) + '_parecer.pdf')
               arquivo_relatoria = cStringIO.StringIO(str(pdf_relatoria.data))
               texto_relatoria = PdfReader(arquivo_relatoria).pages
               writer.addpages(texto_relatoria)
        for anexada in self.zsql.anexada_obter_zsql(cod_materia_principal=cod_materia,ind_excluido=0):
            anexada = anexada.cod_materia_anexada
            if hasattr(self.sapl_documentos.materia, str(anexada) + '_texto_integral.pdf'):
               pdf_anexada = getattr(self.sapl_documentos.materia, str(anexada) + '_texto_integral.pdf')
               arquivo_anexada = cStringIO.StringIO(str(pdf_anexada.data))
               texto_anexada = PdfReader(arquivo_anexada).pages
               writer.addpages(texto_anexada)
        for documento in self.zsql.documento_acessorio_obter_zsql(cod_materia = cod_materia,ind_excluido=0):
           cod_documento = documento.cod_documento
           proposicao = self.zsql.proposicao_obter_zsql(ind_mat_ou_doc='D',cod_mat_ou_doc=cod_documento,ind_excluido=0)
           if proposicao:
              cod_proposicao = proposicao[0].cod_proposicao
              if hasattr(self.sapl_documentos.proposicao, str(cod_proposicao) + '_signed.pdf'):
                 pdf_proposicao = getattr(self.sapl_documentos.proposicao, str(cod_proposicao) + '_signed.pdf')
                 arquivo_proposicao = cStringIO.StringIO(str(pdf_proposicao.data))
                 texto_proposicao = PdfReader(arquivo_proposicao).pages
                 writer.addpages(texto_proposicao)
           else:
              if hasattr(self.sapl_documentos.materia, str(cod_documento) + '.pdf'):
                 pdf_documento = getattr(self.sapl_documentos.materia, str(cod_documento) + '.pdf')
                 arquivo_documento = cStringIO.StringIO(str(pdf_documento.data))
                 texto_documento = PdfReader(arquivo_documento).pages
                 writer.addpages(texto_documento)
        for tram in self.zsql.tramitacao_obter_zsql(cod_materia=cod_materia,rd_ordem='1',ind_excluido=0):
            tramitacao = tram.cod_tramitacao
            if hasattr(self.sapl_documentos.materia.tramitacao, str(tramitacao) + '_tram.pdf'):
               tram = getattr(self.sapl_documentos.materia.tramitacao, str(tramitacao) + '_tram.pdf')
               existe_arquivo = 1
            elif hasattr(self.sapl_documentos.materia.tramitacao, str(tramitacao) + '_tram_signed.pdf'):
               tram = getattr(self.sapl_documentos.materia.tramitacao, str(tramitacao) + '_tram_signed.pdf')
               existe_arquivo = 1
            else:
               existe_arquivo = 0
            if existe_arquivo == 1:
               arquivo_tram = cStringIO.StringIO(str(tram.data))
               texto_tramitacao = PdfReader(arquivo_tram).pages
               writer.addpages(texto_tramitacao)
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
        self.temp_folder.manage_delObjects(ids=nom_pdf_amigavel)
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
              texto = str(documento.des_tipo_documento.decode('utf-8').upper())+' AO ' + str(materia)
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

        url = self.url() + '/sapl_documentos/proposicao/' + nom_pdf_proposicao
        opener = urllib.urlopen(url)
        f = open('/tmp/' + nom_pdf_proposicao, 'wb').write(opener.read())
        existing_pdf = PdfFileReader('/tmp/'+ nom_pdf_proposicao, strict=False)
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
        d.setFont("Arial_Bold", 12)
        # alinhamento a esquerda
        d.drawString(85, 700, texto)
        # alinhamento centralizado
        #d.drawCentredString(pwidth/2, 700, texto)
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
            if self.sapl_documentos.props_sagl.restpki_access_token!='':
               for wm in range(new_pdf.getNumPages()):
                   watermark_page = new_pdf.getPage(wm)
                   if page == wm:
                      pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)
        outputStream = file('/tmp/' + nom_pdf_saida, "wb")
        output.write(outputStream)
        outputStream.close()
        data = open('/tmp/' + nom_pdf_saida, 'rb').read()              
        if nom_pdf_saida in storage_path:
           documento = getattr(storage_path,nom_pdf_saida)
           documento.manage_upload(file=data)
        else:
           storage_path.manage_addFile(id=nom_pdf_saida,file=data)
        os.unlink('/tmp/'+nom_pdf_saida)
        os.unlink('/tmp/'+nom_pdf_proposicao)

    def restpki_client(self):
        restpki_url = 'https://restpkiol.azurewebsites.net/'
        #restpki_url = 'https://pki.rest/'
        restpki_access_token = self.sapl_documentos.props_sagl.restpki_access_token            
        restpki_client = RestPkiClient(restpki_url, restpki_access_token)
        return restpki_client

    def pades_signature(self, codigo, tipo_doc, cod_usuario):
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
                      storage_path = self.sapl_documentos.administrativo
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

        # Verifica se existe arquivo    
        tmp_path = '/tmp'        
        if os.path.exists(os.path.join(tmp_path, pdf_tosign)):
           os.unlink(os.path.join(tmp_path, pdf_tosign))           
           msg = 'O documento está em processo de assinatura! Tente novamente em instantes...'
           raise ValueError(msg)
        else:
           # Read the PDF path
           arq = getattr(storage_path, pdf_tosign)
           arquivo = cStringIO.StringIO(str(arq.data))           
           arquivo.seek(0)
           f = open('/tmp/' + pdf_tosign, 'wb').write(arquivo.read())
        
        pdf_tmp = pdf_tosign
        pdf_path = '%s/%s' % (tmp_path, pdf_tosign)

        # Read the PDF stamp image
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()  
        id_logo = portal.sapl_documentos.props_sagl.id_logo
        if hasattr(self.sapl_documentos.props_sagl, id_logo):
           url = self.url() + '/sapl_documentos/props_sagl/' + id_logo
        else:
           url = self.url() + '/imagens/brasao.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        f = open('/tmp/' + id_logo, 'rb')
        pdf_stamp = f.read()
        f.close()

        signature_starter = PadesSignatureStarter(self.restpki_client())
        signature_starter.set_pdf_path(pdf_path)
        signature_starter.signature_policy_id = StandardSignaturePolicies.PADES_BASIC
        signature_starter.security_context_id = StandardSecurityContexts.PKI_BRAZIL
        if tipo_doc == 'peticao' or tipo_doc == 'tramitacao' or tipo_doc == 'tramitacao_adm' or tipo_doc == 'norma':
#        if len(qtde_assinaturas) <= 3:
           signature_starter.visual_representation = ({
               'text': {
                   # The tags {{signerName}} and {{signerNationalId}} will be substituted according to the user's
                   # certificate
                   # signerName -> full name of the signer
                   # br_cpf_formatted -> if the certificate is ICP-Brasil, contains the signer's CPF
                   'text': 'Assinado digitalmente por {{signerName}} {{br_cpf_formatted}}',
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
        else:
#        elif len(qtde_assinaturas) >= 3:
           signature_starter.visual_representation = ({
               'text': {
                   # The tags {{signerName}} and {{signerNationalId}} will be substituted according to the user's
                   # certificate
                   # signerName -> full name of the signer
                   # br_cpf_formatted -> if the certificate is ICP-Brasil, contains the signer's CPF
                   'text': 'Assinado digitalmente por {{signerName}} {{br_cpf_formatted}}',
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
               'position': self.get_visual_representation_position(4)
           })
        token = signature_starter.start_with_webpki()
 
        return token, pdf_path, codigo, tipo_doc, cod_usuario

    def pades_signature_action(self, token, codigo, tipo_doc, cod_usuario):
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

        tmp_path = "/tmp"

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

        signature_finisher.write_signed_pdf(os.path.join(tmp_path, file_hash))

        data = open('/tmp/' + file_hash, "rb").read()

        for file in [file_hash]:
            if tipo_doc != 'proposicao':  
               self.margem_direita(codigo, tipo_doc, cod_assinatura_doc, cod_usuario, file_hash)
            if hasattr(storage_path,filename):
               documento = getattr(storage_path,filename)
               documento.manage_upload(file=data)
               if os.path.exists(os.path.join(tmp_path, file_hash)):
                  os.unlink(os.path.join(tmp_path, file_hash))
               if os.path.exists(os.path.join(tmp_path, filename)):
                  os.unlink(os.path.join(tmp_path, filename))                  
               if os.path.exists(os.path.join(tmp_path, old_filename)):
                  os.unlink(os.path.join(tmp_path, old_filename))
            else:
               storage_path.manage_addFile(id=filename,file=data)
               if os.path.exists(os.path.join(tmp_path, file_hash)):
                  os.unlink(os.path.join(tmp_path, file_hash))
               if os.path.exists(os.path.join(tmp_path, filename)):
                  os.unlink(os.path.join(tmp_path, filename))                    
               if os.path.exists(os.path.join(tmp_path, old_filename)):
                  os.unlink(os.path.join(tmp_path, old_filename))

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

        qtde_assinaturas = []
        for item in self.zsql.assinatura_documento_obter_zsql(cod_assinatura_doc=cod_assinatura_doc):
            qtde_assinaturas.append(item.cod_usuario)        
            if item.ind_assinado == 1:
               if item.ind_prim_assinatura == 1:
                  for usuario in self.zsql.usuario_obter_zsql(cod_usuario=item.cod_usuario):
                      nom_autor = usuario.nom_completo
                      break
               else:
                  for usuario in self.zsql.usuario_obter_zsql(cod_usuario=cod_usuario): 
                      nom_autor = usuario.nom_completo
                      break 
            else:
                  for usuario in self.zsql.usuario_obter_zsql(cod_usuario=cod_usuario): 
                      nom_autor = usuario.nom_completo
                      break             
            if len(qtde_assinaturas) == 2:
               outros = " e outro"
            elif len(qtde_assinaturas) > 2:
               outros = " e outros"
            else:
               outros = ''                                 

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
           storage_path = self.sapl_documentos.administrativo
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
        #arq = getattr(self.sapl_documentos.documentos_assinados, nom_pdf_assinado)
        arq = open('/tmp/' + file_hash, "rb")
        #arquivo = cStringIO.StringIO(arq)
        existing_pdf = PdfFileReader(arq, strict=False)
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
           documento = getattr(storage_path,nom_pdf_documento)
           documento.manage_upload(file=outputStream.getvalue())
        else:
           storage_path.manage_addFile(nom_pdf_documento)
           output.write(outputStream)
           arq=storage_path[nom_pdf_documento]
           arq.manage_edit(title=nom_pdf_documento,filedata=outputStream.getvalue(),content_type='application/pdf')

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
        url = self.url() + '/sapl_documentos/proposicao/' + pdf_proposicao
        opener = urllib.urlopen(url)
        f = open('/tmp/' + pdf_proposicao, 'wb').write(opener.read())
        arq = open('/tmp/' + pdf_proposicao, "rb")
        existing_pdf = PdfFileReader(arq, strict=False)
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
           documento = getattr(storage_path,pdf_assinado)
           documento.manage_upload(file=outputStream.getvalue())
        else:
           storage_path.manage_addFile(pdf_assinado)
           output.write(outputStream)
           arq=storage_path[pdf_assinado]
           arq.manage_edit(title=pdf_assinado,filedata=outputStream.getvalue(),content_type='application/pdf')

        if os.path.exists(os.path.join('/tmp/', pdf_proposicao)):
           os.unlink(os.path.join('/tmp/', pdf_proposicao))

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

        # obtem dados da sessao
        for item in self.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen):
            for tipo in self.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=item.tip_sessao):
                id_sessao = str(item.num_sessao_plen) + 'ª Sessão ' + tipo.nom_sessao
            data = item.dat_inicio_sessao
            num_legislatura = item.num_legislatura
            data1 = self.pysc.data_converter_pysc(item.dat_inicio_sessao)            

        # obtem presidente da sessao
        nom_presidente = ''       
        for composicao in self.zsql.composicao_mesa_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen, cod_cargo=1, ind_excluido=0):
            for parlamentar in self.zsql.parlamentar_obter_zsql(cod_parlamentar=composicao.cod_parlamentar):
                nom_presidente = str(parlamentar.nom_parlamentar.decode('utf-8').upper())

        # se for vazio, obter presidente da Casa                
        if nom_presidente == '':
           data1 = self.pysc.data_converter_pysc(data) 
           for sleg in self.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=num_legislatura, data=data1):
               for cod_presidente in self.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp, cod_cargo=1):
                   for presidencia in self.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
                       nom_presidente = str(presidencia.nom_parlamentar.decode('utf-8').upper())
 
        # prepara carimbo
        packet = StringIO.StringIO()
        can = canvas.Canvas(packet)
        can.drawImage(logo, 490, 695,  width=50, height=50, mask='auto')
        texto = "%s" % (str(nom_resultado.decode('utf-8').upper()))
        sessao = "%s - %s" % (id_sessao, data)
        presidente = "%s " % (nom_presidente)
        cargo = "Presidente"
        pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))   
        pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))             
        can.setFont('Arial_Bold', 10)
        can.drawString(400, 730, texto)
        can.setFont('Arial', 9)
        can.drawString(400, 720, sessao)
        can.drawString(400, 710, presidente)
        can.drawString(400, 700, cargo)          
        can.showPage()              
        can.save()     
        new_pdf = PdfFileReader(packet)         
        output = PdfFileWriter()     
        # adiciona carimbo aos documentos               
        for item in self.zsql.ordem_dia_obter_zsql(cod_sessao_plen=cod_sessao_plen, cod_materia=cod_materia):
            data = item.dat_ordem
            for materia in self.zsql.materia_obter_zsql(cod_materia=item.cod_materia):
                if materia.des_tipo_materia == 'Requerimento':
                   storage_path = self.sapl_documentos.materia
                   nom_pdf_saida = str(materia.cod_materia) + "_texto_integral.pdf"                
                   if hasattr(storage_path, nom_pdf_saida):
                      url = self.url() + '/sapl_documentos/materia/' + nom_pdf_saida
                      opener = urllib.urlopen(url)
                      f = open('/tmp/' + nom_pdf_saida, 'wb').write(opener.read())
                      existing_pdf = PdfFileReader('/tmp/'+ nom_pdf_saida, strict=False)
                      numPages = existing_pdf.getNumPages()
                      # Mescla canvas
                      for page in range(existing_pdf.getNumPages()):
                          page_pdf = existing_pdf.getPage(page)
                          # carimbo na primeira pagina
                          if page == 0:
                             page_pdf.mergePage(new_pdf.getPage(0))
                          output.addPage(page_pdf)
                      outputStream = file('/tmp/' + nom_pdf_saida, "wb")                          
                      output.write(outputStream)
                      outputStream.close()
                      data = open('/tmp/' + nom_pdf_saida, 'rb').read()
                      documento = getattr(storage_path,nom_pdf_saida)
                      documento.manage_upload(file=data)
                      os.unlink('/tmp/'+nom_pdf_saida) 
        
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

InitializeClass(SAGLTool)

