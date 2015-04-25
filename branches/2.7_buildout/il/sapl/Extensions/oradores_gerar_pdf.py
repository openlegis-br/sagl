## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer

def convertFile(self,cod_sessao_plen):
    # Conversao para PDF
    nom_arquivo_odt = "%s"%cod_sessao_plen+'_oradores_expediente.odt'
    nom_arquivo_pdf = "%s"%cod_sessao_plen+'_oradores_expediente.pdf'
    url = self.sapl_documentos.oradores_expediente.absolute_url() + "/%s"%nom_arquivo_odt
    odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    renderer.run()
    data = open(output_file_pdf, "rb").read()
    for file in [output_file_pdf]:
        self.sapl_documentos.oradores_expediente.manage_addFile(id=file,title=file,file=file)
        os.unlink(file)


