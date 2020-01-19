###############################################################################
#
# Copyright (c) 2005 by Interlegis
#
# GNU General Public Licence (GPL)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
###############################################################################

import Portal
from lexml import SAPLOAIServer

from config import PROJECTNAME

from AccessControl import ModuleSecurityInfo
from Products.PythonScripts.Utility import allow_module

from Products.CMFCore.utils import ToolInit

import SAPLTool

def initialize(context):
    # inicializa a instalacao e estrutura do SAGL-OpenLegis

    ModuleSecurityInfo('socket.socket').declarePublic('fileno')
    ModuleSecurityInfo('tempfile.NamedTemporaryFile').declarePublic('flush')

    allow_module('zlib')
    allow_module('urllib')
    allow_module('urllib2')
    allow_module('sys')
    allow_module('os')
    allow_module('restpki_client')
    allow_module('Acquisition')
    allow_module('ExtensionClass')
    allow_module('App.FindHomes')
    allow_module('trml2pdf')
    allow_module('cStringIO.StringIO')
    allow_module('time')
    allow_module('_strptime')
    allow_module('csv')
    allow_module('pdb')
    allow_module('simplejson')
    allow_module('tempfile.NamedTemporaryFile')
    allow_module('collections')
    allow_module('base64')
    allow_module('socket')
    allow_module('fcntl')
    allow_module('struct')
    allow_module('array')
    allow_module('datetime')
    allow_module('datetime.datetime.timetuple')
    allow_module('PyPDF2')
    allow_module('pdfrw')
    allow_module('StringIO')
    allow_module('PIL')
    allow_module('uuid')
    allow_module('binascii')
    allow_module('re')

    tools = (SAPLTool.SAPLTool,)
    ToolInit('SAPL Tool',
                tools = tools,
                icon = 'tool.gif'
                ).initialize( context )

    context.registerClass( Portal.SAPL,
                           constructors=( Portal.manage_addSAPLForm,
                                          Portal.manage_addSAPL,),
                           icon='interlegisIcon.gif')

    context.registerClass( lexml.SAPLOAIServer.SAPLOAIServer,
                           constructors = ( SAPLOAIServer.manage_addSAPLOAIServerForm,
                                            SAPLOAIServer.manage_addSAPLOAIServer, ),
                            icon='oai_service.png')

