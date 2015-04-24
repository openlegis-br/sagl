## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer

def convertFile(self,cod_materia):
    # Conversao para PDF
    nom_arquivo_odt = "%s"%cod_materia+'_texto_integral.odt'
    nom_arquivo_pdf = "%s"%cod_materia+'_texto_integral.pdf'
    url = self.sagl_documentos.materia_odt.absolute_url() + "/%s"%nom_arquivo_odt
    odtFile = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_pdf = os.path.normpath(nom_arquivo_pdf)
    renderer = Renderer(odtFile,locals(),output_file_pdf,pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    renderer.run()
    data = open(output_file_pdf, "rb").read()                 
    for file in [output_file_pdf]:
        self.sagl_documentos.materia.manage_addFile(id=file,file=file)
        os.unlink(file)

