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
""" Unit tests for DiscussionTool module.
"""

import unittest
import Testing

from AccessControl.SecurityManagement import newSecurityManager
from zope.component import getSiteManager
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.tests.base.dummy import DummyFolder
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyTool
from Products.CMFCore.tests.base.dummy import DummyUserFolder
from Products.CMFCore.tests.base.testcase import SecurityTest


class DiscussionToolTests(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.DiscussionTool import DiscussionTool

        return DiscussionTool

    def test_interfaces(self):
        from Products.CMFCore.interfaces import IDiscussionTool

        verifyClass(IDiscussionTool, self._getTargetClass())


class DiscussionToolSecurityTests(SecurityTest):

    def _getTargetClass(self):
        from Products.CMFDefault.DiscussionTool import DiscussionTool

        return DiscussionTool

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def setUp(self):
        from Products.CMFCore.interfaces import IDiscussionTool

        SecurityTest.setUp(self)
        self.site = DummySite('site')
        self.dtool = self._makeOne()
        self.ttool = DummyTool()
        sm = getSiteManager()
        sm.registerUtility(self.dtool, IDiscussionTool)
        sm.registerUtility(self.ttool, ITypesTool)

    def tearDown(self):
        cleanUp()
        SecurityTest.tearDown(self)

    def test_overrideDiscussionFor(self):
        acl_users = self.site._setObject('acl_users', DummyUserFolder())
        newSecurityManager(None, acl_users.all_powerful_Oz)
        dtool = self.dtool
        foo = self.site._setObject('foo', DummyFolder())
        baz = foo._setObject('baz', DummyFolder())

        dtool.overrideDiscussionFor(foo, 1)
        self.assertTrue(hasattr(foo.aq_base, 'allow_discussion'))
        try:
            dtool.overrideDiscussionFor(baz, None)
        except KeyError:
            self.fail('CMF Collector issue #201 (acquisition bug): '
                      'KeyError raised')
        dtool.overrideDiscussionFor(foo, None)
        self.assertFalse(hasattr(foo.aq_base, 'allow_discussion'))

        # https://bugs.launchpad.net/zope-cmf/+bug/162532: Don't break
        # if allow_discussion only exists at the class level
        class DummyContent:
            allow_discussion = False

            def getId(self):
                return 'dummy'

        dummy = DummyContent()
        try:
            dtool.overrideDiscussionFor(dummy, None)
        except AttributeError:
            self.fail('Launchpad issue 162532: AttributeError raised')

    def test_overrideDiscussionFor_w_string_numerics(self):
        acl_users = self.site._setObject('acl_users', DummyUserFolder())
        newSecurityManager(None, acl_users.all_powerful_Oz)
        dtool = self.dtool
        foo = self.site._setObject( 'foo', DummyFolder() )

        dtool.overrideDiscussionFor(foo, '0')
        self.assertEqual(foo.aq_base.allow_discussion, False)

        dtool.overrideDiscussionFor(foo, '1')
        self.assertEqual(foo.aq_base.allow_discussion, True)

    def test_isDiscussionAllowedFor(self):
        # Test for Collector issue #398 (allow_discussion wrongly
        # acquired and used from parent)
        acl_users = self.site._setObject('acl_users', DummyUserFolder())
        newSecurityManager(None, acl_users.all_powerful_Oz)
        dtool = self.dtool
        foo = self.site._setObject('foo', DummyFolder())
        baz = foo._setObject('baz', DummyFolder())
        dtool.overrideDiscussionFor(foo, 1)

        self.assertFalse(dtool.isDiscussionAllowedFor(baz))

        # Make sure isDiscussionAllowedFor does not blow up on items
        # that aren't content and/or discussable at all.
        self.assertFalse(dtool.isDiscussionAllowedFor(self.ttool))

    def test_getDiscussionFor(self):
        dtool = self.dtool
        foo = self.site._setObject('foo', DummyFolder())
        foo.allow_discussion = 1
        baz = foo._setObject('baz', DummyFolder())
        baz.allow_discussion = 1

        self.assertFalse(hasattr(foo.aq_base, 'talkback'))
        dtool.getDiscussionFor(foo)
        self.assertTrue(hasattr(foo.aq_base, 'talkback'))
        self.assertFalse(hasattr(baz.aq_base, 'talkback'))
        dtool.getDiscussionFor(baz)
        self.assertTrue(hasattr(baz.aq_base, 'talkback'),
                        'CMF Collector issue #119 (acquisition bug): '
                        'talkback not created')


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(DiscussionToolTests),
        unittest.makeSuite(DiscussionToolSecurityTests),
        ))
