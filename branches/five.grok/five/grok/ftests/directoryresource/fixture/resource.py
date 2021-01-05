import os
from five import grok

class DirectoryResourceFoo(grok.DirectoryResource):
    grok.path('foo')

class IAnotherLayer(grok.IDefaultBrowserLayer):
    grok.skin('another')

class DirectoryResourceFooOnLayer(grok.DirectoryResource):
    grok.layer(IAnotherLayer)
    grok.path('anotherfoo')

class DirectoryResourceBarWithName(grok.DirectoryResource):
    grok.name('fropple')
    grok.path('bar')

class DirectoryResourceBazInsubdirWithName(grok.DirectoryResource):
    grok.name('frepple')
    grok.path('bar/baz')

absolute_path = os.path.join(os.path.dirname(__file__), 'bar', 'baz')

class DirectoryResourceQuxWithNameAbsolutePath(grok.DirectoryResource):
    grok.name('frupple')
    grok.path(absolute_path)
