from Products.ILSAPL.config import GLOBALS
from Products.CMFDefault.Portal import CMFSite

from Products.CMFCore.permissions import AccessContentsInformation, ListFolderContents, ManageProperties, View
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault import Portal, DublinCore
import Globals, csv

from Products.ZODBMountPoint.MountedObject import manage_addMounts

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base
from ComputedAttribute import ComputedAttribute

class SAPL(CMFSite):
    """
    Inicia um novo OpenLegis baseado em um CMFSite.
    """
    security=ClassSecurityInfo()
    meta_type = portal_type = 'SAPL'

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


Globals.InitializeClass(SAPL)

class SAPLGenerator(Portal.PortalGenerator):

    klass = SAPL

    # Metodo para adicionar o mount point do sapl_documentos
    def setupMountPoint(self, p):
        path_sapl = p.getId()
        try:
            p.manage_addProduct['ZODBMountPoint'].manage_addMounts(paths=["/%s/sapl_documentos" % path_sapl],create_mount_points=1)
        except:
            p.manage_addProduct['OFSP'].manage_addFolder(id='sapl_documentos')

    # Metodo para a importacao do OpenLegis
    def setupConteudo(self, p):        
        # estrutura do diretorio de armazenamento de documentos
        for o in ['props_sapl.zexp','administrativo.zexp','ata_sessao.zexp','modelo.zexp','proposicao.zexp','parlamentar.zexp','materia.zexp','materia_odt.zexp','norma_juridica.zexp','pauta_sessao.zexp','reuniao_comissao.zexp','parecer_comissao.zexp','oradores_expediente.zexp','oradores.zexp','emenda.zexp', 'substitutivo.zexp']:
            p.sapl_documentos.manage_importObject(o)

        # importar conteudos na raiz do sistema
        for o in ['modelo_proposicao.zexp','pdflabels.zexp','gerar_etiquetas_pdf.zexp']:
            p.manage_importObject(o)

    # Metodo para configurar a skin
    def setupSAPLSkins(self, p):
        sk_tool = getToolByName(p, 'portal_skins')

        # pega a definicao da skin layer basica do cmf
        path=[elem.strip() for elem in sk_tool.getSkinPath('Basic').split(',')]

        # retira as layers padroes do cmf
        existing_layers=sk_tool.objectIds()
        cmfdefault_layers=('zpt_topic', 'zpt_content', 'zpt_generic',
                           'zpt_control', 'topic', 'content', 'generic',
                           'control', 'Images', 'no_css', 'nouvelle')
        for layer in cmfdefault_layers:
            # tenha certeza que ira remover apenas se a layer nao existir
            # ou se ela eh um Filesystem Directory View
            # para prevenir a exclusao de custom layers
            remove = 0
            l_ob = getattr(sk_tool, layer, None)
            if not l_ob or getattr(l_ob, 'meta_type', None) == \
                   'Filesystem Directory View':
                remove = 1
            # remove da definicao de layer
            if layer in path and remove: path.remove(layer)
            # remove da skin tool
            if layer in existing_layers and remove:
                sk_tool.manage_delObjects(ids=[layer])

        # adiciona a layer do Openlegis
        sapldir = 'sk_sapl'
        if sapldir not in path:
            try:
                path.insert( path.index( 'custom')+1, sapldir )
            except ValueError:
                path.append( sapldir )

        path=','.join(path)
        sk_tool.addSkinSelection('SAPL', path, make_default=1)

        addDirectoryViews( sk_tool, 'skins', GLOBALS )

        skins_map=sk_tool._getSelections()

        if skins_map.has_key('No CSS'):
            del skins_map['No CSS']
        if skins_map.has_key('Nouvelle'):
            del skins_map['Nouvelle']
        if skins_map.has_key('Basic'):
            del skins_map['Basic']
        sk_tool.selections=skins_map

    # Metodo para inserir as novas roles.
    def setupRoles(self, p):
        p.__ac_roles__ = ('Administrador','Autor','Operador Lexml','Operador Sessao Plenaria','Operador','Operador Parlamentar','Operador Norma','Operador Tabela Auxiliar','Operador Mesa Diretora','Operador Comissao','Operador Materia','Operador Protocolo','Operador Modulo Administrativo','Assessor Parlamentar','Operador Arquivo')

    # Metodo para criar usuario padrao
    def setupAdicionarUsuarios(self, p):
        p.acl_users._addUser(name='operador',password='operador',confirm='operador',roles=['Operador'],domains=[])
        p.acl_users._addUser(name='lexml',password='lexml',confirm='lexml',roles=['Operador Lexml'],domains=[])
        p.acl_users._addUser(name='administrador',password='administrador',confirm='administrador',roles=['Administrador'],domains=[])

        
    # Metodo para criacao da conexao do banco de dados
    def setupDatabase(self, p, database):
        if database == 'MySQL':
            p.manage_addProduct['ZMySQLDA'].manage_addZMySQLConnection(id='dbcon_interlegis',title='Banco de Dados OpenLegis (MySQL)',connection_string='interlegis sapl sapl',check=True,use_unicode=True,auto_create_db=False)
        else:
            p.manage_addProduct['ZPsycopgDA'].manage_addZPsycopgConnection(id='dbcon_interlegis',title='Banco de Dados OpenLegis (PostgreSQL)',connection_string='dbname=interlegis user=sapl password=sapl host=localhost')
    
    # Metodo para adicao da tool
    def setupTool(self, p):
        p.manage_addProduct['ILSAPL'].manage_addTool(type="SAPL Tool")

    def setupSAPL(self, p):
        self.setupMountPoint(p)
        self.setupConteudo(p)
        self.setupSAPLSkins(p)
        self.setupRoles(p)
        self.setupAdicionarUsuarios(p)
        self.setupTool(p)

    def create(self, parent, id, create_userfolder):
        id = str(id)
        portal = self.klass(id=id)
        parent._setObject(id, portal)
        p = parent.this()._getOb(id)
        self.setup(p, create_userfolder)
        self.setupSAPL(p)
        return p

from Products.PageTemplates.PageTemplateFile import PageTemplateFile

manage_addSAPLForm = PageTemplateFile('www/addSAPL', globals())
manage_addSAPLForm.__name__ = 'addSAPL'

def manage_addSAPL(self, id, title='Sistema Aberto de Gestão Legislativa', description='',
                   create_userfolder=1, database='MySQL',
                   RESPONSE=None):
    """ Adicionar uma instancia OpenLegis.
    """
    gen = SAPLGenerator()
    id = id.strip()
    p = gen.create(self, id, create_userfolder)
    
    # cria a conexao com o banco de dados
    gen.setupDatabase(p, database)

    if RESPONSE is not None:
        RESPONSE.redirect(p.absolute_url())
