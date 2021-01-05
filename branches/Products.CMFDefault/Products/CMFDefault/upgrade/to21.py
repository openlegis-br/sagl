##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Upgrade steps to CMFDefault 2.1.
"""

import logging

from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from five.localsitemanager import find_next_sitemanager
from five.localsitemanager.registry import FiveVerifyingAdapterLookup
from five.localsitemanager.registry import PersistentComponents
from zope.component import getMultiAdapter
from zope.component.globalregistry import base
from zope.component.hooks import setSite
from zope.interface.interfaces import ComponentLookupError
from zope.dottedname.resolve import resolve

from Products.CMFCore.DirectoryView import _dirreg
from Products.CMFCore.DirectoryView import _generateKey
from Products.CMFCore.interfaces import IDirectoryView
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.context import SetupEnviron
from Products.GenericSetup.interfaces import IBody

_COMPONENTS_XML = """\
<?xml version="1.0"?>
<componentregistry>
 <adapters/>
 <utilities>
  <utility interface="Products.CMFCore.interfaces.IDiscussionTool"
     object="portal_discussion"/>
  <utility interface="Products.CMFCore.interfaces.IMetadataTool"
     object="portal_metadata"/>
  <utility interface="Products.CMFCore.interfaces.IPropertiesTool"
     object="portal_properties"/>
  <utility interface="Products.CMFCore.interfaces.ISiteRoot" object=""/>
  <utility interface="Products.CMFCore.interfaces.ISyndicationTool"
     object="portal_syndication"/>
  <utility interface="Products.CMFCore.interfaces.IUndoTool"
     object="portal_undo"/>
  <utility interface="Products.GenericSetup.interfaces.ISetupTool"
     object="portal_setup"/>
  <utility interface="Products.MailHost.interfaces.IMailHost"
     object="MailHost"/>
 </utilities>
</componentregistry>
"""

_ACTIONS_XML = """\
<?xml version="1.0"?>
<object name="portal_actions" meta_type="CMF Actions Tool"
   xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <object name="object" meta_type="CMF Action Category">
  <object name="interfaces" meta_type="CMF Action" i18n:domain="cmf_default">
   <property name="title" i18n:translate="">Interfaces</property>
   <property name="description"
      i18n:translate="">Assign marker interfaces</property>
   <property name="url_expr">string:${object_url}/edit-markers.html</property>
   <property name="link_target"></property>
   <property
      name="icon_expr">string:${portal_url}/interfaces_icon.png</property>
   <property name="available_expr"></property>
   <property name="permissions">
    <element value="Manage portal"/>
   </property>
   <property name="visible">True</property>
  </object>
 </object>
</object>
"""

_BAD_UTILITIES = [
         'Products.CMFCalendar.interfaces.ICalendarTool',
         'Products.CMFCore.interfaces.IActionsTool',
         'Products.CMFCore.interfaces.ICatalogTool',
         'Products.CMFCore.interfaces.IContentTypeRegistry',
         'Products.CMFCore.interfaces.ISkinsTool',
         'Products.CMFCore.interfaces.ITypesTool',
         'Products.CMFCore.interfaces.IURLTool',
         'Products.CMFCore.interfaces.IConfigurableWorkflowTool',
         'Products.CMFCore.interfaces.IMembershipTool',
         'Products.CMFCore.interfaces.IRegistrationTool',
         ]

_TOOL_UTILITIES = (
    ('portal_uidgenerator', 'Products.CMFUid.interfaces.IUniqueIdGenerator'),
    ('portal_uidannotation', 'Products.CMFUid.interfaces.IUniqueIdAnnotationManagement'),
    ('portal_uidhandler', 'Products.CMFUid.interfaces.IUniqueIdHandler'),
    ('portal_actionicons', 'Products.CMFActionIcons.interfaces.IActionIconsTool'),
)

def check_root_site_manager(tool):
    """2.0.x to 2.1.0 upgrade step checker
    """
    portal = aq_parent(aq_inner(tool))
    try:
        # We have to call setSite to make sure we have a site with a proper
        # acquisition context.
        setSite(portal)
        sm = portal.getSiteManager()
        if sm.utilities.LookupClass != FiveVerifyingAdapterLookup:
            return True
    except ComponentLookupError:
        return True

    for tool_interface in _BAD_UTILITIES:
        try:
            iface = resolve(tool_interface)
        except ImportError:
            continue

        if sm.queryUtility(iface) is not None:
            return True

    for tool_id, tool_interface in _TOOL_UTILITIES:
        tool_obj = getToolByName(portal, tool_id, default=None)
        try:
            iface = resolve(tool_interface)
        except ImportError:
            continue

        if tool_obj is not None and sm.queryUtility(iface) is None:
            return True

    return False

def upgrade_root_site_manager(tool):
    """2.0.x to 2.1.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    portal = aq_parent(aq_inner(tool))
    try:
        setSite(portal)
        sm = portal.getSiteManager()
        if sm.utilities.LookupClass != FiveVerifyingAdapterLookup:
            sm.__parent__ = aq_base(portal)
            sm.utilities.LookupClass = FiveVerifyingAdapterLookup
            sm.utilities._createLookup()
            sm.utilities.__parent__ = sm
            logger.info('LookupClass replaced.')
        else:
            for tool_interface in _BAD_UTILITIES:
                try:
                    iface = resolve(tool_interface)
                except ImportError:
                    continue

                if sm.queryUtility(iface) is not None:
                    sm.unregisterUtility(provided=iface)
                    logger.info('Unregistered utility for %s' % tool_interface)

            for tool_id, tool_interface in _TOOL_UTILITIES:
                tool_obj = getToolByName(portal, tool_id, default=None)
                try:
                    iface = resolve(tool_interface)
                except ImportError:
                    continue

                if tool_obj is not None and sm.queryUtility(iface) is None:
                    sm.registerUtility(tool_obj, iface)
                    logger.info('Registered %s for interface %s' % (
                                                      tool_id, tool_interface))
            return
    except ComponentLookupError:
        next = find_next_sitemanager(portal)
        if next is None:
            next = base
        name = '/'.join(portal.getPhysicalPath())
        sm = PersistentComponents(name, (next,))
        sm.__parent__ = aq_base(portal)
        portal.setSiteManager(sm)
        logger.info("Site manager '%s' added." % name)
    getMultiAdapter((sm, SetupEnviron()), IBody).body = _COMPONENTS_XML
    logger.info('Utility registrations added.')

