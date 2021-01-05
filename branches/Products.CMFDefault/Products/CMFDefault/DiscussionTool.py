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
""" Basic portal discussion access tool.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from Acquisition import aq_base
from AccessControl.class_init import InitializeClass
from App.special_dtml import DTMLFile
from OFS.SimpleItem import SimpleItem
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.interfaces import IDiscussionResponse
from Products.CMFCore.interfaces import IDiscussionTool
from Products.CMFCore.interfaces import IDynamicType
from Products.CMFCore.utils import _checkPermission
from Products.CMFCore.utils import registerToolInterface
from Products.CMFCore.utils import UniqueObject
from Products.CMFDefault.DiscussionItem import DiscussionItemContainer
from Products.CMFDefault.exceptions import AccessControl_Unauthorized
from Products.CMFDefault.exceptions import DiscussionNotAllowed
from Products.CMFDefault.permissions import ManagePortal
from Products.CMFDefault.permissions import ModifyPortalContent
from Products.CMFDefault.utils import _dtmldir

_marker = []


@implementer(IDiscussionTool)
class DiscussionTool(UniqueObject, SimpleItem):

    """ Links content to discussions.
    """

    id = 'portal_discussion'
    meta_type = 'Default Discussion Tool'

    security = ClassSecurityInfo()

    manage_options = ( ({'label': 'Overview',
                         'action': 'manage_overview'},)
                     + SimpleItem.manage_options
                     )

    #
    #   ZMI methods
    #
    security.declareProtected(ManagePortal, 'manage_overview')
    manage_overview = DTMLFile( 'explainDiscussionTool', _dtmldir )

    #
    #   'portal_discussion' interface methods
    #

    security.declarePublic( 'overrideDiscussionFor' )
    def overrideDiscussionFor(self, content, allowDiscussion):
        """ Override discussability for the given object or clear the setting.
        """
        if not _checkPermission(ModifyPortalContent, content):
            raise AccessControl_Unauthorized

        if allowDiscussion is None or allowDiscussion == 'None':
            disc_flag = getattr(aq_base(content), 'allow_discussion', _marker)
            if disc_flag is not _marker:
                try:
                    del content.allow_discussion
                except AttributeError:
                    # https://bugs.launchpad.net/zope-cmf/+bug/162532
                    pass
        else:
            # https://bugs.launchpad.net/zope-cmf/+bug/1042836/
            if allowDiscussion in ('True', 'true', 'on'):
                allowDiscussion = True
            elif allowDiscussion in ('False', 'false', 'off'):
                allowDiscussion = False
            content.allow_discussion = bool(int(allowDiscussion))

    security.declarePublic( 'getDiscussionFor' )
    def getDiscussionFor(self, content):
        """ Get DiscussionItemContainer for content, create it if necessary.
        """
        if not self.isDiscussionAllowedFor( content ):
            raise DiscussionNotAllowed

        if not IDiscussionResponse.providedBy(content) and \
                getattr( aq_base(content), 'talkback', None ) is None:
            # Discussion Items use the DiscussionItemContainer object of the
            # related content item, so only create one for other content items
            self._createDiscussionFor(content)

        return content.talkback # Return wrapped talkback

    security.declarePublic( 'isDiscussionAllowedFor' )
    def isDiscussionAllowedFor( self, content ):
        """ Get boolean indicating whether discussion is allowed for content.
        """
        if hasattr( aq_base(content), 'allow_discussion' ):
            return bool(content.allow_discussion)

        if IDynamicType.providedBy(content):
            # Grabbing type information objects only works for dynamic types
            typeInfo = content.getTypeInfo()
            if typeInfo:
                return bool( typeInfo.allowDiscussion() )

        return False

    #
    #   Utility methods
    #
    security.declarePrivate( '_createDiscussionFor' )
    def _createDiscussionFor( self, content ):
        """ Create DiscussionItemContainer for content, if allowed.
        """
        if not self.isDiscussionAllowedFor( content ):
            raise DiscussionNotAllowed

        content.talkback = DiscussionItemContainer()
        return content.talkback

InitializeClass( DiscussionTool )
registerToolInterface('portal_discussion', IDiscussionTool)
