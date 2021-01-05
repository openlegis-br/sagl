#############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from zope.traversing.browser import absoluteurl
from zope.traversing.browser.interfaces import IAbsoluteURL
from zope.publisher.interfaces.browser import IBrowserRequest

from grokcore.view.interfaces import IGrokView

from Acquisition import aq_inner

from zope import component
from grokcore import component as grok


class ViewAbsoluteURL(absoluteurl.AbsoluteURL, grok.MultiAdapter):
    grok.adapts(IGrokView, IBrowserRequest)
    grok.provides(IAbsoluteURL)

    def _obj(self):
        return aq_inner(self.context.context)

    def __str__(self):
        return self._obj().absolute_url() + '/' + self.context.__view_name__

    __call__ = __str__

    def breadcrumbs(self):
        obj_breadcrumbs = component.getMultiAdapter(
            (self._obj(), self.request), IAbsoluteURL).breadcrumbs()

        obj_breadcrumbs += ({'name': self.context.__view_name__,
                                'url': self()},)

        return obj_breadcrumbs
