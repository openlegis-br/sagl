##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Grok test helpers
"""

from Testing.ZopeTestCase.layer import ZopeLite
from grokcore.component import zcml
from zope.component.testlayer import ZCMLFileLayer
from zope.configuration.config import ConfigurationMachine
import five.grok


def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok('grokcore.component.meta', config)
    zcml.do_grok('grokcore.view.meta.views', config)
    zcml.do_grok('grokcore.view.meta.templates', config)
    zcml.do_grok('grokcore.view.meta.skin', config)
    # Use the Five override for the page template factory
    # zcml.do_grok('grokcore.view.templatereg', config)
    zcml.do_grok('five.grok.templatereg', config)
    zcml.do_grok('five.grok.meta', config)
    zcml.do_grok(module_name, config)
    config.execute_actions()



class Zope2FunctionalLayer(ZCMLFileLayer):

    def setUp(self):
        super(Zope2FunctionalLayer, self).setUp()
        ZopeLite.setUp()

    def tearDown(self):
        ZopeLite.tearDown()
        super(Zope2FunctionalLayer, self).tearDown()


FunctionalLayer = Zope2FunctionalLayer(five.grok)

