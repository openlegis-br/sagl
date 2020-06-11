## Script (Python) "protocolo_salvar_como_texto_integral_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_protocolo, cod_materia, ind_sobrescrever=1
##title=
##
ok = 0
id = str(cod_materia) + '_texto_integral_signed.pdf'
try:
    doc = context.sagl_documentos.materia[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sagl_documentos.materia.manage_delObjects(id)
        tmp_copy = context.sagl_documentos.protocolo.manage_copyObjects(ids=str(cod_protocolo)+'_protocolo_signed.pdf')
        tmp_id = context.sagl_documentos.materia.manage_pasteObjects(tmp_copy)[0]['new_id']
        context.sagl_documentos.materia.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        ok = 1
except KeyError:
    tmp_copy = context.sagl_documentos.protocolo.manage_copyObjects(ids=str(cod_protocolo)+ '_protocolo_signed.pdf')
    tmp_id = context.sagl_documentos.materia.manage_pasteObjects(tmp_copy)[0]['new_id']
    context.sagl_documentos.materia.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    ok = 1
return ok