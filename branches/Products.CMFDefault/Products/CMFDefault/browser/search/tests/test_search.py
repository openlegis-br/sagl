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
"""Search form tests"""

import unittest

from datetime import date
from datetime import timedelta

from zope.component import getSiteManager
from zope.i18nmessageid import Message
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import ICatalogTool
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFDefault.browser.test_utils import DummyRequest


class DummyPropertiesTool(object):

    def getProperty(self, id, d=None):
        return 'iso-8859-1'


class StatusVocabularyTests(unittest.TestCase):

    def setUp(self):
        class DummyCatalogTool(object):
            def uniqueValuesFor(self, name):
                return ('foo', 'bar')

        sm = getSiteManager()
        sm.registerUtility(DummyCatalogTool(), ICatalogTool)
        sm.registerUtility(DummyPropertiesTool(), IPropertiesTool)

    def tearDown(self):
        cleanUp()

    def _makeOne(self):
        from Products.CMFDefault.browser.search.interfaces import status_vocab

        return status_vocab(None)

    def test_terms(self):
        vocab = self._makeOne()
        self.assertEqual(len(vocab), 3)
        terms = [ t for t in vocab ]

        self.assertEqual(terms[0].value, u'')
        self.assertEqual(terms[0].token, '')
        self.assertTrue(isinstance(terms[0].token, str))
        self.assertEqual(terms[0].title, u'-- any --')
        self.assertTrue(isinstance(terms[0].title, Message))

        self.assertEqual(terms[1].value, 'foo')
        self.assertEqual(terms[1].token, 'foo')
        self.assertTrue(isinstance(terms[1].token, str))
        self.assertEqual(terms[1].title, u'foo')
        self.assertTrue(isinstance(terms[1].title, Message))


class SubjectVocabularyTests(unittest.TestCase):

    def setUp(self):
        class DummyCatalogTool(object):
            def uniqueValuesFor(self, name):
                return ('foo', 'bar')

        sm = getSiteManager()
        sm.registerUtility(DummyCatalogTool(), ICatalogTool)
        sm.registerUtility(DummyPropertiesTool(), IPropertiesTool)

    def tearDown(self):
        cleanUp()

    def _makeOne(self):
        from Products.CMFDefault.browser.search.interfaces import subject_vocab

        return subject_vocab(None)

    def test_terms(self):
        vocab = self._makeOne()
        self.assertEqual(len(vocab), 3)
        terms = [ t for t in vocab ]

        self.assertEqual(terms[0].value, u'')
        self.assertEqual(terms[0].token, '')
        self.assertTrue(isinstance(terms[0].token, str))
        self.assertEqual(terms[0].title, u'-- any --')
        self.assertTrue(isinstance(terms[0].title, Message))

        self.assertEqual(terms[1].value, 'foo')
        self.assertEqual(terms[1].token, '666f6f')
        self.assertTrue(isinstance(terms[1].token, str))
        self.assertEqual(terms[1].title, u'foo')
        self.assertTrue(isinstance(terms[1].title, unicode))


class DateVocabularyTests(unittest.TestCase):

    def setUp(self):
        class DummyMembershipTool(object):
            def isAnonymousUser(self):
                return True

        sm = getSiteManager()
        sm.registerUtility(DummyMembershipTool(), IMembershipTool)

    def tearDown(self):
        cleanUp()

    def _makeOne(self):
        from Products.CMFDefault.browser.search.interfaces import date_vocab

        return date_vocab(None)

    def test_terms(self):
        vocab = self._makeOne()
        self.assertEqual(len(vocab), 4)
        terms = [ t for t in vocab ]

        self.assertEqual(terms[0].value, None)
        self.assertEqual(terms[0].token, 'ever')
        self.assertTrue(isinstance(terms[0].token, str))
        self.assertEqual(terms[0].title, u'Ever')
        self.assertTrue(isinstance(terms[0].title, Message))

        date_value = date.today() - timedelta(days=1)
        self.assertEqual(terms[1].value, date_value)
        self.assertEqual(terms[1].token, 'yesterday')
        self.assertTrue(isinstance(terms[1].token, str))
        self.assertEqual(terms[1].title, u'Yesterday')
        self.assertTrue(isinstance(terms[1].title, Message))

        date_value = date.today() - timedelta(days=7)
        self.assertEqual(terms[2].value, date_value)
        self.assertEqual(terms[2].token, 'last_week')
        self.assertTrue(isinstance(terms[2].token, str))
        self.assertEqual(terms[2].title, u'Last week')
        self.assertTrue(isinstance(terms[2].title, Message))

        date_value = date.today() - timedelta(days=31)
        self.assertEqual(terms[3].value, date_value)
        self.assertEqual(terms[3].token, 'last_month')
        self.assertTrue(isinstance(terms[3].token, str))
        self.assertEqual(terms[3].title, u'Last month')
        self.assertTrue(isinstance(terms[3].title, Message))


