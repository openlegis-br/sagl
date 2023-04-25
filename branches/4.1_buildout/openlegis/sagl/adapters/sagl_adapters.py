from zope.component import adapter
from zope.interface import implementer
from Products.CMFCore.utils import getToolByName
from openlegis.sagl.interfaces import IFileSAGL

from zopyx.txng3.core.interfaces import IIndexableContent
from zopyx.txng3.core.content import IndexContentCollector as ICC
from zopyx.txng3.core.config import DEFAULT_LANGUAGE

@implementer(IIndexableContent)
@adapter(IFileSAGL)
class FileAdapter:
    """ Adapter para o tipo File do Zope
    """
    def __init__(self, context):
        self.context = context
        self.encoding = 'utf-8'
        self.language = DEFAULT_LANGUAGE

    def indexableContent(self, fields):
        icc = ICC()
        self.addPrincipiaSearchSource(icc)
        return icc

    def addPrincipiaSearchSource(self, icc):
        body = str(self.context)
        ct = self.context.content_type
        if body:
            icc.addBinary('PrincipiaSearchSource', body, ct, None, self.language)

