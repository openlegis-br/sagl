## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer   
 
def createReport(self,inf_basicas_dic,nom_arquivo,des_tipo_documento,nom_documento,txt_ementa,dat_documento,data_documento,nom_autor,materia_vinculada,modelo_proposicao):
    # Criacao ODT
    url = self.sapl_documentos.modelo.materia.documento_acessorio.absolute_url() + "/%s"%modelo_proposicao
    template_file = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_odt = "%s"%nom_arquivo
    renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python',forceOoCall=True)
    renderer.run()                                                                             
    data = open(output_file_odt, "rb").read()                 
    for file in [output_file_odt]:
        os.unlink(file)
        self.sapl_documentos.materia_odt.manage_addFile(id=nom_arquivo,file=data)
