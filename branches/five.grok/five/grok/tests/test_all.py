##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import unittest
import doctest

from Testing.ZopeTestCase import FunctionalDocTestSuite
from five.grok.testing import FunctionalLayer


options = doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE


def test_suite():
    suite = unittest.TestSuite()

    for name in ['adapters', 'annotation', 'multiadapter', 'utilities',
                 'subscribers']:
        test = FunctionalDocTestSuite(
            module='five.grok.tests.%s' % name,
            optionflags=options)
        test.layer = FunctionalLayer
        suite.addTest(test)
    return suite
