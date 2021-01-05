"""
A directory resource defined without an explicit name direective is available
through the dotted name of the module in which the directoryresource is
defined::

  >>> from Testing.testbrowser import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open(
  ...     'http://localhost/'
  ...     '++resource++five.grok.ftests.directoryresource.fixture.resource/file.txt')
  >>> print browser.contents
  Foo resource file's content.

Directoryresource registrations can be differentiated based on layers (and
skins)::

  >>> browser.open(
  ...     'http://localhost/++skin++another/'
  ...     '++resource++five.grok.ftests.directoryresource.fixture.resource/file.txt')
  >>> print browser.contents
  Anotherfoo resource file's content.

This resource is only available on the particular layer::

  >>> browser.open(
  ...     'http://localhost/++skin++another/'
  ...     '++resource++five.grok.ftests.directoryresource.fixture.resource/'
  ...     'anotherfile.txt')
  >>> print browser.contents
  Anotherfoo resource anotherfile's content.

  >>> browser.handleErrors = True
  >>> browser.open(
  ...     'http://localhost/'
  ...     '++resource++five.grok.ftests.directoryresource.fixture.resource/'
  ...     'anotherfile.txt')
  Traceback (most recent call last):
  ...
  HTTPError: HTTP Error 404: Not Found

Directoryresources can be registered under an explicit name::

  >>> browser.handleErrors = False
  >>> browser.open('http://localhost/++resource++fropple/file.txt')
  >>> print browser.contents
  Bar resource file's content.

Subdirectories are published as directoryresources recusively::

  >>> browser.open('http://localhost/++resource++fropple/baz/file.txt')
  >>> print browser.contents
  Baz resource file's content.

A relative path to a directory with resources::

  >>> browser.open('http://localhost/++resource++frepple/file.txt')
  >>> print browser.contents
  Baz resource file's content.

An absolute path to a directory with resources::

  >>> browser.open('http://localhost/++resource++frupple/file.txt')
  >>> print browser.contents
  Baz resource file's content.

We can restricted-traverse to resources in directories and subdirectories:

  >>> app.restrictedTraverse('++resource++five.grok.ftests.directoryresource.fixture.resource/file.txt')
  <Products.Five.browser.resource.FileResource object at ...>
  
  >>> app.restrictedTraverse('++resource++frupple/file.txt')
  <Products.Five.browser.resource.FileResource object at ...>
  
  >>> app.restrictedTraverse('++resource++fropple/baz/file.txt')
  <Products.Five.browser.resource.FileResource object at ...>

"""
