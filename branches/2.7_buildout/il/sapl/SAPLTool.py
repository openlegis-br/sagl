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
import cStringIO
from appy.pod.renderer import Renderer

#imports para o maps
import sys
import six
import base64
import simplejson as json

from lacunarestpki import *

from zope.testbrowser.browser import Browser
browser = Browser()

restpki_access_token = 'xmf2cIV29DFzg20PTIbRyTLR0nxnk9VvC1LYVsXdvy0YUKYZnrHFam8SivOCZEquEmQfIv44jT0W4RnjCjxAgDfbT2Iwcp6d5IZGAItx_vaY8SMXiPMuDN5MVhTvFGoYL2mXMswggcJcq4pj7wgFttBnVneWJOnCeMmlIBOT4KbHSWqLc8ZpG78khrQ_ou1lhhqKrUD05cHXa6LcfPen8Ub2Ja3sNwRnZ1hjEUL5DGc9-kEND4UwTcVBZTPle2ckZ16PSIaxOMi9BeL4httwsreYT_eie8UpEevSEJeOMRK2a5RKy1FfK2TK1zwAdSnfl0cH5bpeqlyl4d2dnFjtpwca_aNBuQuHLtuOv1W-TjFlaXaiWgsoJS5U1Qv3W6Neq7YsZzyxqnwFMQUbtdP612yu6bw2J3K6sQBZhym1UCQM08jEJy86HSoA5NekYv0IzyH2tovIVpTBYgbcQRQa6GsqAsn0jYp6VdSwVeDWYy4B8pcuUCj9pL1AAbQrcfO09wh6nA'                       

