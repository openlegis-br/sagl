##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Test Products.CMFDefault.browser.folder
"""

import unittest
from Testing import ZopeTestCase

from zope.component import getSiteManager
from zope.publisher.browser import TestRequest
from zope.publisher.interfaces.browser import IBrowserPublisher
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.interfaces import IURLTool
from Products.CMFCore.PortalFolder import PortalFolder
from Products.CMFCore.tests.base.dummy import DummyContent
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyTool
from Products.CMFDefault.browser.content.folder import ContentsView
from Products.CMFDefault.browser.content.folder import FolderView
from Products.CMFDefault.testing import FunctionalLayer


class FolderContentsViewTests(unittest.TestCase):

    def setUp(self):
        """Setup a site"""
        self.site = site = DummySite('site')
        sm = getSiteManager()
        sm.registerUtility(DummyTool(), IMembershipTool)
        sm.registerUtility(DummyTool().__of__(site), IPropertiesTool)
        sm.registerUtility(DummyTool().__of__(site), IURLTool)
        sm.registerUtility(DummyTool(), ITypesTool)
        folder = PortalFolder('test_folder')
        self.folder = site._setObject('test_folder', folder)

    def tearDown(self):
        cleanUp()

    def _make_one(self, name="DummyItem"):
        content = DummyContent(name)
        content.portal_type = "Dummy Content"
        self.folder._setObject(name, content)

    def _make_batch(self):
        """Add enough objects to force pagination"""
        batch_size = ContentsView._BATCH_SIZE
        for i in range(batch_size + 2):
            content_id = "Dummy%s" % i
            self._make_one(content_id)

    def test_getNavigationURL(self):
        url = 'http://example.com/folder_contents'
        self._make_batch()
        view = ContentsView(self.folder, TestRequest(ACTUAL_URL=url))
        view._getNavigationVars = lambda: {}
        self.assertTrue(view._getNavigationURL(25) == url + "?form.b_start=25")

    def test_view(self):
        view = ContentsView(self.folder, TestRequest())
        self.assertTrue(IBrowserPublisher.providedBy(view))

    def test_up_info(self):
        view = ContentsView(self.folder, TestRequest())
        self.assertEqual({'url': u'', 'id': u'Root', 'icon': u''},
                         view.up_info())

    def test_list_batch_items(self):
        view = ContentsView(self.folder, TestRequest())
        view._getNavigationVars = lambda: {}
        self.assertEqual(view.listBatchItems(), ())

    def test_is_orderable(self):
        view = ContentsView(self.folder, TestRequest())
        view._getNavigationVars = lambda: {}
        self.assertFalse(view.is_orderable())

    def test_sort_can_be_changed(self):
        view = ContentsView(self.folder, TestRequest())
        view._getNavigationVars = lambda: {}
        self.assertFalse(view.can_sort_be_changed())

    def test_show_basic_empty(self):
        view = ContentsView(self.folder, TestRequest())
        view._getNavigationVars = lambda: {}
        self.assertFalse(view.show_basic())

    def test_show_basic(self):
        self._make_one()
        view = ContentsView(self.folder, TestRequest())
        view._getNavigationVars = lambda: {}
        self.assertTrue(view.show_basic())

    def test_show_paste(self):
        view = ContentsView(self.folder, TestRequest())
        self.assertFalse(view.show_paste())

    def test_validate_items(self):
        """Cannot validate forms without widgets"""
        view = ContentsView(self.folder, TestRequest())
        self.assertRaises(AttributeError,
                          view.validate_items, "", {'foo': 'bar'})

    def test_get_ids(self):
        request = TestRequest(form={'form.select_ids': ['DummyItem1',
                                                        'DummyItem3']})
        view = ContentsView(self.folder, request)
        self.assertEqual(view._get_ids(), ['DummyItem1', 'DummyItem3'])


class FolderViewTests(unittest.TestCase):

    def setUp(self):
        """Setup a site"""
        self.site = site = DummySite('site')
        folder = PortalFolder('test_folder')
        self.folder = site._setObject('test_folder', folder)

    def _make_one(self, name="DummyItem"):
        content = DummyContent(name)
        content.portal_type = "Dummy Content"
        self.folder._setObject(name, content)

    def _make_batch(self):
        """Add enough objects to force pagination"""
        batch_size = ContentsView._BATCH_SIZE
        for i in range(batch_size + 2):
            content_id = "Dummy%s" % i
            self._make_one(content_id)

    def test_getNavigationURL(self):
        url = 'http://example.com/view'
        self._make_batch()
        view = FolderView(self.folder, TestRequest(ACTUAL_URL=url))
        self.assertEqual(view._getNavigationURL(25), url + "?b_start:int=25")

    def test_folder_has_local(self):
        self._make_one('local_pt')
        view = FolderView(self.folder, TestRequest())
        self.assertTrue(view.has_local())

    def test_folder_not_has_local(self):
        self._make_one()
        view = FolderView(self.folder, TestRequest())
        self.assertFalse(view.has_local())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FolderContentsViewTests))
    suite.addTest(unittest.makeSuite(FolderViewTests))
    s = ZopeTestCase.FunctionalDocFileSuite('folder.txt')
    s.layer = FunctionalLayer
    suite.addTest(s)
    return suite
