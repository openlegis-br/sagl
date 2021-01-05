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
"""Syndication configuration views.
"""

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getAdapter
from zope.component import getUtility
from zope.formlib import form

from Products.CMFCore.interfaces import ISyndicationTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.formlib.form import SettingsEditFormBase
from Products.CMFDefault.SyndicationInfo import ISyndicationInfo
from Products.CMFDefault.utils import Message as _


class Site(SettingsEditFormBase):

    """Enable or disable syndication for a site."""

    form_fields = form.FormFields(ISyndicationInfo).omit('enabled')
    label = _(u"Configure Portal Syndication")

    actions = form.Actions(
        form.Action(
            name="enable",
            label=_(u"Enable Syndication"),
            condition="disabled",
            success="handle_enable",
            ),
        form.Action(
            name="change",
            label=_(u"Change"),
            condition="enabled",
            success="handle_change",
            ),
        form.Action(
            name="disable",
            label=_(u"Disable Syndication"),
            condition="enabled",
            success="handle_disable"
        )
    )

    redirect = ("portal_actions", "global/syndication")

    @memoize
    def getContent(self):
        syndtool = getUtility(ISyndicationTool)
        return syndtool

    @memoize
    def enabled(self, action=None):
        return self.getContent().enabled

    @memoize
    def disabled(self, action=None):
        return not self.getContent().enabled

    def handle_enable(self, action, data):
        self.getContent().enable()
        self._handle_success(action, data)
        self.status = _(u"Syndication enabled.")
        self._setRedirect(*self.redirect)

    def handle_change(self, action, data):
        self._handle_success(action, data)
        self.status = _(u"Syndication settings changed.")
        self._setRedirect(*self.redirect)

    def handle_disable(self, action, data):
        self.getContent().disable()
        self.status = _(u"Syndication disabled.")
        self._setRedirect(*self.redirect)


class Folder(Site):

    """Enable, disable and customise syndication settings for a folder.
    """

    label = _(u"Configure Folder Syndication")

    actions = form.Actions(*Site.actions.actions)
    actions.append(
        form.Action(
        name="revert",
        label=_(u"Revert to Site Default"),
        condition="enabled",
        success="handle_revert",
            )
        )

    redirect = ("portal_actions", "object/syndication")

    @memoize
    def getContent(self):
        return getAdapter(self.context, ISyndicationInfo)

    @memoize
    def allowed(self, action=None):
        return self.getContent().allowed

    def handle_revert(self, action, data):
        self.getContent().revert()
        self.status = _(u"Syndication reset to site default.")
        self._setRedirect(*self.redirect)
