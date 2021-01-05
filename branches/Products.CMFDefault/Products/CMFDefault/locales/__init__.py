##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Makers for z3c.recipe.i18n.
"""
import os

def tal_strings_html(path, domain, include_default_domain, exclude_dirs, **kw):
    from zope.app.locales.extract import tal_strings

    return tal_strings(path, domain, include_default_domain,
                       exclude=exclude_dirs, filePattern='*.html')

def tal_strings_xml(path, domain, include_default_domain, exclude_dirs, **kw):
    from zope.app.locales.extract import tal_strings

    return tal_strings(path, domain, include_default_domain,
                       exclude=exclude_dirs, filePattern='*.xml')

def manual_pot(path, domain, **kw):
    catalog = {}
    manual_file = os.path.join(path, 'locales', domain+'-manual.pot')
    if os.path.exists(manual_file):
        manual = file(manual_file, 'r')
        for i, line in enumerate(manual):
            if line.startswith('msgid'):
                catalog[line[5:].strip().strip('"')] = [(manual_file, i+1)]
        manual.close()
    return catalog
