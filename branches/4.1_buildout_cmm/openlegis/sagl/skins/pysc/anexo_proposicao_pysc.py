## Script (Python) "anexo_proposicao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao, listar=None, nomear=None
##title=
##
if listar:
    documentos = context.sapl_documentos.proposicao.objectIds()
    existentes = []
    for documento in documentos:
        if documento.startswith(cod_proposicao) and len(documento) == len(cod_proposicao) or documento.startswith(cod_proposicao + '_anexo_'):
           dic = {}
           dic['nom_documento'] = documento
           nome_arquivo = string.split(documento,'.')[0]
           dic['sequencia'] = string.split(nome_arquivo,'_')[2].zfill(2)
           existentes.append(dic)
    existentes.sort(key=lambda dic: dic['sequencia'])
    lista = []
    for dic in existentes:
        nome = dic.get('nom_documento',dic)
        lista.append(nome)   
    existentes = lista
    return existentes

if nomear:
    documentos = context.sapl_documentos.proposicao.objectIds()
    existentes = [documento for documento in documentos if documento.startswith(cod_proposicao) and len(documento) == len(cod_proposicao) or documento.startswith(cod_proposicao + '_anexo_')]
    count = 1
    while True:
        nome = cod_proposicao + '_anexo_' + str(count)+ '.pdf'
        if nome not in existentes:
            return nome
            break
        else:
            count+=1
