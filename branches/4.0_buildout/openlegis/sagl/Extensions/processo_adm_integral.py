# -*- coding: utf-8 -*-
import os
import cStringIO
from DateTime import DateTime
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
#from PyPDF4 import PdfFileWriter, PdfFileReader, PdfFileMerger
#from PyPDF4.utils import PdfReadError
from pdfrw import PdfReader, PdfWriter, PageMerge, IndirectPdfDict

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def processo_adm_gerar_pdf(context):
    cod_documento = context.REQUEST['cod_documento']

    writer = PdfFileWriter()
    merger = PdfFileMerger(strict=False)
    for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
       nom_pdf_amigavel = documento.sgl_tipo_documento+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+'.pdf'
       id_processo = documento.sgl_tipo_documento+' '+str(documento.num_documento)+'/'+str(documento.ano_documento)
    nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
    pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
    capa = cStringIO.StringIO(str(context.modelo_proposicao.capa_processo_adm(cod_documento=cod_documento)))
    texto_capa = capa
    merger.append(texto_capa)
    if hasattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf'):
       arq = getattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf')
       arquivo = cStringIO.StringIO(str(arq.data))
       texto_documento = PdfFileReader(arquivo)
       merger.append(texto_documento)
    elif hasattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf'):
       arq = getattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf')
       arquivo = cStringIO.StringIO(str(arq.data))
       texto_documento = PdfFileReader(arquivo)
       merger.append(texto_documento)
    anexos = []
    for docvinculado in context.zsql.documento_administrativo_vinculado_obter_zsql(cod_documento_vinculante=documento.cod_documento, ind_excluido=0):
       if hasattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf'):
          dic_anexo = {}
          dic_anexo["data"] = DateTime(docvinculado.dat_documento_vinculado, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          if docvinculado.num_protocolo_vinculado != '' and docvinculado.num_protocolo_vinculado != None:
             for protocolo in context.zsql.protocolo_obter_zsql(num_protocolo=docvinculado.num_protocolo_vinculado, ano_protocolo=docvinculado.ano_documento_vinculado):
                 dic_anexo["data"] = DateTime(protocolo.dat_timestamp, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf')
          dic_anexo["id"] = getattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf').absolute_url()
          anexos.append(dic_anexo)
       elif hasattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf'):
          dic_anexo = {}
          dic_anexo["data"] = DateTime(docvinculado.dat_documento_vinculado, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          if docvinculado.num_protocolo_vinculado != '' and docvinculado.num_protocolo_vinculado != None:
             for protocolo in context.zsql.protocolo_obter_zsql(num_protocolo=docvinculado.num_protocolo_vinculado, ano_protocolo=docvinculado.ano_documento_vinculado):
                 dic_anexo["data"] = DateTime(protocolo.dat_timestamp, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf')
          dic_anexo["id"] = getattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf').absolute_url()
          anexos.append(dic_anexo)
    for docadm in context.zsql.documento_acessorio_administrativo_obter_zsql(cod_documento=documento.cod_documento, ind_excluido=0):
       if hasattr(context.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf'):
          dic_anexo = {}
          dic_anexo["data"] = DateTime(docadm.dat_documento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf')
          dic_anexo["id"] = getattr(context.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf').absolute_url()
          anexos.append(dic_anexo)
    for tram in context.zsql.tramitacao_administrativo_obter_zsql(cod_documento=documento.cod_documento, rd_ordem='1', ind_excluido=0):
        if hasattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf'):
           dic_anexo = {}
           dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
           dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf')
           dic_anexo["id"] = getattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf').absolute_url()
           anexos.append(dic_anexo)
        elif hasattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf'):
           dic_anexo = {}
           dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
           dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf')
           dic_anexo["id"] = getattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf').absolute_url()
           anexos.append(dic_anexo)
    anexos.sort(key=lambda dic: dic['data'])
    for dic in anexos:
        arquivo_doc = cStringIO.StringIO(str(dic['arquivo'].data))
        try:
           texto_anexo = PdfFileReader(arquivo_doc, strict=False)
        except:
           msg = msg = 'O arquivo "' + str(dic['id']) + '" não é um documento PDF válido.'
           raise ValueError(msg)
        else:
           merger.append(texto_anexo)
    output_file_pdf = cStringIO.StringIO()
    merger.write(output_file_pdf)
    merger.close()
    output_file_pdf.seek(0)
    context.temp_folder.manage_addFile(nom_pdf_amigavel)
    arq=context.temp_folder[nom_pdf_amigavel]
    arq.manage_edit(title=nom_pdf_amigavel,filedata=output_file_pdf.getvalue(),content_type='application/pdf')
    arq = getattr(context.temp_folder,nom_pdf_amigavel)
    context.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
    context.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)
    context.temp_folder.manage_delObjects(nom_pdf_amigavel)
    return arq
