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
""" CMFDefault product exceptions.
"""

from zope.schema import ValidationError
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('cmf_default')

from AccessControl import ModuleSecurityInfo
security = ModuleSecurityInfo('Products.CMFDefault.exceptions')

security.declarePublic('AccessControl_Unauthorized')
from Products.CMFCore.exceptions import AccessControl_Unauthorized

security.declarePublic('BadRequest')
from Products.CMFCore.exceptions import BadRequest

security.declarePublic('CopyError')
from Products.CMFCore.exceptions import CopyError

security.declarePublic('ResourceLockedError')
from Products.CMFCore.exceptions import ResourceLockedError

security.declarePublic('WorkflowException')
from Products.CMFCore.WorkflowCore import WorkflowException

security.declarePublic('zExceptions_Unauthorized')
from Products.CMFCore.exceptions import zExceptions_Unauthorized


security.declarePublic('EditingConflict')
class EditingConflict(Exception):
    """ Editing conflict error.
    """


security.declarePublic('DiscussionNotAllowed')
class DiscussionNotAllowed(Exception):
    """ Discussion not allowed error.
    """


security.declarePublic('IllegalHTML')
class IllegalHTML(ValueError):
    """ Illegal HTML error.
    """


security.declarePublic('MetadataError')
class MetadataError(Exception):
    """ Metadata error.
    """

class EmailAddressInvalid(ValidationError):
    __doc__ = _(u'Invalid email address.')
