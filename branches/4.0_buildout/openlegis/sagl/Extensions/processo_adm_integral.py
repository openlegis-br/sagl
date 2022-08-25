# -*- coding: utf-8 -*-
import os
from io import BytesIO
from DateTime import DateTime
from PyPDF4 import PdfFileWriter, PdfFileReader, PdfFileMerger
from pdfrw import PdfReader, PdfWriter, PageMerge, IndirectPdfDict
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128, qr
from reportlab.graphics.shapes import Drawing
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.utils import ImageReader
import shutil

# obter altura da pagina
def getPageSizeH(p):
    h = int(p.mediaBox.getHeight())
    return h


# obter largura da pagina
def getPageSizeW(p):
    w = int(p.mediaBox.getWidth())
    return w

def processo_adm_gerar_pdf(context):
    cod_documento = context.REQUEST['cod_documento']
    foldername =  str(cod_documento) + '_proc_adm'
    dirpath = os.path.join('/tmp/', foldername)
    processo_integral =  str(cod_documento) + '_processo_integral.pdf'
    if not os.path.exists(dirpath):
       os.makedirs(dirpath)
    writer = PdfFileWriter()
    merger = PdfFileMerger(strict=False)
    for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=cod_documento):
       nom_pdf_amigavel = documento.sgl_tipo_documento+'-'+str(documento.num_documento)+'-'+str(documento.ano_documento)+'.pdf'
       id_processo = documento.sgl_tipo_documento+' '+str(documento.num_documento)+'/'+str(documento.ano_documento)
       dat_documento = documento.dat_documento
    nom_pdf_amigavel = nom_pdf_amigavel.decode('latin-1').encode("utf-8")
    pdfmetrics.registerFont(TTFont('Arial', '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial_Bold', '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf'))
    anexos = []
    if hasattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf'):
       dic_anexo = {}
       dic_anexo["data"] = DateTime(dat_documento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
       dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral_signed.pdf')
       anexos.append(dic_anexo)
    elif hasattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf'):
       dic_anexo = {}
       dic_anexo["data"] = DateTime(dat_documento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
       dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(cod_documento) + '_texto_integral.pdf')
       anexos.append(dic_anexo)
    for docvinculado in context.zsql.documento_administrativo_vinculado_obter_zsql(cod_documento_vinculante=documento.cod_documento, ind_excluido=0):
       if hasattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf'):
          dic_anexo = {}
          dic_anexo["data"] = DateTime(docvinculado.dat_documento_vinculado, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          for protocolo in context.zsql.protocolo_obter_zsql(num_protocolo=docvinculado.num_protocolo_vinculado, ano_protocolo=docvinculado.ano_documento_vinculado):
              dic_anexo["data"] = DateTime(protocolo.dat_timestamp, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral_signed.pdf')
          anexos.append(dic_anexo)
       elif hasattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf'):
          dic_anexo = {}
          dic_anexo["data"] = DateTime(docvinculado.dat_documento_vinculado, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          for protocolo in context.zsql.protocolo_obter_zsql(num_protocolo=docvinculado.num_protocolo_vinculado, ano_protocolo=docvinculado.ano_documento_vinculado):
              dic_anexo["data"] = DateTime(protocolo.dat_timestamp, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(docvinculado.cod_documento_vinculado) + '_texto_integral.pdf')
          anexos.append(dic_anexo)
    for docadm in context.zsql.documento_acessorio_administrativo_obter_zsql(cod_documento=documento.cod_documento, ind_excluido=0):
       if hasattr(context.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf'):
          dic_anexo = {}
          dic_anexo["data"] = DateTime(docadm.dat_documento, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
          dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo, str(docadm.cod_documento_acessorio) + '.pdf')
          anexos.append(dic_anexo)
    for tram in context.zsql.tramitacao_administrativo_obter_zsql(cod_documento=documento.cod_documento, rd_ordem='1', ind_excluido=0):
        if hasattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf'):
           dic_anexo = {}
           dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
           dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram.pdf')
           anexos.append(dic_anexo)
        elif hasattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf'):
           dic_anexo = {}
           dic_anexo["data"] = DateTime(tram.dat_tramitacao, datefmt='international').strftime('%Y-%m-%d %H:%M:%S')
           dic_anexo["arquivo"] = getattr(context.sapl_documentos.administrativo.tramitacao, str(tram.cod_tramitacao) + '_tram_signed.pdf')
           anexos.append(dic_anexo)
    anexos.sort(key=lambda dic: dic['data'])
    anexos = [(i + 1, j) for i, j in enumerate(anexos)]
    for i, dic in anexos:
        arquivo_doc = BytesIO(str(dic['arquivo'].data))
        texto_anexo = PdfFileReader(arquivo_doc)
        nom_pdf = str(i) + '.pdf'
        f = open(os.path.join(dirpath) + '/' + nom_pdf, 'wb').write(str(dic['arquivo'].data))
        merger.append(texto_anexo)

    file_paths = []   
    for root, directories, files in os.walk(dirpath):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    file_paths.sort()

    merger = PdfFileMerger()

    for path in file_paths:
        merger.append(path)

    merger.write('/tmp/' +  nom_pdf_amigavel)
    merger.close()

    download = open('/tmp/' + nom_pdf_amigavel, 'rb').read()

    arquivo_doc = BytesIO(download)

    existing_pdf = PdfFileReader(arquivo_doc, strict=False)
    numPages = existing_pdf.getNumPages()
    # cria novo PDF
    packet = BytesIO()
    can = canvas.Canvas(packet)
    for page_num, i in enumerate(range(numPages), start=1):
        page = existing_pdf.getPage(i)
        pwidth = getPageSizeW(page)
        pheight = getPageSizeH(page)
        can.setPageSize((pwidth, pheight))
        can.setFillColorRGB(0,0,0)
        # Numero de pagina
        num_pagina = "fls. %s/%s" % (page_num, numPages)
        can.saveState()
        can.setFont('Arial', 9)
        can.drawCentredString(pwidth-45, pheight-60, id_processo)
        can.setFont('Arial_Bold', 9)
        can.drawCentredString(pwidth-45, pheight-72, num_pagina)
        can.restoreState()
        can.showPage()
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    output = PdfFileWriter()
    for page in range(existing_pdf.getNumPages()):
        pdf_page = existing_pdf.getPage(page)
        # numeração de páginas
        for wm in range(new_pdf.getNumPages()):
            watermark_page = new_pdf.getPage(wm)
            if page == wm:
               pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)
    outputStream = BytesIO()
    output.write(outputStream)

    context.REQUEST.RESPONSE.setHeader('Content-Type', 'application/pdf')
    context.REQUEST.RESPONSE.setHeader('Content-Disposition','inline; filename=%s' %nom_pdf_amigavel)

    if os.path.exists(dirpath) and os.path.isdir(dirpath):
       shutil.rmtree(dirpath)
       file = '/tmp/'+nom_pdf_amigavel
       os.unlink(file)

    return outputStream.getvalue()

