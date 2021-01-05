"""
Testing that grokcore subscribers work under Zope2:

  >>> from five.grok.tests.subscribers import *
  >>> grok.testing.grok('five.grok.tests.subscribers')

You can subscribe to events using the @grok.subscribe decorator:

  >>> from OFS.SimpleItem import SimpleItem
  >>> item = SimpleItem()
  >>> item.id = 'one'
  >>> zope.event.notify(ObjectEvent(item))
  >>> items
  ['one']
  >>> items2
  ['ONE']

The decorated event handling function can also be called directly:

  >>> otheritem = SimpleItem()
  >>> otheritem.id = 'two'
  >>> itemAdded(otheritem,None)
  >>> items
  ['one', 'two']

"""
import zope.event
from five import grok
from zope.component.interfaces import IObjectEvent, ObjectEvent

from OFS.interfaces import ISimpleItem

items = []
items2 = []

@grok.subscribe(ISimpleItem, IObjectEvent)
def itemAdded(item, event):
    items.append(item.getId())

@grok.subscribe(ISimpleItem, IObjectEvent)
def itemAddedInstance(item, event):
    items2.append(item.getId().upper())
