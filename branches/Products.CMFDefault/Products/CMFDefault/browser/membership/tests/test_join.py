##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Test Products.CMFDefault.browser.join
"""

import unittest
from Testing import ZopeTestCase

from zope.component.testing import PlacelessSetup

from Products.CMFDefault.browser.skins.tests.test_ursa import (
                    DummyRequest, DummyContext,
                    DummyPropertiesTool, DummyURLTool, DummyActionsTool
                    )
from Products.CMFDefault.testing import FunctionalLayer


class JoinFormViewTests(unittest.TestCase, PlacelessSetup):

    def setUp(self):
        PlacelessSetup.setUp(self)

    def tearDown(self):
        PlacelessSetup.tearDown(self)

    def _getTargetClass(self):
        from Products.CMFDefault.browser.membership.join import JoinFormView

        return JoinFormView

    def _makeOne(self, site=None):
        if site is None:
            site = self._makeSite()
        request = DummyRequest()
        return self._getTargetClass()(site, request)

    def _makeSite(self,):
        from zope.component import getSiteManager
        from Products.CMFCore.interfaces import IPropertiesTool
        site = DummyContext()
        tool = site.portal_properties = DummyPropertiesTool()
        sm = getSiteManager()
        sm.registerUtility(tool, IPropertiesTool)
        site.portal_url = DummyURLTool(site)
        site.portal_membership = DummyMembershipTool()
        site.portal_registration = DummyRegistrationTool()
        site.portal_actions = DummyActionsTool()
        site.absolute_url = lambda: 'http://example.com'
        return site

    def test_validation_not_required(self):
        site = self._makeSite()
        site.portal_properties.validate_email = False
        view = self._makeOne(site)
        self.assertTrue(view.form_fields.get("password"))

    def test_validation_required(self):
        site = self._makeSite()
        site.portal_properties.validate_email = True
        view = self._makeOne(site)
        self.assertEqual(view.form_fields.get("password"), None)

    def test_logged_in_user(self):
        # logged in users cannot join
        # they get to see the preferences
        pass

    def test_successful_registration_validation_not_required(self):
        # can proceed straight to login
        pass

    def test_successful_registration_validation_required(self):
        # note that password will be sent by email
        pass


class DummyRegistrationTool:
    pass

class DummyMembershipTool:
    pass

class DummyActionsTool:
    pass


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(JoinFormViewTests))
    s = ZopeTestCase.FunctionalDocFileSuite('join.txt')
    s.layer = FunctionalLayer
    suite.addTest(s)
    return suite
