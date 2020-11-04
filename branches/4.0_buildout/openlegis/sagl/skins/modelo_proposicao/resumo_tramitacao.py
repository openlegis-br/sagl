## Script (Python) "resumo_tramitacao"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_materia
##title=
##
REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

inf_basicas_dic = {}
casa={}
aux=context.sapl_documentos.props_sagl.propertyItems()
for item in aux:
    casa[item[0]]=item[1]
localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
estado = context.zsql.localidade_obter_zsql(tip_localidade="U")
for uf in estado:
    if localidade[0].sgl_uf == uf.sgl_uf:
        nom_estado = uf.nom_localidade.encode('utf-8')
        break
inf_basicas_dic['nom_camara']= casa['nom_casa'].encode('utf-8')
inf_basicas_dic["nom_estado"] = nom_estado.encode('utf-8')
for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
    inf_basicas_dic['nom_localidade']= local.nom_localidade.encode('utf-8')
    inf_basicas_dic['sgl_uf']= local.sgl_uf

for materia in context.zsql.materia_obter_zsql(cod_materia=cod_materia):
 if materia.num_protocolo:
    for protocolo in context.zsql.protocolo_pesquisar_zsql(num_protocolo=materia.num_protocolo,ano_protocolo=materia.ano_ident_basica):
      if protocolo.cod_protocolo:
         num_protocolo = str(protocolo.num_protocolo) + '/' + str(protocolo.ano_protocolo)
         dat_protocolo = context.pysc.iso_to_port_pysc(protocolo.dat_protocolo)
         hor_protocolo = protocolo.hor_protocolo[0:2]+':'+protocolo.hor_protocolo[3:5]
 else:
    num_protocolo = ''
    dat_protocolo = materia.dat_apresentacao
    hor_protocolo = ''
  
 dat_vencimento = " "
 if materia.dat_fim_prazo != None:
   dat_vencimento = context.pysc.iso_to_port_pysc(materia.dat_fim_prazo)
 num_proposicao = str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica)
 des_tipo_materia = materia.des_tipo_materia.encode('utf-8')
 txt_ementa = materia.txt_ementa.encode('utf-8')
 nom_autor = ""
 autores = context.zsql.autoria_obter_zsql(cod_materia=cod_materia)
 fields = autores.data_dictionary().keys()
 lista_autor = []
 for autor in autores:
   for field in fields:
      nome_autor = autor['nom_autor_join'].encode('utf-8')
   lista_autor.append(nome_autor)
 nom_autor = ', '.join(['%s' % (value) for (value) in lista_autor])
 regime_tramitacao = ""
 if materia.cod_regime_tramitacao != None:
   for regime in context.zsql.regime_tramitacao_obter_zsql(cod_regime_tramitacao=materia.cod_regime_tramitacao):
     regime_tramitacao = regime.des_regime_tramitacao.encode('utf-8')
 nom_arquivo = 'resumo-tramitacao-'+materia.sgl_tipo_materia+'-'+str(materia.num_ident_basica)+'-'+str(materia.ano_ident_basica)+'.odt'
 nom_arquivo = nom_arquivo.encode('utf-8')

return context.resumo_tramitacao_gerar_odt(inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_proposicao, des_tipo_materia, nom_autor, txt_ementa, regime_tramitacao, nom_arquivo)
#return inf_basicas_dic, num_protocolo, dat_protocolo, hor_protocolo, dat_vencimento, num_proposicao, des_tipo_materia, nom_autor, txt_ementa, regime_tramitacao, nom_arquivo
