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
""" SyndicationInfo is an adapter for IFolderish objects.
"""

from datetime import datetime

from AccessControl.SecurityInfo import ClassSecurityInfo
from DateTime import DateTime
from OFS.SimpleItem import SimpleItem
from zope.annotation.interfaces import IAnnotations
from zope.component import adapts
from zope.component import getUtility
from zope.component import getAdapter
from zope.interface import alsoProvides
from zope.interface import implements
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import noLongerProvides
from zope.schema import Bool, Choice, Datetime, Int
from zope.schema.vocabulary import SimpleVocabulary

from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.interfaces import ISyndicatable
from Products.CMFCore.interfaces import ISyndicationInfo
from Products.CMFCore.interfaces import ISyndicationTool
from Products.CMFDefault.formlib.vocabulary import SimpleVocabulary
from Products.CMFDefault.SyndicationTool import SyndicationTool
from Products.CMFDefault.utils import Message as _


class SyndicationInformation(SimpleItem):
    #DEPRECATED
    """
    Existing implementation creates a full SimpleItem which is not directly
    editable
    """

    id='syndication_information'
    meta_type='SyndicationInformation'

available_periods = (
    (u'hourly', 'hourly', _(u'Hourly')),
    (u'daily', 'daily', _(u'Daily')),
    (u'weekly', 'weekly', _(u'Weekly')),
    (u'monthly', 'monthly', _(u'Monthly')),
    (u'yearly', 'yearly', _(u'Yearly')))


class ISyndicationInfo(ISyndicationInfo):

    period = Choice(
        title=_(u"Update period"),
        vocabulary=SimpleVocabulary.fromTitleItems(available_periods),
    )

    frequency = Int(
        title=_(u"Update frequency"),
        description=_(u"This is a multiple of the update period. An"
                      u" update frequency of '3' and an update period"
                      u" of 'Monthly' will mean an update every three months."),
    )

    base = Datetime(
        title=_(u"Update base"),
        description=_(u""),
        default=datetime.now()
    )

    max_items = Int(
        title=_(u"Maximum number of items"),
        description=_(u""),
        default=15
    )

    enabled = Bool(
        required=False,
    )

@implementer(ISyndicationInfo)
class SyndicationInfo(object):
    """
    Annotations adapter.
    Folders which can be syndicated are given the ISyndicatable interface
    Local syndication information is stored as a dictionary under the
    __cmf.syndication_info key of the annotations
    """

    __slots__ = ()
    adapts(IFolderish)
    key = "__cmf.SyndicationInfo"
    security = ClassSecurityInfo()

    def __init__(self, context):
        self.context = context

    @property
    def site_settings(self):
        """Get site syndication tool"""
        return getUtility(ISyndicationTool)

    @property
    def allowed(self):
        return self.site_settings.enabled

    def _get_property(self, attr):
        """
        Get a value from the annotation or site settings.
        """
        annotations = getAdapter(self.context, IAnnotations)
        annotation = annotations.get(self.key, None)
        if annotation is None:
            return getattr(self.site_settings, attr)
        return annotation.get(attr, getattr(self.site_settings, attr))

    def _set_property(self, attr, value):
        """
        Set a value on the annotation
        """
        annotations = getAdapter(self.context, IAnnotations)
        if not annotations.get(self.key):
            annotations[self.key] = {}
        annotation = annotations.get(self.key, None)
        annotation[attr] = value

    security.declarePublic('period')
    @property
    def period(self):
        return self._get_property('period')

    @period.setter
    def period(self, value):
        self._set_property('period', value)

    @property
    def frequency(self):
        return self._get_property('frequency')

    @frequency.setter
    def frequency(self, value):
        self._set_property('frequency', value)

    security.declarePublic('base')
    @property
    def base(self):
        return self._get_property('base')

    @base.setter
    def base(self, value):
        return self._set_property('base', value)

    def rfc822(self):
        as_zope = DateTime(self.base.isoformat())
        return as_zope.rfc822()

    security.declarePublic('max_items')
    @property
    def max_items(self):
        return self._get_property('max_items')

    @max_items.setter
    def max_items(self, value):
        self._set_property('max_items', value)

    @property
    def enabled(self):
        """Is syndication available for the site and a folder"""
        return self.site_settings.enabled \
               and ISyndicatable.providedBy(self.context)

    def enable(self):
        """Enable syndication for a folder"""
        alsoProvides(self.context, ISyndicatable)

    def disable(self):
        """Disable syndication for a folder"""
        self.revert()
        noLongerProvides(self.context, ISyndicatable)

    def revert(self):
        """Remove local values"""
        annotations = getAdapter(self.context, IAnnotations)
        try:
            del annotations[self.key]
        except KeyError:
            pass
