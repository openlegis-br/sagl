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
""" Unit tests for SkinnedFolder module.
"""

import unittest
import Testing

from zope.interface.verify import verifyClass

from Products.CMFCore.testing import ConformsToFolder


class SkinnedFolderTests(ConformsToFolder, unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.SkinnedFolder import SkinnedFolder

        return SkinnedFolder

    def test_interfaces(self):
        from OFS.interfaces import IOrderedContainer
        from Products.CMFCore.interfaces import IContentish

        verifyClass(IContentish, self._getTargetClass())
        verifyClass(IOrderedContainer, self._getTargetClass())


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(SkinnedFolderTests),
        ))
