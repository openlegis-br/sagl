##############################################################################
#
# Copyright (c) 2012 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Notification emails.
"""

from email.utils import formataddr

from zope.component import getUtility

from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.browser.utils import decode
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.browser.utils import ViewBase
from Products.CMFDefault.utils import makeEmail
from Products.CMFDefault.utils import Message as _


class _EmailBase(ViewBase):

    def _makeEmail(self):
        mtext = self.index()
        headers = {'Subject': self._subject,
                   'From': self._from,
                   'To': u'<{0}>'.format(self.email)}
        return makeEmail(mtext, self.context, headers)

    @property
    @decode
    def _from(self):
        return formataddr((
            self.ptool.getProperty('email_from_name'),
            self.ptool.getProperty('email_from_address')))

    @property
    @memoize
    def ptool(self):
        return getUtility(IPropertiesTool)

    @property
    @memoize
    @decode
    def portal_title(self):
        return self.ptool.title()

    @property
    @memoize
    @decode
    def portal_description(self):
        return self.ptool.getProperty('description')

    @property
    @memoize
    def portal_url(self):
        return self._getPortalURL()


class RegisteredEmail(_EmailBase):

    """Email for registration notification.
    """

    def __call__(self, member=None, password='secret',
                 email='foo@example.org'):
        self.member_id = member and member.getId() or 'foo'
        self.password = password
        self.email = email
        return self._makeEmail()

    @property
    def _subject(self):
        return _(u'${portal_title}: Your Membership Information',
                 mapping={'portal_title': self.portal_title})

    @property
    @memoize
    def login_url(self):
        atool = getUtility(IActionsTool)
        return atool.getActionInfo('user/login')['url']

    @property
    @memoize
    @decode
    def signature(self):
        return self.ptool.getProperty('email_from_name')


class PasswordEmail(_EmailBase):

    """Email for password notification.
    """

    def __call__(self, member=None, password='secret'):
        self.password = password
        self.email = member and member.getProperty('email') \
                     or 'foo@example.org'
        return self._makeEmail()

    @property
    def _subject(self):
        return _(u'${portal_title}: Membership reminder',
                 mapping={'portal_title': self.portal_title})
