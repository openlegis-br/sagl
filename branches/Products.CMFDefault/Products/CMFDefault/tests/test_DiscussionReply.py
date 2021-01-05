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
""" Unit tests for http://zope.org/Collectors/CMF/318
"""

import unittest
from Testing import ZopeTestCase

from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManagement import getSecurityManager
from zope.component.hooks import setSite

from Products.CMFDefault.permissions import AccessContentsInformation
from Products.CMFDefault.permissions import View
from Products.CMFDefault.testing import FunctionalLayer


class DiscussionReplyTest(ZopeTestCase.FunctionalTestCase):

    layer = FunctionalLayer

    def afterSetUp(self):
        setSite(self.app.site)
        self.portal = self.app.site
        # Become a Manager
        self.uf = self.portal.acl_users
        self.uf.userFolderAddUser('manager', '', ['Manager'], [])
        self.site_login('manager')
        # Make a document
        self.discussion = self.portal.portal_discussion
        self.portal.invokeFactory('Document', id='doc')
        self.discussion.overrideDiscussionFor(self.portal.doc, 1)
        # Publish it
        self.workflow = self.portal.portal_workflow
        self.workflow.doActionFor(self.portal.doc, 'publish')

    def site_login(self, name):
        user = self.uf.getUserById(name)
        user = user.__of__(self.uf)
        newSecurityManager(None, user)

    def testDiscussionReply(self):
        self.discussion.getDiscussionFor(self.portal.doc)
        reply_id = self.portal.doc.talkback.createReply('Title', 'Text')
        talkback = self.discussion.getDiscussionFor(self.portal.doc)
        reply = talkback.getReply(reply_id)
        self.assertEqual(reply.Title(), 'Title')
        self.assertEqual(reply.EditableBody(), 'Text')

        # Make sure the user who created the reply can actually see it
        # https://bugs.launchpad.net/zope-cmf/+bug/161720
        state = self.portal.portal_workflow.getInfoFor(reply, 'review_state')
        self.assertEqual(state, 'published')
        sm = getSecurityManager()
        self.assertTrue(sm.checkPermission(View, reply))
        self.assertTrue(sm.checkPermission(AccessContentsInformation, reply))


class DiscussionReplyTestMember(DiscussionReplyTest):

    # Run the test again as another Member, i.e. reply to someone
    # else's document.

    def afterSetUp(self):
        DiscussionReplyTest.afterSetUp(self)
        self.uf.userFolderAddUser('member', '', ['Member'], [])
        self.site_login('member')


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DiscussionReplyTest))
    suite.addTest(unittest.makeSuite(DiscussionReplyTestMember))
    return suite
