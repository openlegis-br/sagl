##parameters=member=None, password='secret'
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
options['password'] = password

headers = {}
headers['Subject'] = _(u'${portal_title}: Membership reminder',
                      mapping={'portal_title': decode(ptool.title(), script)})
headers['From'] = '%s <%s>' % (ptool.getProperty('email_from_name'),
                               ptool.getProperty('email_from_address'))
headers['To'] = '<%s>' % (member and member.getProperty('email') or
                          'foo@example.org')

mtext = context.password_email_template(**decode(options, script))
return makeEmail(mtext, script, headers)
