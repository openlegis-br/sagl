five.grok
=========

Overview
--------

This package is meant to provide all the grok functionalities into
Zope 2.

How-to
------

This text explains you how to use grok constructs in Zope 2.

    <<< from five import grok
    <<< from OFS.ObjectManager import ObjectManager
    <<< from OFS.SimpleItem import Item

Let's make a Folder as a base class...

    <<< class SimpleFolder(ObjectManager, Item):
    ...     def __init__(self, id=None):
    ...         if id is not None:
    ...             self.id = str(id)

and use it to define our own business object.

    <<< class GrokVillage(SimpleFolder):
    ...
    ...     def addCave(self, id):
    ...         cave = Cave(id)
    ...         self._setObject(id, cave)
    ...         return cave

This class can be used by application code :
Let's instantiate a village and store it in ZODB root.

    >>> from zope.component import getUtility
    >>> from five.grok.README import *
    >>> app = getRootFolder()
    >>> request = app.REQUEST

    >>> village = GrokVillage(id='amsterdam')
    >>> app._setObject('amsterdam', village)
    'amsterdam'
    >>> village = getattr(app, 'amsterdam') # get it back wrapped

Let's define a filesystem directory that will hold the templates
that grok will use with our views.

    <<< grok.templatedir('readme_templates')

Let's create a view on the GrokVillage.

    <<< class GrokVillageView(grok.View):
    ...     grok.context(GrokVillage)
    ...
    ...     def getCaves(self):
    ...         cavesInfos = []
    ...         for cave in self.context.objectValues():
    ...             caveInfo = dict(id=cave.id, caveWomen=cave.numberOfCaveWomen())
    ...             cavesInfos.append(caveInfo)
    ...         return cavesInfos


Views
`````

The example above uses a filesystem template. We can also use inline
templates, like this:

    <<< class InlineGrokVillage(grok.View):
    ...     grok.context(GrokVillage)
    ...     grok.name('inline')

    <<< inlinegrokvillage = grok.PageTemplate(u'Village: <b tal:content="here/id"></b>')

Or, we could specify the ``render()`` method explicitly:

    <<< class Cave(SimpleFolder):
    ...
    ...     def numberOfCaveWomen(self):
    ...         return len(self.objectIds())

    <<< class CaveView(grok.View):
    ...     grok.context(Cave)
    ...
    ...     def render(self):
    ...         return 'This is the %s cave, there is %s cavewomen in this cave.' %\
    ...                                 (self.context.id,
    ...                                  self.context.numberOfCaveWomen())

Let's create an add view, and a new content ``CaveWoman``. You can
provide some actual code in the ``update()`` method which is called
before ``render()``::

    <<< class AddCaveWoman(grok.View):
    ...     grok.context(Cave)
    ...     grok.name(u'cave-woman-add')
    ...
    ...     def render(self):
    ...         return 'Add a Cave Woman ...'
    ...
    ...     def update(self, id=None, name=None,
    ...                age=None, hairType=None, size=0,
    ...                weight=0):
    ...         self.context._setObject(id, CaveWoman(name, age, hairType,
    ...                                               size, weight))

A ``CaveWoman`` is defined using an interface::

    <<< from zope.interface import Interface
    <<< from zope import schema

    <<< class ICaveWoman(Interface):
    ...     name = schema.TextLine(title=u"Name")
    ...     age = schema.Int(title=u"Age")
    ...     hairType = schema.TextLine(title=u"Hair Type")
    ...     size = schema.Int(title=u"Size")
    ...     weight = schema.Int(title=u"Weight")

    <<< class CaveWoman(grok.Model):
    ...     grok.implements(ICaveWoman)
    ...
    ...     def __init__(self, name, age, hairType, size,
    ...                  weight):
    ...         self.name = name
    ...         self.age = age
    ...         self.hairType = hairType
    ...         self.size = size
    ...         self.weight = weight


Forms
`````

We are going to define a display form for a ``CaveWoman``, it's going
to be the default view::

    <<< class Index(grok.DisplayForm):
    ...     grok.context(CaveWoman)

And the same way an edition form::

    <<< class Edit(grok.EditForm):
    ...     grok.context(CaveWoman)


We can even create custom forms::

    <<< class ISearchWoman(Interface):
    ...     name = schema.TextLine(title=u"Woman to search")

    <<< class Search(grok.Form):
    ...     grok.context(Cave)
    ...
    ...     form_fields = grok.Fields(ISearchWoman)
    ...
    ...     def update(self):
    ...         # Default search results
    ...         self.results = []
    ...
    ...     @grok.action(u"Search")
    ...     def search(self, name):
    ...         # Stupid not efficient search
    ...         for cave in self.context.objectValues():
    ...             if cave.id.startswith(name):
    ...                 self.results.append(cave)

Adapters
````````

