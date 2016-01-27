## Script (Python) "obter_odt_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento, cod_materia, ind_sobrescrever=0
##title=
##
ok = 0
id = str(cod_documento) + '.odt'
try:
    doc = context.sapl_documentos.materia_odt[id]
    if (int(ind_sobrescrever)==1):
        doc=''     
        context.sapl_documentos.materia_odt.manage_delObjects(id)
        tmp_copy = context.sapl_documentos.materia_odt.manage_copyObjects(ids=str(cod_materia)+'_texto_integral.odt')
        tmp_id = context.sapl_documentos.materia_odt.manage_pasteObjects(tmp_copy)[0]['new_id']
        context.sapl_documentos.materia_odt.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
        ok = 1
except KeyError:
    tmp_copy = context.sapl_documentos.materia_odt.manage_copyObjects(ids=str(cod_materia)+ '_texto_integral.odt')
    tmp_id = context.sapl_documentos.materia_odt.manage_pasteObjects(tmp_copy)[0]['new_id']
    context.sapl_documentos.materia_odt.manage_renameObjects(ids=list([tmp_id]),new_ids=list([id]))
    ok = 1
