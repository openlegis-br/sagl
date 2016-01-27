"""
SAPL setup handlers.
"""


def setupMountPoint(portal):
    # Metodo para adicionar o mount point do sapl_documentos
    if not hasattr(portal, 'sapl_documentos'):
        path_sapl = portal.getId()
        try:
            portal.manage_addProduct['ZODBMountPoint'].manage_addMounts(paths=["/%s/sapl_documentos" % path_sapl],create_mount_points=1)
        except:
            portal.manage_addProduct['OFSP'].manage_addFolder(id='sapl_documentos')


def setupConteudo(portal):
    # Metodo para a importacao do SAPL
    # estrutura do diretorio das materias legislativas
    if hasattr(portal, 'sapl_documentos'):
        for o in [
            'administrativo.zexp',
            'anexo_sessao.zexp',
            'ata_sessao.zexp',
            'emenda.zexp',
            'materia.zexp',
            'materia_odt.zexp',
            'modelo.zexp',
            'norma_juridica.zexp',
            'oradores.zexp',
            'oradores_expediente.zexp',
            'painel.zexp',
            'parecer_comissao.zexp',
            'parlamentar.zexp',
            'pauta_sessao.zexp',
            'proposicao.zexp',
            'props_sapl.zexp',
            'reuniao_comissao.zexp',
            'substitutivo.zexp',
        ]:
            if o[:len(o)-5] not in portal.sapl_documentos.objectIds():
                portal.sapl_documentos.manage_importObject(o)

    # importar conteudos na raiz do SAPL
#    for o in ['XSD.zexp','XSLT.zexp', 'modelo_proposicao.zexp', 'pdflabels.zexp', 'gerar_etiquetas_pdf.zexp']:
    for o in ['modelo_proposicao.zexp', 'pdflabels.zexp', 'gerar_etiquetas_pdf.zexp']:
        if o[:len(o)-5] not in portal.objectIds():
            portal.manage_importObject(o)


def setupAdicionarUsuarios(portal):
    # Metodo para criar usuario padrao
    portal.acl_users._addUser(name='saploper',password='saploper',confirm='saploper',roles=['Operador'],domains=[])
    portal.acl_users._addUser(name='sapllexml',password='sapllexml',confirm='sapllexml',roles=['Operador Lexml'],domains=[])
    portal.acl_users._addUser(name='sapladm',password='sapladm',confirm='sapladm',roles=['Administrador'],domains=[])


def setupAdicionaSPDO(portal):
    props = portal.sapl_documentos.props_sapl
    try:
        props.manage_addProperty('use_spdo', False, 'boolean')
    except:
        pass
    try:
        props.manage_addProperty('end_spdo', 'http://10.1.1.1:8380/spdo', 'string')
    except:
        pass

def setupAdicionaAcomp(portal):
    props = portal.sapl_documentos.props_sapl
    try:
        props.manage_addProperty('acompanhamento_materia', '1', 'int')
    except:
        pass


def importar_estrutura(context):
    if context.readDataFile('sapl-final.txt') is None:
        return
    site = context.getSite()
    setupMountPoint(site)
    setupConteudo(site)
    setupAdicionarUsuarios(site)
    setupAdicionaSPDO(site)
    setupAdicionaAcomp(site)
