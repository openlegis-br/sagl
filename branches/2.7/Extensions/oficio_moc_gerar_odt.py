## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer  
 
def createReport(self, inf_basicas_dic, num_ident_basica, nom_autor):
    # Criacao ODT
    url = self.sapl_documentos.modelo.documento_administrativo.absolute_url() + "/oficio_mocao.odt"
    template_file = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_odt = "oficio_mocao.odt"
    renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python',forceOoCall=True)
    renderer.run()                          
    data = open(output_file_odt, "rb").read()                 
    for file in [output_file_odt]:
        os.unlink(file)                                                                                                      
    self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
    self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
    return data 
