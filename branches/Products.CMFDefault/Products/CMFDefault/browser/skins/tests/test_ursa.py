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
""" Test Products.CMFDefault.browser.ursa
"""

import unittest

from zope.component import getSiteManager
from zope.component.testing import PlacelessSetup
from zope.i18n.interfaces import IUserPreferredCharsets
from zope.interface import alsoProvides

from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import ISyndicationTool
from Products.CMFCore.interfaces import IURLTool
from Products.CMFCore.interfaces import IWorkflowTool
from Products.CMFDefault.utils import PRODUCTS_CMFCALENDAR_INSTALLED
from Products.CMFDefault.utils import PRODUCTS_CMFUID_INSTALLED

if PRODUCTS_CMFCALENDAR_INSTALLED:
    from Products.CMFCalendar.interfaces import ICalendarTool

if PRODUCTS_CMFUID_INSTALLED:
    from Products.CMFUid.interfaces import IUniqueIdHandler


class UrsineGlobalsTests(unittest.TestCase, PlacelessSetup):

    def setUp(self):
        PlacelessSetup.setUp(self)

    def tearDown(self):
        PlacelessSetup.tearDown(self)

    def _getTargetClass(self):
        from Products.CMFDefault.browser.skins.ursa import UrsineGlobals
        return UrsineGlobals

    def _makeOne(self, context=None, request=None):
        if context is None:
            context = self._makeContext()
        if request is None:
            request = DummyRequest()
        return self._getTargetClass()(context, request)

    def _makeContext(self):
        context = DummyContext()
        sm = getSiteManager()
        tool = context.portal_properties = DummyPropertiesTool()
        sm.registerUtility(tool, IPropertiesTool)
        tool = context.portal_membership = DummyMembershipTool()
        sm.registerUtility(tool, IMembershipTool)
        return context

    def test_ctor_wo_def_charset_doesnt_set_content_type(self):
        context = self._makeContext()
        request = DummyRequest()
        response = request.response
        self._makeOne(context, request)
        self.assertEqual(len(response._set_headers), 0)

    def test_ctor_w_resp_charset_doesnt_set_content_type(self):
        context = self._makeContext()
        request = DummyRequest()
        response = request.response
        response._orig_headers['content-type'] = 'text/html; charset=UTF-8'
        self._makeOne(context, request)
        self.assertEqual(len(response._set_headers), 0)

    def test_ctor_w_resp_charset_w_def_charset_doesnt_override_charset(self):
        context = self._makeContext()
        context.portal_properties.default_charset = 'latin1'
        request = DummyRequest()
        response = request.response
        response._orig_headers['content-type'] = 'text/html; charset=UTF-8'
        self._makeOne(context, request)
        self.assertEqual(len(response._set_headers), 0)

    def test_ctor_wo_resp_charst_w_def_charset_sets_charset(self):
        context = self._makeContext()
        context.portal_properties.default_charset = 'latin1'
        request = DummyRequest()
        response = request.response
        response._orig_headers['content-type'] = 'text/html'
        self._makeOne(context, request)
        self.assertEqual(len(response._set_headers), 1)
        self.assertEqual(response._set_headers[0],
                         ('content-type', 'text/html; charset=latin1'))

    def test_ptool(self):
        view = self._makeOne()
        tool = view.context.portal_properties
        self.assertTrue(view.ptool is tool)

    def test_utool(self):
        view = self._makeOne()
        tool = DummyURLTool()
        getSiteManager().registerUtility(tool, IURLTool)
        self.assertTrue(view.utool is tool)

    def test_mtool(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        self.assertTrue(view.mtool is tool)

    def test_atool(self):
        view = self._makeOne()
        tool = DummyActionsTool()
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertTrue(view.atool is tool)

    def test_wtool(self):
        view = self._makeOne()
        tool = DummyWorkflowTool()
        getSiteManager().registerUtility(tool, IWorkflowTool)
        self.assertTrue(view.wtool is tool)

    def test_syndtool(self):
        view = self._makeOne()
        tool = DummyTool()
        getSiteManager().registerUtility(tool, ISyndicationTool)
        self.assertTrue(view.syndtool is tool)

    def test_uidtool(self):
        view = self._makeOne()
        if PRODUCTS_CMFUID_INSTALLED:
            tool = DummyTool()
            getSiteManager().registerUtility(tool, IUniqueIdHandler)
            self.assertTrue(view.uidtool is tool)

    def test_uidtool_not_installed(self):
        view = self._makeOne()
        self.assertFalse(view.uidtool_installed)

    def test_uidtool_installed(self):
        view = self._makeOne()
        if PRODUCTS_CMFUID_INSTALLED:
            getSiteManager().registerUtility(DummyTool(), IUniqueIdHandler)
            self.assertTrue(view.uidtool_installed)

    def test_caltool(self):
        view = self._makeOne()
        if PRODUCTS_CMFCALENDAR_INSTALLED:
            tool = DummyTool()
            getSiteManager().registerUtility(tool, ICalendarTool)
            self.assertTrue(view.caltool is tool)

    def test_caltool_not_installed(self):
        view = self._makeOne()
        self.assertFalse(view.caltool_installed)

    def test_caltool_installed(self):
        view = self._makeOne()
        if PRODUCTS_CMFCALENDAR_INSTALLED:
            getSiteManager().registerUtility(DummyTool(), ICalendarTool)
            self.assertTrue(view.caltool_installed)

    def test_portal_object(self):
        view = self._makeOne()
        portal = DummyContext()
        tool = DummyURLTool()
        tool.getPortalObject = lambda: portal
        getSiteManager().registerUtility(tool, IURLTool)
        self.assertTrue(view.portal_object is portal)

    def test_portal_url(self):
        view = self._makeOne()
        tool = DummyURLTool()
        tool.__call__ = lambda: 'http://example.com/'
        getSiteManager().registerUtility(tool, IURLTool)
        self.assertEqual(view.portal_url, 'http://example.com/')

    def test_portal_title(self):
        view = self._makeOne()
        portal = DummyContext()
        portal.Title = lambda: 'TITLE'
        tool = DummyURLTool()
        tool.getPortalObject = lambda: portal
        getSiteManager().registerUtility(tool, IURLTool)
        self.assertEqual(view.portal_title, 'TITLE')

    def test_portal_title_nonascii(self):
        NONASCII = u'B\xe4r'
        context = self._makeContext()
        view = self._makeOne(context)
        context.Title = lambda: NONASCII.encode('latin-1')
        context.portal_properties.default_charset = 'latin1'
        tool = DummyURLTool()
        tool.getPortalObject = lambda: context
        getSiteManager().registerUtility(tool, IURLTool)
        self.assertEqual(view.portal_title, NONASCII)

    def test_object_title(self):
        view = self._makeOne()
        view.context.Title = lambda: 'TITLE'
        self.assertEqual(view.object_title, 'TITLE')

    def test_object_title_nonascii(self):
        NONASCII = u'B\xe4r'
        context = self._makeContext()
        view = self._makeOne(context)
        view.context.Title = lambda: NONASCII.encode('latin-1')
        context.portal_properties.default_charset = 'latin1'
        self.assertEqual(view.object_title, NONASCII)

    def test_object_description(self):
        view = self._makeOne()
        view.context.Description = lambda: 'DESCRIPTION'
        self.assertEqual(view.object_description, 'DESCRIPTION')

    def test_object_description_nonascii(self):
        NONASCII = u'B\xe4r'
        context = self._makeContext()
        view = self._makeOne(context)
        view.context.Description = lambda: NONASCII.encode('latin-1')
        context.portal_properties.default_charset = 'latin1'
        self.assertEqual(view.object_description, NONASCII)

    def test_trunc_id(self):
        view = self._makeOne()
        view.context.getId = lambda: 'ID'
        self.assertEqual(view.trunc_id, 'ID')

    def test_trunc_id_w_long_id(self):
        view = self._makeOne()
        view.context.getId = lambda: 'X' * 20
        self.assertEqual(view.trunc_id, 'X' * 15 + '...')

    def test_icon_w_getIconURL_w_icon(self):
        view = self._makeOne()
        view.context.getIconURL = lambda: 'ICON'
        view.context.icon = 'ICON2'
        self.assertEqual(view.icon, 'ICON')

    def test_icon_wo_getIconURL_w_icon(self):
        view = self._makeOne()
        view.context.icon = 'ICON'
        self.assertEqual(view.icon, 'ICON')

    def test_icon_wo_getIconURL_wo_icon(self):
        view = self._makeOne()
        self.assertEqual(view.icon, '')

    def test_typename(self):
        view = self._makeOne()
        view.context.getPortalTypeName = lambda: 'TYPENAME'
        self.assertEqual(view.typename, 'TYPENAME')

    def test_wf_state(self):
        view = self._makeOne()
        tool = DummyWorkflowTool()
        getSiteManager().registerUtility(tool, IWorkflowTool)
        self.assertEqual(view.wf_state, 'DUMMY')

    def test_page_title_wo_match(self):
        view = self._makeOne()
        view.context.Title = lambda: 'CONTEXT'
        portal = DummyContext()
        portal.Title = lambda: 'SITE'
        tool = DummyURLTool()
        tool.getPortalObject = lambda: portal
        getSiteManager().registerUtility(tool, IURLTool)
        self.assertEqual(view.page_title, 'SITE: CONTEXT')

    def test_page_title_w_match(self):
        view = self._makeOne()
        view.context.Title = lambda: 'MATCH'
        portal = DummyContext()
        portal.Title = lambda: 'MATCH'
        tool = DummyURLTool()
        tool.getPortalObject = lambda: portal
        getSiteManager().registerUtility(tool, IURLTool)
        self.assertEqual(view.page_title, 'MATCH')

    def test_breadcrumbs_at_root(self):
        PATHS_TO_CONTEXTS = []
        site = DummySite(PATHS_TO_CONTEXTS)
        sm = getSiteManager()
        ptool = site.portal_properties = DummyPropertiesTool()
        sm.registerUtility(ptool, IPropertiesTool)
        ptool.title = lambda: 'SITE'
        utool = site.portal_url = DummyURLTool(site, PATHS_TO_CONTEXTS)
        utool.__call__ = lambda: 'http://example.com/'
        sm.registerUtility(utool, IURLTool)
        view = self._makeOne(context=site)
        crumbs = view.breadcrumbs
        self.assertEqual(len(crumbs), 1)
        self.assertEqual(crumbs[0]['id'], 'root')
        self.assertEqual(crumbs[0]['title'], 'SITE')
        self.assertEqual(crumbs[0]['url'], 'http://example.com/')

    def test_breadcrumbs_not_root(self):
        context = DummyContext()
        context.Title = lambda: 'CONTEXT'
        context.absolute_url = lambda: 'http://example.com/parent/child'
        parent = DummyContext()
        parent.Title = lambda: 'PARENT'
        parent.absolute_url = lambda: 'http://example.com/parent'
        PATHS_TO_CONTEXTS = [(('parent',), parent),
                             (('parent', 'child'), context),
                            ]
        site = DummySite(PATHS_TO_CONTEXTS)
        sm = getSiteManager()
        ptool = context.portal_properties = DummyPropertiesTool()
        sm.registerUtility(ptool, IPropertiesTool)
        ptool.title = lambda: 'SITE'
        utool = context.portal_url = DummyURLTool(site, PATHS_TO_CONTEXTS)
        utool.__call__ = lambda: 'http://example.com/'
        sm.registerUtility(utool, IURLTool)

        view = self._makeOne(context=context)

        crumbs = view.breadcrumbs

        self.assertEqual(len(crumbs), 3)
        self.assertEqual(crumbs[0]['id'], 'root')
        self.assertEqual(crumbs[0]['title'], 'SITE')
        self.assertEqual(crumbs[0]['url'], 'http://example.com/')
        self.assertEqual(crumbs[1]['id'], 'parent')
        self.assertEqual(crumbs[1]['title'], 'PARENT')
        self.assertEqual(crumbs[1]['url'], 'http://example.com/parent')
        self.assertEqual(crumbs[2]['id'], 'child')
        self.assertEqual(crumbs[2]['title'], 'CONTEXT')
        self.assertEqual(crumbs[2]['url'], 'http://example.com/parent/child')

    def test_member(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        member = DummyUser()
        tool.getAuthenticatedMember = lambda: member
        self.assertTrue(view.member is member)

    def test_membersfolder(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        membersfolder = object()
        tool.getMembersFolder = lambda: membersfolder
        self.assertTrue(view.membersfolder is membersfolder)

    def test_isAnon_tool_returns_True(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        tool.isAnonymousUser = lambda: True
        self.assertTrue(view.isAnon)

    def test_isAnon_tool_returns_False(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        tool.isAnonymousUser = lambda: False
        self.assertFalse(view.isAnon)

    def test_membername_anonymous(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        tool.isAnonymousUser = lambda: True
        self.assertEqual(view.membername, u'Guest')

    def test_membername_not_anonymous(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        tool.isAnonymousUser = lambda: False
        member = DummyUser()
        member.getProperty = lambda x: 'John Smith'
        tool.getAuthenticatedMember = lambda: member
        self.assertEqual(view.membername, u'John Smith')

    def test_membername_not_anonymous_wo_fullname(self):
        view = self._makeOne()
        tool = view.context.portal_membership
        tool.isAnonymousUser = lambda: False
        member = DummyUser()
        member.getId = lambda: 'luser'
        member.getProperty = lambda x: ''
        tool.getAuthenticatedMember = lambda: member
        self.assertEqual(view.membername, u'luser')

    def test_status_message_missing(self):
        view = self._makeOne()
        view.request.form = {}
        self.assertEqual(view.status_message, None)

    def test_status_message(self):
        view = self._makeOne()
        view.request.form = {'portal_status_message': 'FOO'}
        view.request.getPreferredCharsets = lambda: []
        alsoProvides(view.request, IUserPreferredCharsets)
        self.assertEqual(view.status_message, 'FOO')

    def test_status_message_nonascii(self):
        NONASCII = u'B\xe4r'
        view = self._makeOne()
        view.request.form = {'portal_status_message': NONASCII.encode('utf-8')}
        view.request.getPreferredCharsets = lambda: ['utf-8']
        alsoProvides(view.request, IUserPreferredCharsets)
        self.assertEqual(view.status_message, NONASCII)

    def test_actions(self):
        ACTIONS = {'global': [],
                   'user': [],
                   'object': [],
                   'folder': [],
                   'workflow': [],
                  }
        view = self._makeOne()
        tool = DummyActionsTool(ACTIONS)
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.actions, ACTIONS)

    def test_global_actions(self):
        ACTIONS = {'global': [DummyAction('a'), DummyAction('b')],
                   'user': [],
                   'object': [],
                   'folder': [],
                   'workflow': [],
                  }
        view = self._makeOne()
        tool = DummyActionsTool(ACTIONS)
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.global_actions, ACTIONS['global'])

    def test_user_actions(self):
        ACTIONS = {'global': [],
                   'user': [DummyAction('a'), DummyAction('b')],
                   'object': [],
                   'folder': [],
                   'workflow': [],
                  }
        view = self._makeOne()
        tool = DummyActionsTool(ACTIONS)
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.user_actions, ACTIONS['user'])

    def test_object_actions(self):
        ACTIONS = {'global': [],
                   'user': [],
                   'object': [DummyAction('a'), DummyAction('b')],
                   'folder': [],
                   'workflow': [],
                  }
        view = self._makeOne()
        tool = DummyActionsTool(ACTIONS)
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.object_actions, ACTIONS['object'])

    def test_folder_actions(self):
        ACTIONS = {'global': [],
                   'user': [],
                   'object': [],
                   'folder': [DummyAction('a'), DummyAction('b')],
                   'workflow': [],
                  }
        view = self._makeOne()
        tool = DummyActionsTool(ACTIONS)
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.folder_actions, ACTIONS['folder'])

    def test_workflow_actions(self):
        ACTIONS = {'global': [],
                   'user': [],
                   'object': [],
                   'folder': [],
                   'workflow': [DummyAction('a'), DummyAction('b')],
                  }
        view = self._makeOne()
        tool = DummyActionsTool(ACTIONS)
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.workflow_actions, ACTIONS['workflow'])

    def test_search_form_url(self):
        view = self._makeOne()
        tool = DummyActionsTool()
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.search_form_url, u'site/search_form')

    def test_search_url(self):
        view = self._makeOne()
        tool = DummyActionsTool()
        getSiteManager().registerUtility(tool, IActionsTool)
        self.assertEqual(view.search_url, u'site/search')


