# -*- coding: utf-8 -*-
import sys, os, string
import shutil
import zipfile
def baixar_pdf(context):
    cod_sessao_plen = context.REQUEST['cod_sessao_plen']
    foldername =  str(cod_sessao_plen) + '_ind'
    zipname =  str(cod_sessao_plen) + '_ind.zip'
    dirpath = os.path.join('/tmp/', foldername)
    if not os.path.exists(dirpath):
       os.makedirs(dirpath)
    for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
        if item.cod_materia != None:
           for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,ind_excluido=0):
               if materia.des_tipo_materia == 'Indicação':
                  nom_pdf = str(materia.cod_materia) + "_texto_integral.pdf"
                  if hasattr(context.sapl_documentos.materia, nom_pdf):
                     arq = getattr(context.sapl_documentos.materia, nom_pdf)
                     f = open(os.path.join(dirpath) + '/' + nom_pdf, 'wb').write(arq.data)

    if os.path.exists(dirpath):
       file_paths = []
       for root, directories, files in os.walk(dirpath):
           for filename in files:
               filepath = os.path.join(root, filename)
               file_paths.append(filepath)
       with zipfile.ZipFile('/tmp/' + zipname,'w') as zip:
           for file in file_paths:
               zip.write(file)
              
       download = open('/tmp/' + zipname, 'rb')
       arquivo = download.read()
       context.REQUEST.RESPONSE.headers['Content-Type'] = 'application/zip'
       context.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%zipname

    if os.path.exists(dirpath) and os.path.isdir(dirpath):
       shutil.rmtree(dirpath)
       file = '/tmp/'+zipname
       os.unlink(file)
       
    return arquivo

