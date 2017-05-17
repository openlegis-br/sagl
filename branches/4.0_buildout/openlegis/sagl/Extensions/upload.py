# -*- coding: utf-8 -*-
import sys, os, string
def uploadFiles(context):
    ''' upload all files in file pointed to by the request
    parameter "uploadDir" into the folder "context"
    "uploadDir" should be a valid pathname on the local file system
    containing only files
    '''
    msg = []
    files = []
    filename = context.REQUEST['uploadDir']
    try:
       files = os.listdir(filename)
    except:
       msg.append('<h2>Não há arquivos no caminho ' +filename+'</h2>')
    for file in files:
       fd = open(filename+os.sep+file,'r')
       arquivo = fd.read()
       fd.close()
       if file in context:
          documento = getattr(context,file)
          documento.manage_upload(file=arquivo)
          msg.append('<li> Arquivo '+file+' == atualizado </li>')
       else:
          context.manage_addFile(id=file,file=arquivo)
          msg.append('<li> Arquivo '+file+' ++ adicionado </li>')
    return '<html><head></head><body><ul>'+string.join(msg)+'</ul></body></html>'