class DummyContext:

    pass


class DummyAction:

    def __init__(self, id):
        self.id = id


class DummySite:

    def __init__(self, paths_to_contexts=()):
        self.paths_to_contexts = paths_to_contexts[:]

    def unrestrictedTraverse(self, path):
        for known, context in self.paths_to_contexts:
            if path == known:
                return context
        raise ValueError('Unknown path: %s' % path)


class DummyPropertiesTool:

    def getProperty(self, id, d=None):
        return getattr(self, id, d)


class DummyURLTool:

    def __init__(self, site=None, paths_to_contexts=()):
        self.site = site
        self.paths_to_contexts = paths_to_contexts[:]

    def getPortalObject(self):
        return self.site

    def getRelativeContentPath(self, context):
        if context is self.site:
            return ()
        for path, known in self.paths_to_contexts:
            if context is known:
                return path
        raise ValueError('Unknown context: %s' % context)


class DummyMembershipTool:

    pass


class DummyActionsTool(object):

    def __init__(self, actions=None):
        if actions is None:
            actions = {}
        self.actions = actions.copy()

    def listFilteredActionsFor(self, context):
        return self.actions

    def getActionInfo(self, action_chain):
        return {'url': u'site/{1}'.format(*action_chain.split('/'))}


class DummyWorkflowTool:

    review_state = 'DUMMY'

    def getInfoFor(self, context, key, default):
        if key == 'review_state':
            return self.review_state


class DummyTool(object):

    pass


class DummyUser:

    pass


class DummyResponse:

    def __init__(self, **kw):
        self._orig_headers = kw.copy()
        self._set_headers = []

    def getHeader(self, key):
        return self._orig_headers.get(key, '')

    def setHeader(self, key, value):
        self._set_headers.append((key, value))


class DummyRequest(object):

    def __init__(self):
        self.response = DummyResponse()


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(UrsineGlobalsTests),
    ))
