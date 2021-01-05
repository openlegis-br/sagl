##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Discussion item portal type.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from Acquisition import Implicit
from Acquisition import aq_base
from Acquisition import aq_inner
from Acquisition import aq_parent
from AccessControl.class_init import InitializeClass
from DateTime.DateTime import DateTime
from OFS.Traversable import Traversable
from Persistence import Persistent
from Persistence import PersistentMapping
from zope.component import getUtility
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.interfaces import ICallableOpaqueItemEvents
from Products.CMFCore.interfaces import IDiscussable
from Products.CMFCore.interfaces import IDiscussionResponse
from Products.CMFCore.interfaces import IDiscussionTool
from Products.CMFDefault.Document import Document
from Products.CMFDefault.permissions import AccessContentsInformation
from Products.CMFDefault.permissions import ManagePortal
from Products.CMFDefault.permissions import ReplyToItem
from Products.CMFDefault.permissions import View


@implementer(IDiscussionResponse)
class DiscussionItem(Document):

    """ Class for content which is a response to other content.
    """


    meta_type = 'Discussion Item'
    portal_type = 'Discussion Item'
    allow_discussion = 1
    in_reply_to = ''

    security = ClassSecurityInfo()

    security.declareProtected(View, 'listCreators')
    def listCreators(self):
        """ List Dublin Core Creator elements - resource authors.
        """
        if not hasattr(aq_base(self), 'creators'):
            # for content created with CMF versions before 1.5
            if hasattr(aq_base(self), 'creator') and self.creator != 'unknown':
                self.creators = (self.creator,)
            else:
                self.creators = ()
        return self.creators

    #
    #   IDiscussionResponse interface
    #
    security.declareProtected(View, 'inReplyTo')
    def inReplyTo(self, REQUEST=None):
        """ Return the IDiscussable object to which we are a reply.

            Two cases obtain:

              - We are a "top-level" reply to a non-DiscussionItem piece
                of content;  in this case, our 'in_reply_to' field will
                be None.

              - We are a nested reply;  in this case, our 'in_reply_to'
                field will be the ID of the parent DiscussionItem.
        """
        tool = getUtility(IDiscussionTool)
        talkback = tool.getDiscussionFor(self)
        return talkback._getReplyParent(self.in_reply_to)

    security.declarePrivate(View, 'setReplyTo')
    def setReplyTo(self, reply_to):
        """
            Make this object a response to the passed object.
        """
        if getattr(reply_to, 'meta_type', None) == self.meta_type:
            self.in_reply_to = reply_to.getId()
        else:
            self.in_reply_to = ''

    security.declareProtected(View, 'parentsInThread')
    def parentsInThread(self, size=0):
        """
            Return the list of items which are "above" this item in
            the discussion thread.

            If 'size' is not zero, only the closest 'size' parents
            will be returned.
        """
        parents = []
        current = self
        while not size or len(parents) < size:
            parent = current.inReplyTo()
            assert not parent in parents  # sanity check
            parents.insert(0, parent)
            if parent.meta_type != self.meta_type:
                break
            current = parent
        return parents

InitializeClass(DiscussionItem)


