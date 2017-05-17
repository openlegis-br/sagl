"""
SAGL-OpenLegis setup handlers.
"""

def setupMountPoint(portal):
    # Metodo para adicionar o mount point de documentos
    if not hasattr(portal, 'documentos'):
        path_sagl = portal.getId()
        try:
            portal.manage_addProduct['ZODBMountPoint'].manage_addMounts(paths=["/%s/documentos" % path_sagl],create_mount_points=1)
        except:
            portal.manage_addProduct['OFSP'].manage_addFolder(id='documentos')

def setupConteudo(portal):
    # Metodo para a importacao do SAGL-OpenLegis
    # estrutura do diretorio para armazenamento de documentos
    if hasattr(portal, 'documentos'):
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
            'propriedades.zexp',
            'protocolo.zexp',
            'reuniao_comissao.zexp',
            'substitutivo.zexp',
        ]:
            if o[:len(o)-5] not in portal.documentos.objectIds():
                portal.documentos.manage_importObject(o)

    # importar conteudos na raiz do SAGL-OpenLegis
    for o in ['modelo_proposicao.zexp', 'webeditor.zexp', 'pdflabels.zexp', 'gerar_etiquetas_pdf.zexp', 'upload_form.zexp', 'trigger_upload.zexp']:
        if o[:len(o)-5] not in portal.objectIds():
            portal.manage_importObject(o)

def setupAdicionarUsuarios(portal):
    # Metodo para criar usuario padrao
    portal.acl_users._addUser(name='operador',password='openlegis',confirm='openlegis',roles=['Operador'],domains=[])
    portal.acl_users._addUser(name='lexml',password='openlegis',confirm='openlegis',roles=['Operador Lexml'],domains=[])
    portal.acl_users._addUser(name='administrador',password='openlegis',confirm='openlegis',roles=['Administrador'],domains=[])

def setupAdicionaAcomp(portal):
    props = portal.documentos.propriedades
    try:
        props.manage_addProperty('acompanhamento_materia', '1', 'int')
    except:
        pass

def importar_estrutura(context):
    if context.readDataFile('sagl-final.txt') is None:
        return
    site = context.getSite()
    setupMountPoint(site)
    setupConteudo(site)
    setupAdicionarUsuarios(site)
    setupAdicionaAcomp(site)
