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
""" Unit tests for the SyndicationInfo adapter.
"""

from datetime import datetime
import unittest
import Testing

from zope.annotation.interfaces import IAnnotations
from zope.component import getSiteManager
from zope.component import getAdapter
from zope.interface.verify import verifyClass

from Products.CMFCore.interfaces import ISyndicationTool
from Products.CMFCore.tests.base.testcase import TransactionalTest


class SyndicationInfoTests(TransactionalTest):

    def setUp(self):
        from zope.annotation.attribute import AttributeAnnotations
        from Products.CMFCore.interfaces import IFolderish
        from Products.CMFCore.PortalFolder import PortalFolder

        super(SyndicationInfoTests, self).setUp()
        self.app._setObject('portal', PortalFolder('portal'))
        self.portal = self.app.portal
        self.syndtool = DummySyndicationTool()
        sm = getSiteManager()
        sm.registerUtility(self.syndtool, ISyndicationTool)
        sm.registerAdapter(AttributeAnnotations, [IFolderish], IAnnotations)

    def _getTargetClass(self):
        from Products.CMFDefault.SyndicationInfo import SyndicationInfo

        return SyndicationInfo

    def _makeOne(self):
        from zope.interface import alsoProvides
        from Products.CMFCore.PortalFolder import PortalFolder
        folder = PortalFolder('folder')

        self.portal._setObject('folder', folder)
        alsoProvides(folder, IAnnotations)

        return self._getTargetClass()(folder)

    def test_interfaces(self):
        from Products.CMFCore.interfaces import ISyndicationInfo

        verifyClass(ISyndicationInfo, self._getTargetClass())

    def test_site_settings(self):
        adapter = self._makeOne()
        self.assertTrue(adapter.site_settings is self.syndtool)

    def test_annotation(self):
        adapter = self._makeOne()
        annotations = getAdapter(adapter.context, IAnnotations)
        self.assertFalse(adapter.key in annotations)
        adapter.base = datetime.today()
        self.assertTrue(adapter.key in annotations)

    def test_set(self):
        adapter = self._makeOne()
        now = datetime.today()
        settings = {'max_items': 10, 'frequency': 7, 'period': 'daily',
                    'base': now}
        adapter.base = now
        adapter.period = 'daily'
        adapter.frequency = 7
        adapter.max_items = 10
        for k, v in settings.items():
            self.assertEqual(getattr(adapter, k), v)

    def test_rfc822(self):
        adapter = self._makeOne()
        now = datetime.today()
        adapter.base = now
        self.assertEqual(adapter.rfc822(),
                         now.strftime("%a, %d %b %Y %H:%M:%S +0000"))

    def revert(self):
        adapter = self._makeOne()
        settings = {'max_items': 20, 'frequency': 1, 'period': 'monthly',
                    'base': datetime.today()}
        setattr(adapter.context, adapter.key, settings)
        self.assertEqual(getattr(adapter.context, adapter.key, settings))
        adapter.revert()
        self.assertNotEqual(getattr(adapter.context, adapter.key, settings))

    def test_not_enabled_by_default(self):
        adapter = self._makeOne()
        self.assertFalse(adapter.enabled)

    def test_enable(self):
        adapter = self._makeOne()
        self.syndtool.enabled = True
        adapter.enable()
        self.assertTrue(adapter.enabled)

    def test_get_default_values(self):
        adapter = self._makeOne()
        self.assertFalse(hasattr(adapter.context, adapter.key))
        self.assertEqual(adapter.period, self.syndtool.period)
        self.assertEqual(adapter.frequency, self.syndtool.frequency)
        self.assertEqual(adapter.base, self.syndtool.base)
        self.assertEqual(adapter.max_items, self.syndtool.max_items)

    def test_disable(self):
        adapter = self._makeOne()
        self.syndtool.enabled = True
        adapter.enable()
        self.assertTrue(adapter.enabled)
        adapter.disable()
        self.assertFalse(adapter.enabled)


class DummySyndicationTool(object):

    enabled = 0
    period = 'daily'
    frequency = 1
    base = datetime(2010, 10, 3, 12, 0, 0)
    max_items = 15


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(SyndicationInfoTests),
        ))
