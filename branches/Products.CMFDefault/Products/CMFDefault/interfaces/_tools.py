##############################################################################
#
# Copyright (c) 2005 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" CMFDefault tool interfaces.
"""

from Products.CMFCore.interfaces import IMembershipTool as BaseInterface


class IMembershipTool(BaseInterface):

    """ Declare product-specific APIs for CMFDefault's tool.
    """

    __module__ = 'Products.CMFDefault.interfaces'

    def setMembersFolderById(id=''):
        """ Set the members folder object by its id.

        The members folder has to be in the same container as the membership
        tool. id is the id of an existing folder. If id is empty, member areas
        are disabled.

        Permission -- Manage portal
        """