restpki_url = 'https://pki.rest/'
restpki_client = RestPkiClient(restpki_url, restpki_access_token)

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

    nome_arquivo = 'tmp_token_' + str(os.getpid())
    nome_arquivo_atribuido = 'tmp_atribuido_' + str(os.getpid())
    local_arquivo = '/tmp'

    def get_geolocations(self, cidade, cep):
        cidade = cidade.encode('utf-8')
        try:
            cep = cep.encode('utf-8')
        except:
            pass
        url = 'http://maps.google.com/maps/api/geocode/json?address=' + cidade + '&components=postal_code:' + cep + '&sensor=false'
        resp = urllib.urlopen(url).read()
        data = json.loads(resp)
        geolocation = []
        for results in data['results']:
            address_components = results['address_components']
            errado = False
            for address in address_components:
                if 'postal_code' in address['types']:
                    if len(address['long_name']) == 5:
                        if cep.split('-')[0] != address['long_name']:
                            errado = True
                    else:
                        if cep != address['long_name']:
                            errado = True
            if not errado:
                geometry = dict(results['geometry'])
                location = geometry['location']
                lat = str(location['lat'])
                lng = str(location['lng'])
                geolocation.append(lat)
                geolocation.append(lng)
        return geolocation

    def tempo_sessao(self, tempo):
        # retorna a data de inicio da sessao em milisegundos
        dt = datetime.strptime(tempo, "%d/%m/%Y %H:%M")
        return time.mktime(dt.timetuple()) * 1000

    def arquivo_atribuido(self, criar = None):
        path = self.local_arquivo + '/' + self.nome_arquivo_atribuido
        temporarios = os.listdir(self.local_arquivo)

        for temporario in temporarios:
            if temporario.startswith('tmp_atribuido_') and temporario != self.nome_arquivo_atribuido:
                os.unlink(self.local_arquivo + '/' + temporario)

        if criar:
            try:
                os.unlink(path)
                return os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, 0600), 'wb')
            except OSError:
                return os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, 0600), 'wb')
        else:
            return os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, 0600), 'wb')

    def remover_arquivo_atribuido(self):
        arquivo = self.arquivo_atribuido()
        arquivo.close()
        path = self.local_arquivo + '/' + self.nome_arquivo_atribuido
        os.unlink(path)

    def grava_arquivo_atribuido(self, arquivo, data):
        pickle.dump(data, arquivo)

    def ler_arquivo_atribuido(self):
        lista = []
        path = self.local_arquivo + '/' + self.nome_arquivo_atribuido
        try:
            arquivo = open(path, 'rb')
        except IOError:
            return []
        while 1:
            try:
                lista.append(pickle.load(arquivo))
            except:
                break

        arquivo.close()

        return lista

    def arquivo_token(self, criar=None):
        path = self.local_arquivo + '/' + self.nome_arquivo
        temporarios = os.listdir(self.local_arquivo)

        for temporario in temporarios:
            if temporario.startswith('tmp_token_') and temporario != self.nome_arquivo:
                os.unlink(self.local_arquivo + '/' + temporario)

        if criar:
            try:
                os.unlink(path)
                return os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, 0600), 'wb')
            except OSError:
                return os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, 0600), 'wb')
        else:
            return os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT, 0600), 'wb')

    def nome_arquivo_token(self):
        return self.nome_arquivo

    def gera_token(self, cod_sessao_plen, criar=None):
        presenca = self.zsql.presenca_ordem_dia_obter_zsql(
            cod_sessao_plen = cod_sessao_plen,
            ind_excluido = 0
        )

        codigos = [i.cod_parlamentar for i in presenca]

        tokens = [self.encrypt(codigo) for codigo in codigos]


        arquivo = self.arquivo_token(criar)
        for token in tokens:
            data = {}
            lista = []
            lista.append('')
            lista.append('')
            data[token] = lista
            self.grava_token(arquivo, data)

        arquivo.close()

        return len(tokens)

    def existe_token(self):
        if len(self.ler_token()) > 0:
            return True
        else:
            return False

    def remover_token(self):
        arquivo = self.arquivo_token()
        arquivo.close()
        path = self.local_arquivo + '/' + self.nome_arquivo
        os.unlink(path)

    def grava_token(self, arquivo, data):
        pickle.dump(data, arquivo)

    def ler_token(self):
        lista = []
        path = self.local_arquivo + '/' + self.nome_arquivo
        try:
            arquivo = open(path, 'rb')
        except IOError:
            return []
        while 1:
            try:
                lista.append(pickle.load(arquivo))
            except:
                break

        arquivo.close()

        return lista

    def generate_salt(self):
        salt = ''
        for n in range(7):
            salt += chr(randrange(256))
        return salt

    def encrypt(self, pw):
        pw = str(pw)
        salt = self.generate_salt()
        return b2a_base64(sha.new(pw + salt).digest() + salt)[:-1]

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

            # solucao temporaria
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

            # solucao temporaria
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
            #            else:
            #                urn += 'inicio.vigencia;publicacao;'
            #
            #            if consulta.dat_publicacao:
            #                urn += self.pysc.port_to_iso_pysc(consulta.dat_publicacao)

            return urn
        else:
            return None

    def monta_xml(self,urn,cod_norma):
        #criacao do xml

        # consultas
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

        # garante que a data 'until'(ate) esteja setada, e nao no futuro
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
            #resultado['id_registro_item'] = resultado['name']
            #del resultado['name']
            #record['sets'] = record['sets'].strip().split(' ')
            #if resultado['sets'] == [u'']:
            #    resultado['sets'] = []
            resultado['cd_status'] = 'N'
            resultado['id'] = identificador
            resultado['when_modified'] = norma.timestamp
            resultado['deleted'] = 0
            if norma.ind_excluido == 1:
                resultado['deleted'] = 1
            #                resultado['cd_status'] = 'D'
            yield {'record': resultado,
                   #                   'sets': ['person'],
                   'metadata': resultado['tx_metadado_xml'],
                   #                   'assets':{}
            }

    def url(self):
        utool = getToolByName(self, 'portal_url')
        return utool.portal_url()

    def get_brasao(self):
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sapl.id_logo
        if id_logo in portal.sapl_documentos.props_sapl.objectValues('Image'):
            url = self.url() + '/sapl_documentos/props_sapl/' + id_logo
        else:
            url = self.url() + '/imagens/brasao.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        brasao = open('/tmp/' + id_logo, 'rb')
        os.unlink('/tmp/' + id_logo)
        return brasao

    def gerar_ata_odt(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_oradores, lst_presidente, lst_psecretario, lst_ssecretario):
        # Criacao ODT
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/ata.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "ata_sessao.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_iom_odt(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_oradores, lst_presidente, lst_psecretario, lst_ssecretario):
        # Criacao ODT
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/iom.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_odt = "publicacao_iom.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_materia_apreciada_odt(self, inf_basicas_dic, lst_votacao):
        # Criacao ODT
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/materia_apreciada.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "materia_apreciada.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_ordem_dia_odt(self, inf_basicas_dic, lst_votacao, lst_presidente):
        # Criacao ODT
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/ordem_dia.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "ordem_dia.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_resumo_odt(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_oradores, lst_presidente, lst_psecretario, lst_ssecretario):
        # Criacao ODT
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/resumo.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "resumo_sessao.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_acessorio_odt(self, inf_basicas_dic, nom_arquivo, des_tipo_documento, nom_documento, txt_ementa, dat_documento, data_documento, nom_autor, materia_vinculada, modelo_proposicao):
        # Criacao ODT
        url = self.sapl_documentos.modelo.materia.documento_acessorio.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.materia_odt.manage_addFile(id=nom_arquivo,file=data)

    def gerar_oficio_ind_odt(self, inf_basicas_dic, lst_indicacao, lst_presidente):
        # Criacao ODT
        url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/oficio_indicacao.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "oficio_indicacao.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_emenda_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        # Criacao ODT
        url = self.sapl_documentos.modelo.materia.emenda.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.emenda.manage_addFile(id=nom_arquivo,file=data)

    def gerar_materia_odt(self, inf_basicas_dic, num_proposicao, nom_arquivo, des_tipo_materia, num_ident_basica, ano_ident_basica, txt_ementa, materia_vinculada, dat_apresentacao, nom_autor, apelido_autor, modelo_proposicao):
        # Criacao ODT
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/%s" % modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.materia_odt.manage_addFile(id=nom_arquivo,file=data)

    def gerar_materia_pdf(self, cod_materia):
        # Conversao para PDF
        nom_arquivo_odt = "%s"%cod_materia+'_texto_integral.odt'
        nom_arquivo_pdf1 = "%s"%cod_materia+'_texto_integral.pdf'
        nom_arquivo_pdf2 = "%s"%cod_materia+'_texto_integral'
        url = self.sapl_documentos.materia_odt.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            self.sapl_documentos.materia.manage_addFile(id=nom_arquivo_pdf1, file=data)
            os.unlink(file)

    def ordem_dia_gerar_pdf(self, cod_sessao_plen):
        # Conversao para PDF
        nom_arquivo_odt = "%s"%cod_sessao_plen+'_pauta_sessao.odt'
    	nom_arquivo_pdf = "%s"%cod_sessao_plen+'_pauta_sessao.pdf'
    	url = self.sapl_documentos.pauta_sessao.absolute_url() + "/%s"%nom_arquivo_odt
    	odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    	output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    	renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3')
    	renderer.run()
    	data = open(output_file_pdf, "rb").read()
    	for file in [output_file_pdf]:
    	    self.sapl_documentos.pauta_sessao.manage_addFile(id=nom_arquivo_pdf,file=data)
    	    os.unlink(file)

    def gerar_proposicao_pdf(self, cod_proposicao):
        # Conversao para PDF
        nom_arquivo_odt = "%s" % cod_proposicao+'.odt'
        nom_arquivo_pdf1 = "%s" % cod_proposicao+'.pdf'
        nom_arquivo_pdf2 = str(cod_proposicao)
        url = self.sapl_documentos.proposicao.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            self.sapl_documentos.proposicao.manage_addFile(id=nom_arquivo_pdf1, file=data)
            os.unlink(file)

    def gerar_norma_odt(self, inf_basicas_dic, nom_arquivo, des_tipo_norma, num_norma, ano_norma, dat_norma, data_norma, txt_ementa, modelo_norma):
        # Criacao ODT
        url = self.sapl_documentos.modelo.norma.absolute_url() + "/%s" % modelo_norma
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.norma_juridica.manage_addFile(id=nom_arquivo,file=data)

    def gerar_norma_pdf(self, cod_norma):
        # Conversao para PDF
        nom_arquivo_odt = "%s"%cod_norma+'_texto_integral.odt'
        nom_arquivo_pdf1 = "%s"%cod_norma+'_texto_consolidado.pdf'
        nom_arquivo_pdf2 = "%s"%cod_norma+'_texto_consolidado'
        url = self.sapl_documentos.norma_juridica.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            self.sapl_documentos.norma_juridica.manage_addFile(id=nom_arquivo_pdf1, file=data)
            os.unlink(file)

    def gerar_proposicao_pdf(self, cod_proposicao):
        # Conversao para PDF
        nom_arquivo_odt = "%s"%cod_proposicao+'.odt'
        nom_arquivo_pdf1 = "%s"%cod_proposicao+'.pdf'
        url = self.sapl_documentos.proposicao.absolute_url() + "/%s"%nom_arquivo_odt
        odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
        output_file_pdf = os.path.normpath(nom_arquivo_pdf1)
        renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_pdf, "rb").read()
        for file in [output_file_pdf]:
            self.sapl_documentos.proposicao.manage_addFile(id=nom_arquivo_pdf1, file=data)
            os.unlink(file)

    def gerar_oficio_odt(self, inf_basicas_dic, nom_arquivo, sgl_tipo_documento, num_documento, ano_documento, txt_ementa, dat_documento, dia_documento, nom_autor, modelo_documento):
        # Criacao ODT
        url = self.sapl_documentos.modelo.documento_administrativo.absolute_url() + "/%s" % modelo_documento
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s" % nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.administrativo.manage_addFile(id=nom_arquivo,file=data)

    def gerar_oficio_moc_odt(self, inf_basicas_dic, num_ident_basica, nom_autor):
        # Criacao ODT
        url = self.sapl_documentos.modelo.documento_administrativo.absolute_url() + "/oficio_mocao.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "oficio_mocao.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_oficio_req_pres_odt(self, inf_basicas_dic, num_ident_basica, nom_autor):
        # Criacao ODT
        url = self.sapl_documentos.modelo.documento_administrativo.absolute_url() + "/oficio_requerimento_pres.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "oficio_req_presidencia.odt"
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
        self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
        return data

    def gerar_parecer_odt(self, inf_basicas_dic,nom_arquivo,nom_comissao, materia, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao):
        # Criacao ODT
        url = self.sapl_documentos.modelo.materia.parecer.absolute_url() + "/parecer.odt"
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.parecer_comissao.manage_addFile(id=nom_arquivo,file=data)

    def gerar_proposicao_odt(self, inf_basicas_dic, num_proposicao,nom_arquivo,des_tipo_materia,num_ident_basica,ano_ident_basica,txt_ementa,materia_vinculada,dat_apresentacao,nom_autor,apelido_autor,modelo_proposicao):
        # Criacao ODT
        url = self.sapl_documentos.modelo.materia.absolute_url() + "/%s"%modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.proposicao.manage_addFile(id=nom_arquivo,file=data)

    def gerar_substitutivo_odt(self,inf_basicas_dic, num_proposicao,nom_arquivo,des_tipo_materia,num_ident_basica,ano_ident_basica,txt_ementa,materia_vinculada,dat_apresentacao,nom_autor,apelido_autor,modelo_proposicao):
        # Criacao ODT
        url = self.sapl_documentos.modelo.materia.substitutivo.absolute_url() + "/%s"%modelo_proposicao
        template_file = cStringIO.StringIO(urllib.urlopen(url).read())
        brasao_file = self.get_brasao()

        # atribui o brasao no locals
        exec 'brasao = brasao_file'

        output_file_odt = "%s"%nom_arquivo
        renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3')
        renderer.run()
        data = open(output_file_odt, "rb").read()
        for file in [output_file_odt]:
            os.unlink(file)
            self.sapl_documentos.substitutivo.manage_addFile(id=nom_arquivo,file=data)


    def pades_signature(self, cod_proposicao):

        # If the user was redirected here by /upload (signature with file uploaded by user), the "userfile" route argument
        # will contain the filename under the uploads/ folder. Otherwise (signature with server file), we'll sign a sample
        # document.
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
        #pdf_path = open('/tmp/' + pdf_file, 'rb')

        # Read the PDF stamp image
        utool = getToolByName(self, 'portal_url')
        portal = utool.getPortalObject()
        id_logo = portal.sapl_documentos.props_sapl.id_logo
        if id_logo in portal.sapl_documentos.props_sapl.objectValues('Image'):
            url = self.url() + '/sapl_documentos/props_sapl/' + id_logo
        else:
            url = self.url() + '/imagens/brasao.gif'
        opener = urllib.urlopen(url)
        open('/tmp/' + id_logo, 'wb').write(opener.read())
        f = open('/tmp/' + id_logo, 'rb')
        pdf_stamp = f.read()
        f.close()

        signature_starter = PadesSignatureStarter(restpki_client)
        signature_starter.set_pdf_path(pdf_path)
        signature_starter.signature_policy_id = StandardSignaturePolicies.PADES_BASIC
        signature_starter.security_context_id = StandardSecurityContexts.PKI_BRAZIL
        signature_starter.visual_representation = ({
            'text': {
                # The tags {{signerName}} and {{signerNationalId}} will be substituted according to the user's
                # certificate
                # signerName -> full name of the signer
                # signerNationalId -> if the certificate is ICP-Brasil, contains the signer's CPF
                'text': 'Assinado por {{signerName}} ({{signerNationalId}})',
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
                'opacity': 50,
                # Align the image to the right
                'horizontalAlign': 'Right'
            },

            # Position of the visual representation. We have encapsulated this code in a function to include several
            # possibilities depending on the argument passed to the function. Experiment changing the argument to see
            # different examples of signature positioning (valid values are 1-6). Once you decide which is best for
            # your case, you can place the code directly here.
            'position': self.get_visual_representation_position(2)
        })

        token = signature_starter.start_with_webpki()

        assinar = self.url() + '/cadastros/proposicao/assinar_proposicao'
        #response = browser.open(assinar + '?cod_proposicao='+str(cod_proposicao)+'&token=token&pdf_path='+pdf_path)

        #response = make_response(render_template('pades-signature.html', token=token, pdf_path=pdf_path))

        # The token acquired above can only be used for a single signature attempt. In order to retry the signature it is
        # necessary to get a new token. This can be a problem if the user uses the back button of the browser, since the
        # browser might show a cached page that we rendered previously, with a now stale token. # we force page expiration
        # through HTTP headers to prevent caching of the page.
        #response.headers = get_expired_page_headers()
 
        return token, pdf_path, cod_proposicao
        #return token, pdf_path

    def pades_signature_action(self, token, cod_proposicao):
        # Get the token for this signature (rendered in a hidden input field, see pades-signature.html template)
        token = token
        cod_proposicao = cod_proposicao

        # Instantiate the PadesSignatureFinisher class, responsible for completing the signature process
        signature_finisher = PadesSignatureFinisher(restpki_client)

        # Set the token
        signature_finisher.token = token

        # Call the finish() method, which finalizes the signature process and returns the signed PDF
        signature_finisher.finish()

        # Get information about the certificate used by the user to sign the file. This method must only be called after
        # calling the finish() method.
        signer_cert = signature_finisher.certificate

        # At this point, you'd typically store the signed PDF on your database. For demonstration purposes, we'll
        # store the PDF on a temporary folder publicly accessible and render a link to it.
        filename = "%s"%cod_proposicao+'_signed.pdf'

        tmp_path = "/tmp"

        signature_finisher.write_signed_pdf(os.path.join(tmp_path, filename))

        signature_finisher.write_signed_pdf(filename)

        data = open('/tmp/' + filename, "rb").read()
        for file in [filename]:
            os.unlink(file)
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

        #return signer_cert, filename

        #return render_template('pades-signature-action.html', signed_file="%s/%s" % (UPLOAD_FOLDER, filename),signer_cert=signer_cert)

    def get_visual_representation_position(self, sample_number):
        if sample_number == 1:
            # Example #1: automatic positioning on footnote. This will insert the signature, and future signatures,
            # ordered as a footnote of the last page of the document
            return PadesVisualPositioningPresets.get_footnote(restpki_client)
        elif sample_number == 2:
            # Example #2: get the footnote positioning preset and customize it
            visual_position = PadesVisualPositioningPresets.get_footnote(restpki_client)
            visual_position['auto']['container']['left'] = 2.54
            visual_position['auto']['container']['bottom'] = 1.35
            visual_position['auto']['container']['right'] = 2.54
            return visual_position
        elif sample_number == 3:
            # Example #3: automatic positioning on new page. This will insert the signature, and future signatures,
            # in a new page appended to the end of the document.
            return PadesVisualPositioningPresets.get_new_page(restpki_client)
        elif sample_number == 4:
            # Example #4: get the "new page" positioning preset and customize it
            visual_position = PadesVisualPositioningPresets.get_new_page(restpki_client)
            visual_position['auto']['container']['left'] = 2.54
            visual_position['auto']['container']['top'] = 2.54
            visual_position['auto']['container']['right'] = 2.54
            visual_position['auto']['signatureRectangleSize']['width'] = 6
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

