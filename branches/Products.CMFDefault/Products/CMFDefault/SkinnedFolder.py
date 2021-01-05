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
""" Allow the "view" of a folder to be skinned by type.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from zope.component.factory import Factory
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.CMFCatalogAware import CatalogAware
from Products.CMFCore.CMFCatalogAware import WorkflowAware
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.PortalFolder import PortalFolder
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFDefault.permissions import ModifyPortalContent
from Products.CMFDefault.permissions import View

@implementer(IContentish)
class SkinnedFolder(CatalogAware, WorkflowAware, PortalFolder):

    """ Skinned Folder class. 
    """


    security = ClassSecurityInfo()

    manage_options = PortalFolder.manage_options + WorkflowAware.manage_options

    # XXX: maybe we should subclass from DefaultDublinCoreImpl or refactor it

    security.declarePrivate('notifyModified')
    def notifyModified(self):
        """ Take appropriate action after the resource has been modified.

        Update creators.
        """
        self.addCreator()

    security.declareProtected(ModifyPortalContent, 'addCreator')
    addCreator = DefaultDublinCoreImpl.addCreator.__name__

    security.declareProtected(View, 'listCreators')
    listCreators = DefaultDublinCoreImpl.listCreators.__name__

    security.declareProtected(View, 'Creator')
    Creator = DefaultDublinCoreImpl.Creator.__name__

    #
    #   'IContentish' interface method
    #
    security.declareProtected(View, 'SearchableText')
    def SearchableText(self):
        """
        SeachableText is used for full text seraches of a portal.  It
        should return a concatenation of all useful text.
        """
        return "%s %s" % (self.title, self.description)

InitializeClass(SkinnedFolder)

SkinnedFolderFactory = Factory(SkinnedFolder)

def addSkinnedFolder( self, id, title='', description='', REQUEST=None ):
    """
    """
    sf = SkinnedFolder( id, title )
    sf.description = description
    self._setObject(id, sf, suppress_events=True)
    sf = self._getOb( id )
    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect( sf.absolute_url() + '/manage_main' )
