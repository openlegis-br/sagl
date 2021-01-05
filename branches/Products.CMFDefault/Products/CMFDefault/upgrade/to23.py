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
"""Upgrade steps to CMFDefault 2.3.
"""

import logging

from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from OFS.userfolder import UserFolder
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError
from zope.dottedname.resolve import resolve

from Products.CMFCore.TypesTool import FactoryTypeInformation
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.context import SetupEnviron
from Products.GenericSetup.interfaces import IBody

_MARKER = object()

def check_cookie_crumbler(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    cctool = getToolByName(tool, 'cookie_authentication', None)
    if cctool is None:
        return False
    cctool = aq_base(cctool)
    for name in ('auto_login_page', 'unauth_page', 'logout_page'):
        if getattr(cctool, name, _MARKER) is not _MARKER:
            return True
    return False

def upgrade_cookie_crumbler(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    cctool = getToolByName(tool, 'cookie_authentication', None)
    if cctool is None:
        return
    cctool = aq_base(cctool)
    for name in ('auto_login_page', 'unauth_page', 'logout_page'):
        if getattr(cctool, name, _MARKER) is not _MARKER:
            delattr(cctool, name)
            logger.info("Cookie crumbler property '%s' removed." % name)

def check_setup_tool(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    registry = tool.getToolsetRegistry()
    try:
        info = registry.getRequiredToolInfo('acl_users')
        if info['class'] == 'AccessControl.User.UserFolder':
            return True
    except KeyError:
        return False
    return False

def upgrade_setup_tool(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    registry = tool.getToolsetRegistry()
    try:
        info = registry.getRequiredToolInfo('acl_users')
        if info['class'] == 'AccessControl.User.UserFolder':
            info['class'] = 'OFS.userfolder.UserFolder'
            tool._p_changed = True
            logger.info("Updated class registered for 'acl_users'.")
    except KeyError:
        return

def check_acl_users(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    from AccessControl.User import UserFolder as OldUserFolder

    portal = aq_parent(aq_inner(tool))
    users = aq_base(portal.acl_users)
    if not getattr(users, '_ofs_migrated', False):
        if users.__class__ is OldUserFolder:
            return True
    return False

def upgrade_acl_users(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    from AccessControl.User import UserFolder as OldUserFolder

    logger = logging.getLogger('GenericSetup.upgrade')
    portal = aq_parent(aq_inner(tool))
    users = aq_base(portal.acl_users)
    if not getattr(users, '_ofs_migrated', False):
        if users.__class__ is OldUserFolder:
            users.__class__ = UserFolder
            users._ofs_migrated = True
            users._p_changed = True
            logger.info("Updated UserFolder class.")

def check_actions_tool(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    atool = getToolByName(tool, 'portal_actions')
    try:
        atool['user']['change_password']
    except KeyError:
        return True
    try:
        atool['global']['members_register']
    except KeyError:
        return True
    try:
        atool['global']['search_form']
    except KeyError:
        return True
    try:
        atool['global']['search']
    except KeyError:
        return True
    try:
        atool['global']['syndication']
    except KeyError:
        return True
    return False

def upgrade_actions_tool(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    atool = getToolByName(tool, 'portal_actions')
    environ = SetupEnviron()
    environ._should_purge = False
    getMultiAdapter((atool, environ), IBody).body = _ACTIONS_PASSWORD_XML
    logger.info("'change_password' action added.")
    getMultiAdapter((atool, environ), IBody).body = _ACTIONS_REGISTER_XML
    logger.info("'members_register' action added.")
    getMultiAdapter((atool, environ), IBody).body = _ACTIONS_SEARCH_FORM_XML
    logger.info("'search_form' action added.")
    getMultiAdapter((atool, environ), IBody).body = _ACTIONS_SEARCH_XML
    logger.info("'search' action added.")
    getMultiAdapter((atool, environ), IBody).body = _ACTIONS_SYNDICATION_XML
    logger.info("'portal syndication settings' action added.")

_ACTIONS_PASSWORD_XML = """\
<?xml version="1.0"?>
<object name="portal_actions" meta_type="CMF Actions Tool"
   xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <object name="user" meta_type="CMF Action Category">
  <object insert-after="join" name="change_password" meta_type="CMF Action"
     i18n:domain="cmf_default">
   <property name="title" i18n:translate="">Change password</property>
   <property name="description"
      i18n:translate="">Change your password</property>
   <property name="url_expr">string:${portal_url}/password_form</property>
   <property name="link_target"></property>
   <property
      name="icon_expr">string:${portal_url}/preferences_icon.png</property>
   <property name="available_expr">member</property>
   <property name="permissions">
    <element value="Set own password"/>
   </property>
   <property name="visible">True</property>
  </object>
 </object>
</object>
"""

_ACTIONS_REGISTER_XML = """\
<object name="portal_actions" meta_type="CMF Actions Tool"
   xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <object name="global" meta_type="CMF Action Category">
  <object name="members_register" meta_type="CMF Action"
     insert-after="manage_members" i18n:domain="cmf_default">
   <property name="title" i18n:translate="">Register a new member</property>
   <property name="description"
      i18n:translate="">Register a new portal member</property>
   <property name="url_expr">string:${portal_url}/join_form</property>
   <property name="link_target"></property>
   <property name="icon_expr">string:${portal_url}/join_icon.png</property>
   <property name="available_expr"></property>
   <property name="permissions">
    <element value="Manage users"/>
   </property>
   <property name="visible">False</property>
  </object>
 </object>
</object>
"""

_ACTIONS_SEARCH_FORM_XML = """\
<object name="portal_actions" meta_type="CMF Actions Tool"
   xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <object name="global" meta_type="CMF Action Category">
  <object insert-after="members_delete" name="search_form"
     meta_type="CMF Action" i18n:domain="cmf_default">
   <property name="title" i18n:translate="">Search Form</property>
   <property name="description" i18n:translate=""></property>
   <property name="url_expr">string:${portal_url}/search_form</property>
   <property name="link_target"></property>
   <property name="icon_expr"></property>
   <property name="available_expr"></property>
   <property name="permissions">
    <element value="View"/>
   </property>
   <property name="visible">False</property>
  </object>
 </object>
</object>
"""

_ACTIONS_SEARCH_XML = """\
<object name="portal_actions" meta_type="CMF Actions Tool"
   xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <object name="global" meta_type="CMF Action Category">
  <object insert-after="search_form" name="search" meta_type="CMF Action"
     i18n:domain="cmf_default">
   <property name="title" i18n:translate="">Search</property>
   <property name="description" i18n:translate=""></property>
   <property name="url_expr">string:${portal_url}/search</property>
   <property name="link_target"></property>
   <property name="icon_expr"></property>
   <property name="available_expr"></property>
   <property name="permissions">
    <element value="View"/>
   </property>
   <property name="visible">False</property>
  </object>
 </object>
</object>
"""

_ACTIONS_SYNDICATION_XML = """\
<object name="portal_actions" meta_type="CMF Actions Tool"
   xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <object name="global" meta_type="CMF Action Category">
  <object name="syndication" meta_type="CMF Action" i18n:domain="cmf_default">
   <property name="title" i18n:translate="">Site Syndication</property>
   <property name="description"
      i18n:translate="">Enable or disable syndication</property>
   <property
      name="url_expr">string:${portal_url}/@@syndication.html</property>
   <property name="link_target"></property>
   <property name="icon_expr">string:${portal_url}/tool_icon.png</property>
   <property name="available_expr"></property>
   <property name="permissions">
    <element value="Manage portal"/>
   </property>
   <property name="visible">True</property>
  </object>
 </object>
</object>
"""

def check_member_data_tool(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    mdtool = getToolByName(tool, 'portal_memberdata')
    listed = mdtool.getProperty('listed')
    if listed == '':
        return True
    login_time = mdtool.getProperty('login_time')
    if login_time == '2000/01/01':
        return True
    last_login_time = mdtool.getProperty('last_login_time')
    if last_login_time == '2000/01/01':
        return True
    if not mdtool.hasProperty('fullname'):
        return True
    for prop_map in mdtool._propertyMap():
        if prop_map['id'] in ('email', 'fullname', 'last_login_time',
                              'listed', 'login_time', 'portal_skin'):
            if 'd' in prop_map.get('mode', 'wd'):
                return True
    return False

def upgrade_member_data_tool(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    mdtool = getToolByName(tool, 'portal_memberdata')
    listed = mdtool.getProperty('listed')
    if listed == '':
        mdtool._updateProperty('listed', '')
        logger.info("Member data tool property 'listed' fixed.")
    login_time = mdtool.getProperty('login_time')
    if login_time == '2000/01/01':
        mdtool._updateProperty('login_time', '2000/01/01')
        logger.info("Member data tool property 'login_time' fixed.")
    last_login_time = mdtool.getProperty('last_login_time')
    if last_login_time == '2000/01/01':
        mdtool._updateProperty('last_login_time', '2000/01/01')
        logger.info("Member data tool property 'last_login_time' fixed.")
    if not mdtool.hasProperty('fullname'):
        prop_map = list(mdtool._properties)
        prop_map.insert(5, {'id': 'fullname', 'type': 'string', 'mode': 'w'})
        mdtool._properties = prop_map
        logger.info("Member data tool property 'fullname' added.")
    for prop_map in mdtool._propertyMap():
        changed = False
        if prop_map['id'] in ('email', 'fullname', 'last_login_time',
                              'listed', 'login_time', 'portal_skin'):
            if 'd' in prop_map.get('mode', 'wd'):
                prop_map['mode'] = 'w'
                changed = True
        if changed:
            mdtool._p_changed = True
            logger.info("Member data tool property modes fixed.")

_TOOL_UTILITIES = (
    ('caching_policy_manager', 'Products.CMFCore.interfaces.ICachingPolicyManager'),
    ('content_type_registry', 'Products.CMFCore.interfaces.IContentTypeRegistry'),
    ('cookie_authentication', 'Products.CMFCore.interfaces.ICookieCrumbler'),
    ('portal_actions', 'Products.CMFCore.interfaces.IActionsTool'),
    ('portal_calendar', 'Products.CMFCalendar.interfaces.ICalendarTool'),
    ('portal_catalog', 'Products.CMFCore.interfaces.ICatalogTool'),
    ('portal_memberdata', 'Products.CMFCore.interfaces.IMemberDataTool'),
    ('portal_membership', 'Products.CMFCore.interfaces.IMembershipTool'),
    ('portal_registration', 'Products.CMFCore.interfaces.IRegistrationTool'),
    ('portal_skins', 'Products.CMFCore.interfaces.ISkinsTool'),
    ('portal_types', 'Products.CMFCore.interfaces.ITypesTool'),
    ('portal_url', 'Products.CMFCore.interfaces.IURLTool'),
    ('portal_workflow', 'Products.CMFCore.interfaces.IWorkflowTool'),
)

def check_root_site_manager(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    portal = aq_parent(aq_inner(tool))
    try:
        sm = portal.getSiteManager()
    except ComponentLookupError:
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
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    portal = aq_parent(aq_inner(tool))
    try:
        sm = portal.getSiteManager()
    except ComponentLookupError:
        logger.warning("Site manager missing.")
        return

    for tool_id, tool_interface in _TOOL_UTILITIES:
        tool_obj = getToolByName(portal, tool_id, default=None)
        try:
            iface = resolve(tool_interface)
        except ImportError:
            continue

        if tool_obj is not None and sm.queryUtility(iface) is None:
            sm.registerUtility(tool_obj, iface)
            logger.info('Registered %s for interface %s' % (tool_id,
                                                            tool_interface))

def DateTime_to_datetime(Zope_DateTime):
    """
    Convert from Zope DateTime to Python datetime and strip timezone
    """
    from DateTime.DateTime import DateTime
    naive = DateTime(str(Zope_DateTime).rsplit(' ', 1)[0])
    return naive.asdatetime()

def change_to_adapter(SyndicationInformation, path=None):
    """
    Read values from the SyndicationInformation object and set them on
    the adapter and then delete the SyndicationInformation object
    """
    from zope.component import getAdapter
    from Products.CMFDefault.SyndicationInfo import ISyndicationInfo
    folder = aq_parent(aq_inner(SyndicationInformation))
    adapter = getAdapter(folder, ISyndicationInfo)
    adapter.period = SyndicationInformation.syUpdatePeriod
    adapter.base = DateTime_to_datetime(SyndicationInformation.syUpdateBase)
    adapter.frequency = SyndicationInformation.syUpdateFrequency
    adapter.max_items = SyndicationInformation.max_items
    if getattr(SyndicationInformation, 'isAllowed', False):
        adapter.enable()
    folder._delObject(SyndicationInformation.getId())

def check_syndication_tool(tool):
    """Convert if portal_syndication exists"""
    portal = aq_parent(aq_inner(tool))
    try:
        syndication = getToolByName(portal, "portal_syndication")
    except AttributeError:
        return False
    infos = portal.ZopeFind(portal,
                            obj_metatypes=["SyndicationInformation"],
                            search_sub=True)
    if infos != []:
        return True

def upgrade_syndication_tool(tool):
    """Replace SyndicatonInformation objects with SyndicationInfo adapters"""
    logger = logging.getLogger('GenericSetup.upgrade')
    portal = aq_parent(aq_inner(tool))
    syndication = getToolByName(portal, "portal_syndication")
    syndication.base = DateTime_to_datetime(syndication.syUpdateBase)
    syndication.enabled = syndication.isAllowed and True or False
    infos = portal.ZopeFindAndApply(portal,
                                    obj_metatypes=["SyndicationInformation"],
                                    search_sub=True,
                                    apply_func=change_to_adapter)
    logger.info("SyndicationTool updated and SyndicationInformation replaced by Annotations")

def check_root_properties(tool):
    """2.3.0-beta to 2.3.0 upgrade step checker
    """
    portal = aq_parent(aq_inner(tool))
    enable_actionicons = portal.getProperty('enable_actionicons')
    if isinstance(enable_actionicons, tuple):
        return True
    return False

def upgrade_root_properties(tool):
    """2.3.0-beta to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    portal = aq_parent(aq_inner(tool))
    enable_actionicons = portal.getProperty('enable_actionicons')
    if isinstance(enable_actionicons, tuple):
        enable_actionicons = bool(enable_actionicons[0])
        portal._updateProperty('enable_actionicons', enable_actionicons)
        logger.info("'enable_actionicons' property fixed.")

_ACTION_URLS = {
    'criteria.html': 'criteria', # CMFTopic
    'discussionitem_view': '',
    'document_edit_form': 'edit',
    'document_view': '',
    'edit.html': 'edit',
    'favorite_view': '',
    'file_edit_form': 'edit',
    'file_view': 'view',
    'folder_edit_form': 'properties',
    'folder_localrole_form': 'share',
    'image_edit_form': 'edit',
    'image_view': 'view',
    'link_edit_form': 'edit',
    'link_view': '',
    'metadata_edit_form': 'properties',
    'newsitem_edit_form': 'edit',
    'newsitem_view': '',
    'properties.html': 'properties',
    'topic_criteria_form': 'criteria', # CMFTopic
    'topic_edit_form': 'properties', # CMFTopic
    'view.html': 'view'}

_ALIASES = {
    'Event': {'(Default)': '@@view', 'edit': '@@edit',
              'view': ''}, # CMFCalendar
    'Topic': {'(Default)': '@@view', 'criteria': '',
              'folder_contents': '@@edit', 'index.html': '@@view',
              'properties': '', 'view': ''}} # CMFTopic

def check_type_infos(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    ttool = getToolByName(tool, 'portal_types')
    for ti in ttool.listTypeInfo():
        immediate_view = ti.getProperty('immediate_view')
        if immediate_view in  _ACTION_URLS:
                return True

        for ai in ti.listActions():
            parts = ai.getActionExpression().rsplit('/')
            if len(parts) < 2:
                continue
            old_name = parts[1]
            if old_name in _ACTION_URLS:
                return True

        ti_id = ti.getId()
        if ti_id in _ALIASES:
            for k, v in _ALIASES[ti_id].iteritems():
                if ti.queryMethodID(k) != v:
                    return True
            icon_expr = ti.getProperty('icon_expr')
            if icon_expr == 'string:${portal_url}/topic_icon.gif':
                return True
    return False

def upgrade_type_infos(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    ttool = getToolByName(tool, 'portal_types')
    for ti in ttool.listTypeInfo():
        changed = False
        immediate_view = ti.getProperty('immediate_view')
        if immediate_view in  _ACTION_URLS:
            ti._setPropValue('immediate_view', _ACTION_URLS[immediate_view])
            changed = True

        for ai in ti.listActions():
            parts = ai.getActionExpression().rsplit('/')
            if len(parts) < 2:
                continue
            old_name = parts[1]
            if old_name in _ACTION_URLS:
                new_name = _ACTION_URLS[old_name] or '(Default)'
                if new_name == '(Default)':
                    ai.setActionExpression(parts[0])
                else:
                    ai.setActionExpression('{0}/{1}'.format(parts[0],
                                                            new_name))
                aliases = ti.getMethodAliases()
                old_value = aliases.pop(old_name, None)
                if old_name.endswith('.html'):
                    old_name = '@@{0}'.format(old_name)
                aliases[new_name] = old_value or old_name
                ti.setMethodAliases(aliases)
                changed = True

        ti_id = ti.getId()
        if ti_id in _ALIASES:
            for k, v in _ALIASES[ti_id].iteritems():
                if ti.queryMethodID(k) != v:
                    aliases = ti.getMethodAliases()
                    aliases[k] = v
                    ti.setMethodAliases(aliases)
                    changed = True
            icon_expr = ti.getProperty('icon_expr')
            if icon_expr == 'string:${portal_url}/topic_icon.gif':
                icon_expr = 'string:${portal_url}/++resource++topic_icon.gif'
                ti._updateProperty('icon_expr', icon_expr)
                changed = True

        if changed:
            logger.info("TypeInfo '%s' changed." % ti.getId())

def check_portal_types(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    ttool = getToolByName(tool, 'portal_types')
    try:
        ttool['Home Folder']
    except KeyError:
        return True
    try:
        ttool['Members Folder']
    except KeyError:
        return True
    return False

def upgrade_portal_types(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    ttool = getToolByName(tool, 'portal_types')
    wtool = getToolByName(tool, 'portal_workflow')
    environ = SetupEnviron()
    environ._should_purge = False
    try:
        ttool['Home Folder']
    except KeyError:
        getMultiAdapter((ttool, environ), IBody).body = _TTOOL_HOME_XML
        obj = ttool['Home Folder']
        getMultiAdapter((obj, environ), IBody).body = _HOME_FOLDER_XML
        getMultiAdapter((wtool, environ), IBody).body = _WTOOL_HOME_XML
        logger.info("'Home Folder' type added.")
    try:
        ttool['Members Folder']
    except KeyError:
        getMultiAdapter((ttool, environ), IBody).body = _TTOOL_MEMBERS_XML
        obj = ttool['Members Folder']
        getMultiAdapter((obj, environ), IBody).body = _MEMBERS_FOLDER_XML
        getMultiAdapter((wtool, environ), IBody).body = _WTOOL_MEMBERS_XML
        logger.info("'Members Folder' type added.")

_TTOOL_HOME_XML = """\
<?xml version="1.0"?>
<object name="portal_types">
 <object insert-after="Folder" name="Home Folder"
    meta_type="Factory-based Type Information"/>
</object>
"""

_HOME_FOLDER_XML = """\
<?xml version="1.0"?>
<object name="Home Folder" meta_type="Factory-based Type Information"
   i18n:domain="cmf_default" xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <property name="title" i18n:translate="">Home Folder</property>
 <property name="description"
    i18n:translate="">A home folder for portal members.</property>
 <property name="icon_expr">string:${portal_url}/folder_icon.gif</property>
 <property name="content_meta_type">Portal Folder</property>
 <property name="product"></property>
 <property name="factory">cmf.folder.home</property>
 <property
    name="add_view_expr">string:${folder_url}/++add++Home%20Folder</property>
 <property name="link_target"></property>
 <property name="immediate_view">properties</property>
 <property name="global_allow">False</property>
 <property name="filter_content_types">False</property>
 <property name="allowed_content_types"/>
 <property name="allow_discussion">False</property>
 <alias from="(Default)" to="index_html"/>
 <alias from="folder_contents" to="@@edit"/>
 <alias from="index.html" to="index_html"/>
 <alias from="view" to="index_html"/>
 <action title="View" action_id="view" category="object" condition_expr=""
    icon_expr="string:${portal_url}/preview_icon.png" link_target=""
    url_expr="string:${object_url}" visible="True">
  <permission value="View"/>
 </action>
 <action title="Edit" action_id="edit" category="object" condition_expr=""
    icon_expr="string:${portal_url}/edit_icon.png" link_target=""
    url_expr="string:${object_url}/properties" visible="True">
  <permission value="Manage properties"/>
 </action>
 <action title="Local Roles" action_id="localroles" category="object"
    condition_expr="" icon_expr="string:${portal_url}/localroles_icon.png"
    link_target="" url_expr="string:${object_url}/share" visible="True">
  <permission value="Change local roles"/>
 </action>
 <action title="Folder contents" action_id="folderContents" category="object"
    condition_expr="" icon_expr="string:${portal_url}/folder_icon.png"
    link_target="" url_expr="string:${object_url}/folder_contents"
    visible="True">
  <permission value="List folder contents"/>
 </action>
</object>
"""

_TTOOL_MEMBERS_XML = """\
<?xml version="1.0"?>
<object name="portal_types">
 <object insert-after="Link" name="Members Folder"
    meta_type="Factory-based Type Information"/>
</object>
"""

_MEMBERS_FOLDER_XML = """\
<?xml version="1.0"?>
<object name="Members Folder" meta_type="Factory-based Type Information"
   i18n:domain="cmf_default" xmlns:i18n="http://xml.zope.org/namespaces/i18n">
 <property name="title" i18n:translate="">Members Folder</property>
 <property name="description"
    i18n:translate="">A container for home folders.</property>
 <property name="icon_expr">string:${portal_url}/folder_icon.gif</property>
 <property name="content_meta_type">Portal Folder</property>
 <property name="product"></property>
 <property name="factory">cmf.folder</property>
 <property
    name="add_view_expr">string:${folder_url}/++add++Members%20Folder</property>
 <property name="link_target"></property>
 <property name="immediate_view">properties</property>
 <property name="global_allow">False</property>
 <property name="filter_content_types">True</property>
 <property name="allowed_content_types">
  <element value="Home Folder"/>
 </property>
 <property name="allow_discussion">False</property>
 <alias from="(Default)" to="@@roster"/>
 <alias from="folder_contents" to="@@edit"/>
 <alias from="index.html" to="@@roster"/>
 <alias from="view" to="@@roster"/>
 <action title="View" action_id="view" category="object" condition_expr=""
    icon_expr="string:${portal_url}/preview_icon.png" link_target=""
    url_expr="string:${object_url}" visible="True">
  <permission value="View"/>
 </action>
 <action title="Edit" action_id="edit" category="object" condition_expr=""
    icon_expr="string:${portal_url}/edit_icon.png" link_target=""
    url_expr="string:${object_url}/properties" visible="True">
  <permission value="Manage properties"/>
 </action>
 <action title="Local Roles" action_id="localroles" category="object"
    condition_expr="" icon_expr="string:${portal_url}/localroles_icon.png"
    link_target="" url_expr="string:${object_url}/share" visible="True">
  <permission value="Change local roles"/>
 </action>
 <action title="Folder contents" action_id="folderContents" category="object"
    condition_expr="" icon_expr="string:${portal_url}/folder_icon.png"
    link_target="" url_expr="string:${object_url}/folder_contents"
    visible="True">
  <permission value="List folder contents"/>
 </action>
</object>
"""

_WTOOL_HOME_XML = """\
<?xml version="1.0"?>
<object name="portal_workflow">
 <bindings>
  <type type_id="Home Folder"/>
 </bindings>
</object>
"""

_WTOOL_MEMBERS_XML = """\
<?xml version="1.0"?>
<object name="portal_workflow">
 <bindings>
  <type type_id="Members Folder"/>
 </bindings>
</object>
"""

def check_member_areas(tool):
    """2.2.x to 2.3.0 upgrade step checker
    """
    mtool = getToolByName(tool, 'portal_membership')
    members = mtool.getMembersFolder()
    if members is None:
        return False
    if 'index_html' in members:
        if members['index_html'].meta_type == 'DTML Method':
            return True
    if members.getPortalTypeName() != 'Members Folder':
        return True
    for f in members.objectValues('Portal Folder'):
        if f.getPortalTypeName() != 'Home Folder':
            return True
    return False

def upgrade_member_areas(tool):
    """2.2.x to 2.3.0 upgrade step handler
    """
    logger = logging.getLogger('GenericSetup.upgrade')
    mtool = getToolByName(tool, 'portal_membership')
    members = mtool.getMembersFolder()
    if members is None:
        return
    if 'index_html' in members:
        if members['index_html'].meta_type == 'DTML Method':
            members._delObject('index_html')
            logger.info("'index_html' method removed from members.")
    if members.getPortalTypeName() != 'Members Folder':
        members._setPortalTypeName('Members Folder')
        logger.info("Portal type of '{0}' fixed.".format(members.getId()))
    for f in members.objectValues('Portal Folder'):
        if f.getPortalTypeName() != 'Home Folder':
            f._setPortalTypeName('Home Folder')
            logger.info("Portal type of '{0}' fixed.".format(f.getId()))
