##############################################################################
#
# Copyright (c) 2005 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Unit tests for SyndicationTool module.
"""

import unittest
import Testing

import warnings
from datetime import datetime
from datetime import timedelta

from zope.component import getSiteManager
from zope.component import queryAdapter
from zope.interface import alsoProvides
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.tests.base.testcase import SecurityTest


class Dummy:

    period = None
    frequency = None
    base = None
    max_items = None

    def getId(self):
        return 'dummy'


class DummyInfo(object):

    def __init__(self, context):
        self.context = context

    def __call__(self):
        pass

    def set_f(self, frequency):
        self.context.frequency = frequency

    def get_f(self):
        return self.context.frequency

    frequency = property(get_f, set_f)

    def get_p(self):
        return self.context.period

    def set_p(self, period):
        self.context.period = period

    period = property(get_p, set_p)

    def get_b(self):
        return self.context.base

    def set_b(self, base):
        self.context.base = base

    base = property(get_b, set_b)

    def get_m(self):
        return self.context.max_items

    def set_m(self, max_items):
        self.context.max_items = max_items

    max_items = property(get_m, set_m)

    @property
    def enabled(self):
        if hasattr(self.context, 'enabled'):
            return self.context.enabled
        return False

    def enable(self):
        self.context.enabled = True

    def disable(self):
        self.context.enabled = False


class SyndicationToolTests(SecurityTest):

    def _getTargetClass(self):
        from Products.CMFDefault.SyndicationTool import SyndicationTool
        return SyndicationTool

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _makeContext(self):
        from Products.CMFCore.interfaces import IFolderish, ISyndicationInfo
        self.folder = folder = Dummy()
        alsoProvides(folder, IFolderish)
        sm = getSiteManager()
        sm.registerAdapter(DummyInfo, [IFolderish], ISyndicationInfo)
        return folder

    def _makeInfo(self, context):
        info = DummyInfo(context)
        return info

    def tearDown(self):
        cleanUp()
        SecurityTest.tearDown(self)

    def test_interfaces(self):
        from Products.CMFCore.interfaces import ISyndicationTool

        verifyClass(ISyndicationTool, self._getTargetClass())

    def test_empty(self):
        ONE_MINUTE = timedelta(0, 61, 0)

        tool = self._makeOne()

        self.assertEqual(tool.period, 'daily')
        self.assertEqual(tool.frequency, 1)
        self.assertTrue(datetime.now() - tool.base < ONE_MINUTE)
        self.assertFalse(tool.enabled)
        self.assertEqual(tool.max_items, 15)

    def test_enable_site_syndication(self):
        tool = self._makeOne()
        self.assertFalse(tool.enabled)
        tool.enable()
        self.assertTrue(tool.enabled)

    def test_disable_site_syndication(self):
        tool = self._makeOne()
        self.assertFalse(tool.enabled)
        tool.enable()
        tool.disable()
        self.assertFalse(tool.enabled)

    def test_object_not_syndicatable(self):
        tool = self._makeOne()
        self.assertFalse(tool.isSyndicationAllowed(Dummy))

    def test_object_is_syndicatable(self):
        from Products.CMFCore.interfaces import ISyndicationInfo
        self._makeOne()
        context = self._makeContext()
        adapter = queryAdapter(context, ISyndicationInfo)
        self.assertTrue(adapter is not None)

    def test_object_syndication_is_disabled(self):
        tool = self._makeOne()
        context = self._makeContext()
        self.assertFalse(tool.isSyndicationAllowed(context))

    def test_enable_object_syndication(self):
        tool = self._makeOne()
        tool.enabled = True
        context = self._makeContext()
        tool.enableSyndication(context)
        self.assertTrue(tool.isSyndicationAllowed(context))

    def test_editSyInformationProperties_normal(self):
        PERIOD = 'hourly'
        FREQUENCY = 4
        NOW = datetime.now()
        MAX_ITEMS = 42

        tool = self._makeOne()
        tool.enable()
        context = self._makeContext()
        tool.enableSyndication(context)

        tool.editSyInformationProperties(context,
                                         updatePeriod=PERIOD,
                                         updateFrequency=FREQUENCY,
                                         updateBase=NOW,
                                         max_items=MAX_ITEMS,
                                        )
        info = tool.getSyndicationInfo(context)
        self.assertEqual(info.frequency, FREQUENCY)
        self.assertEqual(info.period, PERIOD)
        self.assertEqual(info.base, NOW)
        self.assertEqual(info.max_items, MAX_ITEMS)

    def test_getSyndicatableContent(self):
        # http://www.zope.org/Collectors/CMF/369
        # Make sure we use a suitable base class call when determining
        # syndicatable content
        from Products.CMFCore.PortalFolder import PortalFolder
        from Products.CMFCore.CMFBTreeFolder import CMFBTreeFolder
        from Products.CMFCore.TypesTool import TypesTool

        PERIOD = 'hourly'
        FREQUENCY = 4
        NOW = datetime.now()
        MAX_ITEMS = 42

        getSiteManager().registerUtility(TypesTool(), ITypesTool)
        self.app._setObject('pf', PortalFolder('pf'))
        self.app._setObject('bf', CMFBTreeFolder('bf'))
        tool = self._makeOne()
        tool.period = PERIOD
        tool.frequency = FREQUENCY
        tool.base = NOW
        tool.enable()
        tool.max_items = MAX_ITEMS

        self.assertEqual(len(tool.getSyndicatableContent(self.app.pf)), 0)
        self.assertEqual(len(tool.getSyndicatableContent(self.app.bf)), 0)

    def test_getUpdateBase(self):
        NOW = datetime.now()

        tool = self._makeOne()
        tool.base = NOW

        self.assertEqual(NOW.strftime("%a, %d %b %Y %H:%M:%S +0000"),
                         tool.getUpdateBase())

    def test_getUpdateBaseWithContext(self):
        NOW = datetime.now()

        tool = self._makeOne()
        tool.enable()

        context = self._makeContext()
        info = self._makeInfo(context)
        tool.enableSyndication(context)
        info.base = NOW

        self.assertEqual(NOW.strftime("%a, %d %b %Y %H:%M:%S +0000"),
                         tool.getUpdateBase(context))

    def test_getHTML4UpdateBase(self):
        NOW = datetime.now()

        tool = self._makeOne()
        tool.base = NOW

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            as_HTML4 = tool.getHTML4UpdateBase()

        self.assertEqual(NOW.strftime("%Y-%m-%dT%H:%M:%SZ"), as_HTML4)

    def test_getHTML4UpdateBaseWithContext(self):
        NOW = datetime.now()

        tool = self._makeOne()
        tool.enable()

        context = self._makeContext()
        info = self._makeInfo(context)
        tool.enableSyndication(context)
        info.base = NOW

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            as_HTML4 = tool.getHTML4UpdateBase(context)

        self.assertEqual(NOW.strftime("%Y-%m-%dT%H:%M:%SZ"), as_HTML4)

    def test_getMaxItems(self):
        max_items = 5

        tool = self._makeOne()
        tool.max_items = max_items

        self.assertEqual(max_items, tool.getMaxItems())

    def test_getMaxItemsWithContext(self):
        max_items = 10

        tool = self._makeOne()
        tool.enable()

        context = self._makeContext()
        info = self._makeInfo(context)
        tool.enableSyndication(context)
        info.max_items = max_items

        self.assertEqual(max_items, tool.getMaxItems(context))

    def test_getUpdatePeriod(self):
        period = 3

        tool = self._makeOne()
        tool.period = period

        self.assertEqual(period, tool.getUpdatePeriod())

    def test_getUpdatePeriodWithContext(self):
        period = 2

        tool = self._makeOne()
        tool.enable()

        context = self._makeContext()
        info = self._makeInfo(context)
        tool.enableSyndication(context)
        info.period = period

        self.assertEqual(period, tool.getUpdatePeriod(context))

    def test_getUpdateFrequency(self):
        frequency = 'monthly'

        tool = self._makeOne()
        tool.frequency = frequency

        self.assertEqual(frequency, tool.getUpdateFrequency())

    def test_getUpdateFrequencyWithContext(self):
        frequency = 'weekly'

        tool = self._makeOne()
        tool.enable()

        context = self._makeContext()
        info = self._makeInfo(context)
        tool.enableSyndication(context)
        info.frequency = frequency

        self.assertEqual(frequency, tool.getUpdateFrequency(context))


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(SyndicationToolTests),
        ))
