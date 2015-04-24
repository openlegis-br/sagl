"""
SAGL setup handlers.
"""

def setupMountPoint(portal):
    # Metodo para adicionar o mount point do sagl_documentos
    path_sagl = portal.getId()
    try:
        portal.manage_addProduct['ZODBMountPoint'].manage_addMounts(paths=["/%s/sagl_documentos" % path_sagl],create_mount_points=1)
    except:
        portal.manage_addProduct['OFSP'].manage_addFolder(id='sagl_documentos')


def setupConteudo(portal):
    # Metodo para a importacao do SAGL
    # estrutura do diretorio das materias legislativas
    if hasattr(portal, 'sagl_documentos'):
        for o in [
            'anexo_sessao.zexp',
            'administrativo.zexp',
            'ata_sessao.zexp',
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
            'props_sagl.zexp',
            'reuniao_comissao.zexp',
        ]:
            portal.sagl_documentos.manage_importObject(o)

    # importar conteudos na raiz do SAGL
#    for o in ['XSD.zexp','XSLT.zexp', 'modelo_proposicao.zexp', 'pdflabels.zexp', 'gerar_etiquetas_pdf.zexp']:
    for o in ['modelo_proposicao.zexp', 'pdflabels.zexp', 'gerar_etiquetas_pdf.zexp']:
        if o[:len(o)-5] not in portal.objectIds():
            portal.manage_importObject(o)


def setupAdicionarUsuarios(portal):
    # Metodo para criar usuario padrao
    portal.acl_users._addUser(name='operador',password='operador',confirm='operador',roles=['Operador'],domains=[])
    portal.acl_users._addUser(name='lexml',password='lexml',confirm='lexml',roles=['Operador Lexml'],domains=[])
    portal.acl_users._addUser(name='administrador',password='administrador',confirm='administrador',roles=['Administrador'],domains=[])


def importar_estrutura(context):
    if context.readDataFile('sagl-final.txt') is None:
        return
    site = context.getSite()
    setupMountPoint(site)
    setupConteudo(site)
    setupAdicionarUsuarios(site)
