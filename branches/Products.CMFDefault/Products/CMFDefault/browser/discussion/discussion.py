from zope.component import getUtility
from zope.interface import Interface
from zope.formlib import form
from zope.schema import TextLine, Text

from Products.CMFCore.interfaces import IDiscussionTool
from Products.CMFDefault.formlib.form import EditFormBase
from Products.CMFDefault.browser.utils import ViewBase
from Products.CMFDefault.utils import Message as _
from Products.PythonScripts.standard import structured_text
from Products.CMFDefault.utils import html_marshal
from Products.CMFDefault.browser.utils import decode, memoize


class View(ViewBase):
    """
    View a comment in the context of a discussion
    """

    @memoize
    @decode
    def text(self):
        return self.context.CookedBody()

    @memoize
    @decode
    def aboveInThread(self):
        """Discussion parent breadcrumbs
        """
        items = [ {'url': parent.getActionInfo('object/view')['url'],
                   'title': parent.Title() or parent.getId()}
                  for parent in self.context.parentsInThread() ]
        return tuple(items)


class IDiscussion(Interface):


    title = TextLine(
        title=_("Subject (Title)")
    )

    text = Text(
        title=_("Reply body")
    )


class Discuss(EditFormBase):
    """
    Discuss an item
    """

    form_fields = form.FormFields(IDiscussion)
    actions = form.Actions(
        form.Action(
            name="add",
            label=_("Add"),
            condition=1,
            validator="validate",
            success="handle_add"
            ),
        form.Action(
            name="edit",
            label=_("Edit"),
            condition=1,
            success="handle_edit",
            ),
        form.Action(
            name="preview",
            label=_("Preview"),
            condition=1,
            success="handle_preview",
            )
    )

    redirect = ("portal_actions", "object/view")

    @property
    @memoize
    def dtool(self):
        return getUtility(IDiscussionTool)

    @property
    def is_preview(self):
        pass

    def handle_add(self, action, data):
        """Create comment and redirect to it"""
        talkback = self.dtool.getDiscussionFor(self.context)
        replyID = talkback.createReply(title=data['title'], text=data['text'])
        reply = talkback.getReply(replyID)

        self.status = _(u"Reply added.")
        self.context.setRedirect(reply, "object/view")

    def handle_preview(self, action, data):
        """Preview comment and allow editing or adding"""
        pass

    def handle_edit(self, action, data):
        """Edit comment before submitting it"""
        pass

    #form = context.REQUEST.form
    #is_preview = False
    #if add and \
            #context.validateHTML(**form) and \
            #context.discussion_reply(**form):
        #return
    #elif preview and \
            #context.validateHTML(**form):
        #is_preview = True


    #options = {}

    #title = form.get('title', context.Title())
    #text = form.get('text', '')
    #options['is_preview'] = is_preview
    #options['title'] = title
    #options['text'] = text
    #options['cooked_text'] = structured_text(text)

    #if is_preview:
        #hidden_vars = [ {'name': n, 'value': v}
                        #for n, v in html_marshal(title=title, text=text) ]
    #else:
        #hidden_vars = []
    #buttons = []
    #target = atool.getActionInfo('object/reply', context)['url']
    #buttons.append( {'name': 'add', 'value': _(u'Add')} )
    #if is_preview:
        #buttons.append( {'name': 'edit', 'value': _(u'Edit')} )
    #else:
        #buttons.append( {'name': 'preview', 'value': _(u'Preview')} )
    #options['form'] = { 'action': target,
                        #'listHiddenVarInfos': tuple(hidden_vars),
                        #'listButtonInfos': tuple(buttons) }

    #return context.discussion_reply_template(**decode(options, script))



class Delete(EditFormBase):
    """
    Delete an item from a discussion
    """

    @property
    @memoize
    def dtool(self):
        return getUtility(IDiscussionTool)

    def __call__(self):
        parent = self.context.inReplyTo()
        talkback = self.dtool.getDiscussionFor(parent)
        talkback.deleteReply(self.context.getId())
        self.status = _(u'Reply deleted.')
        self.context = parent
        self._setRedirect('portal_types', 'object/view')
