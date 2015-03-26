## Script (Python) "anexos_sessao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen='', listar=None, nomear=None
##title=
##

if listar:
    if not 'anexos_sessao' in context.sagl_documentos.objectIds():
        import pdb;pdb.set_trace()

    else:
        anexos_sessao = context.sagl_documentos.anexos_sessao.anexos_sessao.objectIds()
        return anexos_sessao

if nomear:
    anexos_sessao = context.sagl_documentos.anexos_sessao.anexos_sessao.objectIds()
    count = 1
    while True:
        nome = cod_sessao_plen + '_' + 'anexo_sessao_' + str(count)
        if nome not in anexos_sessao:
            return nome
            break
        else:
            count+=1
