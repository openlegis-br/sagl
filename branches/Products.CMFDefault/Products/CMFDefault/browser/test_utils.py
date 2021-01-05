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
"""Various utilities for testing browser views"""

from zope.publisher.browser import TestRequest


class DummyResponse(object):

    def redirect(self, value):
        self.location = value


class DummyRequest(TestRequest):

    def __init__(self, **kw):
        super(DummyRequest, self).__init__(kw)
        self._response = DummyResponse()

    def getPreferredCharsets(self):
        return ['utf-8']
