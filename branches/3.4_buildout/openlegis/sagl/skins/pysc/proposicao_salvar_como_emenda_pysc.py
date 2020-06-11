## Script (Python) "proposicao_salvar_como_emenda_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao, cod_emenda, ind_sobrescrever=0
##title=
##
ok = 0
id = str(cod_emenda) + '_emenda.odt'
odt_proposicao = str(cod_proposicao) + '.odt'
pdf_proposicao = str(cod_proposicao) + '.pdf'

try:
    doc = context.sagl_documentos.emenda[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sagl_documentos.emenda.manage_delObjects(id)
        if hasattr(context.sagl_documentos.proposicao,odt_proposicao):
           tmp_copy = context.sagl_documentos.proposicao.manage_copyObjects(ids=str(cod_proposicao)+'.odt')
           tmp_id = context.sagl_documentos.emenda.manage_pasteObjects(tmp_copy)[0]['new_id']
           context.sagl_documentos.emenda.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        if hasattr(context.sagl_documentos.proposicao,pdf_proposicao):
           context.sagl_documentos.proposicao.manage_delObjects(pdf_proposicao)
        for anexo in context.pysc.anexo_proposicao_pysc(cod_proposicao,listar=True):
           context.sagl_documentos.proposicao.manage_delObjects(anexo)
        ok = 1
except KeyError:
    if hasattr(context.sagl_documentos.proposicao,odt_proposicao):
       tmp_copy = context.sagl_documentos.proposicao.manage_copyObjects(ids=str(cod_proposicao)+ '.odt')
       tmp_id = context.sagl_documentos.emenda.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sagl_documentos.emenda.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    if hasattr(context.sagl_documentos.proposicao,pdf_proposicao):
       context.sagl_documentos.proposicao.manage_delObjects(pdf_proposicao)
    for anexo in context.pysc.anexo_proposicao_pysc(cod_proposicao,listar=True):
       context.sagl_documentos.proposicao.manage_delObjects(anexo)
    ok = 1
return ok
