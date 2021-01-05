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
""" Unit tests for Discussions.
"""

import unittest
import Testing

from AccessControl.SecurityManagement import newSecurityManager
from zope.component import getSiteManager
from zope.interface.verify import verifyClass

from Products.CMFCore.CatalogTool import CatalogTool
from Products.CMFCore.interfaces import ICatalogTool
from Products.CMFCore.interfaces import IDiscussionTool
from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.testing import EventZCMLLayer
from Products.CMFCore.tests.base.dummy import DummyContent
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyUser
from Products.CMFCore.tests.base.testcase import SecurityTest
from Products.CMFCore.tests.base.tidata import FTIDATA_DUMMY
from Products.CMFCore.TypesTool import FactoryTypeInformation as FTI
from Products.CMFCore.TypesTool import TypesTool
from Products.CMFDefault.DiscussionTool import DiscussionTool
from Products.CMFDefault.exceptions import DiscussionNotAllowed

def has_path(catalog, path):
    if isinstance(path, tuple):
        path = '/'.join(path)
    return bool(catalog.getrid(path))


class DiscussionItemTests(unittest.TestCase):

    def test_interfaces(self):
        from Products.CMFCore.interfaces import ICatalogableDublinCore
        from Products.CMFCore.interfaces import IContentish
        from Products.CMFCore.interfaces import IDiscussionResponse
        from Products.CMFCore.interfaces import IDublinCore
        from Products.CMFCore.interfaces import IDynamicType
        from Products.CMFCore.interfaces import IMutableDublinCore
        from Products.CMFDefault.DiscussionItem import DiscussionItem

        verifyClass(ICatalogableDublinCore, DiscussionItem)
        verifyClass(IContentish, DiscussionItem)
        verifyClass(IDiscussionResponse, DiscussionItem)
        verifyClass(IDublinCore, DiscussionItem)
        verifyClass(IDynamicType, DiscussionItem)
        verifyClass(IMutableDublinCore, DiscussionItem)


