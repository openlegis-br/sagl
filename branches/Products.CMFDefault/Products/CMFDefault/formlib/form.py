##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Formlib form base classes.
"""

from datetime import datetime
#from sets import Set

from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
#from Products.Five.browser.decode import processInputs
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import adapts
from zope.component import getUtility
from zope.component.interfaces import IFactory
from zope.container.interfaces import INameChooser
from zope.formlib import form
from zope.formlib.interfaces import IPageForm
from zope.interface import implementsOnly
from zope.interface import implementer
from zope.schema import ASCIILine
from ZPublisher import HTTPRequest
from ZTUtils import make_query

from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.interfaces import ITypeInformation
from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.browser.utils import ViewBase
from Products.CMFDefault.exceptions import AccessControl_Unauthorized
from Products.CMFDefault.exceptions import zExceptions_Unauthorized
from Products.CMFDefault.formlib.widgets import IDInputWidget
from Products.CMFDefault.interfaces import ICMFDefaultSkin
from Products.CMFDefault.permissions import AddPortalContent
from Products.CMFDefault.utils import Message as _
from Products.CMFDefault.utils import translate


class _EditFormMixin(ViewBase):

    template = ViewPageTemplateFile('editform.pt')
    noChangesMessage = _(u'Nothing to change.')
    # disables new behavior of zope.formlib 4.1
    ignoreContext = True

    def _setRedirect(self, provider_id, action_path, keys=''):
        provider = getToolByName(self.context, provider_id)
        try:
            target = provider.getActionInfo(action_path, self.context,
                                            check_condition=1)['url']
        except (ValueError, zExceptions_Unauthorized):
            target = self._getPortalURL()

        kw = {}
        if self.status:
            message = translate(self.status, self.context)
            if isinstance(message, unicode):
                message = message.encode(self._getBrowserCharset())
            kw['portal_status_message'] = message
        for k in keys.split(','):
            k = k.strip()
            v = self.request.form.get(k,
                self.request.form.get('{0}.{1}'.format(self.prefix, k), None))
            if v:
                if isinstance(v, unicode):
                    v = v.encode(self._getBrowserCharset())
                kw[k] = v

        query = kw and '?{0}'.format(make_query(kw)) or ''
        self.request.response.redirect('{0}{1}'.format(target, query))

        return ''

    def update(self):
        # XXX: if we don't set default_encoding explicitly, main_template might
        #      set a different charset
        self.request.response.setHeader('Content-Type',
            'text/html; charset=%s' % HTTPRequest.default_encoding)
        # BBB: for Zope < 2.14
        if not getattr(self.request, 'postProcessInputs', False):
            processInputs(self.request, [HTTPRequest.default_encoding])
        super(_EditFormMixin, self).update()

    def handle_cancel_validate(self, action, data):
        return []

    def handle_failure(self, action, data, errors):
        if self.status:
            message = translate(self.status, self.context)
            self.request.other['portal_status_message'] = message


class EditFormBase(_EditFormMixin, form.PageForm):

    pass


class SettingsEditFormBase(_EditFormMixin, form.PageForm):

    """Base class for editing global settings.
    """

    actions = form.Actions(
        form.Action(
            name='change',
            label=_(u'Change'),
            success='handle_change_success',
            failure='handle_failure'),
        form.Action(
            name='cancel',
            label=_(u'Cancel'),
            validator='handle_cancel_validate',
            success='handle_cancel_success'))

    description = u''
    successMessage = _(u"Settings changed.")

    def getContent(self):
        return self.context

    def setUpWidgets(self, ignore_request=False):
        self.adapters = {}
        self.widgets = form.setUpEditWidgets(
            self.form_fields, self.prefix, self.getContent(), self.request,
            adapters=self.adapters, ignore_request=ignore_request
            )

    def applyChanges(self, data):
        return form.applyData(self.getContent(), self.form_fields, data,
                              self.adapters)

    def _handle_success(self, action, data):
        # normalize set and datetime
        for k, v in data.iteritems():
            if isinstance(v, Set):
                data[k] = set(v)
            elif isinstance(v, datetime) and v.tzinfo:
                # DatetimeWidget returns offset-aware datetime objects
                data[k] = v.replace(tzinfo=None)
        changes = self.applyChanges(data)
        if changes:
            self.status = self.successMessage
        else:
            self.status = self.noChangesMessage
        return changes

@implementer(IPageForm)
class ContentAddFormBase(_EditFormMixin, form.PageAddForm):

    adapts(IFolderish, ICMFDefaultSkin, ITypeInformation)

    security = ClassSecurityInfo()
    security.declareObjectPrivate()

    actions = form.Actions(
        form.Action(
            name='add',
            label=form._('Add'),
            condition=form.haveInputWidgets,
            success='handle_add',
            failure='handle_failure'),
        form.Action(
            name='cancel',
            label=_(u'Cancel'),
            validator='handle_cancel_validate',
            success='handle_cancel_success'))

    def __init__(self, context, request, ti):
        self.context = context
        self.request = request
        self.ti = ti

    security.declareProtected(AddPortalContent, '__call__')
    def __call__(self):
        container = self.context
        portal_type = self.ti.getId()

        # check allowed (sometimes redundant, but better safe than sorry)
        if not self.ti.isConstructionAllowed(container):
            raise AccessControl_Unauthorized('Cannot create %s' % portal_type)

        # check container constraints
        ttool = getUtility(ITypesTool)
        container_ti = ttool.getTypeInfo(container)
        if container_ti is not None and \
                not container_ti.allowType(portal_type):
            raise ValueError('Disallowed subobject type: %s' % portal_type)

        return super(ContentAddFormBase, self).__call__()

    @property
    def label(self):
        obj_type = translate(self.ti.Title(), self.context)
        return _(u'Add ${obj_type}', mapping={'obj_type': obj_type})

    @property
    def description(self):
        return self.ti.Description()

    #same as in form.AddFormBase but without action decorator
    def handle_add(self, action, data):
        self.createAndAdd(data)

    def handle_cancel_success(self, action, data):
        return self._setRedirect('portal_types',
                                 ('object/folderContents', 'object/view'))

    def create(self, data):
        id = data.pop('id', '') or ''
        factory = getUtility(IFactory, self.ti.factory)
        obj = factory(id=id, **data)
        obj._setPortalTypeName(self.ti.getId())
        return obj

    def add(self, obj):
        container = self.context

        name = INameChooser(container).chooseName(obj.getId(), obj)
        obj.id = name
        container._setObject(name, obj)
        obj = container._getOb(name)

        obj_type = translate(obj.Type(), container)
        self.status = _(u'${obj_type} added.', mapping={'obj_type': obj_type})
        self._finished_add = True
        self._added_obj = obj
        return obj

    def nextURL(self):
        obj = self._added_obj

        message = translate(self.status, self.context)
        if isinstance(message, unicode):
            message = message.encode(self._getBrowserCharset())
        return '%s/%s?%s' % (obj.absolute_url(), self.ti.immediate_view,
                             make_query(portal_status_message=message))

InitializeClass(ContentAddFormBase)


class FallbackAddView(ContentAddFormBase):

    """Add view for IDynamicType content.
    """

    form_fields = form.FormFields(ASCIILine(__name__='id', title=_(u'ID')))
    form_fields['id'].custom_widget = IDInputWidget

    def createAndAdd(self, data):
        if not self.ti.product:
            return super(FallbackAddView, self).createAndAdd(data)

        # for portal types with oldstyle factories
        container = self.context
        name = container.invokeFactory(self.ti.getId(), data['id'])
        obj = container._getOb(name)

        obj_type = translate(obj.Type(), container)
        self.status = _(u'${obj_type} added.', mapping={'obj_type': obj_type})
        self._finished_add = True
        self._added_obj = obj
        return obj


class ContentEditFormBase(SettingsEditFormBase):

    actions = form.Actions(
        form.Action(
            name='change',
            label=_(u'Change'),
            validator='handle_validate',
            success='handle_change_success',
            failure='handle_failure'),
        form.Action(
            name='change_and_view',
            label=_(u'Change and View'),
            validator='handle_validate',
            success='handle_change_and_view_success',
            failure='handle_failure'))

    @property
    def label(self):
        obj_type = translate(self.context.Type(), self.context)
        return _(u'Edit ${obj_type}', mapping={'obj_type': obj_type})

    @property
    def successMessage(self):
        obj_type = translate(self.context.Type(), self.context)
        return _(u'${obj_type} changed.', mapping={'obj_type': obj_type})

    def handle_validate(self, action, data):
        if self.context.wl_isLocked():
            return (_(u'This resource is locked via webDAV.'),)
        return self.validate(action, data)

    def applyChanges(self, data):
        changes = super(ContentEditFormBase, self).applyChanges(data)
        # ``changes`` is a dictionary; if empty, there were no changes
        if changes:
            self.context.reindexObject()
        return changes

    def handle_change_success(self, action, data):
        self._handle_success(action, data)
        return self._setRedirect('portal_types', 'object/edit')

    def handle_change_and_view_success(self, action, data):
        self._handle_success(action, data)
        return self._setRedirect('portal_types', 'object/view')


class DisplayFormBase(form.PageDisplayForm, ViewBase):

    template = ViewPageTemplateFile('viewform.pt')

    def getContent(self):
        return self.context

    def setUpWidgets(self, ignore_request=False):
        self.adapters = {}
        self.widgets = form.setUpEditWidgets(
            self.form_fields, self.prefix, self.getContent(), self.request,
            adapters=self.adapters, for_display=True,
            ignore_request=ignore_request
            )

    def update(self):
        # XXX: if we don't set default_encoding explicitly, main_template might
        #      set a different charset
        self.request.response.setHeader('Content-Type',
            'text/html; charset=%s' % HTTPRequest.default_encoding)
        # BBB: for Zope < 2.14
        if not getattr(self.request, 'postProcessInputs', False):
            processInputs(self.request, [HTTPRequest.default_encoding])
        super(DisplayFormBase, self).update()

    @property
    def label(self):
        return self.context.Type()
