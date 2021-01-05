##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Link instances represent explicit links-as-content.
"""

from urllib import parse

from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from App.special_dtml import DTMLFile
import transaction
from zope.component.factory import Factory
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.PortalContent import PortalContent
from Products.CMFCore.utils import contributorsplitter
from Products.CMFCore.utils import keywordsplitter
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFDefault.exceptions import ResourceLockedError
from Products.CMFDefault.interfaces import ILink
from Products.CMFDefault.interfaces import IMutableLink
from Products.CMFDefault.permissions import ModifyPortalContent
from Products.CMFDefault.permissions import View
from Products.CMFDefault.utils import _dtmldir
from Products.CMFDefault.utils import formatRFC822Headers
from Products.CMFDefault.utils import parseHeadersBody
from Products.GenericSetup.interfaces import IDAVAware


def addLink( self
           , id
           , title=''
           , remote_url=''
           , description=''
           ):
    """Add a Link instance to 'self'.
    """
    o=Link( id, title, remote_url, description )
    self._setObject(id, o, suppress_events=True)


@implementer(IMutableLink, ILink, IDAVAware)
class Link(PortalContent, DefaultDublinCoreImpl):

    """A Link.
    """

    URL_FORMAT = format = 'text/url'
    effective_date = expiration_date = None

    security = ClassSecurityInfo()

    def __init__( self
                , id
                , title=''
                , remote_url=''
                , description=''
                ):
        DefaultDublinCoreImpl.__init__(self)
        self.id=id
        self.title=title
        self.description=description
        self._edit(remote_url)
        self.format=self.URL_FORMAT

    security.declareProtected(ModifyPortalContent, 'manage_edit')
    manage_edit = DTMLFile( 'zmi_editLink', _dtmldir )

    security.declareProtected(ModifyPortalContent, 'manage_editLink')
    def manage_editLink( self, remote_url, REQUEST=None ):
        """
            Update the Link via the ZMI.
        """
        self._edit( remote_url )
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect( self.absolute_url()
                                        + '/manage_edit'
                                        + '?manage_tabs_message=Link+updated'
                                        )

    security.declarePrivate( '_edit' )
    def _edit( self, remote_url ):
        """
            Edit the Link
        """
        tokens = urlparse.urlparse( remote_url, 'http' )
        if tokens[0] == 'http':
            if tokens[1]:
                # We have a nethost. All is well.
                url = urlparse.urlunparse(tokens)
            elif tokens[2:] == ('', '', '', ''):
                # Empty URL
                url = ''
            else:
                # Relative URL, keep it that way, without http:
                tokens = ('', '') + tokens[2:]
                url = urlparse.urlunparse(tokens)
        else:
            # Other scheme, keep original
            url = urlparse.urlunparse(tokens)
        self.remote_url = url

    security.declareProtected(ModifyPortalContent, 'edit')
    def edit(self, remote_url ):
        """ Update and reindex. """
        self._edit( remote_url )
        self.reindexObject()

    security.declareProtected(View, 'SearchableText')
    def SearchableText(self):
        """
            text for indexing
        """
        return "%s %s" % (self.title, self.description)

    security.declareProtected(View, 'getRemoteUrl')
    def getRemoteUrl(self):
        """
            returns the remote URL of the Link
        """
        return self.remote_url

    security.declarePrivate('_writeFromPUT')
    def _writeFromPUT(self, body):
        headers, body = parseHeadersBody(body)
        lines = body.split('\n')
        self.edit(lines[0])
        headers['Format'] = self.URL_FORMAT
        new_subject = keywordsplitter(headers)
        headers['Subject'] = new_subject or self.Subject()
        new_contrib = contributorsplitter(headers)
        headers['Contributors'] = new_contrib or self.Contributors()
        headers = dict((k.lower(), v) for k, v in headers.iteritems())
        self._editMetadata(**headers)

    ## FTP handlers
    security.declareProtected(ModifyPortalContent, 'PUT')
    def PUT(self, REQUEST, RESPONSE):
        """
            Handle HTTP / WebDAV / FTP PUT requests.
        """
        self.dav__init(REQUEST, RESPONSE)
        self.dav__simpleifhandler(REQUEST, RESPONSE, refresh=1)
        body = REQUEST.get('BODY', '')
#        try:
#            self._writeFromPUT( body )
#            RESPONSE.setStatus(204)
#            return RESPONSE
#        except ResourceLockedError, msg:
#            transaction.abort()
#            RESPONSE.setStatus(423)
#            return RESPONSE

    security.declareProtected(View, 'manage_FTPget')
    def manage_FTPget(self):
        """
            Get the link as text for WebDAV src / FTP download.
        """
        hdrlist = self.getMetadataHeaders()
        hdrtext = formatRFC822Headers( hdrlist )
        bodytext = '%s\n\n%s' % ( hdrtext, self.getRemoteUrl() )

        return bodytext

    security.declareProtected(View, 'get_size')
    def get_size( self ):
        """ Used for FTP and apparently the ZMI now too.
        """
        return len(self.manage_FTPget())

InitializeClass(Link)

LinkFactory = Factory(Link)
