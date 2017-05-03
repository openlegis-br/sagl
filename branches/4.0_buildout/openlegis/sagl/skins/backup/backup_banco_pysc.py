## Script (Python) "backup_banco_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION
nome="bkpbancosagl"

# Faz o backup do banco de dados como 'bkpbancosagl.sql' no diretório var do Zope
dump_banco = context.banco_backup(banco='openlegis',usuario='root',nome=nome)

if dump_banco[0]==1: #Se ocorrer erro, retorna-o.
   retorno=dump_banco[1]
else: #Se não, exporta a pasta documentos
   context.documentos.manage_exportObject()
   retono='Foram gerados os arquivos \'%s.sql\' e \'documentos.zexp\' na pasta var da instancia do Zope do SAGL.'%nome

#Retorna a mensagem
return response.redirect('backup_sagl?banco=%s' % retorno)
