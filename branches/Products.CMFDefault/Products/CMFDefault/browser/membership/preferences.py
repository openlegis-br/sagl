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
"""Change user preferences.
"""

from zope.component import adapts
from zope.component import getUtility
from zope.component import queryUtility
from zope.formlib import form
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.schema import Bool
from zope.schema import Choice
from zope.schema import TextLine
from zope.schema.vocabulary import SimpleVocabulary

from Products.CMFCore.interfaces import IMember
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import ISkinsTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.formlib.form import SettingsEditFormBase
from Products.CMFDefault.formlib.schema import EmailLine
from Products.CMFDefault.utils import Message as _


def portal_skins(context):
    stool = queryUtility(ISkinsTool)
    if stool is None:
        return SimpleVocabulary(())
    return SimpleVocabulary.fromValues(stool.getSkinSelections())


class IPreferencesSchema(Interface):

    """Schema for member views.
    """

    fullname = TextLine(
        title=_(u'Full Name'),
        description=_(u'given names and surname'),
        required=False,
        missing_value=u'')

    email = EmailLine(
        title=_(u'Email Address'),
        description=_(u'info@example.org'))

    listed = Bool(
        title=_(u'Listed status'),
        description=_(u"Select to be listed on the public membership roster."))

    portal_skin = Choice(
        title=_(u'Skin'),
        vocabulary=u"cmf.AvailableSkins",
        required=False,
        missing_value='')

@implementer(IPreferencesSchema)
class PreferencesSchemaAdapter(object):

    """Adapter for IMember.
    """

    adapts(IMember)

    def __init__(self, context):
        self.context = context

    def __getattr__(self, name):
        return self.context.getProperty(name)

    def __setattr__(self, name, value):
        if name in ('email', 'listed', 'portal_skin'):
            self.context.setMemberProperties({name: value})
        else:
            object.__setattr__(self, name, value)

    def _getFullName(self):
        ptool = getUtility(IPropertiesTool)
        encoding = ptool.getProperty('default_charset', None)
        return self.context.getProperty('fullname').decode(encoding)

    def _setFullName(self, value):
        ptool = getUtility(IPropertiesTool)
        encoding = ptool.getProperty('default_charset', None)
        self.context.setMemberProperties({'fullname': value.encode(encoding)})

    fullname = property(_getFullName, _setFullName)


class PreferencesFormView(SettingsEditFormBase):

    """Edit view for IPreferencesSchema.

    Only user can change his own preference.
    User can change the following preferences:
    Full name
    Email address
    Listed or unlisted
    User's chosen skin if set
    """

    label = _(u"Member Preferences")
    successMessage = _(u"Member preferences changed.")

    form_fields = form.FormFields(IPreferencesSchema)

    @memoize
    def getContent(self):
        mtool = getUtility(IMembershipTool)
        member = mtool.getAuthenticatedMember()
        return PreferencesSchemaAdapter(member)

    def applyChanges(self, data):
        changes = super(PreferencesFormView, self).applyChanges(data)
        if any('portal_skin' in v for v in changes.itervalues()):
            stool = queryUtility(ISkinsTool)
            if stool is not None:
                stool.updateSkinCookie()
        return changes

    def handle_change_success(self, action, data):
        self._handle_success(action, data)
        return self._setRedirect('portal_actions', 'user/preferences')

    def handle_cancel_success(self, action, data):
        return self._setRedirect('portal_actions', 'user/mystuff')
