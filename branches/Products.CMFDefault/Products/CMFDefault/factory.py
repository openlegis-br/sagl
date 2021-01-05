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
""" Configured site factory implementation.
"""

from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from zope.component.hooks import setSite

from Products.CMFCore.interfaces import ISiteRoot
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup import EXTENSION
from Products.GenericSetup import profile_registry
from Products.GenericSetup.tool import SetupTool

from Products.CMFDefault.Portal import CMFSite
from Products.CMFDefault.utils import _wwwdir

_TOOL_ID = 'portal_setup'


def addConfiguredSiteForm(dispatcher):
    """ Wrap the PTF in 'dispatcher', including 'profile_registry' in options.
    """
    wrapped = PageTemplateFile( 'siteAddForm', _wwwdir ).__of__( dispatcher )

    base_profiles = []
    extension_profiles = []
    
    def key(value):
        """Sort function for profiles info"""
        return value.get('title')

    profiles = profile_registry.listProfileInfo(for_=ISiteRoot)
    for info in sorted(profiles, key=key):
        if info.get('type') == EXTENSION:
            extension_profiles.append(info)
        else:
            base_profiles.append(info)

    return wrapped( base_profiles=tuple(base_profiles),
                    extension_profiles =tuple(extension_profiles) )

def addConfiguredSite(dispatcher, site_id, profile_id, snapshot=True,
                      RESPONSE=None, extension_ids=()):
    """ Add a CMFSite to 'dispatcher', configured according to 'profile_id'.
    """
    site = CMFSite( site_id )
    dispatcher._setObject( site_id, site )
    site = dispatcher._getOb( site_id )
    setSite(site)

    site._setObject(_TOOL_ID, SetupTool(_TOOL_ID))
    setup_tool = getToolByName(site, _TOOL_ID)

    setup_tool.setBaselineContext('profile-%s' % profile_id)
    setup_tool.runAllImportStepsFromProfile('profile-%s' % profile_id)
    for extension_id in extension_ids:
        setup_tool.runAllImportStepsFromProfile('profile-%s' % extension_id)

    if snapshot is True:
        setup_tool.createSnapshot( 'initial_configuration' )

    if RESPONSE is not None:
        RESPONSE.redirect( '%s/%s/manage_main?update_menu=1'
                         % (dispatcher.absolute_url(), site_id) )
