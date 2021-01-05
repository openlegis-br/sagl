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
""" This module implements a portal-managed File class.  It is based on
Zope's built-in File object, but modifies the behaviour slightly to
make it more Portal-friendly.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from OFS.Cache import Cacheable
import OFS.Image  # disambiguation
from zope.component.factory import Factory
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.PortalContent import PortalContent
from Products.CMFCore.utils import _checkConditionalGET
from Products.CMFCore.utils import _OldCacheHeaders
from Products.CMFCore.utils import _setCacheHeaders
from Products.CMFCore.utils import _ViewEmulator
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFDefault.interfaces import IFile
from Products.CMFDefault.interfaces import IMutableFile
from Products.CMFDefault.permissions import ModifyPortalContent
from Products.CMFDefault.permissions import View
from Products.GenericSetup.interfaces import IDAVAware


def addFile( self
           , id
           , title=''
           , file=''
           , content_type=''
           , precondition=''
           , subject=()
           , description=''
           , contributors=()
           , effective_date=None
           , expiration_date=None
           , format='text/html'
           , language=''
           , rights=''
           ):
    """
    Add a File
    """

    # cookId sets the id and title if they are not explicity specified
    id, title = OFS.Image.cookId(id, title, file)

    self=self.this()

    # Instantiate the object and set its description.
    fobj = File( id, title, '', content_type, precondition, subject
               , description, contributors, effective_date, expiration_date
               , format, language, rights
               )

    # Add the File instance to self
    self._setObject(id, fobj, suppress_events=True)

    # 'Upload' the file.  This is done now rather than in the
    # constructor because the object is now in the ZODB and
    # can span ZODB objects.
    self._getOb(id).manage_upload(file)

#
#   Fix up PortalContent's over-generalization (OFS.Image.File has
#   a *method* 'manage_edit', which is supposed to be POSTed to from its
#   template, 'manage_editForm'.
#
manage_options = []
for mapping in PortalContent.manage_options:
    mapping = mapping.copy()
    if mapping['label'] == 'Edit':
        mapping['action'] = 'manage_editForm'
    manage_options.append(mapping)
manage_options.extend(Cacheable.manage_options)
manage_options = tuple(manage_options)

@implementer(IMutableFile, IFile, IDAVAware)
class File(PortalContent, OFS.Image.File, DefaultDublinCoreImpl):

    """A Portal-managed File.
    """


    effective_date = expiration_date = None
    icon = PortalContent.icon
    id = None

    manage_options = manage_options

    security = ClassSecurityInfo()

    def __init__( self
                , id
                , title=''
                , file=''
                , content_type=''
                , precondition=''
                , subject=()
                , description=''
                , contributors=()
                , effective_date=None
                , expiration_date=None
                , format=None
                , language='en-US'
                , rights=''
                ):
        OFS.Image.File.__init__( self, id, title, file
                               , content_type, precondition )
        self._setId(id)
        delattr(self, '__name__')

        # If no file format has been passed in, rely on what OFS.Image.File
        # detected. Unlike Images, which have code to try and pick the content
        # type out of the binary data, File objects only provide the correct
        # type if a "hint" in the form of a filename extension is given.
        if format is None:
            format = self.content_type 

        DefaultDublinCoreImpl.__init__( self, title, subject, description
                               , contributors, effective_date, expiration_date
                               , format, language, rights )

    security.declareProtected(View, 'SearchableText')
    def SearchableText(self):
        """
        SeachableText is used for full text seraches of a portal.  It
        should return a concatenation of all useful text.
        """
        return "%s %s" % (self.title, self.description)

    security.declarePrivate('_isNotEmpty')
    def _isNotEmpty(self, file):
        """ Do various checks on 'file' to try to determine non emptiness. """
        if not file:
            return 0                    # Catches None, Missing.Value, ''
        elif file and (type(file) is type('')):
            return 1
        elif getattr(file, 'filename', None):
            return 1
        elif not hasattr(file, 'read'):
            return 0
        else:
            file.seek(0,2)              # 0 bytes back from end of file
            t = file.tell()             # Report the location
            file.seek(0)                # and return pointer back to 0
            if t: return 1
            else: return 0

    security.declarePrivate('_edit')
    def _edit(self, precondition='', file=''):
        """ Perform changes for user """
        if precondition: self.precondition = precondition
        elif self.precondition: del self.precondition

        if self._isNotEmpty(file):
            self.manage_upload(file)

    security.declareProtected(ModifyPortalContent, 'edit')
    def edit(self, precondition='', file=''):
        """ Update and reindex. """
        self._edit( precondition, file )
        self.reindexObject()

    security.declareProtected(View, 'index_html')
    def index_html(self, REQUEST, RESPONSE):
        """
        The default view of the contents of a File or Image.

        Returns the contents of the file or image.  Also, sets the
        Content-Type HTTP header to the objects content type.
        """
        view = _ViewEmulator().__of__(self)

        # If we have a conditional get, set status 304 and return
        # no content 
        if _checkConditionalGET(view, extra_context={}):
            return ''

        RESPONSE.setHeader('Content-Type', self.content_type)

        # old-style If-Modified-Since header handling.
        if self._setOldCacheHeaders():
            # Make sure the CachingPolicyManager gets a go as well
            _setCacheHeaders(view, extra_context={})
            return ''

        try:
            return OFS.Image.File.index_html(self, REQUEST, RESPONSE)
        finally:
            # There are 2 Cache Managers which can be in play....
            # need to decide which to use to determine where the cache headers
            # are decided on.
            if self.ZCacheable_getManager() is not None:
                self.ZCacheable_set(None)
            else:
                _setCacheHeaders(view, extra_context={})


    def _setOldCacheHeaders(self):
        # return False to disable this simple caching behaviour
        return _OldCacheHeaders(self) 

    security.declareProtected(View, 'download')
    def download(self, REQUEST, RESPONSE):
        """Download this item.

        Calls OFS.Image.File.index_html to perform the actual transfer after
        first setting Content-Disposition to suggest a filename.

        This method is deprecated, use the URL of this object itself. Because
        the default view of a File object is to download, rather than view,
        this method is obsolete. Also note that certain browsers do not deal
        well with a Content-Disposition header.

        """

        RESPONSE.setHeader('Content-Disposition',
                           'attachment; filename=%s' % self.getId())
        return self.index_html(self, REQUEST, RESPONSE)

    security.declareProtected(View, 'Format')
    def Format(self):
        """ Dublin Core element - resource format """
        return self.content_type

    security.declareProtected(ModifyPortalContent, 'setFormat')
    def setFormat(self, format):
        """ Dublin Core element - resource format """
        self.manage_changeProperties(content_type=format)

    security.declareProtected(ModifyPortalContent, 'PUT')
    def PUT(self, REQUEST, RESPONSE):
        """ Handle HTTP (and presumably FTP?) PUT requests """
        OFS.Image.File.PUT( self, REQUEST, RESPONSE )
        self.reindexObject()

InitializeClass(File)

FileFactory = Factory(File)
