#############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
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

import grokcore.annotation.interfaces
import grokcore.component.interfaces
import grokcore.security.interfaces
import grokcore.site.interfaces
import grokcore.view.interfaces
import grokcore.viewlet.interfaces

def api(name):
    from zope.dottedname.resolve import resolve
    from zope.interface import Interface

    try:
        return True, resolve(name)
    except ImportError:
        return False, Interface


HAVE_FORMLIB, IGrokcoreFormlibAPI = api(
    'grokcore.formlib.interfaces.IGrokcoreFormlibAPI')
HAVE_LAYOUT, IGrokcoreLayoutAPI = api(
    'grokcore.layout.interfaces.IGrokcoreLayoutAPI')


class IFiveGrokView(grokcore.view.interfaces.IGrokView):
    """A five.grok view is a specific implementation of a
    grokcore.view.View.
    """


class IFiveGrokAPI(grokcore.annotation.interfaces.IGrokcoreAnnotationAPI,
                   grokcore.component.interfaces.IGrokcoreComponentAPI,
                   grokcore.security.interfaces.IGrokcoreSecurityAPI,
                   grokcore.site.interfaces.IGrokcoreSiteAPI,
                   grokcore.view.interfaces.IGrokcoreViewAPI,
                   grokcore.viewlet.interfaces.IGrokcoreViewletAPI,
                   IGrokcoreFormlibAPI,
                   IGrokcoreLayoutAPI):
    """Official five.grok API.
    """
