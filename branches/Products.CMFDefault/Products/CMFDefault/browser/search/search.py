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
"""Search views"""

from DateTime.DateTime import DateTime
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.formlib import form
from ZPublisher.HTTPRequest import record

from .interfaces import ISearchSchema
from Products.CMFCore.interfaces import ICatalogTool
from Products.CMFDefault.browser.utils import decode
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.widgets.batch import BatchViewBase
from Products.CMFDefault.formlib.form import EditFormBase
from Products.CMFDefault.formlib.widgets import ChoiceMultiSelectWidget
from Products.CMFDefault.permissions import ReviewPortalContent
from Products.CMFDefault.utils import Message as _

EPOCH = DateTime('1970/01/01 00:00:00 UTC')


class Search(EditFormBase):

    """Portal Search Form"""

    template = ViewPageTemplateFile('search.pt')

    actions = form.Actions(
        form.Action(
            name='search',
            label=_(u"Search"),
            success='handle_search',
            failure='handle_failure',
            ),
        )

    @property
    def label(self):
        return _(u'Search ${portal_title}',
                 mapping={'portal_title': self.title()})

    @property
    def form_fields(self):
        form_fields = form.FormFields(ISearchSchema)
        form_fields['review_state'].custom_widget = ChoiceMultiSelectWidget
        form_fields['Subject'].custom_widget = ChoiceMultiSelectWidget
        form_fields['portal_type'].custom_widget = ChoiceMultiSelectWidget
        if not self._checkPermission(ReviewPortalContent):
            form_fields = form_fields.omit('review_state')
        return form_fields

    def handle_search(self, action, data):
        if 'form.created' in self.request.form:
            del self.request.form['form.created']
        if 'created' in data and data['created']:
            created = record()
            created.query = DateTime(str(data['created']))
            created.range = 'min'
            self.request.form['form.created'] = created
        return self._setRedirect('portal_actions', 'global/search',
                                 'review_state,SearchableText,Title,Subject,'
                                 'Description,created,portal_type,'
                                 'listCreators')


class SearchView(BatchViewBase):

    """View for search results.
    """

    # helpers

    @memoize
    def _getNavigationVars(self):
        kw = self.request.form.copy()
        for k, v in kw.items():
            if k in ('review_state', 'SearchableText', 'Title', 'Subject',
                     'Description', 'portal_type', 'listCreators'):
                if isinstance(v, (list, tuple)):
                    v = filter(None, v)
                if not v:
                    del kw[k]
            elif k in ('created',):
                if v['query'] == EPOCH and v['range'] == 'min':
                    del kw[k]
                else:
                    # work around problems with DateTime in records
                    kw[k] = v.copy()
            elif k in ('go', 'go.x', 'go.y'):
                del kw[k]
        return kw

    @memoize
    def _get_items(self):
        ctool = getUtility(ICatalogTool)
        return ctool.searchResults(self._getNavigationVars())

    # interface

    @memoize
    @decode
    def listBatchItems(self):
        items = [ {'description': item.Description,
                   'icon': item.getIconURL,
                   'title': item.Title,
                   'type': item.Type,
                   'date': item.Date,
                   'url': item.getURL(),
                   'format': None}
                  for item in self._getBatchObj() ]
        return tuple(items)