Now, we can create an adapter for our new ``CaveWoman`` content which
is going to give information her facebook profile::

    <<< class ICaveWomanSummarizer(Interface):
    ...
    ...     def info():
    ...         """
    ...         return filtered informations
    ...         """

    <<< class CaveWomanFaceBookProfile(grok.Adapter):
    ...     grok.context(CaveWoman)
    ...     grok.provides(ICaveWomanSummarizer)
    ...
    ...     def info(self):
    ...         return {'hair': self.context.hairType,
    ...                 'weight': self.context.weight,
    ...                 'size': self.context.size}


Global utility
``````````````

We can create a local utility. When a ``CaveWoman`` is added, we can
lookup our utility and use it::

    <<< from zope.container.interfaces import IObjectAddedEvent
    <<< from zope.component import getUtility

    <<< class ICaveInformations(Interface):
    ...
    ...     def getHairStatistics(cave):
    ...         """
    ...         return the statistics about the cavewoman's hair in the cave
    ...         """

    <<< class CaveInformations(grok.GlobalUtility):
    ...     grok.implements(ICaveInformations)
    ...     grok.provides(ICaveInformations)
    ...
    ...     def getHairStatistics(self, cave):
    ...         browns = 0
    ...         blonds = 0
    ...         for caveWoman in cave.objectValues():
    ...             if caveWoman.hairType == 'blond':
    ...                 blonds += 1
    ...             elif caveWoman.hairType == 'brown':
    ...                 browns += 1
    ...         return blonds, browns

    <<< from Acquisition import aq_parent
    <<< @grok.subscribe(CaveWoman, IObjectAddedEvent)
    ... def handle(obj, event):
    ...     profile = ICaveWomanSummarizer(obj)
    ...     caveInfos = getUtility(ICaveInformations)
    ...     village = aq_parent(obj)
    ...     nbrOfBlond, nbrOfBrown = caveInfos.getHairStatistics(village)
    ...     if nbrOfBlond >= nbrOfBrown:
    ...         obj.hairType = 'brown'
    ...     else:
    ...         obj.hairType = 'blond'
    ...     print """Hey caveman there is a new cavewoman in the cave, here
    ... are the most important informations about her:
    ...  * Hair Type: %(hair)s
    ...  * Weight: %(weight)s
    ...  * Size: %(size)s""" % profile.info()


Test
````

And finally we can test all created components::

    >>> from zope.component import queryMultiAdapter

    >>> martijnCave = village.addCave('martijn-cave')
    >>> belgianCave = village.addCave('belgian-cave')
    >>> queryMultiAdapter((martijnCave, request), name='caveview')()
    'This is the martijn-cave cave, there is 0 cavewomen in this cave.'

    >>> queryMultiAdapter((belgianCave, request), name='caveview')()
    'This is the belgian-cave cave, there is 0 cavewomen in this cave.'

    >>> addView = queryMultiAdapter((belgianCave, request),
    ...                             name=u'cave-woman-add')

    >>> addView.update(id='emma', name='Emma', age=22,
    ...                size=160, weight=47)
    Hey caveman there is a new cavewoman in the cave, here
    are the most important informations about her:
      * Hair Type: brown
      * Weight: 47
      * Size: 160

    >>> addView.update(id='carla', name='Carla', age=23,
    ...                size=160, weight=47)
    Hey caveman there is a new cavewoman in the cave, here
    are the most important informations about her:
      * Hair Type: blond
      * Weight: 47
      * Size: 160

    >>> addView.update(id='layla', name='Layla', age=24,
    ...                size=164, weight=56)
    Hey caveman there is a new cavewoman in the cave, here
    are the most important informations about her:
      * Hair Type: brown
      * Weight: 56
      * Size: 164

    >>> addView = queryMultiAdapter((martijnCave, request),
    ...                             name=u'cave-woman-add')

    >>> addView.update(id='betty', name='Betty', age=52,
    ...                size=160, weight=90)
    Hey caveman there is a new cavewoman in the cave, here
    are the most important informations about her:
      * Hair Type: brown
      * Weight: 90
      * Size: 160

    >>> queryMultiAdapter((martijnCave, request), name='caveview')()
    'This is the martijn-cave cave, there is 1 cavewomen in this cave.'

    >>> queryMultiAdapter((belgianCave, request), name='caveview')()
    'This is the belgian-cave cave, there is 3 cavewomen in this cave.'
    >>> print queryMultiAdapter((village, request), name='grokvillageview')()
    <html>
    <body>
    <div>
    In cave martijn-cave there is 1 cavewomen.
    </div>
    <div>
    In cave belgian-cave there is 3 cavewomen.
    </div>
    <div>
        And just to prove that we have a Zope 2 template, let's do something
        ugly: <b>amsterdam</b>
    </div>
    </body>
    </html>
    <BLANKLINE>

    >>> print queryMultiAdapter((village, request), name='inline')()
    Village: <b>amsterdam</b>
