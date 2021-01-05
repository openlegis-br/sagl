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
""" CMFDefault portal_syndication tool.

Manage outbound RSS syndication of folder content.
"""

from datetime import datetime
from warnings import warn

from AccessControl.SecurityInfo import ClassSecurityInfo
from Acquisition import aq_base
from AccessControl.class_init import InitializeClass
from App.special_dtml import HTMLFile
from DateTime.DateTime import DateTime
from OFS.SimpleItem import SimpleItem

from zope.component import getAdapter, queryAdapter
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.interfaces import ISyndicationTool, ISyndicationInfo
from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.PortalFolder import PortalFolderBase
from Products.CMFCore.utils import _checkPermission
from Products.CMFCore.utils import registerToolInterface
from Products.CMFCore.utils import UniqueObject
from Products.CMFDefault.exceptions import AccessControl_Unauthorized
from Products.CMFDefault.permissions import ManagePortal
from Products.CMFDefault.permissions import ManageProperties
from Products.CMFDefault.utils import _dtmldir


class SyndicationError(Exception):

    pass

@implementer(ISyndicationTool)
class SyndicationTool(UniqueObject, SimpleItem):
    """ The syndication tool manages the site-wide policy for
        syndication of folder content as RSS.
    """

    id = 'portal_syndication'
    meta_type = 'Default Syndication Tool'

    security = ClassSecurityInfo()

    #Default Sitewide Values
    isAllowed = enabled = False
    syUpdatePeriod = period = 'daily'
    syUpdateFrequency = frequency = 1
    syUpdateBase = base = datetime.now()
    max_items = 15

    #ZMI Methods
    manage_options = ( ( { 'label'  : 'Overview'
                         , 'action' : 'overview'
                         , 'help'   : ( 'CMFDefault'
                                      , 'Syndication-Tool_Overview.stx' )
                         },
                        )
                     )

    security.declareProtected(ManagePortal, 'overview')
    overview = HTMLFile('synOverview', _dtmldir)

    def _syndication_info(self, obj):
        """Get a SyndicationInfo adapter for managing object
        syndication settings
        """
        adapter = queryAdapter(obj, ISyndicationInfo)
        if adapter is None:
            raise SyndicationError("Syndication is not possible")
        return adapter

    security.declareProtected(ManageProperties, 'editSyInformationProperties')
    def editSyInformationProperties( self
                                   , obj
                                   , updatePeriod=None
                                   , updateFrequency=None
                                   , updateBase=None
                                   , max_items=None
                                   , REQUEST=None
                                   ):
        """
        Edit syndication properties for the obj being passed in.
        These are held on the syndication_information object.
        Not Sitewide Properties.
        """
        info = self.getSyndicationInfo(obj)

        if not info.enabled:
            raise SyndicationError('Syndication is Disabled')

        info.period = updatePeriod or self.period
        info.frequency = updateFrequency or self.frequency
        info.base = updateBase or self.base
        info.max_items = max_items or self.max_items

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    security.declareProtected(ManageProperties, 'enableSyndication')
    def enableSyndication(self, obj):
        """
        Enable syndication for the obj
        """
        if not self.isSiteSyndicationAllowed():
            raise SyndicationError('Syndication is Disabled')

        info = self._syndication_info(obj)
        info.enable()

    security.declareProtected(ManageProperties, 'disableSyndication')
    def disableSyndication(self, obj):
        """
        Disable syndication for the obj; and remove it.
        """
        info = self._syndication_info(obj)
        info.disable()

    security.declarePublic('getSyndicatableContent')
    def getSyndicatableContent(self, obj):
        """
        An interface for allowing folderish items to implement an
        equivalent of PortalFolderBase.contentValues()
        """
        if hasattr(obj, 'synContentValues'):
            values = obj.synContentValues()
        else:
            values = PortalFolderBase.contentValues(obj)
            values = [v for v in values if not IFolderish.providedBy(v)]
        return values

    security.declarePublic('buildUpdatePeriods')
    def buildUpdatePeriods(self):
        """
        Return a list of possible update periods for the xmlns: sy
        """
        updatePeriods = ( ('hourly',  'Hourly')
                        , ('daily',   'Daily')
                        , ('weekly',  'Weekly')
                        , ('monthly', 'Monthly')
                        , ('yearly',  'Yearly')
                        )
        return updatePeriods

    security.declarePublic('isSiteSyndicationAllowed')
    def isSiteSyndicationAllowed(self):
        """
        Return sitewide syndication policy
        """
        return self.enabled

    security.declarePublic('isSyndicationAllowed')
    def isSyndicationAllowed(self, obj=None):
        """
        Check whether syndication is enabled for the site.  This
        provides for extending the method to check for whether a
        particular obj is enabled, allowing for turning on only
        specific folders for syndication.
        """
        if obj is None:
            return self.isSiteSyndicationAllowed()
        try:
            info = self._syndication_info(obj)
        except SyndicationError:
            return False
        return getattr(info, 'enabled', False)

    security.declarePublic('getSyndicationInfo')
    def getSyndicationInfo(self, obj):
        """
        Return a dictionary of syndication parameters
        """
        info = self._syndication_info(obj)
        if not info.enabled:
            raise SyndicationError('Syndication is not allowed')
        return info

    security.declarePublic('getUpdatePeriod')
    def getUpdatePeriod( self, obj=None ):
        """
        Return the update period for the RSS syn namespace.
        This is either on the object being passed or the
        portal_syndication tool (if a sitewide value or default
        is set)

        NOTE:  Need to add checks for sitewide policies!!!
        """
        if obj is not None:
            period = self.getSyndicationInfo(obj).period
        else:
            period = self.period
        return period

    security.declarePublic('getUpdateFrequency')
    def getUpdateFrequency(self, obj=None):
        """
        Return the update frequency (as a positive integer) for
        the syn namespace.  This is either on the object being
        pass or the portal_syndication tool (if a sitewide value
        or default is set).

        Note:  Need to add checks for sitewide policies!!!
        """
        if obj is not None:
            frequency = self.getSyndicationInfo(obj).frequency
        else:
            frequency = self.frequency

        return frequency

    security.declarePublic('getUpdateBase')
    def getUpdateBase(self, obj=None):
        """
        Return the base date formatted as RFC 822 to be used with the update
        frequency and the update period to calculate a publishing schedule.
        """
        if obj is not None:
            base = self.getSyndicationInfo(obj).base
        else:
            base = self.base
        as_zope = DateTime(base.isoformat())
        return as_zope.rfc822()

    security.declarePublic('getHTML4UpdateBase')
    def getHTML4UpdateBase(self, obj=None):
        """
        Return HTML4 formated UpdateBase DateTime
        """
        warn("RSS 2.0 uses RFC 822 formatting"
             " this method will be removed in CMF 2.4",
             DeprecationWarning, stacklevel=2)
        # HTML4 is almost the same as isoformat()
        if obj is not None:
            base = obj.base
        else:
            base = self.base
        # normalise
        base = base.replace(tzinfo=None)
        as_zope = DateTime(base.isoformat())
        return as_zope.HTML4()

    security.declarePublic('getMaxItems')
    def getMaxItems(self, obj=None):
        """
        Return the max_items to be displayed in the syndication
        """
        if obj is not None:
            max_items = self.getSyndicationInfo(obj).max_items
        else:
            max_items = self.max_items
        return max_items

InitializeClass(SyndicationTool)
registerToolInterface('portal_syndication', ISyndicationTool)
