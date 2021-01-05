##parameters=allow_discussion, title=None, subject=None, description=None, contributors=None, effective_date=None, expiration_date=None, format=None, language=None, rights=None, **kw
##
from Products.CMFCore.utils import getUtilityByInterfaceName
from Products.CMFDefault.exceptions import ResourceLockedError
from Products.CMFDefault.utils import Message as _

dtool = getUtilityByInterfaceName('Products.CMFCore.interfaces.IDiscussionTool')

def tuplify( value ):

    if not same_type( value, () ):
        value = tuple( value )

    temp = filter( None, value )
    return tuple( temp )

if title is None:
    title = context.Title()

if subject is None:
    subject = context.Subject()
else:
    subject = tuplify( subject )

if description is None:
    description = context.Description()

if contributors is None:
    contributors = context.Contributors()
else:
    contributors = tuplify( contributors )

if effective_date is None:
    effective_date = context.EffectiveDate()

if expiration_date is None:
    expiration_date = context.expires()

if format is None:
    format = context.Format()

if language is None:
    language = context.Language()

if rights is None:
    rights = context.Rights()

if allow_discussion == 'default':
    allow_discussion = None
elif allow_discussion == 'off':
    allow_discussion = False
elif allow_discussion == 'on':
    allow_discussion = True
dtool.overrideDiscussionFor(context, allow_discussion)

try:
    context.editMetadata( title=title
                        , description=description
                        , subject=subject
                        , contributors=contributors
                        , effective_date=effective_date
                        , expiration_date=expiration_date
                        , format=format
                        , language=language
                        , rights=rights
                        )
    return context.setStatus(True, _(u'Metadata changed.'))
except ResourceLockedError, errmsg:
    return context.setStatus(False, errmsg)
