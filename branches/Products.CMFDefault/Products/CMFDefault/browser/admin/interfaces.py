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
"""Schema for portal forms.
"""

import codecs

from zope.interface import Interface
from zope.schema import ASCIILine
from zope.schema import Bool
from zope.schema import Choice
from zope.schema import TextLine

from Products.CMFDefault.formlib.vocabulary import SimpleVocabulary
from Products.CMFDefault.utils import Message as _

available_policies = (
    (u'email', True, _(u"Generate and email members' initial password")),
    (u'select', False, _(u"Allow members to select their initial password")))

def check_encoding(value):
    encoding = ""
    try:
        encoding = codecs.lookup(value)
    except LookupError:
        pass
    return encoding != ""


class IPortalConfig(Interface):

    """Schema for portal configuration form.
    """

    email_from_name = TextLine(
        title=_(u"Portal 'From' name"),
        description=_(u"When the portal generates mail, it uses this name as "
                      u"its (apparent) sender."),
        required=False,
        missing_value=u'')

    email_from_address = TextLine(
        title=_(u"Portal 'From' address"),
        description=_(u"When the portal generates mail, it uses this address "
                      u"as its (apparent) return address."),
        required=False,
        missing_value=u'')

    smtp_server = TextLine(
        title=_(u"SMTP server"),
        description=_(u"This is the address of your local SMTP (out-going "
                      u"mail) server."),
        required=False,
        missing_value=u'')

    title = TextLine(
        title=_(u"Portal title"),
        description=_(u"This is the title which appears at the top of every "
                      u"portal page."),
        required=False,
        missing_value=u'')

    description = TextLine(
        title=_(u"Portal description"),
        description=_(u"This description is made available via syndicated "
                      u"content and elsewhere. It should be fairly brief."),
        required=False,
        missing_value=u'')

    validate_email = Choice(
        title=_(u"Password policy"),
        vocabulary=SimpleVocabulary.fromTitleItems(available_policies),
        default=False)

    default_charset = ASCIILine(
        title=_(u"Portal default encoding"),
        description=_(u"Charset used to decode portal content strings. If "
                      u"empty, 'ascii' is used."),
        required=False,
        constraint=check_encoding,
        default="utf-8")

    email_charset = ASCIILine(
        title=_(u"Portal email encoding"),
        description=_(u"Charset used to encode emails send by the portal. If "
                      u"empty, 'utf-8' is used if necessary."),
        required=False,
        constraint=check_encoding,
        default="utf-8")

    enable_actionicons = Bool(
        title=_(u"Show action icons"),
        description=_(u"Actions available to the user are shown as textual "
                      u"links. With this option enabled, they are also shown "
                      u"as icons if the action definition specifies one."),
        required=False)

    enable_permalink = Bool(
        title=_(u"Show permalinks"),
        description=_(u"If permalinks are enabled then a unique identifier is "
                      u"assigned to every item of content independent of it's "
                      u"id or position in a site. This requires the CMFUid "
                      u"tool to be installed."),
        required=False)
