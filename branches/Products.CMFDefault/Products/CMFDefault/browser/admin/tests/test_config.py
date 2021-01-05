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
"""Tests for portal configuration form"""

import unittest

from Testing import ZopeTestCase

from Products.CMFDefault.testing import FunctionalLayer

ftest_suite = ZopeTestCase.FunctionalDocFileSuite('portal_config.txt',
                        )

ftest_suite.layer = FunctionalLayer

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestSuite((ftest_suite,)))
    return suite