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
"""Browser views for metadata.
"""

from Acquisition import aq_self
from zope.component import adapts
from zope.component import getUtility
from zope.formlib import form
from zope.formlib.widgets import DatetimeI18nWidget
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import Choice
from zope.schema import Datetime
from zope.schema import Set
from zope.schema import Text
from zope.schema import TextLine
from zope.schema import Tuple
from zope.schema import URI

from Products.CMFCore.interfaces import IDiscussionTool
from Products.CMFCore.interfaces import IMutableDublinCore
from Products.CMFCore.interfaces import IMutableMinimalDublinCore
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.formlib.form import ContentEditFormBase
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFDefault.formlib.vocabulary import SimpleVocabulary
from Products.CMFDefault.formlib.widgets import SubjectInputWidget
from Products.CMFDefault.formlib.widgets import TupleInputWidget
from Products.CMFDefault.utils import Message as _

available_settings = [
        ('off', False, _(u'Off')),
        ('on', True, _(u'On')) ]


class IMinimalMetadataSchema(Interface):

    """Schema for minimal metadata views.
    """

    title = TextLine(
        title=_(u'Title'),
        required=False,
        missing_value=u'')

    description = Text(
        title=_(u'Description'),
        required=False,
        missing_value=u'')


class IMetadataSchema(Interface):

    """Schema for metadata views.
    """

    allow_discussion = Choice(
        title=_(u'Enable Discussion?'),
        required=False,
        vocabulary=SimpleVocabulary.fromTitleItems(available_settings))

    identifier = URI(
        title=_(u'Identifier'),
        readonly=True)

    title = TextLine(
        title=_(u'Title'),
        required=False,
        missing_value=u'')

    description = Text(
        title=_(u'Description'),
        required=False,
        missing_value=u'')

    subject = Set(
        title=_(u'Subject'),
        required=False,
        missing_value=set(),
        value_type=TextLine())

    contributors = Tuple(
        title=_(u'Contributors'),
        required=False,
        missing_value=(),
        value_type=TextLine())

    created = Datetime(
        title=_(u'Creation Date'),
        readonly=True)

    modified = Datetime(
        title=_(u'Last Modified Date'),
        readonly=True)

    effective = Datetime(
        title=_(u'Effective Date'),
        required=False
        )

    expires = Datetime(
        title=_(u'Expiration Date'),
        required=False
        )

    format = TextLine(
        title=_(u'Format'),
        required=False,
        missing_value=u'')

    language = TextLine(
        title=_(u'Language'),
        required=False,
        missing_value=u'')

    rights = TextLine(
        title=_(u'Rights'),
        required=False,
        missing_value=u'')


@implementer(IMinimalMetadataSchema)
class MinimalMetadataSchemaAdapter(SchemaAdapterBase):

    """Adapter for IMutableMinimalDublinCore.
    """

    adapts(IMutableMinimalDublinCore)

    title = ProxyFieldProperty(IMetadataSchema['title'], 'Title', 'setTitle')
    description = ProxyFieldProperty(IMetadataSchema['description'],
                                     'Description', 'setDescription')

@implementer(IMetadataSchema)
class MetadataSchemaAdapter(SchemaAdapterBase):

    """Adapter for IMutableDublinCore.
    """

    adapts(IMutableDublinCore)

    _effective = ProxyFieldProperty(IMetadataSchema['effective'],
                                    'effective', 'setEffectiveDate')
    _expires = ProxyFieldProperty(IMetadataSchema['expires'],
                                  'expires', 'setExpirationDate')

    def _getEffective(self):
        if self.context.EffectiveDate() == 'None':
            return None
        return self._effective

    def _getExpires(self):
        if self.context.ExpirationDate() == 'None':
            return None
        return self._expires

    def _getAllowDiscussion(self):
        context = aq_self(self.context)
        return getattr(context, 'allow_discussion', None)

    def _setAllowDiscussion(self, value):
        dtool = getUtility(IDiscussionTool)
        dtool.overrideDiscussionFor(self.context, value)

    allow_discussion = property(_getAllowDiscussion, _setAllowDiscussion)
    identifier = ProxyFieldProperty(IMetadataSchema['identifier'],
                                    'Identifier')
    title = ProxyFieldProperty(IMetadataSchema['title'], 'Title', 'setTitle')
    description = ProxyFieldProperty(IMetadataSchema['description'],
                                     'Description', 'setDescription')
    subject = ProxyFieldProperty(IMetadataSchema['subject'],
                                 'Subject', 'setSubject')
    contributors = ProxyFieldProperty(IMetadataSchema['contributors'],
                                      'listContributors', 'setContributors')
    created = ProxyFieldProperty(IMetadataSchema['created'])
    modified = ProxyFieldProperty(IMetadataSchema['modified'])
    effective = property(_getEffective, _effective.__set__)
    expires = property(_getExpires, _expires.__set__)
    format = ProxyFieldProperty(IMetadataSchema['format'],
                                     'Format', 'setFormat')
    language = ProxyFieldProperty(IMetadataSchema['language'],
                                     'Language', 'setLanguage')
    rights = ProxyFieldProperty(IMetadataSchema['rights'],
                                     'Rights', 'setRights')


class MinimalMetadataEditView(ContentEditFormBase):

    """Edit view for IMutableMinimalDublinCore.
    """

    form_fields = form.FormFields(IMinimalMetadataSchema)

    label = _(u'Properties')

    @memoize
    def getContent(self):
        return MinimalMetadataSchemaAdapter(self.context)

    def setUpWidgets(self, ignore_request=False):
        super(MinimalMetadataEditView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['description'].height = 4


class MetadataEditView(ContentEditFormBase):

    """Edit view for IMutableDublinCore.
    """

    actions = form.Actions(
        form.Action(
            name='change',
            label=_(u'Change'),
            validator='handle_validate',
            success='handle_change_success',
            failure='handle_failure'),
        form.Action(
            name='change_and_edit',
            label=_(u'Change and Edit'),
            validator='handle_validate',
            success='handle_change_and_edit_success',
            failure='handle_failure'),
        form.Action(
            name='change_and_view',
            label=_(u'Change and View'),
            validator='handle_validate',
            success='handle_change_and_view_success',
            failure='handle_failure'))

    form_fields = form.FormFields(IMetadataSchema)
    form_fields['subject'].custom_widget = SubjectInputWidget
    form_fields['contributors'].custom_widget = TupleInputWidget
    form_fields['effective'].custom_widget = DatetimeI18nWidget
    form_fields['expires'].custom_widget = DatetimeI18nWidget

    label = _(u'Properties')

    @memoize
    def getContent(self):
        return MetadataSchemaAdapter(self.context)

    def setUpWidgets(self, ignore_request=False):
        super(MetadataEditView,
              self).setUpWidgets(ignore_request=ignore_request)
        self.widgets['allow_discussion']._messageNoValue = _(u'Default')
        self.widgets['description'].height = 4
        self.widgets['subject'].split = True
        self.widgets['contributors'].height = 6
        self.widgets['contributors'].split = True
        self.widgets['created'].split = True
        self.widgets['modified'].split = True
        self.widgets['effective'].split = True
        self.widgets['expires'].split = True

    def handle_change_success(self, action, data):
        self._handle_success(action, data)
        return self._setRedirect('portal_types', 'object/metadata')

    def handle_change_and_edit_success(self, action, data):
        self._handle_success(action, data)
        return self._setRedirect('portal_types', 'object/edit')
