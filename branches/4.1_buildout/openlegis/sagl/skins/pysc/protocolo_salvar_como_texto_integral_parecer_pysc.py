## Script (Python) "protocolo_salvar_como_texto_integral_parecer_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_protocolo, cod_relatoria, ind_sobrescrever=1
##title=
##
ok = 0
id = str(cod_relatoria) + '_parecer.pdf'
try:
    doc = context.sapl_documentos.parecer_comissao[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sapl_documentos.parecer_comissao.manage_delObjects(id)
        tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=str(cod_protocolo)+'_protocolo.pdf')
        tmp_id = context.sapl_documentos.parecer_comissao.manage_pasteObjects(tmp_copy)[0]['new_id']
        context.sapl_documentos.parecer_comissao.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        ok = 1
except KeyError:
    tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=str(cod_protocolo)+ '_protocolo.pdf')
    tmp_id = context.sapl_documentos.parecer_comissao.manage_pasteObjects(tmp_copy)[0]['new_id']
    context.sapl_documentos.parecer_comissao.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    ok = 1
return ok
