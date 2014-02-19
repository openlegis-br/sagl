## Script (Python) "proposicao_calcular_checksum_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_proposicao
##title=
##
txtint_path = 'sapl_documentos/proposicao/' + str(cod_proposicao) + '.odt'
try:
  txtint = context.restrictedTraverse (txtint_path)

  if (txtint.meta_type == 'SDE-Document'):
    x = txtint.checksum()
  else:
    from zlib import crc32
    x = crc32(str(txtint))

  if (x>=0):
    c='P' + str(x)
  else:
    c='M' + str(-1 * x)
except:
  c = 'Doc. Invalido!'
c = c + '/' + str(cod_proposicao)
return c
