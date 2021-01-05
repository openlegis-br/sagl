##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" CMFDefault.interfaces package.
"""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from Products.CMFDefault.interfaces import _content
from Products.CMFDefault.interfaces import _tools

from ._content import IDocument
from ._content import IMutableDocument
from ._content import IMutableNewsItem
from ._content import IMutableLink
from ._content import ILink
from ._content import IMutableFavorite
from ._content import IMutableFile
from ._content import IFile
from ._content import IImage
from ._content import IFavorite
from ._content import IMutableImage
from ._content import INewsItem
from ._tools import IMembershipTool

class ICMFDefaultSkin(IDefaultBrowserLayer):

    """CMF default skin.
    """
