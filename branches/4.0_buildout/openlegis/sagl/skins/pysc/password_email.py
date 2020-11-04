## Script (Python) "password_email"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=email='', member=None, password='secret'
##title=
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import makeEmail
from Products.CMFDefault.utils import Message as _

atool = getToolByName(script, 'portal_actions')
ptool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IPropertiesTool')
utool = getToolByName(script, 'portal_url')
portal_url = utool()

options = {}
options['password'] = password

headers = {}
headers['Subject'] = _(u'${portal_title}: Lembrete de senha',
                      mapping={'portal_title': decode(ptool.title(), script)})
headers['From'] = '%s <%s>' % (ptool.getProperty('email_from_name'),
                               ptool.getProperty('email_from_address'))
headers['To'] = '<%s>' % (email)

mtext = context.generico.password_email_template(**decode(options, script))

return makeEmail(mtext, script, headers)

