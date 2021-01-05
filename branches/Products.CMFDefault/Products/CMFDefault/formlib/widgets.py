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
"""Custom form widgets."""

from zope.component import adapts
from zope.component import getUtility
from zope.formlib.interfaces import ConversionError
from zope.formlib.interfaces import IInputWidget
from zope.formlib.interfaces import WidgetInputError
from zope.formlib.widget import InputWidget
from zope.formlib.widgets import ASCIIWidget
from zope.formlib.widgets import BrowserWidget
from zope.formlib.widgets import FileWidget
from zope.formlib.widgets import MultiCheckBoxWidget
from zope.formlib.widgets import MultiSelectSetWidget
from zope.formlib.widgets import MultiSelectWidget
from zope.formlib.widgets import RadioWidget
from zope.formlib.widgets import TextAreaWidget
from zope.formlib.widgets import TextWidget
from zope.i18nmessageid import MessageFactory
from zope.interface import implementsOnly
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.schema import Set
from zope.schema import Tuple
from zope.schema.interfaces import ISet
from zope.schema.interfaces import ITuple

from Products.CMFCore.interfaces import IMetadataTool
from Products.CMFDefault.exceptions import IllegalHTML
from Products.CMFDefault.utils import scrubHTML
from Products.CMFDefault.utils import Message as _
from Products.CMFDefault.formlib import schema
#from schema import IEmailLine
#from schema import IFileUpload
from Products.CMFDefault.formlib import vocabulary
#from vocabulary import SimpleVocabulary
from zope.interface import implementer

zope_ = MessageFactory("zope")


# generic widgets

def ChoiceRadioWidget(field, request):
    return RadioWidget(field, field.vocabulary, request)

def ChoiceMultiSelectWidget(field, request):
    return MultiSelectWidget(field, field.value_type.vocabulary, request)

def ChoiceCheckBoxWidget(field, request):
    return MultiCheckBoxWidget(field, field.value_type.vocabulary, request)


@implementer(IInputWidget)
class EmailInputWidget(TextWidget):

    adapts(schema.IEmailLine, IBrowserRequest)

    def _toFieldValue(self, input):
        if input == self._missing:
            return self.context.missing_value

#        try:
#            return str(input.strip())
#        except (AttributeError, UnicodeEncodeError), err:
#            raise ConversionError(_(u'Invalid email address.'), err)


class TextInputWidget(TextAreaWidget):

    def getInputValue(self):
        value = super(TextInputWidget, self).getInputValue()
#        if value:
#            try:
#                value = scrubHTML(value)
#            except IllegalHTML, err:
#                self._error = WidgetInputError(self.context.__name__,
#                                               self.label, err.args[0])
#                raise self._error
        return value


@implementer(IInputWidget)
class TupleTextAreaWidget(TextAreaWidget):

    adapts(ITuple, IBrowserRequest)

    def __init__(self, context, field, request):
        super(TupleTextAreaWidget, self).__init__(context, request)

    def _toFieldValue(self, input):
        input = super(TupleTextAreaWidget, self)._toFieldValue(input)
        if isinstance(input, basestring):
            input = tuple([ l.strip()
                            for l in input.splitlines() if l.strip() ])

        if input == ():
            return self.context.missing_value

        return input

    def _toFormValue(self, value):
        if value is not None:
            value = u'\n'.join(value)
        return super(TupleTextAreaWidget, self)._toFormValue(value)


def TupleInputWidget(field, request):
    return TupleTextAreaWidget(field, field.value_type, request)

@implementer(IInputWidget)
class FileUploadWidget(FileWidget):

    adapts(schema.IFileUpload, IBrowserRequest)

    def _toFieldValue(self, input):
        if not input:
            return self.context.missing_value
#        try:
#            filename = input.filename.split('\\')[-1] # for IE
#            input.filename = filename.strip().replace(' ','_')
#        except AttributeError, e:
#            raise ConversionError(zope_('Form input is not a file object'), e)
        return input

    def hasInput(self):
        return ((self.required and self.name+".used" in self.request.form) or
                self.request.form.get(self.name))


# special widgets

class IDInputWidget(ASCIIWidget):

    def getInputValue(self):
        value = super(IDInputWidget, self).getInputValue()
        if value:
            context = getattr(self.context.context, 'context',
                              self.context.context)
            if not context.checkIdAvailable(value):
                err_msg = _(u'Please choose another ID.')
                self._error = WidgetInputError(self.context.__name__,
                                               self.label, err_msg)
                raise self._error
        return value


@implementer(IInputWidget)
class SubjectInputWidget(InputWidget, BrowserWidget):

    adapts(ISet, IBrowserRequest)

    def __init__(self, context, request):
        super(SubjectInputWidget, self).__init__(context, request)
        self._widgets = {}
        self._widget_keys = (1,)
        self.vocabulary = ()
        context = getattr(self.context.context, 'context',
                          self.context.context)
        mdtool = getUtility(IMetadataTool)
        allowed_subjects = mdtool.listAllowedSubjects(context)
        if allowed_subjects:
            items = [ (str(v), unicode(v), unicode(v))
                      for v in allowed_subjects ]
            self.vocabulary = vocabulary.SimpleVocabulary.fromTitleItems(items)
            self._widget_keys = (0, 1)

    def _getWidget(self, i):
        if i not in self._widgets:
            if i == 0:
                field = Set(__name__='1').bind(self.context)
                widget = MultiSelectSetWidget(field, self.vocabulary,
                                              self.request)
                widget.setPrefix(self.name)
                widget.empty_marker_name = widget.name + "-empty-marker"
                widget.size = 3
                self._widgets[0] = widget
            elif i == 1:
                field = Tuple(__name__='', required=False).bind(self.context)
                widget = TupleInputWidget(field, self.request)
                widget.name = self.name
                widget.height = self.vocabulary and 2 or 6
                self._widgets[1] = widget
        return self._widgets[i]

    def getInputValue(self):
        value = set()
        for k in self._widget_keys:
            value = set(self._getWidget(k).getInputValue() or ())|value
        return value

    def hasInput(self):
        value = False
        for k in self._widget_keys:
            value = self._getWidget(k).hasInput() or value
        return value

    def __call__(self):
        values = {0: [], 1: []}
        if not self._renderedValueSet():
            value = self.getInputValue()
        else:
            value = self._data
        for item in value or ():
            if item in self.vocabulary:
                values[0].append(item)
            else:
                values[1].append(item)
        for k in self._widget_keys:
            self._getWidget(k).setRenderedValue(set(values[k]))
        return '\n'.join([ self._getWidget(k)() for k in self._widget_keys ])
