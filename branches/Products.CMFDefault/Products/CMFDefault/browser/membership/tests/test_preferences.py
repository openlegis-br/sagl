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
""" Test Products.CMFDefault.browser.preferences
"""

import unittest
from Testing import ZopeTestCase

from Products.CMFDefault.testing import FunctionalLayer


def test_suite():
    suite = unittest.TestSuite()
    s = ZopeTestCase.FunctionalDocFileSuite('preferences.txt')
    s.layer = FunctionalLayer
    suite.addTest(s)
    return suite
