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
""" Unit tests for adding members.
"""

import unittest
from Testing import ZopeTestCase

from zope.component.hooks import setSite

from Products.CMFDefault.testing import FunctionalLayer


class MembershipTests(ZopeTestCase.FunctionalTestCase):

    layer = FunctionalLayer

    def afterSetUp(self):
        setSite(self.app.site)

    def test_join(self):
        site = self.app.site
        member_id = 'test_user'

        site.portal_registration.addMember(member_id, 'zzyyzz',
                                           properties={'username': member_id,
                                                       'email': 'foo@bar.com'})
        u = site.acl_users.getUser(member_id)
        self.assertTrue(u)

    def test_join_memberproperties(self):
        # Make sure the member data wrapper carries correct properties
        # after joining
        site = self.app.site
        member_id = 'test_user'

        site.portal_registration.addMember(member_id, 'zzyyzz',
                                           properties={'username': member_id,
                                                       'email': 'foo@bar.com'})

        m = site.portal_membership.getMemberById('test_user')
        self.assertEqual(m.getProperty('email'), 'foo@bar.com')
        self.assertEqual(m.getMemberId(), member_id)
        self.assertEqual(m.getRoles(), ('Member', 'Authenticated'))

    def test_join_without_email(self):
        site = self.app.site

        self.assertRaises(ValueError,
                          site.portal_registration.addMember,
                          'test_user',
                          'zzyyzz',
                          properties={'username': 'test_user', 'email': ''}
                          )

    def test_join_with_variable_id_policies(self):
        site = self.app.site
        member_id = 'test.user'

        # Test with the default policy: Names with "." should fail
        self.assertRaises(ValueError,
                          site.portal_registration.addMember,
                          member_id,
                          'zzyyzz',
                          properties={'username': 'Test User',
                                      'email': 'foo@bar.com'}
                          )

        # Now change the policy to allow "."
        new_pattern = "^[A-Za-z][A-Za-z0-9_\.]*$"
        site.portal_registration.manage_editIDPattern(new_pattern)
        site.portal_registration.addMember(member_id, 'zzyyzz',
                                           properties={'username': 'TestUser2',
                                                       'email': 'foo@bar.com'})
        u = site.acl_users.getUser(member_id)
        self.assertTrue(u)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(MembershipTests),
        ))
