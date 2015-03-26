## Script (Python) "documento_acessorio_materia_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_documento='', listar=None, nomear=None
##title=
##

if listar:
    documentos = context.sagl_documentos.materia.objectIds()
    existentes = [documento for documento in documentos if documento.startswith(cod_documento) and len(documento) == len(cod_documento) or documento.startswith(cod_documento + '_') and not 'texto_integral' in documento]
    return existentes

if nomear:
    documentos = context.sagl_documentos.materia.objectIds()
    existentes = [documento for documento in documentos if documento.startswith(cod_documento) and len(documento) == len(cod_documento) or documento.startswith(cod_documento + '_') and not 'texto_integral' in documento]
    count = 1
    while True:
        nome = cod_documento + '_' + str(count)
        if nome not in existentes:
            return nome
            break
        else:
            count+=1
