## Script (Python) "arquivo_pdf_validar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=file
##title=
##
from PyPDF4 import PdfFileReader
from PyPDF4.utils import PdfReadError
request = container.REQUEST
response =  request.response

try:
    pdf = PdfFileReader(file)
except PdfReadError:
    raise ValueError('O arquivo enviado não é um documento PDF válido.')

return file
