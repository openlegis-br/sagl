
from lxml.builder import ElementMaker
from lxml import etree

XSI_NS = 'http://www.w3.org/2001/XMLSchema-instance'

class OAILEXML(object):
    """Padrao oai do LeXML

    Esta registrado sobre o nome 'oai_lexml'
    """

    def __init__(self, prefix, config):
        self.prefix = prefix

        self.ns = {'oai_lexml': 'http://www.lexml.gov.br/oai_lexml',}
        self.schemas = {'oai_lexml': 'http://projeto.lexml.gov.br/esquemas/oai_lexml.xsd'}
    
    def get_namespace(self):
        return self.ns[self.prefix]
    
    def get_schema_location(self):
        return self.schemas[self.prefix]
    
    def __call__(self, element, metadata):

        data = metadata.record

        value = etree.XML(data['metadata'])

        element.append(value)