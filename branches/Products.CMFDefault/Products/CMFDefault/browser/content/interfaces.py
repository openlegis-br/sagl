##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Browser view interfaces.
"""

from zope.interface import Interface
from zope.schema import Choice
from zope.schema import TextLine

from Products.CMFDefault.utils import Message as _


class IFolderItem(Interface):
    """Schema for folderish objects contents."""

    name = TextLine(
        title=u"Name",
        required=False,
        readonly=True)


class IDeltaItem(Interface):
    """Schema for delta"""

    delta = Choice(
        title=_(u'order_delta_label', default=u'by'),
        description=u"Move an object up or down the chosen number of places.",
        required=True,
        vocabulary=u'cmf.contents delta vocabulary',
        default=1)
