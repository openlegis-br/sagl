## encoding: utf-8 
import os, urllib, cStringIO
from appy.pod.renderer import Renderer   
 
def createReport(self, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_reqplen, lst_reqpres, lst_indicacao, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, lst_psecretario, lst_ssecretario):
    # Criacao ODT
    url = self.sapl_documentos.modelo.sessao_plenaria.absolute_url() + "/ata.odt"
    template_file = cStringIO.StringIO(urllib.urlopen(url).read())
    output_file_odt = "ata_sessao.odt"
    renderer = Renderer(template_file, locals(), output_file_odt, pythonWithUnoPath='/usr/bin/python3',forceOoCall=True)
    renderer.run()                                                                            
    data = open(output_file_odt, "rb").read()                 
    for file in [output_file_odt]:
        os.unlink(file)                                                                                                      
    self.REQUEST.RESPONSE.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
    self.REQUEST.RESPONSE.headers['Content-Disposition'] = 'attachment; filename="%s"'%output_file_odt
    return data 
