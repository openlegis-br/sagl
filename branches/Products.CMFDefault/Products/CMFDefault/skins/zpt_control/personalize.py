## Script (Python) "personalize"
##title=Personalization Handler.
##parameters=
REQUEST = context.REQUEST
member = context.portal_membership.getAuthenticatedMember()

failMessage = context.portal_registration.testPropertiesValidity(REQUEST,
                                                                 member)
if failMessage:
    REQUEST.set('portal_status_message', failMessage)
    return context.personalize_form(context, REQUEST,
                                    portal_status_message=failMessage)

member.setProperties(REQUEST)

if 'portal_skin' in REQUEST:
    context.portal_skins.updateSkinCookie()

qs = '/personalize_form?portal_status_message=Member+changed.'

context.REQUEST.RESPONSE.redirect(context.portal_url() + qs)
