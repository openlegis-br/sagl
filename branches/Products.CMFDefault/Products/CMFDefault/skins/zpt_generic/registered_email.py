##parameters=member=None, password='secret', email='foo@example.org'
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import makeEmail
from Products.CMFDefault.utils import Message as _

atool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IActionsTool')
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
utool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IURLTool')
portal_url = utool()


options = {}

options['portal_title'] = ptool.title()
options['portal_description'] = ptool.getProperty('description')
options['portal_url'] = portal_url

member_id = member and member.getId() or 'foo'
options['member_id'] = member_id
options['password'] = password

target = atool.getActionInfo('user/login')['url']
options['login_url'] = '%s' % target

email_from_name = ptool.getProperty('email_from_name')
options['signature'] = email_from_name

headers = {}
headers['Subject'] = _(u'${portal_title}: Your Membership Information',
                      mapping={'portal_title': decode(ptool.title(), script)})
headers['From'] = '%s <%s>' % (email_from_name,
                               ptool.getProperty('email_from_address'))
headers['To'] = '<%s>' % email

mtext = context.registered_email_template(**decode(options, script))
return makeEmail(mtext, script, headers)
