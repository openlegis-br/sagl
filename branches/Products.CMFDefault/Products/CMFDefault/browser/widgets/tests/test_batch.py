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

from zope.publisher.browser import TestRequest


class BatchFormMixinTests(unittest.TestCase):

    def _makeOne(self, batch_size=30):
        from Products.CMFDefault.browser.widgets.batch import BatchFormMixin
        batch = BatchFormMixin(None,
                              TestRequest(ACTUAL_URL='http://example.com'))
        batch.prefix = 'form'
        batch._getNavigationVars = lambda: {}
        batch._get_items = lambda: range(batch_size)
        return batch

    def test_page_count(self):
        batch = self._makeOne()
        self.assertEqual(batch.page_count(), 2)
        batch = self._makeOne(25)
        self.assertEqual(batch.page_count(), 1)
        batch = self._makeOne()
        batch._BATCH_SIZE = 2
        self.assertEqual(batch.page_count(), 15)

    def test_page_number(self):
        batch = self._makeOne()
        self.assertEqual(batch.page_number(), 1)
        batch = self._makeOne(1000)
        batch._getBatchStart = lambda: 250
        self.assertEqual(batch.page_number(), 11)

    def test_summary_length(self):
        batch = self._makeOne()
        self.assertEqual(batch.summary_length(), '30')
        batch = self._makeOne(10000)
        self.assertEqual(batch.summary_length(), '10,000')
        batch = self._makeOne(0)
        self.assertEqual(batch.summary_length(), '')

    def test_summary_type(self):
        batch = self._makeOne()
        self.assertEqual(batch.summary_type(), 'items')
        batch = self._makeOne()
        batch._get_items = lambda: range(1)
        self.assertEqual(batch.summary_type(), 'item')

    def test_navigation_previous(self):
        batch = self._makeOne()
        self.assertEqual(batch.navigation_previous(), None)
        batch = self._makeOne(1000)
        batch._getBatchStart = lambda: 250
        self.assertEqual(batch.navigation_previous(),
                         {'url': u'http://example.com?form.b_start=225',
                          'title': u'Previous ${count} items'}
                         )

    def test_navigation_next(self):
        batch = self._makeOne()
        self.assertEqual(batch.navigation_next(),
                         {'url': u'http://example.com?form.b_start=25',
                          'title': u'Next ${count} items'}
                         )
        batch = self._makeOne(1000)
        batch._getBatchStart = lambda: 250
        self.assertEqual(batch.navigation_next(),
                         {'url': u'http://example.com?form.b_start=275',
                          'title': u'Next ${count} items'}
                         )

    def test_page_range(self):
        batch = self._makeOne()
        self.assertEqual(
            batch.page_range(),
            [{'url': u'http://example.com', 'number': 1},
             {'url': u'http://example.com?form.b_start=25', 'number': 2}])
        batch = self._makeOne(1000)
        self.assertEqual(
            batch.page_range(),
            [{'url': u'http://example.com', 'number': 1},
             {'url': u'http://example.com?form.b_start=25', 'number': 2},
             {'url': u'http://example.com?form.b_start=50', 'number': 3},
             {'url': u'http://example.com?form.b_start=75', 'number': 4},
             {'url': u'http://example.com?form.b_start=100', 'number': 5},
             {'url': u'http://example.com?form.b_start=125', 'number': 6},
             {'url': u'http://example.com?form.b_start=150', 'number': 7},
             {'url': u'http://example.com?form.b_start=175', 'number': 8},
             {'url': u'http://example.com?form.b_start=200', 'number': 9},
             {'url': u'http://example.com?form.b_start=225', 'number': 10}])
        batch = self._makeOne(1000)
        batch._getBatchStart = lambda: 250
        self.assertEqual(
            batch.page_range(),
            [{'url': u'http://example.com?form.b_start=150', 'number': 7},
             {'url': u'http://example.com?form.b_start=175', 'number': 8},
             {'url': u'http://example.com?form.b_start=200', 'number': 9},
             {'url': u'http://example.com?form.b_start=225', 'number': 10},
             {'url': u'http://example.com?form.b_start=250', 'number': 11},
             {'url': u'http://example.com?form.b_start=275', 'number': 12},
             {'url': u'http://example.com?form.b_start=300', 'number': 13},
             {'url': u'http://example.com?form.b_start=325', 'number': 14},
             {'url': u'http://example.com?form.b_start=350', 'number': 15},
             {'url': u'http://example.com?form.b_start=375', 'number': 16}])


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BatchFormMixinTests))
    return suite
