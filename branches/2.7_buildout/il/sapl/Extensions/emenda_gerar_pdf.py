## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer

def convertFile(self,cod_emenda):
    # Conversao para PDF
    nom_arquivo_odt = "%s"%cod_emenda+'_emenda.odt'
    nom_arquivo_pdf = "%s"%cod_emenda+'_emenda.pdf'
    url = self.sapl_documentos.emenda.absolute_url() + "/%s"%nom_arquivo_odt
    odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    renderer.run()
    data = open(output_file_pdf, "rb").read()                 
    for file in [output_file_pdf]:
        self.sapl_documentos.emenda.manage_addFile(id=file,title=file,file=file)
        os.unlink(file)
