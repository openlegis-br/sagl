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
""" Unit tests for Favorites.
"""

import unittest
import Testing

from zope.component import getSiteManager
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.interfaces import IURLTool
from Products.CMFCore.testing import ConformsToContent
from Products.CMFCore.tests.base.dummy import DummyContent
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyTool


class FavoriteTests(ConformsToContent, unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.Favorite import Favorite

        return Favorite

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def setUp(self):
        self.site = DummySite('site')
        sm = getSiteManager()
        sm.registerUtility(self.site, ISiteRoot)
        sm.registerUtility(DummyTool(), IMembershipTool)
        sm.registerUtility(DummyTool().__of__(self.site), IURLTool)
        self.site._setObject( 'target', DummyContent() )

    def tearDown(self):
        cleanUp()

    def test_interfaces(self):
        from Products.CMFDefault.interfaces import IFavorite
        from Products.CMFDefault.interfaces import ILink
        from Products.CMFDefault.interfaces import IMutableFavorite
        from Products.CMFDefault.interfaces import IMutableLink

        verifyClass(IFavorite, self._getTargetClass())
        verifyClass(ILink, self._getTargetClass())
        verifyClass(IMutableFavorite, self._getTargetClass())
        verifyClass(IMutableLink, self._getTargetClass())

    def test_Empty( self ):
        utool = getSiteManager().getUtility(IURLTool)
        f = self.site._setObject('foo', self._makeOne('foo'))

        self.assertEqual( f.getId(), 'foo' )
        self.assertEqual( f.Title(), '' )
        self.assertEqual( f.Description(), '' )
        self.assertEqual( f.getRemoteUrl(), utool() )
        self.assertEqual( f.getObject(), self.site )
        self.assertEqual( f.getIconURL(), self.site.getIconURL() )
        self.assertEqual( f.icon(), '' )

    def test_CtorArgs( self ):
        utool = getSiteManager().getUtility(IURLTool)
        target = self.site.target
        self.assertEqual( self._makeOne( 'foo'
                                       , title='Title'
                                       ).Title(), 'Title' )

        self.assertEqual( self._makeOne( 'bar'
                                       , description='Description'
                                       ).Description(), 'Description' )

        baz = self.site._setObject('foo',
                                self._makeOne('baz', remote_url='target'))
        self.assertEqual( baz.getObject(), target )
        self.assertEqual( baz.getRemoteUrl(), '%s/target' % utool() )
        self.assertEqual( baz.getIconURL(), target.getIconURL() )
        self.assertEqual( baz.icon(), target.icon() )

    def test_edit( self ):
        utool = getSiteManager().getUtility(IURLTool)
        target = self.site.target
        f = self.site._setObject('foo', self._makeOne('foo'))
        f.edit( 'target' )
        self.assertEqual( f.getObject(), target )
        self.assertEqual( f.getRemoteUrl(), '%s/target' % utool() )
        self.assertEqual( f.getIconURL(), target.getIconURL() )
        self.assertEqual( f.icon(), target.icon() )

    def test_editEmpty( self ):
        utool = getSiteManager().getUtility(IURLTool)
        f = self.site._setObject('gnnn', self._makeOne('gnnn'))
        f.edit( '' )
        self.assertEqual( f.getObject(), self.site )
        self.assertEqual( f.getRemoteUrl(), utool() )
        self.assertEqual( f.getIconURL(), self.site.getIconURL() )
        self.assertEqual( f.icon(), '' )


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(FavoriteTests),
        ))
