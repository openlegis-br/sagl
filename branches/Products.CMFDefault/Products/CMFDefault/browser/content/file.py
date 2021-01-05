##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Browser views for files.
"""

from zope.component import adapts
from zope.formlib import form
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import ASCIILine
from zope.schema import Text
from zope.schema import TextLine

from Products.CMFDefault.browser.utils import decode
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.utils import ViewBase
from Products.CMFDefault.formlib.form import ContentAddFormBase
from Products.CMFDefault.formlib.form import ContentEditFormBase
from Products.CMFDefault.formlib.schema import FileUpload
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFDefault.interfaces import IMutableFile
from Products.CMFDefault.utils import Message as _


class IFileSchema(Interface):

    """Schema for file views.
    """

    title = TextLine(
        title=_(u'Title'),
        required=False,
        missing_value=u'')

    language = TextLine(
        title=_(u'Language'),
        required=False,
        missing_value=u'',
        max_length=2)

    description = Text(
        title=_(u'Description'),
        required=False,
        missing_value=u'')

    format = ASCIILine(
        title=_(u'Content type'),
        readonly=True)

    file = FileUpload(
        title=_(u'Upload'),
        required=False)

@implementer(IFileSchema)
class FileSchemaAdapter(SchemaAdapterBase):

    """Adapter for IMutableFile.
    """

    adapts(IMutableFile)

    def _getFile(self):
        return ''

    def _setFile(self, value):
        self.context.manage_upload(value)

    title = ProxyFieldProperty(IFileSchema['title'], 'Title', 'setTitle')
    language = ProxyFieldProperty(IFileSchema['language'],
                                  'Language', 'setLanguage')
    description = ProxyFieldProperty(IFileSchema['description'],
                                     'Description', 'setDescription')
    format = ProxyFieldProperty(IFileSchema['format'], 'Format')
    file = property(_getFile, _setFile)


class FileView(ViewBase):

    """View for IFile.
    """

    # interface

    @memoize
    @decode
    def content_type(self):
        return self.context.getContentType()

    @memoize
    @decode
    def id(self):
        return self.context.getId()

    @memoize
    @decode
    def size(self):
        return self.context.get_size()

    @memoize
    @decode
    def url(self):
        return self.context.absolute_url()


class FileAddView(ContentAddFormBase):

    """Add view for IMutableFile.
    """

    form_fields = (
        form.FormFields(IFileSchema).select('title', 'description') +
        form.FormFields(FileUpload(__name__='file', title=_(u'Upload')))
        )

    def setUpWidgets(self, ignore_request=False):
        super(FileAddView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['description'].height = 3
        self.widgets['file'].displayWidth = 60

    def create(self, data):
        obj = super(FileAddView,
                    self).create(dict(id=data['file'].filename))
        adapted = FileSchemaAdapter(obj)
        adapted.title = data['title']
        adapted.language = u''
        adapted.description = data['description']
        adapted.file = data['file']
        return obj


class FileEditView(ContentEditFormBase):

    """Edit view for IMutableFile.
    """

    form_fields = form.FormFields(IFileSchema).omit('language')

    @memoize
    def getContent(self):
        return FileSchemaAdapter(self.context)

    def setUpWidgets(self, ignore_request=False):
        super(FileEditView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['description'].height = 3
        self.widgets['file'].displayWidth = 60
