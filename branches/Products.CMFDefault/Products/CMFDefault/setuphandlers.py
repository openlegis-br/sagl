##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" CMFDefault setup handlers.
"""

from zope.component import getUtility
from zope.component.interfaces import IFactory

from Products.CMFCore.interfaces import ITypesTool


def importVarious(context):
    """ Import various settings.

    This provisional handler will be removed again as soon as full handlers
    are implemented for these steps.
    """
    logger = context.getLogger('various')

    # Only run step if a flag file is present
    if context.readDataFile('various.txt') is None:
        logger.debug('Nothing to import.')
        return

    site = context.getSite()

    ttool = getUtility(ITypesTool)
    portal_type = ttool.getTypeInfo('Members Folder')
    factory = getUtility(IFactory, portal_type.factory)
    obj = factory(id='Members')
    obj._setPortalTypeName('Members Folder')
    site._setObject('Members', obj)
    logger.info('Members folder imported.')

    site.acl_users.encrypt_passwords = False
    logger.info('Password encryption disabled.')
