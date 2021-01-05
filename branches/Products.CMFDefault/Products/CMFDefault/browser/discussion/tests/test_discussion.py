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
""" Test Products.CMFDefault.browser.rss
"""

import unittest
from Testing import ZopeTestCase

from Products.CMFDefault.testing import FunctionalLayer


ftest_suite = ZopeTestCase.FunctionalDocFileSuite('discussion.txt')
ftest_suite.layer = FunctionalLayer

def test_suite():
    return unittest.TestSuite((
        ftest_suite,
    ))
