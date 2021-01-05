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
""" Unit tests for File module.
"""

import unittest
import Testing

from mimetypes import guess_type
from os.path import join as path_join

from App.Common import rfc1123_date
from zope.component import getSiteManager
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import ICachingPolicyManager
from Products.CMFCore.testing import ConformsToContent
from Products.CMFCore.tests.base.dummy import DummyCachingManager
from Products.CMFCore.tests.base.dummy import DummyCachingManagerWithPolicy
from Products.CMFCore.tests.base.dummy import FAKE_ETAG
from Products.CMFCore.tests.base.testcase import TransactionalTest
from Products.CMFDefault import tests

TESTS_HOME = tests.__path__[0]
TEST_JPG = path_join(TESTS_HOME, 'TestImage.jpg')
TEST_SWF = path_join(TESTS_HOME, 'TestFile.swf')


class FileTests(ConformsToContent, unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.File import File

        return File

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_interfaces(self):
        from Products.CMFDefault.interfaces import IFile
        from Products.CMFDefault.interfaces import IMutableFile

        verifyClass(IFile, self._getTargetClass())
        verifyClass(IMutableFile, self._getTargetClass())

    def test_getId_on_old_File_instance(self):
        file = self._makeOne('testfile')
        self.assertEqual(file.getId(), 'testfile')
        # Mimick old instance when base classes had OFS.Image.File first
        file.__name__ = 'testfile'
        delattr(file, 'id')
        self.assertEqual(file.getId(), 'testfile')

    def test_File_setFormat(self):
        # Setting the DC.format must also set the content_type property
        file = self._makeOne('testfile', format='image/jpeg')
        self.assertEqual(file.Format(), 'image/jpeg')
        self.assertEqual(file.content_type, 'image/jpeg')
        file.setFormat('image/gif')
        self.assertEqual(file.Format(), 'image/gif')
        self.assertEqual(file.content_type, 'image/gif')

    def test_FileContentTypeUponConstruction(self):
        # Test the content type after calling the constructor with the
        # file object being passed in (http://www.zope.org/Collectors/CMF/370)
        EXPECTED = guess_type('foo.jpg')[0]
        testfile = open(TEST_JPG, 'rb')
        # Notice the cheat? File objects lack the extra intelligence that
        # picks content types from the actual file data, so it needs to be
        # helped along with a file extension...
        file = self._makeOne('testfile.jpg', file=testfile)
        testfile.close()
        self.assertEqual(file.Format(), EXPECTED)
        self.assertEqual(file.content_type, EXPECTED)


class CachingTests(TransactionalTest):

    def _getTargetClass(self):
        from Products.CMFDefault.File import File

        return File

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _extractFile(self):
        f = open(TEST_SWF, 'rb')
        try:
            data = f.read()
        finally:
            f.close()

        return TEST_SWF, data

    def tearDown(self):
        cleanUp()
        TransactionalTest.tearDown(self)

    def test_index_html_with_304_from_cpm(self):
        cpm = DummyCachingManagerWithPolicy()
        getSiteManager().registerUtility(cpm, ICachingPolicyManager)
        _path, ref = self._extractFile()
        file = self._makeOne('test_file', 'test_file.swf', file=ref)
        file = file.__of__(self.app)

        mod_time = file.modified().timeTime()

        self.REQUEST.environ['IF_MODIFIED_SINCE'
                            ] = '%s;' % rfc1123_date(mod_time)
        self.REQUEST.environ['IF_NONE_MATCH'
                            ] = '%s;' % FAKE_ETAG

        data = file.index_html(self.REQUEST, self.RESPONSE)
        self.assertEqual(len(data), 0)
        self.assertEqual(self.RESPONSE.getStatus(), 304)

    def test_index_html_200_with_cpm(self):
        # should behave the same as without cpm installed
        cpm = DummyCachingManagerWithPolicy()
        getSiteManager().registerUtility(cpm, ICachingPolicyManager)
        _path, ref = self._extractFile()
        file = self._makeOne('test_file', 'test_file.swf', file=ref)
        file = file.__of__(self.app)

        mod_time = file.modified().timeTime()

        data = file.index_html(self.REQUEST, self.RESPONSE)

        self.assertEqual(len(data), len(ref))
        self.assertEqual(data, ref)
        # ICK!  'HTTPResponse.getHeader' doesn't case-flatten the key!
        self.assertEqual(self.RESPONSE.getHeader('Content-Length'.lower()),
                         str(len(ref)))
        self.assertEqual(self.RESPONSE.getHeader('Content-Type'.lower()),
                         'application/octet-stream')
        self.assertEqual(self.RESPONSE.getHeader('Last-Modified'.lower()),
                         rfc1123_date(mod_time))

    def test_caching(self):
        large_data = '0' * 100000

        def fake_response_write(data):
            return

        response_write = self.RESPONSE.write
        self.RESPONSE.write = fake_response_write
        cpm = DummyCachingManager()
        getSiteManager().registerUtility(cpm, ICachingPolicyManager)
        original_len = len(self.RESPONSE.headers)
        obj = self._makeOne('test_file', 'test_file.swf', file=large_data)
        obj = obj.__of__(self.app)
        obj.index_html(self.REQUEST, self.RESPONSE)
        headers = self.RESPONSE.headers
        self.assertTrue(len(headers) >= original_len + 3)
        self.assertTrue('foo' in headers.keys())
        self.assertTrue('bar' in headers.keys())
        self.assertEqual(headers['test_path'], '/test_file')
        self.RESPONSE.write = response_write

    def test_caching_policy_headers_are_canonical(self):
        """Ensure that headers set by the caching policy manager trump
        any of the same name that from time to time may be set while
        rendering the object."""
        _path, ref = self._extractFile()

        cpm = LMDummyCachingManager()
        getSiteManager().registerUtility(cpm, ICachingPolicyManager)

        self.app.foo = self._makeOne('test_file', 'test_file.swf', file=ref)

        # index_html in OFS will set Last-Modified to ._p_mtime or current time
        self.app.foo.index_html(self.REQUEST, self.RESPONSE)

        headers = self.RESPONSE.headers
        self.assertEqual(headers['last-modified'],
                         "Sun, 06 Nov 1994 08:49:37 GMT")


# We set up a new type of dummy caching manager that sets a bogus
# last modified date.  This should be visible in the request
class LMDummyCachingManager(DummyCachingManager):

    def getHTTPCachingHeaders(self, content, view_name,
                               keywords, time=None):
        return ('Last-modified', 'Sun, 06 Nov 1994 08:49:37 GMT'),


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(FileTests),
        unittest.makeSuite(CachingTests),
        ))
