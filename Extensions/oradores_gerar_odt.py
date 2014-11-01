## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer

def createReport(self, inf_basicas_dic, lst_oradores, lst_presidente, nom_arquivo):
    # Criacao ODT
    url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/oradores.odt"
    template_file = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_odt = "%s"%nom_arquivo
    renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    renderer.run()
    data = open(output_file_odt, "rb").read()
    for file in [output_file_odt]:
        os.unlink(file)
        self.sapl_documentos.oradores_expediente.manage_addFile(id=output_file_odt,file=data)

