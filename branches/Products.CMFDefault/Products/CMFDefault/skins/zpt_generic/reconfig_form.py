##parameters=change=''
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')


form = context.REQUEST.form
if change and \
        context.portal_config_control(**form) and \
        context.setRedirect(atool, 'global/configPortal'):
    return


options = {}

target = atool.getActionInfo('global/configPortal')['url']
buttons = []
buttons.append({'name': 'change', 'value': _(u'Change')})
options['form'] = { 'action': target,
                    'email_from_name': ptool.getProperty('email_from_name'),
                    'email_from_address':
                                      ptool.getProperty('email_from_address'),
                    'smtp_server': ptool.smtp_server(),
                    'title': ptool.title(),
                    'description': ptool.getProperty('description'),
                    'validate_email': ptool.getProperty('validate_email'),
                    'default_charset': ptool.getProperty('default_charset'),
                    'email_charset': ptool.getProperty('email_charset'),
                    'enable_actionicons':
                                      ptool.getProperty('enable_actionicons'),
                    'enable_permalink': ptool.getProperty('enable_permalink'),
                    'listButtonInfos': tuple(buttons) }

return context.reconfig_template(**decode(options, script))
