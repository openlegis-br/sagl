## Script (Python) "proposicao_guardar_odt_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao
##title=
##
ok = 0
odt_proposicao = str(cod_proposicao) + '.odt'
id = str(cod_proposicao) + '_original.odt'
ind_sobrescrever = 1

try:
    doc = context.sapl_documentos.proposicao[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sapl_documentos.proposicao.manage_delObjects(id)
        if hasattr(context.sapl_documentos.proposicao,odt_proposicao):
           tmp_copy = context.sapl_documentos.proposicao.manage_copyObjects(ids=str(cod_proposicao)+'.odt')
           tmp_id = context.sapl_documentos.proposicao.manage_pasteObjects(tmp_copy)[0]['new_id']
           context.sapl_documentos.proposicao.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        ok = 1
except KeyError:
    if hasattr(context.sapl_documentos.proposicao,odt_proposicao):
       tmp_copy = context.sapl_documentos.proposicao.manage_copyObjects(ids=str(cod_proposicao)+ '.odt')
       tmp_id = context.sapl_documentos.proposicao.manage_pasteObjects(tmp_copy)[0]['new_id']
       context.sapl_documentos.proposicao.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    ok = 1

#return ok
