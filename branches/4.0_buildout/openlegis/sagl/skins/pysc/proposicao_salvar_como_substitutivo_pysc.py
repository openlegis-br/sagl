## Script (Python) "proposicao_salvar_como_substitutivo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao, cod_substitutivo, ind_sobrescrever=0
##title=
##
ok = 0
id = str(cod_substitutivo) + '_substitutivo.odt'
odt_proposicao = str(cod_proposicao) + '.odt'
pdf_proposicao = str(cod_proposicao) + '.pdf'

try:
    doc = context.sapl_documentos.substitutivo[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sapl_documentos.substitutivo.manage_delObjects(id)
        if hasattr(context.sapl_documentos.proposicao,odt_proposicao):
           tmp_copy = context.sapl_documentos.proposicao.manage_copyObjects(ids=str(cod_proposicao)+'.odt')
           tmp_id = context.sapl_documentos.substitutivo.manage_pasteObjects(tmp_copy)[0]['new_id']
           context.sapl_documentos.substitutivo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        if hasattr(context.sapl_documentos.proposicao,pdf_proposicao):
           context.sapl_documentos.proposicao.manage_delObjects(pdf_proposicao)
        for anexo in context.pysc.anexo_proposicao_pysc(cod_proposicao,listar=True):
           context.sapl_documentos.proposicao.manage_delObjects(anexo)
        ok = 1
except KeyError:
    if hasattr(context.sapl_documentos.proposicao,odt_proposicao):
       tmp_copy = context.sapl_documentos.proposicao.manage_copyObjects(ids=str(cod_proposicao)+ '.odt')
       tmp_id = context.sapl_documentos.substitutivo.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.substitutivo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    if hasattr(context.sapl_documentos.proposicao,pdf_proposicao):
       context.sapl_documentos.proposicao.manage_delObjects(pdf_proposicao)
    for anexo in context.pysc.anexo_proposicao_pysc(cod_proposicao,listar=True):
       context.sapl_documentos.proposicao.manage_delObjects(anexo)
    ok = 1
return ok
