##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Portal Configuration Form.
"""

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import adapts
from zope.component import getUtility
from zope.formlib import form
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.formlib.form import SettingsEditFormBase
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFDefault.formlib.widgets import ChoiceRadioWidget
from Products.CMFDefault.utils import Message as _

from .interfaces import IPortalConfig

@implementer(IPortalConfig)
class ConfigSchemaAdapter(SchemaAdapterBase):

    """Adapter for IPropertiesTool.
    """

    adapts(IPropertiesTool)

    def __getattr__(self, name):
        if name in ('title', 'smtp_server'):
            value = getattr(self.context, name)()
        else:
            value = self.context.getProperty(name)
        if isinstance(value, str) and self.encoding:
            return value.decode(self.encoding)
        return value

    def __setattr__(self, name, value):
        if name in ('context', 'encoding'):
            SchemaAdapterBase.__setattr__(self, name, value)
            return
        if isinstance(value, unicode) and self.encoding:
            value = value.encode(self.encoding)
        self.context.editProperties({name: value})


class PortalConfig(SettingsEditFormBase):

    form_fields = form.FormFields(IPortalConfig)
    form_fields['validate_email'].custom_widget = ChoiceRadioWidget

    template = ViewPageTemplateFile("config.pt")
    label = _(u'Portal Configuration')
    description = _(u'This form is used to set the portal configuration '
                     'options.')
    successMessage = _(u'Portal settings changed.')

    @memoize
    def getContent(self):
        ptool = getUtility(IPropertiesTool)
        return ConfigSchemaAdapter(ptool)

    def handle_change_success(self, action, data):
        self._handle_success(action, data)
        return self._setRedirect('portal_actions', 'global/configPortal')

    def handle_cancel_success(self, action, data):
        return self._setRedirect('portal_actions', 'ROOT')