class DiscussionItemContainerTests(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.DiscussionItem import DiscussionItemContainer

        return DiscussionItemContainer

    def test_interfaces(self):
        from Products.CMFCore.interfaces import ICallableOpaqueItemEvents
        from Products.CMFCore.interfaces import IDiscussable

        verifyClass(ICallableOpaqueItemEvents, self._getTargetClass())
        verifyClass(IDiscussable, self._getTargetClass())


class DiscussionTests(SecurityTest):

    layer = EventZCMLLayer

    def setUp(self):
        SecurityTest.setUp(self)
        newSecurityManager(None, DummyUser().__of__(self.app.acl_users))
        self.site = DummySite('site').__of__(self.app)
        self.dtool = DiscussionTool()
        self.ttool = TypesTool()
        sm = getSiteManager()
        sm.registerUtility(self.dtool, IDiscussionTool)
        sm.registerUtility(self.ttool, ITypesTool)

    def _makeDummyContent(self, id, *args, **kw):
        return self.site._setObject(id, DummyContent(id, *args, **kw))

    def test_policy(self):
        dtool = self.dtool
        ttool = self.ttool
        test = self._makeDummyContent('test')
        self.assertRaises(DiscussionNotAllowed, dtool.getDiscussionFor, test)
        self.assertTrue(getattr(test, 'talkback', None) is None)

        test.allow_discussion = 1
        self.assertTrue(dtool.getDiscussionFor(test))
        self.assertTrue(test.talkback)

        del test.talkback
        del test.allow_discussion
        fti = FTIDATA_DUMMY[0].copy()
        ttool._setObject('Dummy Content', FTI(**fti))
        self.assertRaises(DiscussionNotAllowed, dtool.getDiscussionFor, test)
        self.assertTrue(getattr(test, 'talkback', None) is None)

        ti = getattr(ttool, 'Dummy Content')
        ti.allow_discussion = 1
        self.assertTrue(dtool.getDiscussionFor(test))
        self.assertTrue(test.talkback)

        del test.talkback
        ti.allow_discussion = 0
        self.assertRaises(DiscussionNotAllowed, dtool.getDiscussionFor, test)
        self.assertTrue(getattr(test, 'talkback', None) is None)

        test.allow_discussion = 1
        self.assertTrue(dtool.getDiscussionFor(test))
        self.assertTrue(test.talkback)

    def test_nestedReplies(self):
        dtool = self.dtool
        test = self._makeDummyContent('test')
        test.allow_discussion = 1
        talkback = dtool.getDiscussionFor(test)
        self.assertEqual(talkback._getDiscussable(), test)
        self.assertEqual(talkback._getDiscussable(outer=1), test)
        self.assertFalse(talkback.hasReplies(test))
        self.assertEqual(len(talkback.getReplies()), 0)

        reply_id = talkback.createReply(title='test', text='blah')
        self.assertTrue(talkback.hasReplies(test))
        self.assertEqual(len(talkback.getReplies()), 1)
        self.assertTrue(talkback.getReply(reply_id))

        reply1 = talkback.getReplies()[0]
        items = talkback._container.items()
        self.assertEqual(reply1.getId(), items[0][0])
        self.assertEqual(reply1.inReplyTo(), test)
        self.assertEqual(reply1.listCreators(), ('dummy',))

        parents = reply1.parentsInThread()
        self.assertEqual(len(parents), 1)
        self.assertTrue(test in parents)

        talkback1 = dtool.getDiscussionFor(reply1)
        self.assertEqual(talkback, talkback1)
        self.assertEqual(len(talkback1.getReplies()), 0)
        self.assertEqual(len(talkback.getReplies()), 1)

        talkback1.createReply(title='test2', text='blah2')
        self.assertEqual(len(talkback._container), 2)
        self.assertTrue(talkback1.hasReplies(reply1))
        self.assertEqual(len(talkback1.getReplies()), 1)
        self.assertEqual(len(talkback.getReplies()), 1)

        reply2 = talkback1.getReplies()[0]
        self.assertEqual(reply2.inReplyTo(), reply1)

        parents = reply2.parentsInThread()
        self.assertEqual(len(parents), 2)
        self.assertEqual(parents[0], test)
        self.assertEqual(parents[1], reply1)

        parents = reply2.parentsInThread(1)
        self.assertEqual(len(parents), 1)
        self.assertEqual(parents[0], reply1)

    def test_itemCataloguing(self):
        ctool = CatalogTool()
        ctool.addColumn('in_reply_to')
        getSiteManager().registerUtility(ctool, ICatalogTool)
        dtool = self.dtool
        test = self._makeDummyContent('test', catalog=1)
        test.allow_discussion = 1

        self.assertEqual(len(ctool), 1)
        self.assertTrue(has_path(ctool, test.getPhysicalPath()))
        talkback = dtool.getDiscussionFor(test)
        self.assertEqual(talkback.getPhysicalPath(),
                         ('', 'bar', 'site', 'test', 'talkback'))
        talkback.createReply(title='test', text='blah')
        self.assertEqual(len(ctool), 2)
        for reply in talkback.getReplies():
            self.assertTrue(has_path(ctool, reply.getPhysicalPath()))
            self.assertTrue(has_path(ctool, '/bar/site/test/talkback/%s'
                                            % reply.getId()))

        reply1 = talkback.getReplies()[0]
        path1 = '/'.join(reply1.getPhysicalPath())
        self.assertEqual(ctool.getMetadataForUID(path1), {'in_reply_to': ''})

        talkback1 = dtool.getDiscussionFor(reply1)
        talkback1.createReply(title='test2', text='blah2')
        for reply in talkback.getReplies():
            self.assertTrue(has_path(ctool, reply.getPhysicalPath()))
            self.assertTrue(has_path(ctool, '/bar/site/test/talkback/%s'
                                            % reply.getId()))
        for reply in talkback1.getReplies():
            self.assertTrue(has_path(ctool, reply.getPhysicalPath()))
            self.assertTrue(has_path(ctool, '/bar/site/test/talkback/%s'
                                            % reply.getId()))

        reply2 = talkback1.getReplies()[0]
        path2 = '/'.join(reply2.getPhysicalPath())
        self.assertEqual(ctool.getMetadataForUID(path2),
                         {'in_reply_to': reply1.getId()})

    def test_itemWorkflowNotification(self):
        from Products.CMFDefault.DiscussionItem import DiscussionItem

        dtool = self.dtool
        test = self._makeDummyContent('test')
        test.allow_discussion = 1
        talkback = dtool.getDiscussionFor(test)

        # Monkey patch into the class to test, urgh.
        def notifyWorkflowCreated(self):
            self.test_wf_notified = 1
            DiscussionItem.inheritedAttribute('notifyWorkflowCreated')(self)
        old_method = getattr(DiscussionItem, 'notifyWorkflowCreated', None)
        DiscussionItem.notifyWorkflowCreated = notifyWorkflowCreated
        DiscussionItem.test_wf_notified = 0

        try:
            talkback.createReply(title='test', text='blah')
            reply = talkback.getReplies()[0]
            self.assertEqual(reply.test_wf_notified, 1)
        finally:
            delattr(DiscussionItem, 'test_wf_notified')
            if old_method is None:
                delattr(DiscussionItem, 'notifyWorkflowCreated')
            else:
                DiscussionItem.notifyWorkflowCreated = old_method

    def test_deletePropagation(self):
        ctool = CatalogTool()
        getSiteManager().registerUtility(ctool, ICatalogTool)
        dtool = self.dtool
        test = self._makeDummyContent('test', catalog=1)
        test.allow_discussion = 1

        talkback = dtool.getDiscussionFor(test)
        talkback.createReply(title='test', text='blah')
        self.assertEqual(len(ctool), 2)
        self.site._delObject('test')
        self.assertEqual(len(ctool), 0)

    def test_deleteReplies(self):
        dtool = self.dtool
        ctool = CatalogTool()
        getSiteManager().registerUtility(ctool, ICatalogTool)
        test = self._makeDummyContent('test')
        test.allow_discussion = 1

        # Create a structure 6 levels deep for testing
        talkback = dtool.getDiscussionFor(test)
        id1 = talkback.createReply(title='test1', text='blah')
        reply1 = talkback.getReply(id1)
        talkback1 = dtool.getDiscussionFor(reply1)
        id2 = talkback1.createReply(title='test2', text='blah')
        reply2 = talkback1.getReply(id2)
        talkback2 = dtool.getDiscussionFor(reply2)
        id3 = talkback2.createReply(title='test3', text='blah')
        reply3 = talkback2.getReply(id3)
        talkback3 = dtool.getDiscussionFor(reply3)
        id4 = talkback3.createReply(title='test4', text='blah')
        reply4 = talkback3.getReply(id4)
        talkback4 = dtool.getDiscussionFor(reply4)
        id5 = talkback4.createReply(title='test5', text='blah')
        reply5 = talkback4.getReply(id5)
        talkback5 = dtool.getDiscussionFor(reply5)
        id6 = talkback5.createReply(title='test6', text='blah')
        reply6 = talkback5.getReply(id6)
        talkback6 = dtool.getDiscussionFor(reply6)

        self.assertEqual(len(talkback.getReplies()), 1)
        self.assertEqual(len(talkback1.getReplies()), 1)
        self.assertEqual(len(talkback2.getReplies()), 1)
        self.assertEqual(len(talkback3.getReplies()), 1)
        self.assertEqual(len(talkback4.getReplies()), 1)
        self.assertEqual(len(talkback5.getReplies()), 1)
        self.assertEqual(len(talkback6.getReplies()), 0)
        self.assertEqual(len(ctool), 7)

        talkback3.deleteReply(id4)
        self.assertEqual(len(talkback.getReplies()), 1)
        self.assertEqual(len(talkback1.getReplies()), 1)
        self.assertEqual(len(talkback2.getReplies()), 1)
        self.assertEqual(len(talkback3.getReplies()), 0)
        self.assertEqual(len(ctool), 4)

        talkback.deleteReply(id1)
        self.assertEqual(len(talkback.getReplies()), 0)
        self.assertEqual(len(ctool), 1)

    def test_newTalkbackIsWrapped(self):
        test = self._makeDummyContent('test')
        test.allow_discussion = 1
        dtool = self.dtool
        talkback = dtool.getDiscussionFor(test)
        self.assertTrue(hasattr(talkback, 'aq_base'))
        # Acquire REQUEST
        self.assertTrue(getattr(talkback, 'REQUEST'))

    def test_existingTalkbackIsWrapped(self):
        test = self._makeDummyContent('test')
        test.allow_discussion = 1
        dtool = self.dtool
        dtool.getDiscussionFor(test)
        talkback = dtool.getDiscussionFor(test)
        self.assertTrue(hasattr(talkback, 'aq_base'))
        # Acquire REQUEST
        self.assertTrue(getattr(talkback, 'REQUEST'))


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(DiscussionItemTests),
        unittest.makeSuite(DiscussionItemContainerTests),
        unittest.makeSuite(DiscussionTests),
        ))
