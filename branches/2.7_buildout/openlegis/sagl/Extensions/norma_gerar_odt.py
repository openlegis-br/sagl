## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer   
 
def createReport(self,inf_basicas_dic,nom_arquivo,des_tipo_norma,num_norma,ano_norma,dat_norma,data_norma,txt_ementa,modelo_norma):
    # Criacao ODT
    url = self.sagl_documentos.modelo.norma.absolute_url() + "/%s"%modelo_norma
    template_file = cStringIO.StringIO(urllib.urlopen(url).read())
    #output_file_odt = os.path.normpath(nom_arquivo_odt)
    output_file_odt = "%s"%nom_arquivo
    renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    renderer.run()                                                                             
    data = open(output_file_odt, "rb").read()                 
    for file in [output_file_odt]:
        os.unlink(file)
        self.sagl_documentos.norma_juridica.manage_addFile(id=nom_arquivo,file=data)
