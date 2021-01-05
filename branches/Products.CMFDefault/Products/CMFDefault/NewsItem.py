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
""" News content object.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from zope.component.factory import Factory
from zope.interface import implements
from zope.interface import implementer

from Products.CMFDefault.Document import Document
from Products.CMFDefault.interfaces import IMutableNewsItem
from Products.CMFDefault.interfaces import INewsItem
from Products.CMFDefault.permissions import ModifyPortalContent


def addNewsItem( self
               , id
               , title=''
               , description=''
               , text=''
               , text_format=''
               ):
    """Add a NewsItem.
    """
    o=NewsItem( id=id
              , title=title
              , description=description
              , text=text
              , text_format=text_format
              )
    self._setObject(id, o, suppress_events=True)


@implementer(IMutableNewsItem, INewsItem)
class NewsItem(Document):

    """A News Item.
    """


    text_format = 'html'

    security = ClassSecurityInfo()

    security.declareProtected(ModifyPortalContent, 'edit')
    def edit( self, text, description=None, text_format=None ):
        """Edit the News Item.
        """
        if text_format is None:
            text_format = getattr(self, 'text_format', 'structured-text')
        if description is not None:
            self.setDescription( description )
        Document.edit( self, text_format, text )

InitializeClass(NewsItem)

NewsItemFactory = Factory(NewsItem)
