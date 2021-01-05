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
"""Browser views for news items.
"""

from zope.component import adapts
from zope.formlib import form
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import Choice
from zope.schema import Text
from zope.schema import TextLine

from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.formlib.form import ContentEditFormBase
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFDefault.formlib.widgets import ChoiceRadioWidget
from Products.CMFDefault.formlib.widgets import TextInputWidget
from Products.CMFDefault.interfaces import IMutableNewsItem
from Products.CMFDefault.utils import Message as _


class INewsItemSchema(Interface):

    """Schema for news item views.
    """

    title = TextLine(
        title=_(u'Title'),
        readonly=True)

    text_format = Choice(
        title=_(u'Format'),
        vocabulary='cmf.AvailableTextFormats')

    description = Text(
        title=_(u'Lead-in'),
        required=False,
        missing_value=u'')

    text = Text(
        title=_(u'Body'),
        required=False,
        missing_value=u'')

@implementer(INewsItemSchema)
class NewsItemSchemaAdapter(SchemaAdapterBase):

    """Adapter for IMutableNewsItem.
    """

    adapts(IMutableNewsItem)

    title = ProxyFieldProperty(INewsItemSchema['title'], 'Title')
    text_format = ProxyFieldProperty(INewsItemSchema['text_format'])
    description = ProxyFieldProperty(INewsItemSchema['description'],
                                     'Description', 'setDescription')
    text = ProxyFieldProperty(INewsItemSchema['text'],
                              'EditableBody', '_edit')


class NewsItemEditView(ContentEditFormBase):

    """Edit view for INewsItem.
    """

    form_fields = form.FormFields(INewsItemSchema)
    form_fields['text_format'].custom_widget = ChoiceRadioWidget
    form_fields['description'].custom_widget = TextInputWidget
    form_fields['text'].custom_widget = TextInputWidget

    @memoize
    def getContent(self):
        return NewsItemSchemaAdapter(self.context)

    def setUpWidgets(self, ignore_request=False):
        super(NewsItemEditView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['text_format'].orientation = 'horizontal'
        self.widgets['description'].height = 8
        self.widgets['text'].height = 16
