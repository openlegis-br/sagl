##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Unit tests for NewsItem module.
"""

import unittest
import Testing

from zope.interface.verify import verifyClass

from Products.CMFCore.testing import ConformsToContent
from Products.CMFCore.tests.base.content import BASIC_HTML
from Products.CMFCore.tests.base.content import BASIC_STRUCTUREDTEXT
from Products.CMFCore.tests.base.content import DOCTYPE
from Products.CMFCore.tests.base.content import ENTITY_IN_TITLE
from Products.CMFCore.tests.base.testcase import TransactionalTest


class NewsItemTests(ConformsToContent, unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.NewsItem import NewsItem

        return NewsItem

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_interfaces(self):
        from Products.CMFDefault.interfaces import IDocument
        from Products.CMFDefault.interfaces import IMutableNewsItem
        from Products.CMFDefault.interfaces import INewsItem

        verifyClass(IDocument, self._getTargetClass())
        # XXX: different signature
        # verifyClass(IMutableDocument, self._getTargetClass())
        verifyClass(IMutableNewsItem, self._getTargetClass())
        verifyClass(INewsItem, self._getTargetClass())

    def test_Empty_html(self):
        d = self._makeOne('empty', text_format='html')

        self.assertEqual(d.Title(), '')
        self.assertEqual(d.Description(), '')
        self.assertEqual(d.Format(), 'text/html')
        self.assertEqual(d.text_format, 'html')
        self.assertEqual(d.text, '')

    def test_Empty_stx(self):
        d = self._makeOne('foo', text_format='structured-text')

        self.assertEqual(d.Title(), '')
        self.assertEqual(d.Description(), '')
        self.assertEqual(d.Format(), 'text/plain')
        self.assertEqual(d.text_format, 'structured-text')
        self.assertEqual(d.text, '')

    def test_Init_with_stx(self):
        d = self._makeOne('foo', text_format='structured-text',
                          title='Foodoc')

        self.assertEqual(d.Title(), 'Foodoc')
        self.assertEqual(d.Description(), '')
        self.assertEqual(d.Format(), 'text/plain')
        self.assertEqual(d.text_format, 'structured-text')
        self.assertEqual(d.text, '')

    def test_default_format(self):
        d = self._makeOne('foo', text='')

        self.assertEqual(d.Format(), 'text/plain')
        self.assertEqual(d.text_format, 'structured-text')


class NewsItemPUTTests(TransactionalTest):

    def _getTargetClass(self):
        from Products.CMFDefault.NewsItem import NewsItem

        return NewsItem

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_Init(self):
        self.REQUEST['BODY'] = BASIC_STRUCTUREDTEXT
        d = self._makeOne('foo', text='')
        d.PUT(self.REQUEST, self.RESPONSE)

        self.assertEqual(d.Title(), 'My Document')
        self.assertEqual(d.Description(), 'A document by me')
        self.assertEqual(d.Format(), 'text/plain')
        self.assertEqual(d.text_format, 'structured-text')
        self.assertEqual(len(d.Contributors()), 3)
        self.assertTrue(d.cooked_text.find('<p>') >= 0)

    def test_PUT_basic_html(self):
        self.REQUEST['BODY'] = BASIC_HTML
        d = self._makeOne('foo')
        d.PUT(self.REQUEST, self.RESPONSE)

        self.assertEqual(d.Title(), 'Title in tag')
        self.assertEqual(d.Description(), 'Describe me')
        self.assertEqual(d.Format(), 'text/html')
        self.assertEqual(d.text_format, 'html')
        self.assertEqual(d.text.find('</body>'), -1)
        self.assertEqual(len(d.Contributors()), 3)

    def test_PUT_uppered_html(self):
        self.REQUEST['BODY'] = BASIC_HTML.upper()
        d = self._makeOne('foo')
        d.PUT(self.REQUEST, self.RESPONSE)

        self.assertEqual(d.Title(), 'TITLE IN TAG')
        self.assertEqual(d.Description(), 'DESCRIBE ME')
        self.assertEqual(d.Format(), 'text/html')
        self.assertEqual(d.text_format, 'html')
        self.assertEqual(d.text.find('</BODY'), -1)
        self.assertEqual(len(d.Contributors()), 3)

    def test_PUT_entity_in_title(self):
        self.REQUEST['BODY'] = ENTITY_IN_TITLE
        d = self._makeOne('foo')
        d.PUT(self.REQUEST, self.RESPONSE)

        self.assertEqual(d.Title(), '&Auuml;rger')

    def test_PUT_html_with_doctype(self):
        self.REQUEST['BODY'] = '%s\n%s' % (DOCTYPE, BASIC_HTML)
        d = self._makeOne('foo')
        d.PUT(self.REQUEST, self.RESPONSE)

        self.assertEqual(d.Description(), 'Describe me')

    def test_PUT_html_without_newlines(self):
        self.REQUEST['BODY'] = ''.join(BASIC_HTML.split('\n'))
        d = self._makeOne('foo')
        d.PUT(self.REQUEST, self.RESPONSE)

        self.assertEqual(d.Title(), 'Title in tag')
        self.assertEqual(d.Description(), 'Describe me')
        self.assertEqual(d.Format(), 'text/html')
        self.assertEqual(d.text_format, 'html')
        self.assertEqual(d.text.find('</body>'), -1)
        self.assertEqual(len(d.Contributors()), 3)

    def test_PUT_structured_text(self):
        self.REQUEST['BODY'] = BASIC_STRUCTUREDTEXT
        d = self._makeOne('foo')
        d.PUT(self.REQUEST, self.RESPONSE)

        self.assertEqual(d.Title(), 'My Document')
        self.assertEqual(d.Description(), 'A document by me')
        self.assertEqual(d.Format(), 'text/plain')
        self.assertEqual(d.text_format, 'structured-text')
        self.assertEqual(len(d.Contributors()), 3)
        self.assertTrue(d.cooked_text.find('<p>') >= 0)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(NewsItemTests),
        unittest.makeSuite(NewsItemPUTTests),
        ))
