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
"""Workflow forms.
"""

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from zope.formlib import form
from zope.interface import Interface
from zope.schema import Text

from Products.CMFCore.interfaces import IWorkflowTool
from Products.CMFDefault.browser.utils import memoize
from Products.CMFDefault.exceptions import WorkflowException
from Products.CMFDefault.formlib.form import EditFormBase
from Products.CMFDefault.utils import Message as _

STATUS = {'submit': _(u"Item submitted for review."),
          'publish': _(u"Item was published."),
          'retract': _(u"Item was retracted."),
          'reject': _(u"Item was rejected."),
          'hide': _("Item was hidden."),
          'show': _("Item is now visible.")
         }


class IWorkflowSchema(Interface):

    comment = Text(
                title=u"comments",
                required=False
                )


class Submit(EditFormBase):

    """Submit an item for review"""

    template = ViewPageTemplateFile("submit.pt")
    form_fields = form.FormFields(IWorkflowSchema)
    actions = form.Actions(
        form.Action(
            name="submit",
            label=_(u"Submit item"),
            success='handle_workflow',
            failure='handle_failure'
            )
        )

    @property
    @memoize
    def workflow(self):
        return getUtility(IWorkflowTool)

    def handle_workflow(self, action, data):
         pass
#        try:
#            self.workflow.doActionFor(self.context, action.name,
#                                      comment=data['comment'])
#            self.status = STATUS.get(action.name, _(u"Status changed."))
#            self._setRedirect('portal_types', 'object/view')
#        except WorkflowException, errmsg:
#            self.status = errmsg
#            self._setRedirect('portal_actions', 'object/edit')


class Publish(Submit):

    """Publish an item"""

    template = ViewPageTemplateFile("publish.pt")
    form_fields = form.FormFields(IWorkflowSchema)
    actions = form.Actions(
        form.Action(
            name="publish",
            label=_(u"Publish this item"),
            success='handle_workflow',
            failure='handle_failure'
            )
        )


class Retract(Submit):

    """Remove a published object"""

    template = ViewPageTemplateFile("retract.pt")
    form_fields = form.FormFields(IWorkflowSchema)
    actions = form.Actions(
        form.Action(
            name="retract",
            label=_(u"Retract this item"),
            success='handle_workflow',
            failure='handle_failure'
            )
        )


class Reject(Submit):

    """Reject an item submitted for publication"""

    template = ViewPageTemplateFile("reject.pt")
    form_fields = form.FormFields(IWorkflowSchema)
    actions = form.Actions(
        form.Action(
            name="reject",
            label=_(u"Reject this item"),
            success='handle_workflow',
            failure='handle_failure'
            )
        )

class Hide(Submit):

    """Hide a published item"""

    template = ViewPageTemplateFile("hide.pt")
    form_fields = form.FormFields(IWorkflowSchema)
    actions = form.Actions(
        form.Action(
            name="hide",
            label=_(u"Hide this item"),
            success='handle_workflow',
            failure='handle_failure'
            )
        )

class Show(Submit):

    """Reveal a hidden item"""

    template = ViewPageTemplateFile("show.pt")
    form_fields = form.FormFields(IWorkflowSchema)
    actions = form.Actions(
        form.Action(
            name="show",
            label=_(u"Show this item"),
            success='handle_workflow',
            failure='handle_failure'
            )
        )
