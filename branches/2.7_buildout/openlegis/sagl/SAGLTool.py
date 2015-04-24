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
import urllib
import cStringIO
from appy.pod.renderer import Renderer
import simplejson as json


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
        nome_camara = self.sagl_documentos.props_sagl.nom_casa
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

            end_web_casa = self.sagl_documentos.props_sagl.end_web_casa
            sgl_casa = self.sagl_documentos.props_sagl.sgl_casa.lower()
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

            localidade = self.zsql.localidade_obter_zsql(cod_localidade = self.sagl_documentos.props_sagl.cod_localidade)
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
            localidade = self.zsql.localidade_obter_zsql(cod_localidade = self.sagl_documentos.props_sagl.cod_localidade)[0].nom_localidade
            sigla_uf = self.zsql.localidade_obter_zsql(cod_localidade = self.sagl_documentos.props_sagl.cod_localidade)[0].sgl_uf
            if consulta.voc_lexml == 'lei.organica':
                epigrafe = u'%s de %s - %s, de %s' % (consulta.des_tipo_norma, localidade,sigla_uf, consulta.ano_norma)
            elif consulta.voc_lexml == 'constituicao':
                epigrafe = u'%s do Estado de %s, de %s' % (consulta.des_tipo_norma, localidade, consulta.ano_norma)
            else:
                epigrafe = u'%s n° %s,  de %s' % (consulta.des_tipo_norma, consulta.num_norma, self.pysc.data_converter_por_extenso_pysc(consulta.dat_norma))

            ementa = consulta.txt_ementa

            indexacao = consulta.txt_indexacao

            formato = 'text/html'
            id_documento = u'%s_%s' % (str(cod_norma), self.sagl_documentos.norma_juridica.nom_documento)
            if hasattr(self.sagl_documentos.norma_juridica,id_documento):
                arquivo = getattr(self.sagl_documentos.norma_juridica,id_documento)
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
            oai_lexml.append(E.Ementa(ementa.decode))
            if indexacao:
                oai_lexml.append(E.Indexacao(indexacao.decode))
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

InitializeClass(SAGLTool)
