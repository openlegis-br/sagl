##parameters=change='', change_and_edit='', change_and_view=''
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.utils import decode
from Products.CMFDefault.utils import Message as _

mdtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IMetadataTool')


form = context.REQUEST.form
if change and \
        context.metadata_edit_control(**form) and \
        context.setRedirect(context, 'object/metadata'):
    return
elif change_and_edit and \
        context.metadata_edit_control(**form) and \
        context.setRedirect(context, 'object/edit'):
    return
elif change_and_view and \
        context.metadata_edit_control(**form) and \
        context.setRedirect(context, 'object/view'):
    return


options = {}

allow_discussion = getattr(context, 'allow_discussion', None)
if allow_discussion is not None:
    allow_discussion = bool(allow_discussion)
options['allow_discussion'] = allow_discussion

options['identifier'] = context.Identifier()
options['title'] = form.get('title', context.Title())
options['description'] = form.get('description', context.Description())

subject = form.get('subject', context.Subject())
allowed_subjects = mdtool.listAllowedSubjects(context)
extra_subjects = [ s for s in subject if not s in allowed_subjects ]
options['allowed_subjects'] = tuple(allowed_subjects)
options['extra_subjects'] = tuple(extra_subjects)
options['subject'] = tuple(subject)
options['format'] = form.get('format', context.Format())
options['contributors'] = form.get('contributors', context.Contributors())
options['language'] = form.get('language', context.Language())
options['rights'] = form.get('rights', context.Rights())

buttons = []
target = context.getActionInfo('object/metadata')['url']
buttons.append( {'name': 'change', 'value': _(u'Change')} )
buttons.append( {'name': 'change_and_edit', 'value': _(u'Change and Edit')} )
buttons.append( {'name': 'change_and_view', 'value': _(u'Change and View')} )

options['form'] = { 'action': target,
                    'listButtonInfos': tuple(buttons) }

return context.metadata_edit_template(**decode(options, script))
