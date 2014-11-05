## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer   
 
def createReport(self,inf_basicas_dic,nom_arquivo,nom_comissao, materia, nom_autor, txt_ementa, tip_apresentacao, tip_conclusao, data_parecer, nom_relator, lst_composicao,modelo_proposicao):
    # Criacao ODT
    url = self.sapl_documentos.modelo.materia.parecer.absolute_url() + "/%s"%modelo_proposicao
    template_file = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_odt = "%s"%nom_arquivo
    renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    renderer.run()                                                                             
    data = open(output_file_odt, "rb").read()                 
    for file in [output_file_odt]:
        os.unlink(file)
        self.sapl_documentos.parecer_comissao.manage_addFile(id=nom_arquivo,file=data)
    #self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
    #self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
    #return data 
