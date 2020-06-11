"""
SAGL - OpenLegis setup handlers.
"""

def setupMountPoint(portal):
    # Metodo para adicionar o mount point do sagl_documentos
    if not hasattr(portal, 'sagl_documentos'):
        path_sagl = portal.getId()
        try:
            portal.manage_addProduct['ZODBMountPoint'].manage_addMounts(paths=["/%s/sagl_documentos" % path_sagl],create_mount_points=1)
        except:
            portal.manage_addProduct['OFSP'].manage_addFolder(id='sagl_documentos')

def setupConteudo(portal):
    # Metodo para a importacao do SAGL-OpenLegis
    # estrutura do diretorio para armazenamento de documentos
    if hasattr(portal, 'sagl_documentos'):
        for o in [
            'administrativo.zexp',
            'ata_sessao.zexp',
            'documento_comissao.zexp',
            'documentos_assinados.zexp',
            'emenda.zexp',
            'materia.zexp',
            'materia_odt.zexp',
            'modelo.zexp',
            'norma_juridica.zexp',
            'oradores.zexp',
            'oradores_expediente.zexp',
            'parecer_comissao.zexp',
            'parlamentar.zexp',
            'pauta_sessao.zexp',
            'partido.zexp',
            'pessoa.zexp',
            'proposicao.zexp',
            'props_sagl.zexp',
            'protocolo.zexp',
            'reuniao_comissao.zexp',
            'substitutivo.zexp',
        ]:
            if o[:len(o)-5] not in portal.sagl_documentos.objectIds():
                portal.sagl_documentos.manage_importObject(o)

    # importar conteudos na raiz do SAGL - OpenLegis
    for o in ['modelo_proposicao.zexp', 'webeditor.zexp', 'pdflabels.zexp', 'gerar_etiquetas_pdf.zexp', 'upload_form.zexp', 'trigger_upload.zexp']:
        if o[:len(o)-5] not in portal.objectIds():
            portal.manage_importObject(o)


def setupAdicionarUsuarios(portal):
    # Metodo para criar usuario padrao
    portal.acl_users._addUser(name='openlegis', password='openlegis', confirm='openlegis', roles=['Operador','Administrador'], domains=[])
    portal.acl_users._addUser(name='lexml',password='lexml',confirm='lexml',roles=['Operador Lexml'],domains=[])
    

def setupAdicionaAcomp(portal):
    props = portal.sagl_documentos.props_sagl
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
