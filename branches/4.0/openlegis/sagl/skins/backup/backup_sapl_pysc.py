## Script (Python) "backup_sagl_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=pasta
##title=
##
request=context.REQUEST
response=request.RESPONSE
session= request.SESSION
nome="bkpbancosagl"

import os
import App.FindHomes
#diretorio_instancia = App.FindHomes.INSTANCE_HOME
diretorio_var = App.FindHomes.CLIENT_HOME
#executa o comando mysqldump
dumpBanco=os.system('mysqldump -uroot interlegis >  '+diretorio_var+'/dados.sql')

#nome do arquivo composto da hora e da data
data=string.split( DateTime().ISO(),' ')[0]
data=string.split( data,'-')[0]+string.split( data,'-')[1]+string.split( data,'-')[2]
horas=string.split( DateTime().ISO(),' ')[1]
horas=string.split( horas,':')[0]+string.split( horas,':')[1]+string.split( horas,':')[2]
nome=data+'_'+horas+'_'+'bkpsagl.tgz'

#empacota dados
caminho='tar -zcvf '+pasta+nome+' '+diretorio_var+'/DocumentosSapl.fs '+diretorio_var+'/dados.sql'
documentos=os.system(caminho)

remover=os.system('rm '+diretorio_var+'/dados.sql')
if dumpBanco==0:
  if documentos==0:
    return 'Backup concluido!  <a href="javascript:history.go(-1)">[ Voltar ]</a>'
  else:
    return 'Problemas no salvamento dos documentos.  <a href="javascript:history.go(-1)">[ Voltar ]</a>'
else: 
  return 'Salvamento de dados do banco falhou. Tente novamente! <a href="javascript:history.go(-1)">[ Voltar ]</a>'

