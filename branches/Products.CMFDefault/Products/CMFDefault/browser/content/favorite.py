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
"""Browser views for favorites.
"""

import urllib.parse

from zope.component import adapts
from zope.component import getUtility
from zope.formlib import form
from zope.formlib.widgets import BytesWidget
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import ASCIILine
from zope.schema import BytesLine
from zope.schema import Text
from zope.schema import TextLine

from Products.CMFCore.interfaces import IURLTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.formlib.form import ContentAddFormBase
from Products.CMFDefault.formlib.form import ContentEditFormBase
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFDefault.formlib.widgets import IDInputWidget
from Products.CMFDefault.interfaces import IMutableFavorite
from Products.CMFDefault.utils import Message as _


class IFavoriteSchema(Interface):

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
        description=_(u'URL relative to the site root.'),
        required=False,
        missing_value=u'')

@implementer(IFavoriteSchema)
class FavoriteSchemaAdapter(SchemaAdapterBase):

    adapts(IMutableFavorite)

    _remote_url = ProxyFieldProperty(IFavoriteSchema['remote_url'])

    def _getRemoteURL(self):
        return self._remote_url

    def _setRemoteURL(self, value):
        self._remote_url = value
        self.context.remote_uid = self.context._getUidByUrl()

    title = ProxyFieldProperty(IFavoriteSchema['title'], 'Title', 'setTitle')
    language = ProxyFieldProperty(IFavoriteSchema['language'],
                                  'Language', 'setLanguage')
    description = ProxyFieldProperty(IFavoriteSchema['description'],
                                     'Description', 'setDescription')
    remote_url = property(_getRemoteURL, _setRemoteURL)


class FavoriteURIWidget(BytesWidget):

    """Custom widget for remote_url.
    """

    def _toFieldValue(self, input):
        value = super(FavoriteURIWidget, self)._toFieldValue(input)
        if not value:
            return value
        # strip off scheme and machine from URL if present
        tokens = urlparse.urlparse(value, 'http')
        if tokens[1]:
            # There is a nethost, remove it
            tokens = ('', '') + tokens[2:]
            value = urlparse.urlunparse(tokens)
        # if URL begins with site URL, remove site URL
        portal_url = getUtility(IURLTool).getPortalPath()
        if value.startswith(portal_url):
            value = value[len(portal_url):]
        # if site is still absolute, make it relative
        if value[:1]=='/':
            value = value[1:]
        return value


class FavoriteAddView(ContentAddFormBase):

    """Add view for IMutableFavorite.
    """

    form_fields = (
        form.FormFields(ASCIILine(__name__='id', title=_(u'ID'))) +
        form.FormFields(IFavoriteSchema).omit('language')
        )
    form_fields['id'].custom_widget = IDInputWidget
    form_fields['remote_url'].custom_widget = FavoriteURIWidget

    def setUpWidgets(self, ignore_request=False):
        super(FavoriteAddView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['description'].height = 3

    def create(self, data):
        obj = super(FavoriteAddView, self).create(dict(id=data['id']))
        adapted = FavoriteSchemaAdapter(obj)
        adapted.title = data['title']
        adapted.language = u''
        adapted.description = data['description']
        adapted.remote_url = data['remote_url']
        return obj


class FavoriteEditView(ContentEditFormBase):

    """Edit view for IMutableFavorite.
    """

    form_fields = form.FormFields(IFavoriteSchema).omit('language')
    form_fields['remote_url'].custom_widget = FavoriteURIWidget

    @memoize
    def getContent(self):
        return FavoriteSchemaAdapter(self.context)

    def setUpWidgets(self, ignore_request=False):
        super(FavoriteEditView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['description'].height = 3
