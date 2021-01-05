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
"""Tests for portal syndication form.
"""

import unittest

from zope.component import getSiteManager
from zope.i18n.interfaces import IUserPreferredCharsets
from zope.interface import alsoProvides
from zope.interface import implements
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import ISyndicationTool
from Products.CMFCore.interfaces import IURLTool
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyTool
from Products.CMFDefault.browser.test_utils import DummyRequest


class DummySyndicationTool(object):

    enabled = False
    period = updatePeriod = "daily"
    frequency = updateFrequency = 1
    base = updateBase = ""
    max_items = 15

    def isSiteSyndicationAllowed(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False


class SiteSyndicationTests(unittest.TestCase):

    def setUp(self):
        """Setup a site"""
        self.site = DummySite('site')
        sm = getSiteManager()
        from Products.CMFDefault.SyndicationInfo import ISyndicationInfo
        syndtool = DummySyndicationTool()
        alsoProvides(syndtool, ISyndicationInfo)
        sm.registerUtility(syndtool, ISyndicationTool)
        sm.registerUtility(DummyTool(), IActionsTool)
        sm.registerUtility(DummyTool(), IMembershipTool)
        sm.registerUtility(DummyTool().__of__(self.site), IURLTool)

    def tearDown(self):
        cleanUp()

    def _getTargetClass(self):
        from Products.CMFDefault.browser.admin.syndication import Site
        request = DummyRequest(ACTUAL_URL="http://example.com")
        alsoProvides(request, IUserPreferredCharsets)
        return Site(self.site, request)

    def test_enabled(self):
        view = self._getTargetClass()
        self.assertFalse(view.enabled())

    def test_disabled(self):
        view = self._getTargetClass()
        self.assertTrue(view.disabled())

    def test_handle_enable(self):
        view = self._getTargetClass()
        view.adapters = {}
        view.handle_enable("enable", {})
        self.assertTrue(view.enabled())
        self.assertEqual(view.status, u"Syndication enabled.")
        self.assertEqual(view.request.response.location,
            "http://www.foobar.com/bar/site?portal_status_message="
            "Syndication%20enabled.")

    def test_handle_change(self):
        import datetime
        today = datetime.datetime.now()
        view = self._getTargetClass()
        view.adapters = {}
        self.assertEqual(view.getContent().period, 'daily')
        self.assertEqual(view.getContent().frequency, 1)
        self.assertEqual(view.getContent().base, "")
        self.assertEqual(view.getContent().max_items, 15)
        data = {'frequency':3, 'period':'weekly', 'base':today,
                'max_items':10}
        view.handle_change("change", data)
        for k, v in data.items():
            self.assertEqual(getattr(view.getContent(), k), v)
        self.assertEqual(view.status, u"Syndication settings changed.")
        self.assertEqual(view.request.response.location,
            "http://www.foobar.com/bar/site?portal_status_message="
            "Syndication%20settings%20changed.")

    def test_handle_disable(self):
        view = self._getTargetClass()
        view.getContent().enabled = True
        self.assertTrue(view.enabled())
        view.handle_disable("disable", {})
        self.assertTrue(view.disabled())
        self.assertEqual(view.status, u"Syndication disabled.")
        self.assertEqual(view.request.response.location,
            "http://www.foobar.com/bar/site?portal_status_message="
            "Syndication%20disabled.")


class FolderSyndicationTests(unittest.TestCase):

    def setUp(self):
        """Setup a site"""
        self.site = DummySite('site')
        self.syndtool = DummySyndicationTool()
        sm = getSiteManager()
        sm.registerUtility(self.syndtool, ISyndicationTool)
        from Products.CMFDefault.SyndicationInfo import ISyndicationInfo
        from Products.CMFDefault.SyndicationInfo import SyndicationInfo
        sm.registerAdapter(SyndicationInfo, [IFolderish], ISyndicationInfo)
        from zope.annotation.interfaces import IAnnotations
        from zope.annotation.attribute import AttributeAnnotations
        sm.registerAdapter(AttributeAnnotations, [IFolderish], IAnnotations)
        sm.registerUtility(DummyTool(), IActionsTool)
        sm.registerUtility(DummyTool(), IMembershipTool)
        sm.registerUtility(DummyTool().__of__(self.site), IURLTool)

    def tearDown(self):
        cleanUp()

    def _getTargetClass(self):
        from Products.CMFDefault.browser.admin.syndication import Folder
        alsoProvides(self.site, IFolderish)
        request = DummyRequest(ACTUAL_URL="http://example.com")
        alsoProvides(request, IUserPreferredCharsets)
        return Folder(self.site, request)

    def test_allowed(self):
        view = self._getTargetClass()
        self.assertFalse(view.allowed())

    def test_enabled(self):
        view = self._getTargetClass()
        self.assertFalse(view.enabled())

    def test_disabled(self):
        view = self._getTargetClass()
        self.assertTrue(view.disabled())

    def test_handle_enable(self):
        self.syndtool.enabled = True
        view = self._getTargetClass()
        view.adapters = {}
        view.handle_enable("enable", {})
        self.assertTrue(view.enabled())
        self.assertEqual(view.status, u"Syndication enabled.")
        self.assertEqual(view.request.response.location,
            "http://www.foobar.com/bar/site?portal_status_message="
            "Syndication%20enabled.")

    def test_handle_disable(self):
        self.syndtool.enabled = False
        view = self._getTargetClass()
        view.adapters = {}
        view.getContent().enable()
        view.handle_disable("disable", {})
        self.assertFalse(view.enabled())
        self.assertEqual(view.status, u"Syndication disabled.")
        self.assertEqual(view.request.response.location,
            "http://www.foobar.com/bar/site?portal_status_message="
            "Syndication%20disabled.")

    def test_handle_change(self):
        view = self._getTargetClass()
        view.adapters = {}
        values = {'frequency': 4, 'period': 'weekly', 'base': '2010-01-01',
                  'max_items': 25}
        view.handle_change("change", values)
        for k, v in values.items():
            self.assertEqual(getattr(view.getContent(), k), v)
        self.assertEqual(view.status, u"Syndication settings changed.")
        self.assertEqual(view.request.response.location,
            "http://www.foobar.com/bar/site?portal_status_message="
            "Syndication%20settings%20changed.")

    def test_handle_revert(self):
        view = self._getTargetClass()
        view.adapters = {}
        values = {'frequency': 4, 'period': 'weekly', 'base': '2010-01-01',
                  'max_items': 25}
        view.handle_change("change", values)
        view.handle_revert("", values)
        for k, v in values.items():
            self.assertNotEqual(getattr(view.getContent(), k), v)
        self.assertEqual(view.status, u"Syndication reset to site default.")
        self.assertEqual(view.request.response.location,
            "http://www.foobar.com/bar/site?portal_status_message="
            "Syndication%20reset%20to%20site%20default.")


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SiteSyndicationTests))
    suite.addTest(unittest.makeSuite(FolderSyndicationTests))
    return suite
