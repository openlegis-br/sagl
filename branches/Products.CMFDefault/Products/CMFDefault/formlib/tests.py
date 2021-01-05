##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""CMFDefault formlib tests.
"""

import doctest
import unittest
from Testing import ZopeTestCase

from Products.CMFCore.PortalContent import PortalContent
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFDefault.testing import FunctionalLayer
from zope.component.factory import Factory
from zope.interface import implements
from zope.interface import Interface
from zope.schema import TextLine

CONTENT_ZCML = """\
<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:five="http://namespaces.zope.org/five">

  <five:registerClass
      class="Products.CMFDefault.formlib.tests.Foo"
      meta_type="Foo Type"
      permission="cmf.AddPortalContent"
      />

  <utility
      component="Products.CMFDefault.formlib.tests.FooFactory"
      name="test.foo"
      />

</configure>
"""

TYPES_XML = """\
<?xml version="1.0"?>
<object name="portal_types">
 <object name="MyFoo" meta_type="Factory-based Type Information"/>
</object>
"""

MYFOO_XML = """\
<?xml version="1.0"?>
<object name="MyFoo">
 <property name="content_meta_type">Foo Type</property>
 <property name="factory">test.foo</property>
 <property name="add_view_expr">string:${folder_url}/++add++MyFoo</property>
 <action title="View" action_id="view" category="object" url_expr=""/>
</object>
"""


class IFoo(Interface):

    bar = TextLine(title=u'Bar')
    baz = TextLine(title=u'Baz')


class Foo(PortalContent, DefaultDublinCoreImpl):

    implements(IFoo)

    def __init__(self, id, bar='', baz=''):
        DefaultDublinCoreImpl.__init__(self)
        self.id = id
        self.bar = bar
        self.baz = baz

FooFactory = Factory(Foo)


def test_suite():
    suite = unittest.TestSuite()
    s = ZopeTestCase.FunctionalDocFileSuite('form.txt')
    s.layer = FunctionalLayer
    suite.addTest(s)
    suite.addTest(doctest.DocFileSuite('schema.txt',
                                    optionflags=doctest.NORMALIZE_WHITESPACE))
    suite.addTest(doctest.DocFileSuite('widgets.txt',
                                    optionflags=doctest.NORMALIZE_WHITESPACE |
                                                doctest.ELLIPSIS))
    return suite
