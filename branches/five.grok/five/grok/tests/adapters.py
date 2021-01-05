"""
Testing that grokcore adapters work under Zope2:

  >>> from five.grok.tests.adapters import *
  >>> grok.testing.grok('five.grok.tests.adapters')

  >>> from OFS.SimpleItem import SimpleItem
  >>> item = SimpleItem()
  >>> item.id = 'item'
  >>> adapted = IId(item)
  >>> isinstance(adapted, SimpleItemIdAdapter)
  True
  >>> IId.providedBy(adapted)
  True

  >>> adapted.id()
  'item'

  >>> a = A()
  >>> IB(a)
  'adapted to IB'

"""
from zope.interface import Interface
from five import grok
from OFS.interfaces import ISimpleItem

class IId(Interface):

    def id():
        """Returns the ID of the object"""

class SimpleItemIdAdapter(grok.Adapter):
    grok.implements(IId)
    grok.context(ISimpleItem)

    def id(self):
        return self.context.getId()

class A(object):
    pass

class IB(Interface):
    pass

@grok.adapter(A)
@grok.implementer(IB)
def atob(context):
    return 'adapted to IB'
