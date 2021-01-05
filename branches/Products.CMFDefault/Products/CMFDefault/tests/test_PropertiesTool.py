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
""" Unit tests for PropertiesTool module.
"""

import unittest
import Testing

from zope.component import getSiteManager
from zope.component import getUtility
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from OFS.PropertyManager import PropertyManager

from Products.MailHost.interfaces import IMailHost
from Products.MailHost.MailHost import MailHost

from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.testcase import SecurityTest


class PropertiedDummySite(PropertyManager, DummySite):

    _properties = (
        {'id': 'title', 'type': 'string', 'mode': 'w'},
        {'id': 'description', 'type': 'text', 'mode': 'w'},
        {'id': 'email_from_address', 'type': 'string', 'mode': 'w'},
        {'id': 'email_from_name', 'type': 'string', 'mode': 'w'},
        {'id': 'validate_email', 'type': 'boolean', 'mode': 'w'},
        {'id': 'default_charset', 'type': 'string', 'mode': 'w'},
        {'id': 'email_charset', 'type': 'string', 'mode': 'w'},
        {'id': 'enable_permalink', 'type': 'boolean', 'mode': 'w'},
        )
    title = description = email_from_address = email_from_name = ''
    default_charset = email_charset = ''
    validate_email = enable_permalink = False


class PropertiesToolTests(SecurityTest):

    def _makeOne(self, *args, **kw):
        from Products.CMFDefault.PropertiesTool import PropertiesTool

        return PropertiesTool(*args, **kw)

    def setUp(self):
        from Products.CMFCore.interfaces import IPropertiesTool

        SecurityTest.setUp(self)
        self.site = PropertiedDummySite('site')
        sm = getSiteManager()
        sm.registerUtility(MailHost('MailHost'), IMailHost)
        sm.registerUtility(self._makeOne(), IPropertiesTool)
        sm.registerUtility(self.site, ISiteRoot)

    def tearDown(self):
        cleanUp()
        SecurityTest.tearDown(self)

    def test_interfaces(self):
        from Products.CMFCore.interfaces import IPropertiesTool
        from Products.CMFDefault.PropertiesTool import PropertiesTool

        verifyClass(IPropertiesTool, PropertiesTool)

    def test_editProperties(self):
        from Products.CMFCore.interfaces import IPropertiesTool

        # https://bugs.launchpad.net/zope-cmf/+bug/174246
        # PropertiesTool.editProperties fails with traceback due to
        # faulty invocation of the site's manage_changeProperties method
        props = {'email_from_name': 'Test Admin',
                 'email_from_address': 'test@example.com',
                 'description': 'Test MailHost Description',
                 'title': 'Test MailHost',
                 'smtp_server': 'mail.example.com',
                 'validate_email': True,
                 'email_charset': 'iso-8859-15',
                 'default_charset': 'iso-8859-1',
                 'enable_permalink': True}
        tool = getUtility(IPropertiesTool)
        tool.editProperties(props)

        site_prop = self.site.getProperty
        self.assertEqual(getUtility(IMailHost).smtp_host, 'mail.example.com')
        self.assertEqual(site_prop('email_from_name'), 'Test Admin')
        self.assertEqual(site_prop('email_from_address'), 'test@example.com')
        self.assertEqual(site_prop('description'), 'Test MailHost Description')
        self.assertEqual(site_prop('title'), 'Test MailHost')
        self.assertEqual(site_prop('validate_email'), True)
        self.assertEqual(site_prop('email_charset'), 'iso-8859-15')
        self.assertEqual(site_prop('default_charset'), 'iso-8859-1')
        self.assertEqual(site_prop('enable_permalink'), True)

    def test_editProperties_single_value(self):
        from Products.CMFCore.interfaces import IPropertiesTool

        tool = getUtility(IPropertiesTool)
        site_prop = self.site.getProperty

        props = {'description': 'Test MailHost Description'}
        tool.editProperties(props)

        self.assertEqual(getUtility(IMailHost).smtp_host, 'localhost')
        self.assertEqual(site_prop('email_from_name'), '')
        self.assertEqual(site_prop('email_from_address'), '')
        self.assertEqual(site_prop('description'), 'Test MailHost Description')
        self.assertEqual(site_prop('title'), '')
        self.assertEqual(site_prop('validate_email'), False)
        self.assertEqual(site_prop('email_charset'), '')
        self.assertEqual(site_prop('default_charset'), '')
        self.assertEqual(site_prop('enable_permalink'), False)

        props = {'smtp_server': 'mail.example.com'}
        tool.editProperties(props)

        self.assertEqual(getUtility(IMailHost).smtp_host, 'mail.example.com')
        self.assertEqual(site_prop('email_from_name'), '')
        self.assertEqual(site_prop('email_from_address'), '')
        self.assertEqual(site_prop('description'), 'Test MailHost Description')
        self.assertEqual(site_prop('title'), '')
        self.assertEqual(site_prop('validate_email'), False)
        self.assertEqual(site_prop('email_charset'), '')
        self.assertEqual(site_prop('default_charset'), '')
        self.assertEqual(site_prop('enable_permalink'), False)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(PropertiesToolTests),
        ))
