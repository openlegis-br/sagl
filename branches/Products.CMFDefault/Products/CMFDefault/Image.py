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
""" This module implements a portal-managed Image class. It is based on
Zope's built-in Image object.
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
from Products.CMFDefault.interfaces import IImage
from Products.CMFDefault.interfaces import IMutableImage
from Products.CMFDefault.permissions import ModifyPortalContent
from Products.CMFDefault.permissions import View
from Products.GenericSetup.interfaces import IDAVAware


def addImage( self
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
            , format='image/png'
            , language=''
            , rights=''
            ):
    """
        Add an Image
    """

    # cookId sets the id and title if they are not explicity specified
    id, title = OFS.Image.cookId(id, title, file)

    self=self.this()

    # Instantiate the object and set its description.
    iobj = Image( id, title, '', content_type, precondition, subject
                , description, contributors, effective_date, expiration_date
                , format, language, rights
                )

    # Add the Image instance to self
    self._setObject(id, iobj, suppress_events=True)

    # 'Upload' the image.  This is done now rather than in the
    # constructor because it's faster (see File.py.)
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

@implementer(IMutableImage, IImage, IDAVAware)
class Image(PortalContent, OFS.Image.Image, DefaultDublinCoreImpl):

    """A Portal-managed Image.
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
        # detected.
        if format is None:
            format = self.content_type

        DefaultDublinCoreImpl.__init__( self, title, subject, description
                               , contributors, effective_date, expiration_date
                               , format, language, rights )

    security.declareProtected(View, 'SearchableText')
    def SearchableText(self):
        """
            SeachableText is used for full text seraches of a portal.
            It should return a concatanation of all useful text.
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
        """ Update image. """
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
        Display the image, with or without standard_html_[header|footer],
        as appropriate.
        """
        view = _ViewEmulator().__of__(self)

        # If we have a conditional get, set status 304 and return
        # no content
        if _checkConditionalGET(view, extra_context={}):
            return ''

        # old-style If-Modified-Since header handling.
        if self._setOldCacheHeaders():
            # Make sure the CachingPolicyManager gets a go as well
            _setCacheHeaders(view, extra_context={})
            return ''

        try:
            return OFS.Image.Image.index_html(self, REQUEST, RESPONSE)
        finally:
            if self.ZCacheable_getManager() is None:
                # not none cache manager already taken care of
                _setCacheHeaders(view, extra_context={})
            else:
                self.ZCacheable_set(None)
            

    security.declarePrivate('_setOldCacheHeaders')
    def _setOldCacheHeaders(self):
        # return False to disable this simple caching behaviour
        return _OldCacheHeaders(self)

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
        OFS.Image.Image.PUT( self, REQUEST, RESPONSE )
        self.reindexObject()

InitializeClass(Image)

ImageFactory = Factory(Image)
