## Script (Python) "verifica_pdf_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= cod_tramitacao
##title=
##

arquivoPdf=str(cod_tramitacao)+"_tram.pdf"

if hasattr(context.sapl_documentos.administrativo.tramitacao,arquivoPdf):
   return True
else:
   return False

