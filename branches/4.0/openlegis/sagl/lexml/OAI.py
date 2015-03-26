# -*- coding: utf-8 -*-

from datetime import datetime

import oaipmh
import oaipmh.metadata
import oaipmh.server
import oaipmh.error

from metadata import OAILEXML


def get_writer(prefix, config={}):
    writer = OAILEXML
    return writer(prefix, config={})


class OAIServer(object):
    """An OAI-2.0 compliant oai server.
    
    Underlying code is based on pyoai's oaipmh.server'
    """
    
    def __init__(self, sagl_tool, config={}):
        self.config = config
        self.sagl_tool = sagl_tool

    def get_oai_id(self, internal_id):
        return 'oai:%s' % internal_id

    def get_internal_id(self, oai_id):
        return int(oai_id.split('/').pop())

    def get_internal_set_id(self, oai_setspec_id):
        return oai_setspec_id[4:]

    def get_asset_path(self, internal_id, asset):
        return os.path.abspath(
            os.path.join(self.base_asset_path,
                         internal_id,
                         asset['filename']))

    def identify(self):
        result = oaipmh.common.Identify(
            repositoryName=self.config['titulo'],
            baseURL=self.config['base_url'],
            protocolVersion='2.0',
            adminEmails=self.config['email'],
            earliestDatestamp=datetime(2001, 1, 1, 10, 00),
            deletedRecord='transient',
            granularity='YYYY-MM-DDThh:mm:ssZ',
            compression=['identity'],
            toolkit_description=False)
        if self.config['descricao'] is not None:
            result.add_description(self.config['descricao'])
        return result

    def listMetadataFormats(self, identifier=None):
        result = []
        for prefix in self.config['metadata_prefixes']:
            writer = get_writer(prefix, self.config)
            ns = writer.get_namespace()
            schema = writer.get_schema_location()
            result.append((prefix, schema, ns))
        return result
    
    def listRecords(self, metadataPrefix, set=None, from_=None, until=None,
                    cursor=0, batch_size=10):

        self._checkMetadataPrefix(metadataPrefix)
        for record in self._listQuery(set, from_, until, cursor, batch_size):
            header, metadata = self._createHeaderAndMetadata(record)
            yield header, metadata, None

    def listIdentifiers(self, metadataPrefix, set=None, from_=None, until=None,
                        cursor=0, batch_size=10):
        
        self._checkMetadataPrefix(metadataPrefix)
        for record in self._listQuery(set, from_, until, cursor, batch_size):
            yield self._createHeader(record)

    def getRecord(self, metadataPrefix, identifier):
        self._checkMetadataPrefix(metadataPrefix)
        header = None
        metadata = None
        for record in self._listQuery(identifier=identifier):
            header, metadata = self._createHeaderAndMetadata(record)
        if header is None:
            raise oaipmh.error.IdDoesNotExistError(identifier)
        return header, metadata, None

    def _checkMetadataPrefix(self, metadataPrefix):
        if metadataPrefix not in self.config['metadata_prefixes']:
            raise oaipmh.error.CannotDisseminateFormatError

    def _createHeader(self, record):
        oai_id = self.get_oai_id(record['record']['id'])
        datestamp = record['record']['when_modified']
        sets = []
        deleted = record['record']['deleted']

        return oaipmh.common.Header(oai_id, datestamp, sets, deleted)

    def _createHeaderAndMetadata(self, record):
        header = self._createHeader(record)
        metadata = oaipmh.common.Metadata(record['metadata'])
        metadata.record = record
        return header, metadata
    
    def _listQuery(self, set=None, from_=None, until=None, 
                   cursor=0, batch_size=10, identifier=None):

        if identifier:
            identifier = self.get_internal_id(identifier)
        else:
            identifier = ''
        if set:
            set = self.get_internal_set_id(set)
        
        # TODO: verificar se a data eh UTC
        now = datetime.now()
        if until != None and until > now:
            # until nunca deve ser no futuro
            until = now
            
        return self.sagl_tool.oai_query(offset=cursor,
                                        batch_size=batch_size,
                                        from_date=from_,
                                        until_date=until,
                                        identifier=identifier
                                        )


def OAIServerFactory(sagl_tool, config={}):
    """Create a new OAI batching OAI Server given a config and
    a database"""
    for prefix in config['metadata_prefixes']:
        metadata_registry = oaipmh.metadata.MetadataRegistry()
        metadata_registry.registerWriter(prefix, get_writer(prefix, config))
            
    return oaipmh.server.BatchingServer(
        OAIServer(sagl_tool, config),
        metadata_registry=metadata_registry,
        resumption_batch_size=config['batch_size']
        )
