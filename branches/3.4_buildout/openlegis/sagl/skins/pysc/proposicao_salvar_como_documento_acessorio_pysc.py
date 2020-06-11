## Script (Python) "proposicao_salvar_como_documento_acessorio_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao, cod_documento, ind_sobrescrever=0
##title=
##
ok = 0
id = str(cod_documento) + '.odt'
odt_proposicao = str(cod_proposicao) + '.odt'
pdf_proposicao = str(cod_proposicao) + '.pdf'

try:
    doc = context.sagl_documentos.materia_odt[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sagl_documentos.materia_odt.manage_delObjects(id)
        if hasattr(context.sagl_documentos.proposicao,odt_proposicao):
           tmp_copy = context.sagl_documentos.proposicao.manage_cutObjects(ids=str(cod_proposicao)+'.odt')
           tmp_id = context.sagl_documentos.materia_odt.manage_pasteObjects(tmp_copy)[0]['new_id']
           context.sagl_documentos.materia_odt.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        if hasattr(context.sagl_documentos.proposicao,pdf_proposicao):
           context.sagl_documentos.proposicao.manage_delObjects(pdf_proposicao)
        for anexo in context.pysc.anexo_proposicao_pysc(cod_proposicao,listar=True):
           context.sagl_documentos.proposicao.manage_delObjects(anexo)
        ok = 1
except KeyError:
    if hasattr(context.sagl_documentos.proposicao,odt_proposicao):
       tmp_copy = context.sagl_documentos.proposicao.manage_cutObjects(ids=str(cod_proposicao)+ '.odt')
       tmp_id = context.sagl_documentos.materia_odt.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sagl_documentos.materia_odt.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    if hasattr(context.sagl_documentos.proposicao,pdf_proposicao):
       context.sagl_documentos.proposicao.manage_delObjects(pdf_proposicao)
    for anexo in context.pysc.anexo_proposicao_pysc(cod_proposicao,listar=True):
       context.sagl_documentos.proposicao.manage_delObjects(anexo)
    ok = 1
return ok
