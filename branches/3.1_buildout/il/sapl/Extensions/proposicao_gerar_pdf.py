## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer

def convertFile(self,cod_proposicao):
    # Conversao para PDF
    nom_arquivo_odt = "%s"%cod_proposicao+'.odt'
    nom_arquivo_pdf = "%s"%cod_proposicao+'.pdf'
    url = self.sapl_documentos.proposicao.absolute_url() + "/%s"%nom_arquivo_odt
    odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3')
    renderer.run()
    data = open(output_file_pdf, "rb").read()                 
    for file in [output_file_pdf]:
        self.sapl_documentos.proposicao.manage_addFile(id=file,file=file)
        os.unlink(file)
