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
"""Browser view utilities.
"""

from zope.publisher.browser import BrowserView
from zope.component import getUtility

from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import IURLTool
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import getBrowserCharset
from Products.CMFDefault.utils import toUnicode


def decode(meth):
    def decoded_meth(self, *args, **kw):
        return toUnicode(meth(self, *args, **kw), self._getDefaultCharset())
    return decoded_meth

def memoize(meth):
    def memoized_meth(self, *args):
        if not hasattr(self, '__memo__'):
            self.__memo__ = {}
        sig = (meth, args)
        if sig not in self.__memo__:
            self.__memo__[sig] = meth(self, *args)
        return self.__memo__[sig]
    return memoized_meth


class ViewBase(BrowserView):

    # helpers

    @memoize
    def _getTool(self, name):
        # BBB: _getTool is deprecated. Please use getUtility instead.
        return getToolByName(self.context, name)

    @memoize
    def _checkPermission(self, permission):
        mtool = getUtility(IMembershipTool)
        return mtool.checkPermission(permission, self.context)

    @memoize
    def _getPortalURL(self):
        utool = getUtility(IURLTool)
        return utool()

    @memoize
    def _getViewURL(self):
        return self.request['ACTUAL_URL']

    @memoize
    def _getDefaultCharset(self):
        ptool = getUtility(IPropertiesTool)
        return ptool.getProperty('default_charset', None)

    @memoize
    def _getBrowserCharset(self):
        return getBrowserCharset(self.request)

    # interface

    @memoize
    @decode
    def title(self):
        return self.context.Title()

    @memoize
    @decode
    def description(self):
        return self.context.Description()
