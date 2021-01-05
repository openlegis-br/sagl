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
"""Workflow history view"""

from zope.component import getUtility

from Products.CMFCore.interfaces import IWorkflowTool
from Products.CMFDefault.browser.utils import decode
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.utils import ViewBase


class View(ViewBase):

    @property
    @memoize
    def workflow(self):
        return getUtility(IWorkflowTool)

    @memoize
    @decode
    def review_state(self):
        return self.workflow.getInfoFor(self.context, 'review_state')

    @memoize
    @decode
    def review_history(self):
        history = self.workflow.getInfoFor(self.context, 'review_history')
        if not history:
            return
        return reversed(history)
