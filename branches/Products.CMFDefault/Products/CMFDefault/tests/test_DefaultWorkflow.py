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
""" Unit tests for DefaultWorkflow module.
"""

import unittest
import Testing

from zope.component import getSiteManager
from zope.interface.verify import verifyClass
from zope.testing.cleanup import cleanUp

from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.interfaces import IWorkflowTool
from Products.CMFCore.tests.base.dummy import DummyContent
from Products.CMFCore.tests.base.dummy import DummySite
from Products.CMFCore.tests.base.dummy import DummyTool
from Products.CMFCore.tests.base.dummy import DummyUserFolder
from Products.CMFCore.WorkflowTool import WorkflowTool


class DefaultWorkflowDefinitionTests(unittest.TestCase):

    def setUp(self):
        from Products.CMFDefault.DefaultWorkflow \
                import DefaultWorkflowDefinition
        self.site = DummySite('site')
        self.site._setObject('acl_users', DummyUserFolder())

        self.wtool = WorkflowTool()
        self.wtool._setObject('wf', DefaultWorkflowDefinition('wf'))
        self.wtool.setDefaultChain('wf')
        sm = getSiteManager()
        sm.registerUtility(self.wtool, IWorkflowTool)
        sm.registerUtility(DummyTool(), IMembershipTool)
        sm.registerUtility(DummyTool(), ITypesTool)

    def tearDown(self):
        cleanUp()

    def test_interfaces(self):
        from Products.CMFCore.interfaces import IWorkflowDefinition
        from Products.CMFDefault.DefaultWorkflow \
                import DefaultWorkflowDefinition

        verifyClass(IWorkflowDefinition, DefaultWorkflowDefinition)

    def _getDummyWorkflow(self):
        return self.wtool.wf

    def test_isActionSupported(self):

        wf = self._getDummyWorkflow()
        dummy = self.site._setObject('dummy', DummyContent())

        for action in ('submit', 'retract', 'publish', 'reject',):
            self.assertTrue(wf.isActionSupported(dummy, action))

    def test_isActionSupported_with_keywargs(self):

        wf = self._getDummyWorkflow()
        dummy = self.site._setObject('dummy', DummyContent())

        for action in ('submit', 'retract', 'publish', 'reject',):
            self.assertTrue(wf.isActionSupported(dummy, action,
                                                 arg1=1, arg2=2))

    # XXX more tests...


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(DefaultWorkflowDefinitionTests),
        ))
