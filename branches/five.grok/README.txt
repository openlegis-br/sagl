five.grok
=========

.. contents::

Introduction
------------

`five.grok` is a development layer for Zope 2, based on Grok framework
concepts.

The development techniques are similar to the ones used with Grok
framework.

It is based on `grokcore` namespace packages that were factored out of Grok
framework.

Implemented features
--------------------

Coming from Grok, the following components are available to Zope 2
developers:

- Zope 3 Component (Adapter, Global utilities, Subscribers),

- Permissions,

- Views and Viewlets,

- Skins and resources directories,

- Page Templates (using the Zope 2 Page Templates),

- Formlib forms (optional, you need to include the extra ``form``),

- Local sites and local utilities,

- Annotations,

- Layout (optional, you need to include the extra ``layout``).

All those components are available with exactly the same syntax than
in grok. You just have to do::

  from five import grok

Instead of::

  import grok

Installation
------------

After adding the dependency to ``five.grok`` in your project, you have
to load the following ZCML::

  <include package="five.grok" />

Note
~~~~

And for this release we recommend to pin down the following version in
your buildout::

  five.formlib = 1.0.4
  five.localsitemanager = 2.0.5
  grokcore.annotation = 1.3
  grokcore.component = 2.5
  grokcore.formlib = 1.9
  grokcore.layout = 1.5.1
  grokcore.security = 1.6.1
  grokcore.site = 1.6.1
  grokcore.view = 2.7
  grokcore.viewlet = 1.10.1
  martian = 0.14


Zope 2.13 is required. If you wish to use a previous version of Zope
2, look at five.grok 1.0 for Zope 2.10.x or five.grok 1.2 for Zope 2.12.x.


More information
----------------

You can refer to the Grok website: http://grok.zope.org/, and the Grok
documentation: http://grok.zope.org/documentation/.

You can check the doctest included in sources as well.
