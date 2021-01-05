##parameters=
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import getBrowserCharset

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool',
                                  # fallback for bootstrap
                                  getToolByName(script, 'portal_actions'))
caltool = getUtilityByInterfaceName('Products.CMFCalendar.interfaces.ICalendarTool', None)
mtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMembershipTool',
                                  # fallback for bootstrap
                                  getToolByName(script, 'portal_membership'))
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool',
                                  # fallback for bootstrap
                                  getToolByName(script, 'portal_url'))
wtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IWorkflowTool',
                                  # fallback for bootstrap
                                  getToolByName(script, 'portal_workflow'))
uidtool = getUtilityByInterfaceName('Products.CMFUid.interfaces.IUniqueIdHandler', None)
syndtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.ISyndicationTool', None)
portal_object = utool.getPortalObject()
isAnon = mtool.isAnonymousUser()
member = mtool.getAuthenticatedMember()

if not 'charset' in (context.REQUEST.RESPONSE.getHeader('content-type') or ''):
    # Some newstyle views set a different charset - don't override it.
    # Oldstyle views need the default_charset.
    default_charset = ptool.getProperty('default_charset', None)
    if default_charset:
        context.REQUEST.RESPONSE.setHeader('content-type',
                                    'text/html; charset=%s' % default_charset)

message = context.REQUEST.get('portal_status_message')
if message and isinstance(message, str):
    # portal_status_message uses always the browser charset.
    message = message.decode(getBrowserCharset(context.REQUEST))

globals = {'utool': utool,
           'mtool': mtool,
           'atool': atool,
           'wtool': wtool,
           'syndtool': syndtool,
           'caltool_installed': caltool is not None,
           'uidtool_installed': uidtool is not None,
           'portal_object': portal_object,
           'portal_title': portal_object.Title(),
           'object_title': context.Title(),
           'object_description': context.Description(),
           'portal_url': utool(),
           'member': member,
           'membername': isAnon and 'Guest' or (member.getProperty('fullname')
                                                or member.getId()),
           'membersfolder': mtool.getMembersFolder(),
           'isAnon': isAnon,
           'wf_state': wtool.getInfoFor(context, 'review_state', ''),
           'show_actionicons': ptool.getProperty('enable_actionicons'),
           'status_message': message,
           'search_form_url': atool.getActionInfo('global/search_form')['url'],
           'search_url': atool.getActionInfo('global/search')['url']}

return decode(globals, context)
