#############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from zope import interface
from zope.interface.interfaces import IInterface
from zope.formlib import form
from grokcore.formlib.formlib import interface_seen


FORBIDDEN_PACKAGES = ['OFS.interfaces', 'webdav.interfaces',]


def get_auto_fields(context):
    """Get the form fields for context.
    """
    # for an interface context, we generate them from that interface
    if IInterface.providedBy(context):
        return form.Fields(context)
    # if we have a non-interface context, we're autogenerating them
    # from any schemas defined by the context
    fields = form.Fields(*most_specialized_interfaces(context))
    # we pull in this field by default, but we don't want it in our form
    fields = fields.omit('__name__')
    return fields


AutoFields = get_auto_fields


def most_specialized_interfaces(context):
    """Get interfaces for an object without any duplicates.

    Interfaces in a declaration for an object may already have been seen
    because it is also inherited by another interface. Don't return the
    interface twice, as that would result in duplicate names when creating
    the form.

    Don't return any interface from OFS.interfaces, since they
    contains form fields that we don't want.
    """
    declaration = interface.implementedBy(context)
    seen = []
    for iface in declaration.flattened():
        if interface_is_forbidden(iface):
            continue
        if interface_seen(seen, iface):
            continue
        seen.append(iface)
    return seen


def interface_is_forbidden(iface):
    """Return true if the interface is coming from a Zope 2 one,
    defining bad form fields.
    """
    for bad_name in FORBIDDEN_PACKAGES:
        if iface.__identifier__.startswith(bad_name):
            return True
    return False

