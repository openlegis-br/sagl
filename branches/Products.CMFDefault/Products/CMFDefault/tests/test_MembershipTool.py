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
""" Unit tests for MembershipTool module.
"""

import unittest
import Testing

from AccessControl.SecurityManagement import newSecurityManager
from five.localsitemanager import make_objectmanager_site
from zope.component import getSiteManager
from zope.component.hooks import clearSite
from zope.component.hooks import setSite
from zope.component.interfaces import IFactory
from zope.globalrequest import clearRequest
from zope.globalrequest import setRequest
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.interfaces import IWorkflowTool
from Products.CMFCore.PortalFolder import PortalFolder
from Products.CMFCore.testing import EventZCMLLayer
from Products.CMFCore.tests.base.dummy import DummyFolder
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyTool
from Products.CMFCore.tests.base.dummy import DummyType
from Products.CMFCore.tests.base.dummy import DummyUserFolder
from Products.CMFCore.tests.base.testcase import SecurityTest
from Products.CMFCore.tests.base.testcase import TransactionalTest


class DummyTool(DummyTool):

    def getTypeInfo(self, contentType):
        ti = DummyType('Home Folder')
        ti.factory = 'cmf.folder.home'
        return ti


class MembershipToolTests(TransactionalTest):

    def _makeOne(self, *args, **kw):
        from Products.CMFDefault.MembershipTool import MembershipTool

        return MembershipTool(*args, **kw)

    def setUp(self):
        from Products.CMFCore.interfaces import IMembershipTool

        TransactionalTest.setUp(self)
        self.site = DummySite('site').__of__(self.app)
        make_objectmanager_site(self.site)
        setSite(self.site)
        self.site._setObject('portal_membership', self._makeOne())
        sm = getSiteManager()
        sm.registerUtility(self.site.portal_membership, IMembershipTool)

    def tearDown(self):
        clearSite()
        cleanUp()
        TransactionalTest.tearDown(self)

    def test_interfaces(self):
        from Products.CMFDefault.interfaces import IMembershipTool
        from Products.CMFDefault.MembershipTool import MembershipTool

        verifyClass(IMembershipTool, MembershipTool)

    def test_MembersFolder_methods(self):
        from Products.CMFCore.interfaces import IMembershipTool

        mtool = getSiteManager().getUtility(IMembershipTool)
        self.assertEqual(mtool.getMembersFolder(), None)
        self.site._setObject('Members', DummyFolder())
        self.assertEqual(mtool.getMembersFolder(), self.site.Members)
        mtool.setMembersFolderById(id='foo')
        self.assertEqual(mtool.getMembersFolder(), None)
        self.site._setObject('foo', DummyFolder())
        self.assertEqual(mtool.getMembersFolder(), self.site.foo)
        mtool.setMembersFolderById(id='foo/members')
        self.assertEqual(mtool.getMembersFolder(), None)
        self.site.foo._setObject('members', DummyFolder())
        self.assertEqual(mtool.getMembersFolder(), self.site.foo.members)
        mtool.setMembersFolderById()
        # Note: self.site is returned due to DummyObject.restrictedTraverse
        self.assertEqual(mtool.getMembersFolder(), self.site)

    def test_HomeFolder_methods(self):
        from Products.CMFCore.interfaces import IMembershipTool

        mtool = getSiteManager().getUtility(IMembershipTool)
        setRequest(self.REQUEST)
        self.assertEqual(mtool.getHomeFolder(id='member_foo'), None)
        self.assertEqual(mtool.getHomeUrl(id='member_foo'), None)
        self.site._setObject('Members', PortalFolder('Members'))
        self.assertEqual(mtool.getHomeFolder(id='member_foo'), None)
        self.assertEqual(mtool.getHomeUrl(id='member_foo'), None)
        self.site.Members._setObject('member_foo', PortalFolder('member_foo'))
        self.assertEqual(mtool.getHomeFolder(id='member_foo'),
                         self.site.Members.member_foo)
        self.assertEqual(mtool.getHomeUrl(id='member_foo'),
                         'http://nohost/bar/site/Members/member_foo')
        clearRequest()


