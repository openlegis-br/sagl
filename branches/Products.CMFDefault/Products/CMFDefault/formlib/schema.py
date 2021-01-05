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
"""Formlib schema fields and schema adapter base classes.

SchemaAdapterBase and ProxyFieldProperty are legacy code. They should only be
used to adapt old content types that can't handle unicode and datetime
correctly.
"""

from datetime import datetime

from DateTime.DateTime import DateTime
from OFS.Image import Pdata
from zope.component import getUtility
from zope.interface import implements
from zope.publisher.browser import FileUpload as ztkFileUpload
from zope.schema import BytesLine
from zope.schema import Field
from zope.schema.interfaces import IBytes
from zope.schema.interfaces import IBytesLine
from ZPublisher.HTTPRequest import FileUpload as z2FileUpload

from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.utils import checkEmailAddress

from zope.interface import implementer

class SchemaAdapterBase(object):

    def __init__(self, context):
        self.context = context
        ptool = getUtility(IPropertiesTool)
        self.encoding = ptool.getProperty('default_charset', None)


_marker = object()

class ProxyFieldProperty(object):

    """Computed attributes based on schema fields.

    Based on zope.schema.fieldproperty.FieldProperty.
    """

    def __init__(self, field, get_name=None, set_name=None):
        if get_name is None:
            get_name = field.__name__

        self._field = field
        self._get_name = get_name
        self._set_name = set_name

    def __get__(self, inst, cls=None):
        if inst is None:
            return self

        attribute = getattr(inst.context, self._get_name, _marker)
        if attribute is _marker:
            field = self._field.bind(inst)
            attribute = getattr(field, 'default', _marker)
            if attribute is _marker:
                raise AttributeError(self._field.__name__)
        elif isinstance(attribute, Pdata):
            attribute = str(attribute)
        elif callable(attribute):
            attribute = attribute()

        if self._field._type == str:
            return attribute
        if isinstance(self._field, FileUpload):
            return attribute
        if isinstance(attribute, str) and inst.encoding:
            return attribute.decode(inst.encoding)
        if isinstance(attribute, DateTime):
            return attribute.asdatetime().replace(tzinfo=None)
        if isinstance(attribute, (tuple, list)):
            if inst.encoding:
                attribute = [ isinstance(v, str)
                              and v.decode(inst.encoding) or v
                              for v in attribute ]
            if self._field._type == list:
                return attribute
            if self._field._type == tuple:
                return tuple(attribute)
            return set(attribute)
        return attribute

    def __set__(self, inst, value):
        field = self._field.bind(inst)
        field.validate(value)
        if field.readonly:
            raise ValueError(self._field.__name__, 'field is readonly')
        if isinstance(value, unicode) and inst.encoding:
            value = value.encode(inst.encoding)
        elif isinstance(value, datetime):
            value = DateTime(value)
        elif isinstance(value, (set, tuple, list)):
            if inst.encoding:
                value = [ isinstance(v, unicode)
                          and v.encode(inst.encoding) or v
                          for v in value ]
            if not self._field._type == list:
                value = tuple(value)
        if self._set_name:
            getattr(inst.context, self._set_name)(value)
        elif inst.context.hasProperty(self._get_name):
            inst.context._updateProperty(self._get_name, value)
        else:
            setattr(inst.context, self._get_name, value)

    def __getattr__(self, name):
        return getattr(self._field, name)


class IEmailLine(IBytesLine):

    """A field containing an email address.
    """

@implementer(IEmailLine)
class EmailLine(BytesLine):

    """Email schema field.
    """

    default = ''
    missing_value = ''

    def _validate(self, value):
        super(EmailLine, self)._validate(value)
        checkEmailAddress(value)
        return True


class IFileUpload(IBytes):

    """A special bytes field for file uploads.

    This is a hack that allows to use the existing manage_upload code for
    handling FileUpload objects. Might become obsolete in the long run.
    """

@implementer(IFileUpload)
class FileUpload(Field):

    """File upload form field.
    """


    _type = ztkFileUpload, z2FileUpload, str
