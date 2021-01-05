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
""" A simple submit/review/publish workflow.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from AccessControl.class_init import InitializeClass
from DateTime.DateTime import DateTime
from zope.component import getUtility
from zope.component import queryUtility
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.interfaces import ICatalogTool
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import IWorkflowDefinition
from Products.CMFCore.utils import _checkPermission
from Products.CMFCore.utils import _modifyPermissionMappings
from Products.CMFCore.utils import SimpleItemWithProperties
from Products.CMFDefault.exceptions import AccessControl_Unauthorized
from Products.CMFDefault.permissions import ModifyPortalContent
from Products.CMFDefault.permissions import RequestReview
from Products.CMFDefault.permissions import ReviewPortalContent
from Products.CMFDefault.permissions import View

@implementer(IWorkflowDefinition)
class DefaultWorkflowDefinition(SimpleItemWithProperties):

    """ Default workflow definition.
    """


    meta_type = 'CMF Default Workflow'
    id = 'default_workflow'
    title = 'Simple Review / Publish Policy'

    security = ClassSecurityInfo()

    def __init__(self, id):
        self.id = id

    security.declarePrivate('getReviewStateOf')
    def getReviewStateOf(self, ob):
        tool = aq_parent(aq_inner(self))
        status = tool.getStatusOf(self.getId(), ob)
        if status is not None:
            review_state = status['review_state']
        else:
            if hasattr(aq_base(ob), 'review_state'):
                # Backward compatibility.
                review_state = ob.review_state
            else:
                review_state = 'private'
        return review_state

    security.declarePrivate('getCatalogVariablesFor')
    def getCatalogVariablesFor(self, ob):
        '''
        Allows this workflow to make workflow-specific variables
        available to the catalog, making it possible to implement
        queues in a simple way.
        Returns a mapping containing the catalog variables
        that apply to ob.
        '''
        return {'review_state': self.getReviewStateOf(ob)}

    security.declarePrivate('listObjectActions')
    def listObjectActions(self, info):
        '''
        Allows this workflow to
        include actions to be displayed in the actions box.
        Called only when this workflow is applicable to
        info.object.
        Returns the actions to be displayed to the user.
        '''
        if info.isAnonymous:
            return None

        # The following operation is quite expensive.
        # We don't need to perform it if the user
        # doesn't have the required permission.
        content = info.object
        content_url = info.object_url
        content_creator = content.Creator()
        mtool = getUtility(IMembershipTool)
        current_user = mtool.getAuthenticatedMember().getId()
        review_state = self.getReviewStateOf(content)
        actions = []

        allow_review = _checkPermission(ReviewPortalContent, content)
        allow_request = _checkPermission(RequestReview, content)

        append_action = (lambda name, p, url=content_url, a=actions.append:
                         a({'name': name,
                            'url': url + '/' + p,
                            'permissions': (),
                            'category': 'workflow'}))

        show_reject = 0
        show_retract = 0

        if review_state == 'private':
            if allow_review:
                append_action('Publish', 'content_publish_form')
            elif allow_request:
                append_action('Submit', 'content_submit_form')

        elif review_state == 'pending':
            if content_creator == current_user and allow_request:
                show_retract = 1
            if allow_review:
                append_action('Publish', 'content_publish_form')
                show_reject = 1

        elif review_state == 'published':
            if content_creator == current_user and allow_request:
                show_retract = 1
            if allow_review:
                show_reject = 1

        if show_retract:
            append_action('Retract', 'content_retract_form')
        if show_reject:
            append_action('Reject', 'content_reject_form')
        if allow_review or allow_request:
            append_action('Status history', 'content_status_history')

        return actions

    security.declarePrivate('listGlobalActions')
    def listGlobalActions(self, info):
        '''
        Allows this workflow to include actions to be displayed
        in the actions box.  Called on every request.

        Returns the actions to be displayed to the user.
        '''
        if info.isAnonymous:
            return None

        actions = []
        ctool = queryUtility(ICatalogTool)
        if ctool is None:
            return actions

        pending = len(ctool.searchResults(review_state='pending'))
        if pending > 0:
            actions.append(
                {'name': 'Pending review (%d)' % pending,
                 'url': info.portal_url +
                 '/search?review_state=pending',
                 'permissions': (ReviewPortalContent,),
                 'category': 'global'}
                )

        return actions

    security.declarePrivate('isActionSupported')
    def isActionSupported(self, ob, action, **kw):
        '''
        Returns a true value if the given action name is supported.
        '''
        return (action in ('submit', 'retract', 'publish', 'reject',))

    security.declarePrivate('doActionFor')
    def doActionFor(self, ob, action, comment=''):
        '''
        Allows the user to request a workflow action.  This method
        must perform its own security checks.
        '''
        allow_review = _checkPermission(ReviewPortalContent, ob)
        allow_request = _checkPermission(RequestReview, ob)
        review_state = self.getReviewStateOf(ob)
        tool = aq_parent(aq_inner(self))

        if action == 'submit':
            if not allow_request:
                raise AccessControl_Unauthorized('Not authorized')
            elif review_state != 'private':
                raise AccessControl_Unauthorized('Already in submit state')
            self.setReviewStateOf(ob, 'pending', action, comment)

        elif action == 'retract':
            if not allow_request:
                raise AccessControl_Unauthorized('Not authorized')
            elif review_state == 'private':
                raise AccessControl_Unauthorized('Already private')
            content_creator = ob.Creator()
            mtool = getUtility(IMembershipTool)
            current_user = mtool.getAuthenticatedMember().getId()
            if (content_creator != current_user) and not allow_review:
                raise AccessControl_Unauthorized('Not creator or reviewer')
            self.setReviewStateOf(ob, 'private', action, comment)

        elif action == 'publish':
            if not allow_review:
                raise AccessControl_Unauthorized('Not authorized')
            self.setReviewStateOf(ob, 'published', action, comment)

        elif action == 'reject':
            if not allow_review:
                raise AccessControl_Unauthorized('Not authorized')
            self.setReviewStateOf(ob, 'private', action, comment)

    security.declarePrivate('isInfoSupported')
    def isInfoSupported(self, ob, name):
        '''
        Returns a true value if the given info name is supported.
        '''
        return (name in ('review_state', 'review_history'))

    security.declarePrivate('getInfoFor')
    def getInfoFor(self, ob, name, default):
        '''
        Allows the user to request information provided by the
        workflow.  This method must perform its own security checks.
        '''
        # Treat this as public.
        if name == 'review_state':
            return self.getReviewStateOf(ob)

        allow_review = _checkPermission(ReviewPortalContent, ob)
        allow_request = _checkPermission(RequestReview, ob)
        if not allow_review and not allow_request:
            return default

        elif name == 'review_history':
            tool = aq_parent(aq_inner(self))
            history = tool.getHistoryOf(self.getId(), ob)
            # Make copies for security.
            return tuple(map(lambda dict: dict.copy(), history))

    security.declarePrivate('setReviewStateOf')
    def setReviewStateOf(self, ob, review_state, action, comment):
        tool = aq_parent(aq_inner(self))
        mtool = getUtility(IMembershipTool)
        current_user = mtool.getAuthenticatedMember().getId()
        status = {
            'actor': current_user,
            'action': action,
            'review_state': review_state,
            'time': DateTime(),
            'comments': comment,
            }
        tool.setStatusOf(self.getId(), ob, status)
        self.updateRoleMappingsFor(ob)

    security.declarePrivate('notifyCreated')
    def notifyCreated(self, ob):
        '''
        Notifies this workflow after an object has been created
        and put in its new place.
        '''
        self.setReviewStateOf( ob, 'private', 'created', '' )
        self.notifySuccess(ob, 'created', '')

    security.declarePrivate('notifyBefore')
    def notifyBefore(self, ob, action):
        '''
        Notifies this workflow of an action before it happens,
        allowing veto by exception.  Unless an exception is thrown, either
        a notifySuccess() or notifyException() can be expected later on.
        The action usually corresponds to a method name.
        '''
        pass

    security.declarePrivate('notifySuccess')
    def notifySuccess(self, ob, action, result):
        '''
        Notifies this workflow that an action has taken place.
        '''
        pass

    security.declarePrivate('notifyException')
    def notifyException(self, ob, action, exc):
        '''
        Notifies this workflow that an action failed.
        '''
        pass

    security.declarePrivate('updateRoleMappingsFor')
    def updateRoleMappingsFor(self, ob):
        '''
        Changes the object permissions according to the current
        review_state.
        '''
        review_state = self.getReviewStateOf(ob)
        if review_state == 'private':
            anon_view = 0
            owner_modify = 1
            reviewer_view = 0
        elif review_state == 'pending':
            anon_view = 0
            owner_modify = 0  # Require a retraction for editing.
            reviewer_view = 1
        elif review_state == 'published':
            anon_view = 1
            owner_modify = 0
            reviewer_view = 1
        else:   # This object is in an unknown state
            anon_view = 0
            owner_modify = 1
            reviewer_view = 0

        # Modify role to permission mappings directly.

        new_map = { View: {'Anonymous': anon_view,
                           'Reviewer': reviewer_view,
                           'Owner': 1}
                  , ModifyPortalContent: {'Owner': owner_modify}
                  }
        return _modifyPermissionMappings(ob, new_map)

InitializeClass(DefaultWorkflowDefinition)
