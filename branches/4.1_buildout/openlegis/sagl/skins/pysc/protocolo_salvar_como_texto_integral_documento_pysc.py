## Script (Python) "protocolo_salvar_como_texto_integral_documento_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_protocolo, cod_documento, ind_sobrescrever=1
##title=
##
ok = 1
id = str(cod_documento) + '_texto_integral.pdf'

try:
    doc = context.sapl_documentos.administrativo[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sapl_documentos.administrativo.manage_delObjects(id)
        tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=str(cod_protocolo)+'_protocolo.pdf')
        tmp_id = context.sapl_documentos.administrativo.manage_pasteObjects(tmp_copy)[0]['new_id']
        context.sapl_documentos.administrativo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        documento = getattr(context.sapl_documentos.administrativo,id)
        documento.manage_permission('View', roles=['Authenticated', 'Manager'], acquire=0)
        ok = 1
except KeyError:
    tmp_copy = context.sapl_documentos.protocolo.manage_copyObjects(ids=str(cod_protocolo)+ '_protocolo.pdf')
    tmp_id = context.sapl_documentos.administrativo.manage_pasteObjects(tmp_copy)[0]['new_id']
    context.sapl_documentos.administrativo.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    ok = 1
return ok

