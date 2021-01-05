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
""" CMFDefault portal_membership tool.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from Acquisition import aq_inner
from Acquisition import aq_parent
from AccessControl.class_init import InitializeClass
from App.special_dtml import DTMLFile
from zope.component import getUtility
from zope.globalrequest import getRequest
from zope.interface import implementer
from ZPublisher.BaseRequest import RequestContainer

from Products.CMFCore.interfaces import IMembershipTool as IBaseTool
from Products.CMFCore.MembershipTool import HomeFolderFactoryBase
from Products.CMFCore.MembershipTool import MembershipTool as BaseTool
from Products.CMFCore.utils import _checkPermission
from Products.CMFDefault.Document import Document
from Products.CMFDefault.interfaces import IMembershipTool
from Products.CMFDefault.permissions import ListPortalMembers
from Products.CMFDefault.permissions import ManagePortal
from Products.CMFDefault.permissions import ManageUsers
from Products.CMFDefault.permissions import View
from Products.CMFDefault.utils import _dtmldir
from Products.CMFDefault.utils import Message as _

DEFAULT_MEMBER_CONTENT = """\
Default page for %s

  This is the default document created for you when
  you joined this community.

  To change the content just select "Edit"
  in the Tool Box on the left.
"""


@implementer(IMembershipTool)
class MembershipTool(BaseTool):

    """ Implement 'portal_membership' interface using "stock" policies.
    """

    meta_type = 'Default Membership Tool'
    membersfolder_id = 'Members'
    _HOME_FOLDER_FACTORY_NAME = 'cmf.folder.home.bbb2'

    security = ClassSecurityInfo()

    #
    #   ZMI methods
    #
    security.declareProtected( ManagePortal, 'manage_overview' )
    manage_overview = DTMLFile( 'explainMembershipTool', _dtmldir )

    security.declareProtected(ManagePortal, 'manage_mapRoles')
    manage_mapRoles = DTMLFile('membershipRolemapping', _dtmldir )

    security.declareProtected(ManagePortal, 'manage_setMembersFolderById')
    def manage_setMembersFolderById(self, id='', REQUEST=None):
        """ ZMI method to set the members folder object by its id.
        """
        self.setMembersFolderById(id)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect( self.absolute_url()
                    + '/manage_mapRoles'
                    + '?manage_tabs_message=Members+folder+changed.'
                    )

    #
    #   'portal_membership' interface methods
    #
    security.declareProtected(ListPortalMembers, 'getRoster')
    def getRoster(self):
        """ Return a list of mappings for 'listed' members.

        If Manager, return a list of all usernames.  The mapping
        contains the id and listed variables.
        """
        isUserManager = _checkPermission(ManageUsers, self)
        roster = []
        for member in self.listMembers():
            listed = member.getProperty('listed')
            if isUserManager or listed:
                roster.append({'id': member.getId(),
                               'listed': listed})
        return roster

    security.declareProtected(ManagePortal, 'setMembersFolderById')
    def setMembersFolderById(self, id=''):
        """ Set the members folder object by its id.
        """
        self.membersfolder_id = id.strip()

    security.declarePublic('getMembersFolder')
    def getMembersFolder(self):
        """ Get the members folder object.
        """
        parent = aq_parent(aq_inner(self))
        try:
            members_folder = parent.restrictedTraverse(self.membersfolder_id)
        except (AttributeError, KeyError):
            return None
        request_container = RequestContainer(REQUEST=getRequest())
        return members_folder.__of__(request_container)

    def getHomeFolder(self, id=None, verifyPermission=0):
        """ Return a member's home folder object, or None.
        """
        if id is None:
            member = self.getAuthenticatedMember()
            if not hasattr(member, 'getMemberId'):
                return None
            id = member.getMemberId()
        members = self.getMembersFolder()
        if members:
            try:
                folder = members._getOb(id)
                if verifyPermission and not _checkPermission(View, folder):
                    # Don't return the folder if the user can't get to it.
                    return None
                return folder
            except (AttributeError, TypeError, KeyError):
                pass
        return None

    def getHomeUrl(self, id=None, verifyPermission=0):
        """ Return the URL to a member's home folder, or None.
        """
        home = self.getHomeFolder(id, verifyPermission)
        if home is not None:
            return home.absolute_url()
        else:
            return None

InitializeClass(MembershipTool)


class _HomeFolderFactory(HomeFolderFactoryBase):

    """Creates a home folder.
    """

    def __call__(self, id, title=None, *args, **kw):
        item = super(_HomeFolderFactory,
                     self).__call__(id, title=title, *args, **kw)

        # Create Member's initial content
        subitem = Document('index_html', "{0}'s Home".format(id),
                           "{0}'s front page".format(id),
                           'structured-text', DEFAULT_MEMBER_CONTENT % id)
        subitem.manage_setLocalRoles(id, ['Owner'])
        subitem._setPortalTypeName('Document')
        item._setObject('index_html', subitem, suppress_events=True)
        return item

HomeFolderFactory = _HomeFolderFactory()


class _BBBHomeFolderFactory(HomeFolderFactoryBase):

    """Creates a home folder.
    """

    description = _(u'Classic CMFDefault home folder for portal members.')

    def __call__(self, id, title=None, *args, **kw):
        item = super(_BBBHomeFolderFactory,
                     self).__call__(id, title=title, *args, **kw)

        # Create Member's initial content
        mtool = getUtility(IBaseTool)
        if hasattr(mtool, 'createMemberContent'):
            wrapped = item.__of__(mtool.getMembersFolder())
            mtool.createMemberContent(member=mtool.getMemberById(id),
                                      member_id=id,
                                      member_folder=wrapped)
        else:
            subitem = Document('index_html', "{0}'s Home".format(id),
                               "{0}'s front page".format(id),
                               'structured-text', DEFAULT_MEMBER_CONTENT % id)
            subitem.manage_setLocalRoles(id, ['Owner'])
            subitem._setPortalTypeName('Document')
            item._setObject('index_html', subitem, suppress_events=True)
        return item

BBBHomeFolderFactory = _BBBHomeFolderFactory()