@implementer(IDiscussable, ICallableOpaqueItemEvents)
class DiscussionItemContainer(Persistent, Implicit, Traversable):

    """
        Store DiscussionItem objects. Discussable content that
        has DiscussionItems associated with it will have an
        instance of DiscussionItemContainer injected into it to
        hold the discussion threads.
    """


    # for the security machinery to allow traversal
    #__roles__ = None

    security = ClassSecurityInfo()

    def __init__(self):
        self.id = 'talkback'
        self._container = PersistentMapping()

    security.declareProtected(View, 'getId')
    def getId(self):
        return self.id

    security.declareProtected(View, 'getReply')
    def getReply(self, reply_id):
        """
            Return a discussion item, given its ID;  raise KeyError
            if not found.
        """
        return self._container.get(reply_id).__of__(self)

    # Is this right?
    security.declareProtected(View, '__bobo_traverse__')
    def __bobo_traverse__(self, REQUEST, name):
        """
        This will make this container traversable
        """
        target = getattr(self, name, None)
        if target is not None:
            return target

        else:
            try:
                return self.getReply(name)
            except:
                parent = aq_parent(aq_inner(self))
                if parent.getId() == name:
                    return parent
                else:
                    REQUEST.RESPONSE.notFoundError("%s\n%s" % (name, ''))

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container):
        """
            We have juste been added or moved.
            Add the contained items to the catalog.
        """
        if aq_base(container) is not aq_base(self):
            for obj in self.objectValues():
                obj.__of__(self).indexObject()

    security.declarePrivate('manage_afterClone')
    def manage_afterClone(self, item):
        """
            We have just been cloned.
            Notify the workflow about the contained items.
        """
        for obj in self.objectValues():
            obj.__of__(self).notifyWorkflowCreated()

    security.declarePrivate('manage_beforeDelete')
    def manage_beforeDelete(self, item, container):
        """
            Remove the contained items from the catalog.
        """
        if aq_base(container) is not aq_base(self):
            for obj in self.objectValues():
                obj.__of__(self).unindexObject()

    #
    #   OFS.ObjectManager query interface.
    #
    security.declareProtected(AccessContentsInformation, 'objectIds')
    def objectIds(self, spec=None):
        """
            Return a list of the ids of our DiscussionItems.
        """
        if spec and spec is not DiscussionItem.meta_type:
            return []
        return self._container.keys()

    security.declareProtected(AccessContentsInformation, 'objectItems')
    def objectItems(self, spec=None):
        """
            Return a list of (id, subobject) tuples for our DiscussionItems.
        """
        r = []
        a = r.append
        g = self._container.get
        for id in self.objectIds(spec):
            a((id, g(id)))
        return r

    security.declareProtected(AccessContentsInformation, 'objectValues')
    def objectValues(self):
        """
            Return a list of our DiscussionItems.
        """
        return self._container.values()

    #
    #   IDiscussable interface
    #
    security.declareProtected(ReplyToItem, 'createReply')
    def createReply(self, title, text, Creator=None,
                    text_format='structured-text'):
        """
            Create a reply in the proper place
        """
        id = int(DateTime().timeTime())
        while self._container.get(str(id), None) is not None:
            id = id + 1
        id = str(id)

        item = DiscussionItem(id, title=title, description=title)
        self._container[id] = item
        item = item.__of__(self)

        item.setFormat(text_format)
        item._edit(text)
        item.addCreator(Creator)
        item.setReplyTo(self._getDiscussable())

        item.indexObject()
        item.notifyWorkflowCreated()

        return id

    security.declareProtected(ManagePortal, 'deleteReply')
    def deleteReply(self, reply_id):
        """ Remove a reply from this container """
        if reply_id in self._container:
            reply = self._container.get(reply_id).__of__(self)
            my_replies = reply.talkback.getReplies()
            for my_reply in my_replies:
                my_reply_id = my_reply.getId()
                self.deleteReply(my_reply_id)

            if hasattr(reply, 'unindexObject'):
                reply.unindexObject()

            del self._container[reply_id]

    security.declareProtected(View, 'hasReplies')
    def hasReplies(self, content_obj):
        """
            Test to see if there are any dicussion items
        """
        outer = self._getDiscussable(outer=1)
        if content_obj == outer:
            return bool(len(self._container))
        else:
            return bool(len(content_obj.talkback._getReplyResults()))

    security.declareProtected(View, 'replyCount')
    def replyCount(self, content_obj):
        """ How many replies do i have? """
        outer = self._getDiscussable(outer=1)
        if content_obj == outer:
            return len(self._container)
        else:
            replies = content_obj.talkback.getReplies()
            return self._repcount(replies)

    security.declarePrivate('_repcount')
    def _repcount(self, replies):
        """counts the total number of replies

        by recursing thru the various levels
        """
        count = 0

        for reply in replies:
            count = count + 1

            #if there is at least one reply to this reply
            replies = reply.talkback.getReplies()
            if replies:
                count = count + self._repcount(replies)

        return count

    security.declareProtected(View, 'getReplies')
    def getReplies(self):
        """ Return a sequence of the IDiscussionResponse objects which are
            associated with this Discussable
        """
        objects = []
        a = objects.append
        result_ids = self._getReplyResults()

        for id in result_ids:
            a(self._container.get(id).__of__(self))

        return objects

    security.declareProtected(View, 'quotedContents')
    def quotedContents(self):
        """
            Return this object's contents in a form suitable for inclusion
            as a quote in a response.
        """

        return ""

    #
    #   Utility methods
    #
    security.declarePrivate('_getReplyParent')
    def _getReplyParent(self, in_reply_to):
        """
            Return the object indicated by the 'in_reply_to', where
            'None' represents the "outer" content object.
        """
        outer = self._getDiscussable(outer=1)
        if not in_reply_to:
            return outer
        parent = self._container[in_reply_to].__of__(aq_inner(self))
        return parent.__of__(outer)

    security.declarePrivate('_getDiscussable')
    def _getDiscussable(self, outer=0):
        """
        """
        tb = outer and aq_inner(self) or self
        return getattr(tb, 'aq_parent', None)

    security.declarePrivate('_getReplyResults')
    def _getReplyResults(self):
        """
           Get a list of ids of DiscussionItems which are replies to
           our Discussable.
        """
        discussable = self._getDiscussable()
        outer = self._getDiscussable(outer=1)

        if discussable == outer:
            in_reply_to = ''
        else:
            in_reply_to = discussable.getId()

        result = []
        a = result.append
        for key, value in self._container.items():
            if value.in_reply_to == in_reply_to:
                a((key, value))

        result.sort(lambda a, b: cmp(a[1].creation_date, b[1].creation_date))

        return [ x[0] for x in result ]

InitializeClass(DiscussionItemContainer)
