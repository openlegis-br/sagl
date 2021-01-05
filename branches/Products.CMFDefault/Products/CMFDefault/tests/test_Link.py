##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Unit tests for Link module.
"""

import unittest
import Testing

from re import compile

from zope.interface.verify import verifyClass

from Products.CMFCore.testing import ConformsToContent
from Products.CMFCore.tests.base.content import BASIC_RFC822
from Products.CMFCore.tests.base.content import RFC822_W_CONTINUATION


class LinkTests(ConformsToContent, unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.Link import Link

        return Link

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def canonTest(self, table):
        for orig, wanted in table.items():
            # test with constructor
            d = self._makeOne('foo', remote_url=orig)
            self.assertEqual(d.getRemoteUrl(), wanted)
            # test with edit method too
            d = self._makeOne('bar')
            d.edit(orig)
            self.assertEqual(d.getRemoteUrl(), wanted)

    def test_interfaces(self):
        from Products.CMFDefault.interfaces import ILink
        from Products.CMFDefault.interfaces import IMutableLink

        verifyClass(ILink, self._getTargetClass())
        verifyClass(IMutableLink, self._getTargetClass())

    def test_Empty(self):
        d = self._makeOne('foo')
        self.assertEqual(d.Title(), '')
        self.assertEqual(d.Description(), '')
        self.assertEqual(d.getRemoteUrl(), '')
        self.assertEqual(d.format, 'text/url')
        self.assertEqual(d.URL_FORMAT, 'text/url')

        d = self._makeOne('foo', remote_url='bar')
        d.edit('')
        self.assertEqual(d.getRemoteUrl(), '')

        d = self._makeOne('foo', remote_url='http://')
        self.assertEqual(d.getRemoteUrl(), '')

        d = self._makeOne('foo', remote_url='http:')
        self.assertEqual(d.getRemoteUrl(), '')

    def test_fixupMissingScheme(self):
        table = {
            'http://foo.com':      'http://foo.com',
            '//bar.com':           'http://bar.com',
            }
        self.canonTest(table)

    def test_keepRelativeUrl(self):
        table = {
            'baz.com':             'baz.com',
            'baz2.com/index.html': 'baz2.com/index.html',
            '/huh/zoinx.html':     '/huh/zoinx.html',
            'hmmm.com/lol.txt':    'hmmm.com/lol.txt',
            }
        self.canonTest(table)

    def test_trailingSlash(self):
        table = {
            'http://foo.com/bar/': 'http://foo.com/bar/',
            'baz.com/':            'baz.com/',
            '/baz.org/zoinx/':     '/baz.org/zoinx/',
            }
        self.canonTest(table)

    def test_otherScheme(self):
        table = {
            'mailto:user@foo.com':      'mailto:user@foo.com',
            'https://bank.com/account': 'https://bank.com/account',
            }
        self.canonTest(table)


class LinkGETTests(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.Link import Link

        return Link

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_manage_FTPget_empty(self):
        LINES = ['Title: ', 'Subject: ', 'Publisher: No publisher',
                 'Description: ', 'Contributors: ', 'Effective_date: None',
                 'Expiration_date: None', 'Type: Unknown',
                 'Format: text/url', 'Language: ', 'Rights: ', '']
        d = self._makeOne('foo')
        self.assertEqual(d.manage_FTPget().splitlines(), LINES)

    def test_manage_FTPget_nonascii(self):
        NONASCII = u'B\xe4r'.encode('utf-8')
        LINES = ['Title: %s' % NONASCII, 'Subject: ',
                 'Publisher: No publisher', 'Description: ', 'Contributors: ',
                 'Effective_date: None', 'Expiration_date: None',
                 'Type: Unknown', 'Format: text/url', 'Language: ', 'Rights: ',
                 '']
        d = self._makeOne('foo')
        d.setTitle(NONASCII)
        self.assertEqual(d.manage_FTPget().splitlines(), LINES)


class LinkPUTTests(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.Link import Link

        return Link

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_RFC822(self):
        d = self._makeOne('foo')
        d._writeFromPUT(body=BASIC_RFC822)

        self.assertEqual(d.Title(), 'Zope Community')
        self.assertEqual(d.Description()
                        , 'Link to the Zope Community website.')
        self.assertEqual(len(d.Subject()), 3)
        self.assertEqual(d.getRemoteUrl(), 'http://www.zope.org')

    def test_RFC822_w_Continuation(self):
        d = self._makeOne('foo')
        d._writeFromPUT(body=RFC822_W_CONTINUATION)
        rnlinesplit = compile(r'\r?\n?')
        desc_lines = rnlinesplit.split(d.Description())

        self.assertEqual(d.Title(), 'Zope Community')
        self.assertEqual(desc_lines[0]
                        , 'Link to the Zope Community website,')
        self.assertEqual(desc_lines[1]
                        , ' including hundreds of contributed Zope products.')
        self.assertEqual(len(d.Subject()), 3)
        self.assertEqual(d.getRemoteUrl(), 'http://www.zope.org')

    def test_PutWithoutMetadata(self):
        d = self._makeOne('foo')
        d._writeFromPUT(body='')
        self.assertEqual(d.Title(), '')
        self.assertEqual(d.Format(), 'text/url')
        self.assertEqual(d.Description(), '')
        self.assertEqual(d.Subject(), ())
        self.assertEqual(d.Contributors(), ())
        self.assertEqual(d.EffectiveDate(), 'None')
        self.assertEqual(d.ExpirationDate(), 'None')
        self.assertEqual(d.Language(), '')
        self.assertEqual(d.Rights(), '')


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(LinkTests),
        unittest.makeSuite(LinkGETTests),
        unittest.makeSuite(LinkPUTTests),
        ))
