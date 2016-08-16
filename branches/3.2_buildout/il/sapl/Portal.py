# -*- coding: utf-8 -*-

import csv

from zope.site.hooks import setSite

from Products.GenericSetup.tool import SetupTool
from Products.CMFDefault.Portal import CMFSite
from Products.CMFCore.utils import getToolByName

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from App.class_init import InitializeClass

_TOOL_ID = 'portal_setup'
_DEFAULT_PROFILE = 'il.sapl:default'


class SAPL(CMFSite):
    """ Inicia um novo SAGL-OpenLegis baseado em um CMFSite.
    """
    security=ClassSecurityInfo()
    meta_type = portal_type = 'SAPL'

    def __init__( self, id, title='' ):
        CMFSite.__init__( self, id, title )

    def processCSVFile(self, file, as_dict=0):
        reader = csv.reader(file)
        output_list = []
        if as_dict:
            headerList = reader.next()
            for line in reader:
                if line:
                    dd = {}
                    for i, key in enumerate(headerList):
                        dd[key]=line[i]
                    output_list.append(dd)
        else:
            for row in reader:
                output_list.append(row)
        return output_list


InitializeClass(SAPL)


from Products.PageTemplates.PageTemplateFile import PageTemplateFile

manage_addSAPLForm = PageTemplateFile('www/addSAPL', globals())
manage_addSAPLForm.__name__ = 'addSAPL'


def manage_addSAPL(context, id, title='OpenLegis - Processo Legislativo Eletrônico', description='',
                   database='MySQL', profile_id=_DEFAULT_PROFILE, RESPONSE=None):
    """ Adicionar uma instancia do SAGL-OpenLegis.
    """

    context._setObject(id, SAPL(id))
    site = context._getOb(id)
    setSite(site)

    site._setObject(_TOOL_ID, SetupTool(_TOOL_ID))
    setup_tool = getToolByName(site, _TOOL_ID)

    setup_tool.setBaselineContext('profile-Products.CMFDefault:default')
    setup_tool.runAllImportStepsFromProfile('profile-Products.CMFDefault:default')

    setup_tool.setBaselineContext('profile-%s' % profile_id)
    setup_tool.runAllImportStepsFromProfile('profile-%s' % profile_id)

    props = dict(
        title=title,
        description=description,
    )

    site.manage_changeProperties(**props)

    if database == 'MySQL':
        site.manage_addProduct['ZMySQLDA'].manage_addZMySQLConnection(
            id='dbcon_interlegis',
            title='Banco de Dados do SAGL-OpenLegis (MySQL)',
            use_unicode=True,
            connection_string='interlegis sapl sapl'
        )
    else:
        site.manage_addProduct['ZPsycopgDA'].manage_addZPsycopgConnection(
            id='dbcon_interlegis',
            title='Banco de Dados do SAGL-OpenLegis (PostgreSQL)',
            connection_string='dbname=interlegis user=sapl password=sapl host=localhost'
        )

    if RESPONSE is not None:
        RESPONSE.redirect( '%s/%s/manage_main?update_menu=1'
                           % (context.absolute_url(), id) )
