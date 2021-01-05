##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Browser views for links.
"""

import urllib.parse

from zope.component import adapts
from zope.formlib import form
from zope.formlib.widgets import BytesWidget
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import ASCIILine
from zope.schema import BytesLine
from zope.schema import Text
from zope.schema import TextLine

from Products.CMFDefault.formlib.form import ContentAddFormBase
from Products.CMFDefault.formlib.form import ContentEditFormBase
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFDefault.formlib.widgets import IDInputWidget
from Products.CMFDefault.interfaces import IMutableLink
from Products.CMFDefault.utils import Message as _

from Products.CMFDefault.browser.utils import decode, memoize, ViewBase


class ILinkSchema(Interface):

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

    remote_url = BytesLine(
        title=_(u'URL'),
        required=False,
        missing_value=u'')

@implementer(ILinkSchema)
class LinkSchemaAdapter(SchemaAdapterBase):

    adapts(IMutableLink)

    title = ProxyFieldProperty(ILinkSchema['title'], 'Title', 'setTitle')
    language = ProxyFieldProperty(ILinkSchema['language'],
                                  'Language', 'setLanguage')
    description = ProxyFieldProperty(ILinkSchema['description'],
                                     'Description', 'setDescription')
    remote_url = ProxyFieldProperty(ILinkSchema['remote_url'])


class LinkView(ViewBase):

    """View for ILink.
    """

    # interface

    @memoize
    @decode
    def url(self):
        return self.context.getRemoteUrl()


class LinkURIWidget(BytesWidget):

    """Custom widget for remote_url.
    """

    def _toFieldValue(self, input):
        value = super(LinkURIWidget, self)._toFieldValue(input)
        if not value:
            return value
        tokens = urlparse.urlparse(value, 'http')
        if tokens[0] == 'http':
            if tokens[1]:
                # We have a nethost. All is well.
                return urlparse.urlunparse(tokens)
            elif tokens[2:] == ('', '', '', ''):
                # Empty URL
                return u''
            else:
                # Relative URL, keep it that way, without http:
                tokens = ('', '') + tokens[2:]
                return urlparse.urlunparse(tokens)
        else:
            # Other scheme, keep original
            return urlparse.urlunparse(tokens)


class LinkAddView(ContentAddFormBase):

    """Add view for IMutableLink.
    """

    form_fields = (
        form.FormFields(ASCIILine(__name__='id', title=_(u'ID'))) +
        form.FormFields(ILinkSchema).omit('language')
        )
    form_fields['id'].custom_widget = IDInputWidget
    form_fields['remote_url'].custom_widget = LinkURIWidget

    def setUpWidgets(self, ignore_request=False):
        super(LinkAddView, self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['description'].height = 3

    def create(self, data):
        obj = super(LinkAddView, self).create(dict(id=data['id']))
        adapted = LinkSchemaAdapter(obj)
        adapted.title = data['title']
        adapted.language = u''
        adapted.description = data['description']
        adapted.remote_url = data['remote_url']
        return obj


class LinkEditView(ContentEditFormBase):

    """Edit view for IMutableLink.
    """

    form_fields = form.FormFields(ILinkSchema).omit('language')
    form_fields['remote_url'].custom_widget = LinkURIWidget

    @memoize
    def getContent(self):
        return LinkSchemaAdapter(self.context)

    def setUpWidgets(self, ignore_request=False):
        super(LinkEditView, self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['description'].height = 3
