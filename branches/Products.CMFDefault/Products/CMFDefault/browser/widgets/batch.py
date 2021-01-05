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
"""Base classes for batch views.
"""

import sys
import urllib

from zope.formlib import form
from zope.interface import Interface
from zope.schema import Int
from zope.schema import TextLine
from ZTUtils import Batch
from ZTUtils import make_query

from Products.CMFDefault.browser.utils import decode
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.utils import ViewBase
from Products.CMFDefault.utils import Message as _
from Products.CMFDefault.utils import thousands_commas


class IBatchForm(Interface):

    """Schema for batch forms
    """

    b_start = Int(
        title=u"Batch start",
        required=False,
        default=0)


class ISortForm(Interface):

    """Schema for sort keys
    """

    sort_key = TextLine(
        title=u"Sort key",
        required=False)

    reverse = Int(
        title=u"Reverse sort order",
        required=False)


class BatchViewBase(ViewBase):

    """Base class for creating batch-based views.
    """

    _BATCH_SIZE = 25
    _NEXT_PLURAL_MESSAGE = _(u'Next ${count} items')
    _NEXT_SINGULAR_MESSAGE = _(u'Next item')
    _PREV_PLURAL_MESSAGE = _(u'Previous ${count} items')
    _PREV_SINGULAR_MESSAGE = _(u'Previous item')

    @memoize
    def _getBatchStart(self):
        return self._getNavigationVars().get('b_start', 0)

    @memoize
    def _getBatchObj(self):
        b_start = self._getBatchStart()
        items = self._get_items()
        return Batch(items, self._BATCH_SIZE, b_start, orphan=0)

    @memoize
    def _getNavigationVars(self):
        return self.request.form

    @memoize
    def _getNavigationURL(self, b_start):
        target = self._getViewURL()
        kw = self._getNavigationVars().copy()

        kw['b_start'] = b_start
        for k, v in kw.items():
            if not v or k == 'portal_status_message':
                del kw[k]
            elif isinstance(v, unicode):
                kw[k] = v.encode(self._getBrowserCharset())

        query = kw and u'?{0}'.format(make_query(kw)) or u''
        return u'{0}{1}'.format(target, query)

    # interface

    @memoize
    @decode
    def listBatchItems(self):
        batch_obj = self._getBatchObj()

        items = []
        for item in batch_obj:
            item_description = item.Description()
            item_title = item.Title()
            item_type = item.getPortalTypeName()
            if item_type == 'Favorite':
                try:
                    item = item.getObject()
                    item_description = item_description or item.Description()
                    item_title = item_title or item.Title()
                    item_type = item.getPortalTypeName()
                except KeyError:
                    pass
            is_file = item_type in ('File', 'Image')
            is_link = item_type == 'Link'
            items.append({'description': item_description,
                          'format': is_file and item.Format() or '',
                          'icon': item.getIconURL(),
                          'size': is_file and ('%0.1f kB' %
                                             (item.get_size() / 1024.0)) or '',
                          'title': item_title,
                          'type': item.Type(),
                          'url': is_link and item.getRemoteUrl() or
                                 item.absolute_url()})
        return tuple(items)

    @memoize
    def navigation_previous(self):
        batch_obj = self._getBatchObj().previous
        if batch_obj is None:
            return None

        length = len(batch_obj)
        url = self._getNavigationURL(batch_obj.first)
        if length == 1:
            title = self._PREV_SINGULAR_MESSAGE
        else:
            title = _(self._PREV_PLURAL_MESSAGE, mapping={'count': length})
        return {'title': title, 'url': url}

    @memoize
    def navigation_next(self):
        batch_obj = self._getBatchObj().next
        if batch_obj is None:
            return None

        length = len(batch_obj)
        url = self._getNavigationURL(batch_obj.first)
        if length == 1:
            title = self._NEXT_SINGULAR_MESSAGE
        else:
            title = _(self._NEXT_PLURAL_MESSAGE, mapping={'count': length})
        return {'title': title, 'url': url}

    def page_range(self):
        """Create a range of up to ten pages around the current page"""
        b_size = self._BATCH_SIZE
        range_start = max(self.page_number() - 5, 0)
        range_stop = min(max(self.page_number() + 5, 10), self.page_count())

        pages = []
        for p in range(range_start, range_stop):
            b_start = p * b_size
            pages.append({'number': p + 1,
                          'url': self._getNavigationURL(b_start)})
        return pages

    @memoize
    def page_count(self):
        """Count total number of pages in the batch"""
        batch_obj = self._getBatchObj()
        count = (batch_obj.sequence_length - 1) / self._BATCH_SIZE + 1
        return count

    @memoize
    def page_number(self):
        """Get the number of the current page in the batch"""
        return (self._getBatchStart() / self._BATCH_SIZE) + 1

    @memoize
    def summary_length(self):
        length = self._getBatchObj().sequence_length
        if sys.version_info < (2, 7):
            # BBB: for Python 2.6
            return length and thousands_commas(length) or ''
        return length and '{:,}'.format(length) or ''

    @memoize
    def summary_type(self):
        length = self._getBatchObj().sequence_length
        return (length == 1) and _(u'item') or _(u'items')

    @memoize
    @decode
    def summary_match(self):
        return self._getNavigationVars().get('SearchableText', None)


class BatchFormMixin(BatchViewBase):

    """Mixin class for creating batch-based forms.
    """

    hidden_fields = form.FormFields(IBatchForm, ISortForm)

    @memoize
    def _getNavigationVars(self):
        data = {}
        form.getWidgetsData(self.hidden_widgets, self.prefix, data)
        return data

    @memoize
    def _getNavigationURL(self, b_start):
        target = self._getViewURL()
        kw = self._getNavigationVars().copy()

        kw['b_start'] = b_start
        for k, v in kw.items():
            if not v or k == 'portal_status_message':
                del kw[k]
            else:
                new_key = "%s%s" % (form.expandPrefix(self.prefix), k)
                if new_key != k:
                    kw[new_key] = v
                    del kw[k]

        query = kw and ('?%s' % urllib.urlencode(kw)) or ''
        return u'%s%s' % (target, query)

    @memoize
    def setUpWidgets(self, ignore_request=False):
        self.hidden_widgets = form.setUpWidgets(
            self.hidden_fields, self.prefix, self.context, self.request,
            ignore_request=ignore_request)