class TypeVocabularyTests(unittest.TestCase):

    def setUp(self):
        class DummyType(object):
            def __init__(self, id, title):
                self._id = id
                self._title = title
            def getId(self):
                return self._id
            def Title(self):
                return self._title

        class DummyTypesTool(object):
            def listTypeInfo(self):
                return (DummyType('foo', 'Foo'), DummyType('bar', 'Bar'))

        sm = getSiteManager()
        sm.registerUtility(DummyTypesTool(), ITypesTool)
        sm.registerUtility(DummyPropertiesTool(), IPropertiesTool)

    def tearDown(self):
        cleanUp()

    def _makeOne(self):
        from Products.CMFDefault.browser.search.interfaces import type_vocab

        return type_vocab(None)

    def test_terms(self):
        vocab = self._makeOne()
        self.assertEqual(len(vocab), 3)
        terms = [ t for t in vocab ]

        self.assertEqual(terms[0].value, u'')
        self.assertEqual(terms[0].token, '')
        self.assertTrue(isinstance(terms[0].token, str))
        self.assertEqual(terms[0].title, u'-- any --')
        self.assertTrue(isinstance(terms[0].title, Message))

        self.assertEqual(terms[1].value, 'foo')
        self.assertEqual(terms[1].token, 'foo')
        self.assertTrue(isinstance(terms[1].token, str))
        self.assertEqual(terms[1].title, u'Foo')
        self.assertTrue(isinstance(terms[1].title, unicode))


class SearchFormTests(unittest.TestCase):

    def setUp(self):
        class DummyActionsTool(object):
            def getActionInfo(self, action_chain, object=None,
                              check_visibility=False, check_condition=False):
                return {'url': 'foo'}

        sm = getSiteManager()
        sm.registerUtility(DummyActionsTool(), IActionsTool)

    def tearDown(self):
        cleanUp()

    def _getTargetClass(self):
        from Products.CMFDefault.browser.search.search import Search

        return Search

    def _makeOne(self):
        return self._getTargetClass()(DummySite(), DummyRequest())

    def test_is_not_reviewer(self):
        view = self._makeOne()
        view._checkPermission = lambda permission: False
        self.assertEqual(view.form_fields.get('review_state'), None)

    def test_is_reviewer(self):
        view = self._makeOne()
        view._checkPermission = lambda permission: True
        self.assertNotEqual(view.form_fields.get('review_state'), None)

    def test_strip_unused_paramaters(self):
        view = self._makeOne()
        view.request.form = {'portal_type': ['Document'],
                             'review_state': u'',
                             'Subject': u''}
        view.handle_search('search', {})
        self.assertEqual(view.request.response.location,
                         'foo?portal_type:list=Document')


class SearchViewTests(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.browser.search.search import SearchView

        return SearchView

    def _makeOne(self):
        return self._getTargetClass()(DummySite(), DummyRequest())

    def test_add_search_vars_to_hidden(self):
        view = self._makeOne()
        view.request.form = {'portal_type': ['Document']}
        self.assertEqual(view._getNavigationVars(), view.request.form)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(StatusVocabularyTests))
    suite.addTest(unittest.makeSuite(SubjectVocabularyTests))
    suite.addTest(unittest.makeSuite(DateVocabularyTests))
    suite.addTest(unittest.makeSuite(TypeVocabularyTests))
    suite.addTest(unittest.makeSuite(SearchFormTests))
    suite.addTest(unittest.makeSuite(SearchViewTests))
    return suite
