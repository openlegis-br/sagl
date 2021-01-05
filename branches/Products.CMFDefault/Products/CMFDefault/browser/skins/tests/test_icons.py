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
"""
"""

import unittest

from Acquisition import Implicit
from zope.component.testing import PlacelessSetup
from zope.globalrequest import clearRequest
from zope.globalrequest import setRequest

from .test_ursa import DummyActionsTool
from .test_ursa import DummyPropertiesTool
from .test_ursa import DummyResponse
from .test_ursa import DummyURLTool
from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import ITypesTool


class AbsolutIconsTests(unittest.TestCase, PlacelessSetup):

    def setUp(self):
        PlacelessSetup.setUp(self)

    def tearDown(self):
        clearRequest()
        PlacelessSetup.tearDown(self)

    def _getTargetClass(self):
        from Products.CMFDefault.browser.skins.icons import View
        return View

    def _makeOne(self, site=None):
        if site is None:
            site = self._makeSite()
        request = DummyRequest()
        setRequest(request)
        return self._getTargetClass()(site, request)

    def _makeSite(self, types=None, actions=None):
        from zope.component import getSiteManager
        from Products.CMFCore.interfaces import IPropertiesTool
        site = DummyContext()
        tool = site.portal_properties = DummyPropertiesTool()
        sm = getSiteManager()
        sm.registerUtility(tool, IPropertiesTool)
        if types is not None:
            site.portal_url = DummyURLTool(site)
            sm.registerUtility(DummyTypesTool(types), ITypesTool)
            sm.registerUtility(DummyMembershipTool(), IMembershipTool)
        if actions is not None:
            sm.registerUtility(DummyActionsTool(actions), IActionsTool)
        site.absolute_url = lambda: 'http://example.com'
        return site

    def test_show_icons_not_set(self):
        #Show action icons not set
        view = self._makeOne()
        self.assertFalse(view._show_icons)

    def test_show_icons_enabled(self):
        #Show actions set to True
        site = self._makeSite()
        site.portal_properties.enable_actionicons = True
        view = self._makeOne(site)
        self.assertTrue(view._show_icons)

    def test_show_icons_disabled(self):
        #Show action icons set to False
        site = self._makeSite()
        site.portal_properties.enable_actionicons = False
        view = self._makeOne(site)
        self.assertFalse(view._show_icons)

    def test_type_icons_with_action_icons_disabled(self):
        #Type actions should always be visible
        types = [DummyType("Document"), DummyType("Image")]
        site = self._makeSite(types=types)
        view = self._makeOne(site)
        self.assertFalse(view.show_icons)

        css = view.types()
        self.assertEqual(css, """\
.Document {background: url(http://example.com/Document.png) no-repeat 0.1em}

.Image {background: url(http://example.com/Image.png) no-repeat 0.1em}""")

    def test_type_icons_with_action_icons_enabled(self):
        #Type actions should always be visible"""
        types = [DummyType("Document"), DummyType("Image")]
        site = self._makeSite(types=types)
        site.portal_properties.enable_actionicons = True
        view = self._makeOne(site)
        self.assertTrue(view.show_icons)

        css = view.types()
        self.assertEqual(css, """\
.Document {background: url(http://example.com/Document.png) no-repeat 0.1em}

.Image {background: url(http://example.com/Image.png) no-repeat 0.1em}""")

    def test_action_icons_with_action_icons_disabled(self):
        #Action icons disabled. Image less styles should be returned.
        site = self._makeSite(actions=ACTIONS)
        view = self._makeOne(site)
        self.assertFalse(view.show_icons)

        css = view.actions()
        self.assertEqual(css, """/* user actions */

.Login {/* Login.png */}

.Logout {/* Logout.png */}

/* object actions */

.Edit {/* Edit.png */}

/* folder actions */

.folderContents {/* folderContents.png */}

/* workflow actions */

.Publish {/* Publish.png */}

/* global actions */

.Undo {/* Undo.png */}""")

    def test_action_icons_with_action_icons_enabled(self):
        #Action icons enabled. Styles with images should be returned.
        site = self._makeSite(actions=ACTIONS)
        site.portal_properties.enable_actionicons = True
        view = self._makeOne(site)
        self.assertTrue(view.show_icons)

        css = view.actions()
        self.assertEqual(css, """/* user actions */

.Login {background: url(Login.png) no-repeat 0.1em}

.Logout {background: url(Logout.png) no-repeat 0.1em}

/* object actions */

.Edit {background: url(Edit.png) no-repeat 0.1em}

/* folder actions */

.folderContents {background: url(folderContents.png) no-repeat 0.1em}

/* workflow actions */

.Publish {background: url(Publish.png) no-repeat 0.1em}

/* global actions */

.Undo {background: url(Undo.png) no-repeat 0.1em}""")


class DummyContext(Implicit):

    pass


class DummyRequest(object):

    def __init__(self):
        self.response = DummyResponse()

    def get(self, key, default=None):
        return {}


class DummyType:

    def __init__(self, id):
        from Products.CMFCore.Expression import Expression
        self.id = id
        self.icon_expr_object = Expression('string:${portal_url}/%s.png' % id)

    def getIconExprObject(self):
        return getattr(self, 'icon_expr_object', None)


class DummyTypesTool:

    def __init__(self, types=None):
        if types is None:
            self.typeInfos = []
        else:
            self.typeInfos = types[:]

    def listTypeInfo(self):
        return self.typeInfos


def DummyAction(name):
    return {'id': name, 'icon': '%s.png' % name}


ACTIONS = {'global': [DummyAction('Undo')],
           'user': [DummyAction('Login'), DummyAction('Logout')],
           'object': [DummyAction('Edit')],
           'folder': [DummyAction('folderContents')],
           'workflow': [DummyAction('Publish')],
          }


class DummyMembershipTool:

    def isAnonymousUser(self):
        return True
