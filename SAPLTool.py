from warnings import warn
from datetime import datetime
from AccessControl import ClassSecurityInfo
from Globals import DTMLFile
from Globals import InitializeClass
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.ActionInformation import ActionInformation
from Products.CMFCore.ActionProviderBase import ActionProviderBase
from Products.CMFCore.Expression import Expression
from Products.CMFCore.permissions import ListFolderContents
from Products.CMFCore.permissions import ManagePortal
from Products.CMFCore.utils import _checkPermission
from Products.CMFCore.utils import _dtmldir
from Products.CMFCore.utils import SimpleItemWithProperties
from Products.CMFCore.utils import UniqueObject
from lxml.builder import ElementMaker
from lxml import etree
import re
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
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
        camara = [u'Câmara','Camara','camara',u'câmara']
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
                epigrafe = '%s de %s - %s, de %s' % (consulta.des_tipo_norma, localidade,sigla_uf, consulta.ano_norma)
            elif consulta.voc_lexml == 'constituicao':
                epigrafe = '%s do Estado de %s, de %s' % (consulta.des_tipo_norma, localidade, consulta.ano_norma)
            else:
                epigrafe = '%s No. %s,  de %s' % (consulta.des_tipo_norma, consulta.num_norma, self.pysc.data_converter_por_extenso_pysc(consulta.dat_norma))
           
            ementa = consulta.txt_ementa
           
            indexacao = consulta.txt_indexacao
           
            formato = 'text/html'
            id_documento = '%s_%s' % (str(cod_norma), self.sapl_documentos.norma_juridica.nom_documento)
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
                oai_lexml.append(E.Indexacao(indexacao.))
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
InitializeClass(SAPLTool)