def check_root_properties(tool):
    """2.0.x to 2.1.0 upgrade step checker
    """
    portal = aq_parent(aq_inner(tool))
    return not portal.hasProperty('email_charset')

def upgrade_root_properties(tool):
    """2.0.x to 2.1.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    portal = aq_parent(aq_inner(tool))
    portal.manage_addProperty('email_charset', 'iso-8859-1', 'string')
    prop_map = list(portal._properties)
    for i in range(len(prop_map)):
        if prop_map[i]['id'] == 'default_charset':
            email_charset_info = prop_map.pop(-1)
            prop_map.insert(i+1, email_charset_info)
            portal._properties = tuple(prop_map)
            break
    logger.info("'email_charset' property added.")

_FACTORIES = {
    'CMFCore-manage_addPortalFolder': 'cmf.folder',
    'CMFCore-manage_addCMFBTreeFolder': 'cmf.folder.btree',
    'CMFDefault-addDocument': 'cmf.document',
    'CMFDefault-addFavorite': 'cmf.favorite',
    'CMFDefault-addFile': 'cmf.file',
    'CMFDefault-addImage': 'cmf.image',
    'CMFDefault-addLink': 'cmf.link',
    'CMFDefault-addNewsItem': 'cmf.newsitem'}

def check_type_properties(tool):
    """2.0.x to 2.1.0 upgrade step checker
    """
    ttool = getToolByName(tool, 'portal_types')
    for ti in ttool.listTypeInfo():
        key = '%s-%s' % (ti.getProperty('product'), ti.getProperty('factory'))
        if key in _FACTORIES:
            return True
    return False

def upgrade_type_properties(tool):
    """2.0.x to 2.1.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    ttool = getToolByName(tool, 'portal_types')
    for ti in ttool.listTypeInfo():
        key = '%s-%s' % (ti.getProperty('product'), ti.getProperty('factory'))
        if key in _FACTORIES:
            ti._updateProperty('product', '')
            ti._updateProperty('factory', _FACTORIES[key])
            logger.info("TypeInfo '%s' changed." % ti.getId())

def check_actions_tool(tool):
    """2.0.x to 2.1.0 upgrade step checker
    """
    atool = getToolByName(tool, 'portal_actions')
    try:
        atool.object.interfaces
    except AttributeError:
        return True
    return False

def upgrade_actions_tool(tool):
    """2.0.x to 2.1.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    atool = getToolByName(tool, 'portal_actions')
    environ = SetupEnviron()
    environ._should_purge = False
    getMultiAdapter((atool, environ), IBody).body = _ACTIONS_XML
    logger.info("'interfaces' action added.")

def check_skins_tool(tool):
    """2.0.x to 2.1.0 upgrade step checker
    """
    stool = getToolByName(tool, 'portal_skins', None)
    if stool is None:
        return False
    for obj in stool.objectValues():
        if IDirectoryView.providedBy(obj):
            dirpath = obj.getDirPath()
            if dirpath is None:
                continue
            if dirpath not in _dirreg.listDirectories():
                return True
    return False

def _getCurrentKeyFormat(reg_key):
    dirpath = reg_key.replace('\\', '/')
    if dirpath.startswith('Products/'):
        dirpath = dirpath[9:]
    product = ['Products']
    dirparts = dirpath.split('/')
    while dirparts:
        product.append(dirparts[0])
        dirparts = dirparts[1:]
        possible_key = _generateKey('.'.join(product), '/'.join(dirparts))
        if possible_key in _dirreg._directories:
            return possible_key
    return reg_key

def upgrade_skins_tool(tool):
    """2.0.x to 2.1.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    stool = getToolByName(tool, 'portal_skins', None)
    if stool is None:
        return
    for obj in stool.objectValues():
        if IDirectoryView.providedBy(obj):
            dirpath = obj.getDirPath()
            if dirpath is None:
                continue
            if dirpath not in _dirreg.listDirectories():
                obj._dirpath = _getCurrentKeyFormat(dirpath)
                logger.info("DirectoryView '%s' changed." % obj.getId())
