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
""" Unit tests for MetadataTool module.
"""

import unittest
import Testing

from Acquisition import aq_base
from zope.interface.verify import verifyClass


class TestMetadataElementPolicy(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.MetadataTool import MetadataElementPolicy
        return MetadataElementPolicy

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_empty_single_valued(self):
        sv_policy = self._makeOne(0)
        self.assertFalse(sv_policy.isMultiValued())
        self.assertFalse(sv_policy.isRequired())
        self.assertFalse(sv_policy.supplyDefault())
        self.assertFalse(sv_policy.defaultValue())
        self.assertFalse(sv_policy.enforceVocabulary())
        self.assertFalse(sv_policy.allowedVocabulary())

    def test_edit_single_valued(self):
        sv_policy = self._makeOne(0)
        sv_policy.edit(1, 1, 'xxx', 0, '')
        self.assertFalse(sv_policy.isMultiValued())
        self.assertTrue(sv_policy.isRequired())
        self.assertTrue(sv_policy.supplyDefault())
        self.assertEqual(sv_policy.defaultValue(), 'xxx')
        self.assertFalse(sv_policy.enforceVocabulary())
        self.assertFalse(sv_policy.allowedVocabulary())

    def test_empty_multi_valued(self):
        mv_policy = self._makeOne(1)
        self.assertTrue(mv_policy.isMultiValued())
        self.assertFalse(mv_policy.isRequired())
        self.assertFalse(mv_policy.supplyDefault())
        self.assertFalse(mv_policy.defaultValue())
        self.assertFalse(mv_policy.enforceVocabulary())
        self.assertFalse(mv_policy.allowedVocabulary())

    def test_edit_multi_valued(self):
        mv_policy = self._makeOne(1)
        mv_policy.edit(1, 1, 'xxx', 1, ('xxx', 'yyy'))
        self.assertTrue(mv_policy.isMultiValued())
        self.assertTrue(mv_policy.isRequired())
        self.assertTrue(mv_policy.supplyDefault())
        self.assertEqual(mv_policy.defaultValue(), 'xxx')
        self.assertTrue(mv_policy.enforceVocabulary())
        self.assertEqual(len(mv_policy.allowedVocabulary()), 2)
        self.assertTrue('xxx' in mv_policy.allowedVocabulary())
        self.assertTrue('yyy' in mv_policy.allowedVocabulary())


class TestElementSpec(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.MetadataTool import ElementSpec
        return ElementSpec

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_empty_single_valued(self):
        sv_spec = self._makeOne(0)
        self.assertFalse(sv_spec.isMultiValued())
        self.assertEqual(sv_spec.getPolicy(), sv_spec.getPolicy('XYZ'))
        policies = sv_spec.listPolicies()
        self.assertEqual(len(policies), 1)
        self.assertEqual(policies[0][0], None)

    def test_empty_multi_valued(self):
        mv_spec = self._makeOne(1)
        self.assertTrue(mv_spec.isMultiValued())
        self.assertEqual(mv_spec.getPolicy(), mv_spec.getPolicy('XYZ'))
        policies = mv_spec.listPolicies()
        self.assertEqual(len(policies), 1)
        self.assertEqual(policies[0][0], None)


class TestMetadataSchema(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.MetadataTool import MetadataSchema
        return MetadataSchema

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)


class TestMetadataTool(unittest.TestCase):

    def _getTargetClass(self):
        from Products.CMFDefault.MetadataTool import MetadataTool
        return MetadataTool

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _makeTestObjects(self):
        from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl

        class Foo(DefaultDublinCoreImpl):

            description = title = language = format = rights = ''
            subject = ()

            def __init__(self):
                pass # skip DDCI's default values

            def getPortalTypeName(self):
                return 'Foo'

        class Bar(Foo):

            def getPortalTypeName(self):
                return 'Bar'

        return Foo(), Bar()

    def test_interfaces(self):
        from Products.CMFCore.interfaces import IMetadataTool

        verifyClass(IMetadataTool, self._getTargetClass())

    def test_empty(self):
        from Products.CMFDefault.MetadataTool import _DCMI_ELEMENT_SPECS

        tool = self._makeOne()
        self.assertFalse(tool.getPublisher())
        self.assertEqual(tool.getFullName('foo'), 'foo')

        dcmi = tool.DCMI
        specs = list(dcmi.DCMI.listElementSpecs())
        defaults = list(_DCMI_ELEMENT_SPECS)
        specs.sort()
        defaults.sort()

        self.assertEqual(len(specs), len(defaults))
        for i in range(len(specs)):
            self.assertEqual(specs[i][0], defaults[i][0])
            self.assertEqual(specs[i][1].isMultiValued(), defaults[i][1])
            policies = specs[i][1].listPolicies()
            self.assertEqual(len(policies), 1)
            self.assertTrue(policies[0][0] is None)

        self.assertFalse(dcmi.getElementSpec('Title').isMultiValued())
        self.assertFalse(dcmi.getElementSpec('Description').isMultiValued())
        self.assertTrue(dcmi.getElementSpec('Subject').isMultiValued())
        self.assertFalse(dcmi.getElementSpec('Format').isMultiValued())
        self.assertFalse(dcmi.getElementSpec('Language').isMultiValued())
        self.assertFalse(dcmi.getElementSpec('Rights').isMultiValued())

        try:
            dummy = dcmi.getElementSpec('Foo')
        except KeyError:
            pass
        else:
            self.assertTrue(0, "Expected KeyError")

        self.assertFalse(dcmi.listAllowedSubjects())
        self.assertFalse(dcmi.listAllowedFormats())
        self.assertFalse(dcmi.listAllowedLanguages())
        self.assertFalse(dcmi.listAllowedRights())

    def test_DCMI_addElementSpec(self):
        from Products.CMFDefault.MetadataTool import _DCMI_ELEMENT_SPECS

        tool = self._makeOne()
        dcmi = tool.DCMI
        dcmi.addElementSpec('Rating', 1)
        self.assertEqual(len(dcmi.listElementSpecs()),
                         len(_DCMI_ELEMENT_SPECS) + 1)
        rating = dcmi.getElementSpec('Rating')
        self.assertTrue(rating.isMultiValued())

    def test_DCMI_removeElementSpec(self):
        from Products.CMFDefault.MetadataTool import _DCMI_ELEMENT_SPECS

        tool = self._makeOne()
        dcmi = tool.DCMI
        dcmi.removeElementSpec('Rights')

        self.assertEqual(len(dcmi.listElementSpecs()),
                         len(_DCMI_ELEMENT_SPECS) - 1)

        self.assertRaises(KeyError, dcmi.getElementSpec, 'Rights')
        self.assertRaises(KeyError, dcmi.removeElementSpec, 'Foo')

    def test_simplePolicies(self):
        tool = self._makeOne()
        dcmi = tool.DCMI
        tSpec = dcmi.getElementSpec('Title')

        # Fetch default policy.
        tDef = tSpec.getPolicy()
        self.assertFalse(tDef.isRequired())
        self.assertFalse(tDef.supplyDefault())
        self.assertFalse(tDef.defaultValue())

        # Fetch (default) policy for a type.
        tDoc = tSpec.getPolicy('Document')
        self.assertEqual(aq_base(tDoc), aq_base(tDef))

        # Changing default changes policies found from there.
        tDef.edit(1, 1, 'xyz', 0, ())
        self.assertTrue(tDef.isRequired())
        self.assertTrue(tDef.supplyDefault())
        self.assertEqual(tDef.defaultValue(), 'xyz')
        self.assertTrue(tDoc.isRequired())
        self.assertTrue(tDoc.supplyDefault())
        self.assertEqual(tDoc.defaultValue(), 'xyz')

        tSpec.addPolicy('Document')
        self.assertEqual(len(tSpec.listPolicies()), 2)

        tDoc = tSpec.getPolicy('Document')
        self.assertNotEqual(aq_base(tDoc), aq_base(tDef))
        self.assertFalse(tDoc.isRequired())
        self.assertFalse(tDoc.supplyDefault())
        self.assertFalse(tDoc.defaultValue())

        tSpec.removePolicy('Document')
        tDoc = tSpec.getPolicy('Document')
        self.assertEqual(aq_base(tDoc), aq_base(tDef))
        self.assertTrue(tDoc.isRequired())
        self.assertTrue(tDoc.supplyDefault())
        self.assertEqual(tDoc.defaultValue(), 'xyz')

    def test_multiValuedPolicies(self):
        tool = self._makeOne()
        dcmi = tool.DCMI
        sSpec = dcmi.getElementSpec('Subject')

        # Fetch default policy.
        sDef = sSpec.getPolicy()
        self.assertFalse(sDef.isRequired())
        self.assertFalse(sDef.supplyDefault())
        self.assertFalse(sDef.defaultValue())
        self.assertFalse(sDef.enforceVocabulary())
        self.assertFalse(sDef.allowedVocabulary())

        # Fetch (default) policy for a type.
        sDoc = sSpec.getPolicy('Document')
        self.assertEqual(aq_base(sDoc), aq_base(sDef))

        # Changing default changes policies found from there.
        sDef.edit(1, 1, 'xyz', 1, ('foo', 'bar'))
        self.assertTrue(sDef.isRequired())
        self.assertTrue(sDef.supplyDefault())
        self.assertEqual(sDef.defaultValue(), 'xyz')
        self.assertTrue(sDoc.isRequired())
        self.assertTrue(sDoc.supplyDefault())
        self.assertEqual(sDoc.defaultValue(), 'xyz')
        self.assertTrue(sDef.enforceVocabulary())
        self.assertEqual(len(sDef.allowedVocabulary()), 2)
        self.assertTrue('foo' in sDef.allowedVocabulary())
        self.assertTrue('bar' in sDef.allowedVocabulary())
        self.assertTrue(sDoc.enforceVocabulary())
        self.assertEqual(len(sDoc.allowedVocabulary()), 2)
        self.assertTrue('foo' in sDoc.allowedVocabulary())
        self.assertTrue('bar' in sDoc.allowedVocabulary())

        sSpec.addPolicy('Document')
        self.assertEqual(len(sSpec.listPolicies()), 2)

        sDoc = sSpec.getPolicy('Document')
        self.assertNotEqual(aq_base(sDoc), aq_base(sDef))
        self.assertFalse(sDoc.isRequired())
        self.assertFalse(sDoc.supplyDefault())
        self.assertFalse(sDoc.defaultValue())
        self.assertFalse(sDoc.enforceVocabulary())
        self.assertFalse(sDoc.allowedVocabulary())

        sSpec.removePolicy('Document')
        sDoc = sSpec.getPolicy('Document')
        self.assertEqual(aq_base(sDoc), aq_base(sDef))
        self.assertTrue(sDoc.isRequired())
        self.assertTrue(sDoc.supplyDefault())
        self.assertEqual(sDoc.defaultValue(), 'xyz')
        self.assertTrue(sDoc.enforceVocabulary())
        self.assertEqual(len(sDoc.allowedVocabulary()), 2)
        self.assertTrue('foo' in sDoc.allowedVocabulary())
        self.assertTrue('bar' in sDoc.allowedVocabulary())

    def test_vocabularies(self):
        tool = self._makeOne()
        dcmi = tool.DCMI
        fSpec = dcmi.getElementSpec('Format')
        fDef = fSpec.getPolicy()
        formats = ('text/plain', 'text/html')
        fDef.edit(0, 0, '', 0, ('text/plain', 'text/html'))
        self.assertEqual(tool.listAllowedFormats(), formats)

        foo, _bar = self._makeTestObjects()

        self.assertEqual(tool.listAllowedFormats(foo), formats)

        fSpec.addPolicy('Foo')
        self.assertFalse(tool.listAllowedFormats(foo))

        foo_formats = ('image/jpeg', 'image/gif', 'image/png')
        fFoo = fSpec.getPolicy('Foo')
        fFoo.edit(0, 0, '', 0, foo_formats)
        self.assertEqual(tool.listAllowedFormats(foo), foo_formats)

    def test_initialValues_defaults(self):
        tool = self._makeOne()
        foo, _bar = self._makeTestObjects()
        self.assertFalse(foo.Title())
        self.assertFalse(foo.Description())
        self.assertFalse(foo.Subject())
        self.assertFalse(foo.Format(), foo.Format())
        self.assertFalse(foo.Language())
        self.assertFalse(foo.Rights())

        tool.setInitialMetadata(foo)
        self.assertFalse(foo.Title())
        self.assertFalse(foo.Description())
        self.assertFalse(foo.Subject())
        self.assertFalse(foo.Format())
        self.assertFalse(foo.Language())
        self.assertFalse(foo.Rights())

    def test_initialValues_implicit(self):
        # Test default policy.
        tool = self._makeOne()
        dcmi = tool.DCMI
        foo, _bar = self._makeTestObjects()
        fSpec = dcmi.getElementSpec('Format')
        fPolicy = fSpec.getPolicy()
        fPolicy.edit(0, 1, 'text/plain', 0, ())
        tool.setInitialMetadata(foo)
        self.assertFalse(foo.Title())
        self.assertFalse(foo.Description())
        self.assertFalse(foo.Subject())
        self.assertEqual(foo.Format(), 'text/plain')
        self.assertFalse(foo.Language())
        self.assertFalse(foo.Rights())

    def test_initialValues_explicit_raises_if_constraint_fails(self):
        from Products.CMFDefault.exceptions import MetadataError

        # Test type-specific policy.
        tool = self._makeOne()
        dcmi = tool.DCMI
        foo, _bar = self._makeTestObjects()
        tSpec = dcmi.getElementSpec('Title')
        tSpec.addPolicy('Foo')
        tPolicy = tSpec.getPolicy(foo.getPortalTypeName())
        tPolicy.edit(1, 0, '', 0, ())

        self.assertRaises(MetadataError, tool.setInitialMetadata, foo)

    def test_initialValues_explicit_mutliple_types(self):
        tool = self._makeOne()
        dcmi = tool.DCMI
        foo, bar = self._makeTestObjects()
        foo.setTitle('Foo title')

        fSpec = dcmi.getElementSpec('Format')
        fSpec.addPolicy(foo.getPortalTypeName())
        fPolicy = fSpec.getPolicy(foo.getPortalTypeName())
        fPolicy.edit(0, 1, 'text/plain', 0, ())

        tool.setInitialMetadata(foo)
        self.assertEqual(foo.Title(), 'Foo title')
        self.assertFalse(foo.Description())
        self.assertFalse(foo.Subject())
        self.assertEqual(foo.Format(), 'text/plain')
        self.assertFalse(foo.Language())
        self.assertFalse(foo.Rights())

        #   Ensure Foo's policy doesn't interfere with other types.
        tool.setInitialMetadata(bar)
        self.assertFalse(bar.Title())
        self.assertFalse(bar.Description())
        self.assertFalse(bar.Subject())
        self.assertEqual(bar.Format(), '')
        self.assertFalse(bar.Language())
        self.assertFalse(bar.Rights())

    def test_validation(self):
        from Products.CMFDefault.exceptions import MetadataError

        tool = self._makeOne()
        foo, _bar = self._makeTestObjects()
        tool.setInitialMetadata(foo)
        tool.validateMetadata(foo)

        dcmi = tool.DCMI
        tSpec = dcmi.getElementSpec('Title')
        tSpec.addPolicy('Foo')
        tPolicy = tSpec.getPolicy(foo.getPortalTypeName())
        tPolicy.edit(1, 0, '', 0, ())

        self.assertRaises(MetadataError, tool.validateMetadata, foo)

        foo.setTitle('Foo title')
        tool.validateMetadata(foo)

    def test_addSchema_normal(self):
        from Products.CMFDefault.MetadataTool import MetadataSchema

        tool = self._makeOne()
        before = tool.listSchemas()
        self.assertEqual(len(before), 1)
        self.assertEqual(before[0][0], 'DCMI')
        self.assertTrue(isinstance(before[0][1], MetadataSchema))

        tool.addSchema('Arbitrary')

        after = tool.listSchemas()
        self.assertEqual(len(after), 2)
        self.assertEqual(after[0][0], 'DCMI')
        self.assertTrue(isinstance(after[0][1], MetadataSchema))
        self.assertEqual(after[1][0], 'Arbitrary')
        self.assertTrue(isinstance(after[1][1], MetadataSchema))

    def test_addSchema_duplicate(self):
        tool = self._makeOne()
        tool.addSchema('Arbitrary')
        self.assertRaises(KeyError, tool.addSchema, 'Arbitrary')
        self.assertRaises(KeyError, tool.addSchema, 'DCMI')

    def test_removeSchema_normal(self):
        tool = self._makeOne()
        before = tool.listSchemas()
        self.assertEqual(len(before), 1)
        self.assertEqual(before[0][0], 'DCMI')

        tool.addSchema('Arbitrary')
        tool.addSchema('Beneficent')
        tool.addSchema('Grouchy')

        middle = tool.listSchemas()
        self.assertEqual(len(middle), 4)
        self.assertEqual(middle[0][0], 'DCMI')
        self.assertEqual(middle[1][0], 'Arbitrary')
        self.assertEqual(middle[2][0], 'Beneficent')
        self.assertEqual(middle[3][0], 'Grouchy')

        tool.removeSchema('Beneficent')

        after = tool.listSchemas()
        self.assertEqual(len(after), 3)
        self.assertEqual(after[0][0], 'DCMI')
        self.assertEqual(after[1][0], 'Arbitrary')
        self.assertEqual(after[2][0], 'Grouchy')

    def test_removeSchema_invalid(self):
        tool = self._makeOne()
        self.assertRaises(KeyError, tool.removeSchema, 'DCMI')
        tool.addSchema('Arbitrary')
        tool.removeSchema('Arbitrary')
        self.assertRaises(KeyError, tool.removeSchema, 'Arbitrary')


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(TestMetadataElementPolicy),
        unittest.makeSuite(TestElementSpec),
        unittest.makeSuite(TestMetadataTool),
        ))
