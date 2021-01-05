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
""" Unit tests for DublinCore module.
"""

import unittest
import Testing

from AccessControl.SecurityManagement import newSecurityManager
from Acquisition import Implicit
from DateTime.DateTime import DateTime
from zope.component import getSiteManager
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import IMetadataTool
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyUserFolder
from Products.CMFCore.tests.base.testcase import SecurityTest
from Products.CMFDefault.MembershipTool import MembershipTool


def _DateIndexConvert(value):
    # Duplicate date conversion done by DateIndex._convert
    t_tup = value.toZone('UTC').parts()
    yr = t_tup[0]
    mo = t_tup[1]
    dy = t_tup[2]
    hr = t_tup[3]
    mn = t_tup[4]
    t_val = ((((yr * 12 + mo) * 31 + dy) * 24 + hr) * 60 + mn)

    if isinstance(t_val, long):
        # t_val must be IntType, not LongType
        raise OverflowError("Date too big: %s" % repr(value))

    return t_val


class DummyMetadataTool(Implicit):

    def __init__(self, publisher):
        self._publisher = publisher

    def getPublisher(self):
        return self._publisher


class DublinCoreTests(SecurityTest):

    def _makeDummyContent(self, id, *args, **kw):
        from Products.CMFCore.PortalContent import PortalContent
        from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl

        class DummyContent(PortalContent, DefaultDublinCoreImpl):
            pass

        return DummyContent(id, *args, **kw)

    def tearDown(self):
        cleanUp()
        SecurityTest.tearDown(self)

    def test_interfaces(self):
        from Products.CMFCore.interfaces import ICatalogableDublinCore
        from Products.CMFCore.interfaces import IDublinCore
        from Products.CMFCore.interfaces import IMutableDublinCore
        from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl

        verifyClass(ICatalogableDublinCore, DefaultDublinCoreImpl)
        verifyClass(IDublinCore, DefaultDublinCoreImpl)
        verifyClass(IMutableDublinCore, DefaultDublinCoreImpl)

    def test_notifyModified(self):
        site = DummySite('site').__of__(self.app)
        acl_users = site._setObject('acl_users', DummyUserFolder())
        site._setObject('portal_membership', MembershipTool())
        newSecurityManager(None, acl_users.user_foo)
        item = self._makeDummyContent('item').__of__(site)
        self.assertEqual(item.listCreators(), ())
        item.setModificationDate(0)
        initial_date = item.ModificationDate()

        item.notifyModified()
        self.assertEqual(item.listCreators(), ('user_foo',))
        self.assertNotEqual(item.ModificationDate(), initial_date)

    def test_creators_methods(self):
        site = DummySite('site').__of__(self.app)
        acl_users = site._setObject('acl_users', DummyUserFolder())
        site._setObject('portal_membership', MembershipTool())
        newSecurityManager(None, acl_users.user_foo)
        item = self._makeDummyContent('item').__of__(site)
        self.assertEqual(item.listCreators(), ())

        item.addCreator()
        self.assertEqual(item.listCreators(), ('user_foo',))
        newSecurityManager(None, acl_users.user_bar)
        item.addCreator()
        self.assertEqual(item.listCreators(), ('user_foo', 'user_bar'))
        item.addCreator()
        self.assertEqual(item.listCreators(), ('user_foo', 'user_bar'))
        item.addCreator('user_baz')
        self.assertEqual(item.listCreators(),
                         ('user_foo', 'user_bar', 'user_baz'))
        item.setCreators('user_bar')
        self.assertEqual(item.listCreators(), ('user_bar',))
        item.setCreators(('user_baz',))
        self.assertEqual(item.listCreators(), ('user_baz',))

    def test_creators_upgrade(self):
        site = DummySite('site').__of__(self.app)
        acl_users = site._setObject('acl_users', DummyUserFolder())
        site._setObject('portal_membership', MembershipTool())
        newSecurityManager(None, acl_users.user_foo)
        item = self._makeDummyContent('item').__of__(site)
        item.manage_fixupOwnershipAfterAdd()
        # fake an old object < CMF 1.5 without creators
        delattr(item, 'creators')
        self.assertEqual(item.Creator(), 'user_foo')
        newSecurityManager(None, acl_users.user_bar)
        item.addCreator()
        self.assertEqual(item.Creator(), 'user_foo')
        self.assertEqual(item.listCreators(), ('user_foo', 'user_bar'))
        # or if added directly
        delattr(item, 'creators')
        item.addCreator()
        self.assertEqual(item.Creator(), 'user_foo')
        self.assertEqual(item.listCreators(), ('user_foo', 'user_bar'))

    def test_ceiling_parsable(self):
        # Test that a None ceiling date will be parsable by a DateIndex
        site = DummySite('site').__of__(self.app)
        item = self._makeDummyContent('item').__of__(site)
        self.assertEqual(item.expiration_date, None)
        self.assertTrue(_DateIndexConvert(item.expires()))

    def test_publisher_no_metadata_tool(self):
        site = DummySite('site').__of__(self.app)
        item = self._makeDummyContent('item').__of__(site)
        self.assertEqual(item.Publisher(), 'No publisher')

    def test_publisher_with_metadata_tool(self):
        PUBLISHER = 'Some Publisher'
        site = DummySite('site').__of__(self.app)
        tool = DummyMetadataTool(publisher=PUBLISHER)
        getSiteManager().registerUtility(tool, IMetadataTool)
        item = self._makeDummyContent('item').__of__(site)
        self.assertEqual(item.Publisher(), PUBLISHER)

    def test_timezone_metadata(self):
        # http://www.zope.org/Collectors/CMF/325
        # If an item's timestamp(s) are stored in another timezone,
        # e.g. 4 hours further away from UTC, the DC date methods
        # should still return it in the local timezone so that all
        # user-visible dates can be compared to each other by eye.
        site = DummySite('site').__of__(self.app)
        item = self._makeDummyContent('item').__of__(site)
        dates_and_methods = (
            ('modification_date', 'ModificationDate'),
            ('effective_date', 'EffectiveDate'),
            ('effective_date', 'Date'),
            ('expiration_date', 'ExpirationDate'),
            ('creation_date', 'CreationDate'))
        offset = 4  # arbitrary, any value should work.
        for datename, dc_methodname in dates_and_methods:
            orig = getattr(item, datename)
            # Some default to None, fix that.
            if orig is None:
                orig = DateTime()
                setattr(item, datename, orig)
            orig_DC = getattr(item, dc_methodname)()
            # Change the timezone of the date.
            local_offset = orig.tzoffset() % (3600 * 24)
            other_offset = (local_offset + offset) % 24
            otherzone = 'GMT+%d' % other_offset
            setattr(item, datename, orig.toZone(otherzone))
            # Finally, verify that display has not changed.
            new_DC = getattr(item, dc_methodname)()
            self.assertEqual(orig_DC, new_DC)

    def test_Date_with_explicit_timezone(self):
        item = self._makeDummyContent('item')
        item.effective_date = DateTime('2007-01-01T12:00:00Z')
        self.assertEqual(item.Date('US/Eastern'),
                         '2007-01-01 07:00:00')

    def test_CreationDate_with_explicit_timezone(self):
        item = self._makeDummyContent('item')
        item.creation_date = DateTime('2007-01-01T12:00:00Z')
        self.assertEqual(item.CreationDate('US/Eastern'),
                         '2007-01-01 07:00:00')

    def test_ModificationDate_with_explicit_timezone(self):
        item = self._makeDummyContent('item')
        item.modification_date = DateTime('2007-01-01T12:00:00Z')
        self.assertEqual(item.ModificationDate('US/Eastern'),
                         '2007-01-01 07:00:00')

    def test_EffectiveDate_with_explicit_timezone(self):
        item = self._makeDummyContent('item')
        item.effective_date = DateTime('2007-01-01T12:00:00Z')
        self.assertEqual(item.EffectiveDate('US/Eastern'),
                         '2007-01-01 07:00:00')

    def test_ExpirationDate_with_explicit_timezone(self):
        item = self._makeDummyContent('item')
        item.expiration_date = DateTime('2007-01-01T12:00:00Z')
        self.assertEqual(item.ExpirationDate('US/Eastern'),
                         '2007-01-01 07:00:00')


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(DublinCoreTests),
        ))
