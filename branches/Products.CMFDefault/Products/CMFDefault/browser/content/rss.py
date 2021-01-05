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
"""RSS view for syndicatable items"""

from zope.component import getAdapter
from zope.component import getUtility
from zope.sequencesort.ssort import sort
from ZTUtils import LazyFilter

from Products.CMFCore.interfaces import ISyndicationInfo
from Products.CMFCore.interfaces import ISyndicationTool
from Products.CMFCore.interfaces import IURLTool
from Products.CMFDefault.browser.utils import decode
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.utils import ViewBase


connvert_to_hours = {'hourly': 1, 'daily': 24, 'weekly': 7 * 24, 'monthly':
                     30 * 24, 'yearly': 365 * 24}

class View(ViewBase):

    """Return an RSS conform list of content items"""

    @property
    @memoize
    def synd_info(self):
        return getAdapter(self.context, ISyndicationInfo)

    @memoize
    @decode
    def items(self):
        """Return items according to policy"""
        syndtool = getUtility(ISyndicationTool)
        key, reverse = self.context.getDefaultSorting()
        items = syndtool.getSyndicatableContent(self.context)
        items = sort(items, ((key, 'cmp', reverse and 'desc' or 'asc'),))
        items = LazyFilter(items, skip='View')
        for idx, o in enumerate(items):
            if idx < self.synd_info.max_items:
                yield {'title': o.Title(),
                       'description': o.Description(),
                       'creators': o.listCreators(),
                       'subjects': o.Subject(),
                       'rights': o.Rights(),
                       'publisher': o.Publisher(),
                       'url': o.absolute_url(),
                       'date': o.modified().rfc822(),
                       'uid': None}

    @memoize
    @decode
    def channel(self):
        """Provide infomation about the channel"""

        ttl = 60 * (self.synd_info.frequency *
                    connvert_to_hours[self.synd_info.period])

        info = {'base': self.synd_info.rfc822(),
                'ttl': ttl,
                'period': self.synd_info.period,
                'title': self.context.Title(),
                'description': self.context.Description(),
                'portal_url': getUtility(IURLTool)()
                }
        return info
