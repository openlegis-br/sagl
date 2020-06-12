## Script (Python) "proposicao_tipo_texto_integral_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao
##title=
##
try:
    if (context.sapl_documentos.proposicao[cod_proposicao].meta_type == 'File'):
        return 'ODT'
    else:
        return 'ArqExt'
except:
    return ''
