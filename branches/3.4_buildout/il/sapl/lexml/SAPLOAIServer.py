# -*- coding: utf-8 -*-

from datetime import datetime
from DateTime import DateTime
from OFS import SimpleItem, Folder
import Globals
import Acquisition
from Persistence import Persistent
from Globals import PersistentMapping
from AccessControl import ClassSecurityInfo, Permissions
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
import time, os, sys

from OAI import OAIServerFactory

from oaipmh import client, metadata, error, server
from oaipmh.datestamp import datetime_to_datestamp

from Products.CMFCore.utils import getToolByName

manage_addSAPLOAIServerForm = PageTemplateFile('www/addSAPLOAIServer', globals())
manage_addSAPLOAIServerForm.__name__='addSAPLOAIServer'

def manage_addSAPLOAIServer(self, email, titulo, batch_size, base_url, id='oai', REQUEST=None):
    """Adicionar um servidor OAI para integracao com o LeXML.
    """
    SAPL_OAI = SAPLOAIServer(email,titulo,batch_size,base_url)
    self._setObject(id, SAPL_OAI)
    if REQUEST is None:
        return
    try:
        u = self.DestinationURL()
    except:
        u = REQUEST['URL1']
    if REQUEST.has_key('submit_edit'):
        u = "%s/%s" % (u, urllib.quote(id))
    REQUEST.RESPONSE.redirect(u+'/manage_main')

class SAPLOAIServer(SimpleItem.SimpleItem,Persistent):
    """ """
    
    security = ClassSecurityInfo()
    meta_type = 'SAPL OAI Server'
    manage_options = (
        {'label':'Editar', 'action':'manage_main'},
        ) + SimpleItem.SimpleItem.manage_options

    def __init__(self, email, titulo, batch_size, base_url):
        self.id = 'oai'
        self._titulo = titulo
        self._email = email
        self._batch_size = batch_size
        self._base_url = base_url

    manage_editForm = PageTemplateFile(
        "www/editSAPLOAIServer", globals(), __name__='manage_editForm')
    manage_main = manage_editForm

    security.declareProtected('View management screens', 'manage_edit')
    def manage_edit(self, email, titulo,batch_size, base_url, REQUEST=None):
        """Edit settings.
        """
        
        if titulo:
            self._titulo = titulo
        if email:
            self._email = email
        if batch_size:
            self._batch_size = batch_size
        if base_url:
            self._base_url = base_url
        if REQUEST is not None:
            return self.manage_main(manage_tabs_message="Configura&ccedil;&otilde;es alteradas")

    def config(self):
        config = {}
        config['titulo'] = self.get_nome_repositorio()
        config['email'] = self.get_email()
        config['base_url'] = self.get_base_url()
        config['metadata_prefixes'] = ['oai_lexml',]
        config['descricao'] = self.get_descricao_casa()
        config['batch_size'] = self.get_batch_size()
        config['content_type'] = None,
        config['delay'] = 0,
        config['base_asset_path']=None
        return config

    def get_nome_repositorio(self):
        return self._titulo
    
    def get_email(self):
        emails = []
        emails.append(self._email)
        return emails

    def get_descricao_casa(self):
        descricao = ''
        consulta = self.zsql.lexml_provedor_obter_zsql()
        if consulta:
            descricao = consulta[0].xml_provedor
            if descricao:
                descricao = descricao.encode('utf-8')
        return descricao

    def get_batch_size(self):
        return int(self._batch_size)
    
    def get_base_url(self):
        return self._base_url

    def index_html(self, REQUEST=None,RESPONSE=None):
        """ processa os argumentos recebidos pela URL
        """
        if REQUEST is not None:
            return self.handle_request(req=REQUEST)
        else:
            return None

    def write(self, req, data, mimetype,RESPONSE=None):
        """ Retorna os dados para o cliente
        """
        req.RESPONSE.setHeader('Content-Type' , mimetype)
        req.RESPONSE.setHeader('Content-Length' ,len(data))
        return data.decode('utf-8').encode('ascii', 'xmlcharrefreplace')

    def handle_request(self, req,RESPONSE=None):
        if not req.URL.startswith(self._base_url):
            return req.RESPONSE.setStatus('500 Internal Server Error',
                 u'The url "%s" does not start with base url "%s".' % (req.URL,
                                                                      self._base_url))
        sapl_tool = getToolByName(self,'portal_sapl')
        oai_server = OAIServerFactory(sapl_tool, self.config())
        return self.write(req, oai_server.handleRequest(req.form),'text/xml',RESPONSE)

    
