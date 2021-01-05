##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Syndication Upgrade tests.
"""

import unittest
from Testing import ZopeTestCase

from DateTime.DateTime import DateTime
from Products.CMFCore.interfaces import ISyndicationTool, IFolderish
from Products.CMFCore.PortalFolder import PortalFolder
from Products.CMFDefault.SyndicationInfo import ISyndicationInfo
from Products.CMFDefault.SyndicationInfo import SyndicationInfo
from Products.CMFDefault.SyndicationTool import SyndicationTool
from Products.CMFDefault.testing import FunctionalLayer
from zope.component import getAdapter
from zope.component import getSiteManager
from zope.component.hooks import setSite
from zope.testing.cleanup import cleanUp


class FunctionalUpgradeTestCase(ZopeTestCase.FunctionalTestCase):

    layer = FunctionalLayer
    _setup_fixture = 0

    def setUp(self):
        super(FunctionalUpgradeTestCase, self).setUp()
        sm = getSiteManager()
        sm.registerAdapter(SyndicationInfo, [IFolderish], ISyndicationInfo)
        syndication  = SyndicationTool()
        sm.registerUtility(syndication, ISyndicationTool)
        folder = PortalFolder("Dummy Portal Folder")
        self.folder = folder


    def _make_info(self):
        """Add an old style SyndicationInfo to the folder"""
        from Products.CMFDefault.SyndicationInfo import SyndicationInformation
        info = SyndicationInformation()
        info.syUpdateBase = DateTime()
        info.syUpdatePeriod = 1
        info.syUpdateFrequency = 1
        info.isAllowed = 1
        info.max_items = 5
        return info

    def test_upgrade(self):
        info = self._make_info()
        self.folder._setObject(info.getId(), info)
        old_info = self.folder._getOb(info.getId())
        self.assertTrue('syndication_information' in self.folder.objectIds())
        self.assertTrue(isinstance(old_info.syUpdateBase, DateTime))

        from Products.CMFDefault.upgrade.to23 import change_to_adapter
        change_to_adapter(old_info)
        self.assertFalse('syndication_information' in self.folder.objectIds())
        new_info = getAdapter(self.folder, ISyndicationInfo)
        self.assertEqual(new_info.max_items, old_info.max_items)
        self.assertEqual(new_info.period, old_info.syUpdatePeriod)
        self.assertEqual(new_info.frequency, old_info.syUpdateFrequency)
        self.assertFalse(old_info.syUpdateBase.timezoneNaive())
        self.assertTrue(new_info.base.tzinfo is None)

    def TearDown(self):
        cleanUp()


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(FunctionalUpgradeTestCase),
        ))
