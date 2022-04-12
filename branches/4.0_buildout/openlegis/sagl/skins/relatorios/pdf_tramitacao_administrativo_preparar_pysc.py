## Script (Python) "pdf_tramitacao_administrativo_preparar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=hdn_cod_tramitacao,hdn_url
##title=
##
import os
from xml.sax.saxutils import escape

request=context.REQUEST
response=request.RESPONSE
session=request.SESSION

cabecalho={}

#tenta buscar o logotipo da casa LOGO_CASA
if hasattr(context.sapl_documentos.props_sagl,'logo_casa.gif'):
  imagem = context.sapl_documentos.props_sagl['logo_casa.gif'].absolute_url()
else:
  imagem = context.imagens.absolute_url() + "/brasao.gif"

#abaixo é gerado o dic do rodapé da página
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
  casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
data_emissao= DateTime().strftime("%d/%m/%Y")
rodape= casa 
rodape['data_emissao']= data_emissao

estados=context.zsql.localidade_obter_zsql(tip_localidade="u")
for uf in estados:
 if localidade[0].sgl_uf==uf.sgl_uf:
  nom_estado=uf.nom_localidade
  break
inf_basicas_dic = {}
inf_basicas_dic['nom_camara']= casa['nom_casa']
inf_basicas_dic["nom_estado"]="Estado de "+nom_estado
REQUEST=context.REQUEST
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
  rodape['nom_localidade']= "   "+local.nom_localidade
  rodape['sgl_uf']= local.sgl_uf

cod_tramitacao=hdn_cod_tramitacao

tramitacao_dic = {}
#obtém os dados da tramitação
for tramitacao in context.zsql.tramitacao_administrativo_obter_zsql(cod_tramitacao=hdn_cod_tramitacao):
  tramitacao_dic['dat_tramitacao'] = tramitacao.dat_tramitacao
  tramitacao_dic['dat_extenso'] = context.pysc.data_converter_por_extenso_pysc(data=tramitacao.dat_tramitacao)
  tramitacao_dic['dat_encaminha'] = tramitacao.dat_encaminha
  tramitacao_dic['des_status'] = tramitacao.des_status
  if tramitacao.txt_tramitacao != None and tramitacao.txt_tramitacao!='':
     tramitacao_dic['txt_tramitacao'] = context.extensions.xhtml2rml(tramitacao.txt_tramitacao,'P2')
  else:
     tramitacao_dic['txt_tramitacao'] = ''
  if tramitacao.dat_fim_prazo != None:
    tramitacao_dic['dat_fim_prazo'] = tramitacao.dat_fim_prazo
  else:
    for prazo_status in context.zsql.status_tramitacao_administrativo_obter_zsql(cod_status=tramitacao.cod_status):
      if prazo_status.num_dias_prazo != None:
        data_calculada = DateTime() + prazo_status.num_dias_prazo
        tramitacao_dic['dat_fim_prazo'] = DateTime(data_calculada).strftime('%d/%m/%Y')
      else:
        tramitacao_dic['dat_fim_prazo'] = ''

  # dados do documento
  for documento in context.zsql.documento_administrativo_obter_zsql(cod_documento=tramitacao.cod_documento):
   txt_assunto = escape(documento.txt_assunto)  
   tramitacao_dic['id_documento'] = documento.des_tipo_documento.decode('utf-8').upper() +" N° "+ str(documento.num_documento)+"/"+ str(documento.ano_documento)+" - "+ escape(documento.txt_interessado) +" - "+ escape(documento.txt_assunto)

  # unidade de origem
  for unid_origem in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao=tramitacao.cod_unid_tram_local):
   tramitacao_dic['unidade_origem'] = unid_origem.nom_unidade_join 
   if unid_origem.nom_orgao == "Poder Executivo" or unid_origem.nom_orgao == "Poder Executivo - Protocolo" or unid_origem.nom_orgao == "Poder Executivo - Administração" or unid_origem.nom_orgao == "Poder Executivo - Gabinete" or unid_origem.nom_orgao == "Poder Executivo - " or unid_origem.nom_orgao == "Externo - Executivo":
     inf_basicas_dic['nom_camara']= 'Prefeitura Municipal de ' + local.nom_localidade

  # usuario de origem
  for usu_origem in context.zsql.usuario_obter_zsql(cod_usuario=tramitacao.cod_usuario_local):
   tramitacao_dic['usuario_origem'] = usu_origem.col_username
   tramitacao_dic['nom_usuario_origem'] = usu_origem.nom_completo
   tramitacao_dic['nom_cargo_usuario_origem'] = usu_origem.nom_cargo

  # unidade de destino
  for unid_destino in context.zsql.unidade_tramitacao_obter_zsql(cod_unid_tramitacao=tramitacao.cod_unid_tram_dest):
    tramitacao_dic['unidade_destino'] = unid_destino.nom_unidade_join

  # usuario de destino
  if tramitacao.cod_usuario_dest != None:
    for usu_destino in context.zsql.usuario_obter_zsql(cod_usuario=tramitacao.cod_usuario_dest):
     tramitacao_dic['usuario_destino'] = usu_destino.col_username
     tramitacao_dic['nom_usuario_destino'] = usu_destino.nom_completo
     tramitacao_dic['nom_cargo_usuario_destino'] = usu_destino.nom_cargo

caminho=context.pdf_tramitacao_administrativo_gerar(imagem,rodape,inf_basicas_dic,cod_tramitacao,tramitacao_dic,hdn_url,sessao=session.id)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)