class MembershipToolSecurityTests(SecurityTest):

    layer = EventZCMLLayer

    def _makeOne(self, *args, **kw):
        from Products.CMFDefault.MembershipTool import MembershipTool

        return MembershipTool(*args, **kw)

    def setUp(self):
        SecurityTest.setUp(self)
        self.site = DummySite('site').__of__(self.app)
        self.site._setObject('portal_membership', self._makeOne())

    def test_createMemberArea(self):
        from Products.CMFDefault.interfaces import IMembershipTool
        from Products.CMFDefault.MembershipTool import HomeFolderFactory

        mtool = self.site.portal_membership
        members = self.site._setObject('Members', PortalFolder('Members'))
        acl_users = self.site._setObject('acl_users', DummyUserFolder())
        ttool = DummyTool()
        wtool = DummyTool()
        sm = getSiteManager()
        sm.registerUtility(mtool, IMembershipTool)
        sm.registerUtility(ttool, ITypesTool)
        sm.registerUtility(wtool, IWorkflowTool)
        sm.registerUtility(HomeFolderFactory, IFactory, 'cmf.folder.home')

        # permission
        mtool.createMemberArea('user_foo')
        self.assertFalse(hasattr(members.aq_self, 'user_foo'))
        newSecurityManager(None, acl_users.user_bar)
        mtool.createMemberArea('user_foo')
        self.assertFalse(hasattr(members.aq_self, 'user_foo'))
        newSecurityManager(None, acl_users.user_foo)
        mtool.setMemberareaCreationFlag()
        mtool.createMemberArea('user_foo')
        self.assertFalse(hasattr(members.aq_self, 'user_foo'))
        newSecurityManager(None, acl_users.all_powerful_Oz)
        mtool.setMemberareaCreationFlag()
        mtool.createMemberArea('user_foo')
        self.assertTrue(hasattr(members.aq_self, 'user_foo'))

        # default content
        f = members.user_foo
        ownership = acl_users.user_foo
        localroles = (('user_foo', ('Owner',)),)
        self.assertEqual(f.Title(), "user_foo's Home")
        self.assertEqual(f.getPortalTypeName(), 'Home Folder')
        self.assertEqual(f.getOwner(), ownership)
        self.assertEqual(f.get_local_roles(), localroles,
                         'CMF Collector issue #162 (LocalRoles broken): %s'
                         % str(f.get_local_roles()))
        self.assertEqual(f.index_html.getPortalTypeName(), 'Document')
        self.assertEqual(f.index_html.getOwner(), ownership,
                         'CMF Collector issue #162 (Ownership broken): %s'
                         % str(f.index_html.getOwner()))
        self.assertEqual(f.index_html.get_local_roles(), localroles,
                         'CMF Collector issue #162 (LocalRoles broken): %s'
                         % str(f.index_html.get_local_roles()))
        self.assertEqual(wtool.test_notified, f.index_html)

        # acquisition
        self.site.user_bar = 'test attribute'
        newSecurityManager(None, acl_users.user_bar)
        mtool.createMemberArea('user_bar')
        self.assertTrue(hasattr(members.aq_self, 'user_bar'),
                        'CMF Collector issue #102 (acquisition bug)')

    def test_createMemberArea_BBB(self):
        from Products.CMFDefault.interfaces import IMembershipTool
        from Products.CMFDefault.MembershipTool import BBBHomeFolderFactory

        mtool = self.site.portal_membership
        members = self.site._setObject('Members', PortalFolder('Members'))
        acl_users = self.site._setObject('acl_users', DummyUserFolder())
        wtool = DummyTool()
        sm = getSiteManager()
        sm.registerUtility(mtool, IMembershipTool)
        sm.registerUtility(wtool, IWorkflowTool)
        sm.registerUtility(BBBHomeFolderFactory, IFactory,
                           'cmf.folder.home.bbb2')

        # permission
        mtool.createMemberArea('user_foo')
        self.assertFalse(hasattr(members.aq_self, 'user_foo'))
        newSecurityManager(None, acl_users.user_bar)
        mtool.createMemberArea('user_foo')
        self.assertFalse(hasattr(members.aq_self, 'user_foo'))
        newSecurityManager(None, acl_users.user_foo)
        mtool.setMemberareaCreationFlag()
        mtool.createMemberArea('user_foo')
        self.assertFalse(hasattr(members.aq_self, 'user_foo'))
        newSecurityManager(None, acl_users.all_powerful_Oz)
        mtool.setMemberareaCreationFlag()
        mtool.createMemberArea('user_foo')
        self.assertTrue(hasattr(members.aq_self, 'user_foo'))

        # default content
        f = members.user_foo
        ownership = acl_users.user_foo
        localroles = (('user_foo', ('Owner',)),)
        self.assertEqual(f.Title(), "user_foo's Home")
        self.assertEqual(f.getPortalTypeName(), 'Folder')
        self.assertEqual(f.getOwner(), ownership)
        self.assertEqual(f.get_local_roles(), localroles,
                         'CMF Collector issue #162 (LocalRoles broken): %s'
                         % str(f.get_local_roles()))
        self.assertEqual(f.index_html.getPortalTypeName(), 'Document')
        self.assertEqual(f.index_html.getOwner(), ownership,
                         'CMF Collector issue #162 (Ownership broken): %s'
                         % str(f.index_html.getOwner()))
        self.assertEqual(f.index_html.get_local_roles(), localroles,
                         'CMF Collector issue #162 (LocalRoles broken): %s'
                         % str(f.index_html.get_local_roles()))
        self.assertEqual(wtool.test_notified, f.index_html)

        # acquisition
        self.site.user_bar = 'test attribute'
        newSecurityManager(None, acl_users.user_bar)
        mtool.createMemberArea('user_bar')
        self.assertTrue(hasattr(members.aq_self, 'user_bar'),
                        'CMF Collector issue #102 (acquisition bug)')


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(MembershipToolTests),
        unittest.makeSuite(MembershipToolSecurityTests),
        ))
