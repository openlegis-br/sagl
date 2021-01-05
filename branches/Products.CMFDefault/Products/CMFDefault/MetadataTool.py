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
""" CMFDefault portal_metadata tool.
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from App.special_dtml import DTMLFile
from OFS.Folder import Folder
from OFS.SimpleItem import SimpleItem
from Persistence import PersistentMapping
from zope.interface import implements
from zope.interface import implementer

from Products.CMFCore.interfaces import IMetadataTool
from Products.CMFCore.utils import registerToolInterface
from Products.CMFCore.utils import UniqueObject
from Products.CMFDefault.exceptions import MetadataError
from Products.CMFDefault.permissions import ManagePortal
from Products.CMFDefault.permissions import ModifyPortalContent
from Products.CMFDefault.permissions import View
from Products.CMFDefault.utils import _dtmldir


class MetadataElementPolicy(SimpleItem):

    """ Represent a type-specific policy about a particular metadata element.
    """

    security = ClassSecurityInfo()
    #
    #   Default values.
    #
    is_required = 0
    supply_default = 0
    default_value = ''
    enforce_vocabulary = 0
    allowed_vocabulary = ()

    def __init__(self, is_multi_valued=False):
        self.is_multi_valued = bool(is_multi_valued)

    #
    #   Mutator.
    #
    security.declareProtected(ManagePortal, 'edit')
    def edit(self,
             is_required,
             supply_default,
             default_value,
             enforce_vocabulary,
             allowed_vocabulary):
        self.is_required = bool(is_required)
        self.supply_default = bool(supply_default)
        self.default_value = default_value
        self.enforce_vocabulary = bool(enforce_vocabulary)
        self.allowed_vocabulary = tuple(allowed_vocabulary)

    #
    #   Query interface
    #
    security.declareProtected(View, 'isMultiValued')
    def isMultiValued(self):
        """ Can this element hold multiple values?
        """
        return self.is_multi_valued

    security.declareProtected(View, 'isRequired')
    def isRequired(self):
        """ Must this element be supplied?
        """
        return self.is_required

    security.declareProtected(View, 'supplyDefault')
    def supplyDefault(self):
        """ Should the tool supply a default?
        """
        return self.supply_default

    security.declareProtected(View, 'defaultValue')
    def defaultValue(self):
        """ If so, what is the default?
        """
        return self.default_value

    security.declareProtected(View, 'enforceVocabulary')
    def enforceVocabulary(self):
        """ Should the tool enforce the policy's vocabulary?
        """
        return self.enforce_vocabulary

    security.declareProtected(View, 'allowedVocabulary')
    def allowedVocabulary(self):
        """ What are the allowed values?
        """
        return self.allowed_vocabulary

InitializeClass(MetadataElementPolicy)


class ElementSpec(SimpleItem):

    """ Represent all the tool knows about a single metadata element.
    """

    security = ClassSecurityInfo()

    #
    #   Default values.
    #
    is_multi_valued = 0

    def __init__(self, is_multi_valued):
        self.is_multi_valued = is_multi_valued
        self.policies = PersistentMapping()
        self.policies[None] = self._makePolicy()  # set default policy

    security.declarePrivate('_makePolicy')
    def _makePolicy(self):
        return MetadataElementPolicy(self.is_multi_valued)

    security.declareProtected(View, 'isMultiValued')
    def isMultiValued(self):
        """
            Is this element multi-valued?
        """
        return self.is_multi_valued

    security.declareProtected(View, 'getPolicy')
    def getPolicy(self, typ=None):
        """ Find the policy for this element for objects of the given type.

        o Return a default, if none found.
        """
        try:
            return self.policies[typ].__of__(self)
        except KeyError:
            return self.policies[None].__of__(self)

    security.declareProtected(View, 'listPolicies')
    def listPolicies(self):
        """ Return a list of all policies for this element.
        """
        res = []
        for k, v in self.policies.items():
            res.append((k, v.__of__(self)))
        return res

    security.declareProtected(ManagePortal, 'addPolicy')
    def addPolicy(self, typ):
        """ Add a policy to this element for objects of the given type.
        """
        if typ is None:
            raise MetadataError("Can't replace default policy.")

        if typ in self.policies:
            raise MetadataError("Existing policy for content type:" + typ)

        self.policies[typ] = self._makePolicy()

    security.declareProtected(ManagePortal, 'removePolicy')
    def removePolicy(self, typ):
        """ Remove the policy from this element for objects of the given type.

        o Do *not* remvoe the default, however.
        """
        if typ is None:
            raise MetadataError("Can't remove default policy.")
        del self.policies[typ]

InitializeClass(ElementSpec)


class MetadataSchema(SimpleItem):

    """ Describe a metadata schema.
    """

    security = ClassSecurityInfo()

    meta_type = 'Metadata Schema'
    publisher = ''

    def __init__(self, id, element_specs=()):
        self._setId(id)
        self.element_specs = PersistentMapping()
        for name, is_multi_valued in element_specs:
            self.element_specs[name] = ElementSpec(is_multi_valued)

    #
    #   ZMI methods
    #
    manage_options = (
        ({'label': 'Elements', 'action': 'elementPoliciesForm'},) +
        SimpleItem.manage_options)

    security.declareProtected(ManagePortal, 'elementPoliciesForm')
    elementPoliciesForm = DTMLFile('metadataElementPolicies', _dtmldir)

    security.declareProtected(ManagePortal, 'addElementPolicy')
    def addElementPolicy(self,
                         element,
                         content_type,
                         is_required,
                         supply_default,
                         default_value,
                         enforce_vocabulary,
                         allowed_vocabulary,
                         REQUEST=None):
        """ Add a type-specific policy for one of our elements.
        """
        if content_type == '<default>':
            content_type = None

        spec = self.getElementSpec(element)
        spec.addPolicy(content_type)
        policy = spec.getPolicy(content_type)
        policy.edit(is_required,
                    supply_default,
                    default_value,
                    enforce_vocabulary,
                    allowed_vocabulary)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()
                + '/elementPoliciesForm'
                + '?element=' + element
                + '&manage_tabs_message=Policy+added.')

    security.declareProtected(ManagePortal, 'removeElementPolicy')
    def removeElementPolicy(self, element, content_type, REQUEST=None):
        """ Remvoe a type-specific policy for one of our elements.
        """
        if content_type == '<default>':
            content_type = None

        spec = self.getElementSpec(element)
        spec.removePolicy(content_type)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()
                + '/elementPoliciesForm'
                + '?element=' + element
                + '&manage_tabs_message=Policy+removed.')

    security.declareProtected(ManagePortal, 'updateElementPolicy')
    def updateElementPolicy(self,
                            element,
                            content_type,
                            is_required,
                            supply_default,
                            default_value,
                            enforce_vocabulary,
                            allowed_vocabulary,
                            REQUEST=None):
        """ Update a policy for one of our elements

        o 'content_type' will be '<default>' when we edit the default.
        """
        if content_type == '<default>':
            content_type = None
        spec = self.getElementSpec(element)
        policy = spec.getPolicy(content_type)
        policy.edit(is_required,
                    supply_default,
                    default_value,
                    enforce_vocabulary,
                    allowed_vocabulary)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()
                + '/elementPoliciesForm'
                + '?element=' + element
                + '&manage_tabs_message=Policy+updated.')

    #
    #   Element spec manipulation.
    #
    security.declareProtected(ManagePortal, 'listElementSpecs')
    def listElementSpecs(self):
        """ Return a list of ElementSpecs representing the elements we manage.
        """
        res = []
        for k, v in self.element_specs.items():
            res.append((k, v.__of__(self)))
        return res

    security.declareProtected(ManagePortal, 'getElementSpec')
    def getElementSpec(self, element):
        """ Return an ElementSpec for the given 'element'.
        """
        return self.element_specs[element].__of__(self)

    security.declareProtected(ManagePortal, 'addElementSpec')
    def addElementSpec(self, element, is_multi_valued, REQUEST=None):
        """ Add 'element' to our list of managed elements.
        """
        # Don't replace.
        if element in self.element_specs:
            return

        self.element_specs[element] = ElementSpec(is_multi_valued)

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()
                + '/propertiesForm'
                + '?manage_tabs_message=Element+' + element + '+added.')

    security.declareProtected(ManagePortal, 'removeElementSpec')
    def removeElementSpec(self, element, REQUEST=None):
        """ Remove 'element' from our list of managed elements.
        """
        del self.element_specs[element]

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()
                + '/propertiesForm'
                + '?manage_tabs_message=Element+' + element + '+removed.')

    security.declareProtected(ManagePortal, 'listPolicies')
    def listPolicies(self, typ=None):
        """ Show all policies for a given content type

        o If 'typ' is none, return the list of default policies.
        """
        result = []
        for element, spec in self.listElementSpecs():
            result.append((element, spec.getPolicy(typ)))
        return result

InitializeClass(MetadataSchema)


_DCMI_ELEMENT_SPECS = (('Title', 0),
                       ('Description', 0),
                       ('Subject', 1),
                       ('Format', 0),
                       ('Language', 0),
                       ('Rights', 0))

@implementer(IMetadataTool)
class MetadataTool(UniqueObject, Folder):


    id = 'portal_metadata'
    meta_type = 'Default Metadata Tool'

    #
    #   Default values.
    #
    publisher = ''

    security = ClassSecurityInfo()

    def __init__(self, publisher=None):

        self.editProperties(publisher)
        self.DCMI = MetadataSchema('DCMI', _DCMI_ELEMENT_SPECS)

    #
    #   ZMI methods
    #
    manage_options = (
        ({'label': 'Schema', 'action': 'propertiesForm'},
         {'label': 'Overview', 'action': 'manage_overview'}) +
        Folder.manage_options)

    security.declareProtected(ManagePortal, 'manage_overview')
    manage_overview = DTMLFile('explainMetadataTool', _dtmldir)

    security.declareProtected(ManagePortal, 'propertiesForm')
    propertiesForm = DTMLFile('metadataProperties', _dtmldir)

    security.declareProtected(ManagePortal, 'editProperties')
    def editProperties(self, publisher=None, REQUEST=None):
        """ Form handler for "tool-wide" properties
        """
        if publisher is not None:
            self.publisher = publisher

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(self.absolute_url()
                + '/propertiesForm'
                + '?manage_tabs_message=Tool+updated.')

    security.declareProtected(ManagePortal, 'manage_addSchema')
    def manage_addSchema(self, schema_id, elements, REQUEST):
        """ ZMI wrapper around addSchema
        """
        massaged = []
        for element in elements:
            if isinstance(element, basestring):
                element = element.split(',')
                if len(element) < 2:
                    element.append(0)
            massaged.append(element)
        self.addSchema(schema_id, massaged)

        REQUEST['RESPONSE'].redirect(self.absolute_url()
            + '/propertiesForm'
            + '?manage_tabs_message=Schema+added.')

    security.declareProtected(ManagePortal, 'manage_removeSchemas')
    def manage_removeSchemas(self, schema_ids, REQUEST):
        """ ZMI wrapper around removeSchema
        """
        if not schema_ids:
            raise ValueError('No schemas selected!')

        for schema_id in schema_ids:
            self.removeSchema(schema_id)

        REQUEST['RESPONSE'].redirect(self.absolute_url()
            + '/propertiesForm'
            + '?manage_tabs_message=Schemas+removed.')

    security.declarePrivate('getFullName')
    def getFullName(self, userid):
        """ See IMetadataTool.
        """
        return userid   # TODO: do lookup here

    security.declarePublic('getPublisher')
    def getPublisher(self):
        """ See IMetadataTool.
        """
        return self.publisher

    security.declarePublic('listAllowedSubjects')
    def listAllowedSubjects(self, content=None, content_type=None):
        """ See IMetadataTool.
        """
        return self.listAllowedVocabulary('DCMI',
                                          'Subject',
                                          content,
                                          content_type)

    security.declarePublic('listAllowedFormats')
    def listAllowedFormats(self, content=None, content_type=None):
        """ See IMetadataTool.
        """
        return self.listAllowedVocabulary('DCMI',
                                          'Format',
                                          content,
                                          content_type)

    security.declarePublic('listAllowedLanguages')
    def listAllowedLanguages(self, content=None, content_type=None):
        """ See IMetadataTool.
        """
        return self.listAllowedVocabulary('DCMI',
                                          'Language',
                                          content,
                                          content_type)

    security.declarePublic('listAllowedRights')
    def listAllowedRights(self, content=None, content_type=None):
        """ See IMetadata Tool.
        """
        return self.listAllowedVocabulary('DCMI',
                                          'Rights',
                                          content,
                                          content_type)

    security.declarePublic('listAllowedVocabulary')
    def listAllowedVocabulary(self,
                              schema,
                              element,
                              content=None,
                              content_type=None):
        """ See IMetadataTool.
        """
        schema_def = getattr(self, schema)
        spec = schema_def.getElementSpec(element)
        if content_type is None and content:
            content_type = content.getPortalTypeName()
        return spec.getPolicy(content_type).allowedVocabulary()

    security.declarePublic('listSchemas')
    def listSchemas(self):
        """ See IMetadataTool.
        """
        result = [('DCMI', self.DCMI)]
        result.extend(self.objectItems([MetadataSchema.meta_type]))
        return result

    security.declareProtected(ModifyPortalContent, 'addSchema')
    def addSchema(self, schema_id, elements=()):
        """ See IMetadataTool.
        """
        if schema_id == 'DCMI' or schema_id in self.objectIds():
            raise KeyError('Duplicate schema ID: %s' % schema_id)

        schema = MetadataSchema(schema_id, elements)
        self._setObject(schema_id, schema)

        return self._getOb(schema_id)

    security.declareProtected(ModifyPortalContent, 'removeSchema')
    def removeSchema(self, schema_id):
        """ See IMetadataTool.
        """
        if schema_id == 'DCMI' or schema_id not in self.objectIds():
            raise KeyError('Invalid schema ID: %s' % schema_id)

        self._delObject(schema_id)

    security.declareProtected(ModifyPortalContent, 'setInitialMetadata')
    def setInitialMetadata(self, content):
        """ See IMetadataTool.
        """
        for _schema_id, schema in self.listSchemas():
            for element, policy in schema.listPolicies(
                                    content.getPortalTypeName()):

                if not getattr(content, element)():

                    if policy.supplyDefault():
                        setter = getattr(content, 'set%s' % element)
                        setter(policy.defaultValue())
                    elif policy.isRequired():
                        raise MetadataError('Metadata element %s is required.'
                                            % element)

        # TODO:  Call initial_values_hook, if present

    security.declareProtected(View, 'validateMetadata')
    def validateMetadata(self, content):
        """ See IMetadataTool.
        """
        for _schema_id, schema in self.listSchemas():
            for element, policy in schema.listPolicies(
                                    content.getPortalTypeName()):

                value = getattr(content, element)()
                if not value and policy.isRequired():
                    raise MetadataError('Metadata element %s is required.'
                                        % element)

                if value and policy.enforceVocabulary():
                    values = policy.isMultiValued() and value or [value]
                    for value in values:
                        if not value in policy.allowedVocabulary():
                            raise MetadataError(
                                'Value %s is not in allowed vocabulary for '
                                'metadata element %s.' % (value, element))

InitializeClass(MetadataTool)
registerToolInterface('portal_metadata', IMetadataTool)
