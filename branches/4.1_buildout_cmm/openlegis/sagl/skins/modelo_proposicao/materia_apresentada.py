## Script (Python) "materia_apresentada"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
  inf_basicas_dic = {}
  tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
  inf_basicas_dic["cod_sessao_plen"] = sessao.cod_sessao_plen
  inf_basicas_dic["num_sessao_plen"] = sessao.num_sessao_plen
  inf_basicas_dic["nom_sessao"] = tipo_sessao.nom_sessao
  inf_basicas_dic["num_legislatura"] = sessao.num_legislatura
  inf_basicas_dic["num_sessao_leg"] = sessao.num_sessao_leg
  inf_basicas_dic["dat_inicio_sessao"] = sessao.dat_inicio_sessao
  inf_basicas_dic["dia_sessao"] = context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao)
  inf_basicas_dic["hr_inicio_sessao"] = sessao.hr_inicio_sessao
  inf_basicas_dic["dat_fim_sessao"] = sessao.dat_fim_sessao
  inf_basicas_dic["hr_fim_sessao"] = sessao.hr_fim_sessao

  # Materias Apresentadas
  lst_materia_apresentada=[]
  for materia_apresentada in context.zsql.materia_apresentada_sessao_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      dic_materia_apresentada = {}
      # seleciona os detalhes de uma matéria
      if materia_apresentada.cod_materia != None:
         materia = context.zsql.materia_obter_zsql(cod_materia=materia_apresentada.cod_materia)[0]
         dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
         dic_materia_apresentada["txt_ementa"] = materia.txt_ementa
         dic_materia_apresentada["id_materia"] = materia.des_tipo_materia+" "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
         dic_materia_apresentada["link_materia"] = '<link href="'+context.sapl_documentos.absolute_url()+'/materia/'+ str(materia_apresentada.cod_materia) + '_texto_integral.pdf' +'">'+materia.des_tipo_materia.decode('utf-8').upper()+' Nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</link>'
         dic_materia_apresentada["nom_autor"] = ""
         autores = context.zsql.autoria_obter_zsql(cod_materia=materia_apresentada.cod_materia)
         fields = autores.data_dictionary().keys()
         lista_autor = []
         for autor in autores:
             for field in fields:
                 nome_autor = autor['nom_autor_join']
             lista_autor.append(nome_autor)
         dic_materia_apresentada["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         lst_materia_apresentada.append(dic_materia_apresentada)

      elif materia_apresentada.cod_emenda != None:
         for emenda in context.zsql.emenda_obter_zsql(cod_emenda=materia_apresentada.cod_emenda):
             materia = context.zsql.materia_obter_zsql(cod_materia=emenda.cod_materia)[0]
             dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
             dic_materia_apresentada["txt_ementa"] = emenda.txt_ementa
             dic_materia_apresentada["id_materia"] = 'Emenda ' + emenda.des_tipo_emenda + ' nº ' + str(emenda.num_emenda) + " ao " + materia.sgl_tipo_materia + str(materia.num_ident_basica) + "/" + str(materia.ano_ident_basica)
             dic_materia_apresentada["link_materia"] = '<link href="' + context.sapl_documentos.absolute_url() + '/emenda/' + str(materia_apresentada.cod_emenda) + '_emenda.pdf' + '">' + 'EMENDA ' + emenda.des_tipo_emenda.decode('utf-8').upper() + ' Nº ' + str(emenda.num_emenda) + " - " +  materia.sgl_tipo_materia +' ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica) + '</link>'
             dic_materia_apresentada["nom_autor"] = ""
             autores = context.zsql.autoria_emenda_obter_zsql(cod_emenda=emenda.cod_emenda)
             fields = autores.data_dictionary().keys()
             lista_autor = []
             for autor in autores:
                 for field in fields:
                     nome_autor = autor['nom_autor_join']
                 lista_autor.append(nome_autor)
         dic_materia_apresentada["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         lst_materia_apresentada.append(dic_materia_apresentada)

      elif materia_apresentada.cod_substitutivo != None:
         for substitutivo in context.zsql.substitutivo_obter_zsql(cod_substitutivo=materia_apresentada.cod_substitutivo):
             materia = context.zsql.materia_obter_zsql(cod_materia=substitutivo.cod_materia)[0]
             dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
             dic_materia_apresentada["txt_ementa"] = substitutivo.txt_ementa
             dic_materia_apresentada["id_materia"] = 'Substitutivo ' + ' nº ' + str(substitutivo.num_substitutivo) + " ao " + materia.sgl_tipo_materia + ' ' + str(materia.num_ident_basica) + "/" + str(materia.ano_ident_basica)
             dic_materia_apresentada["link_materia"] = '<link href="' + context.sapl_documentos.absolute_url() + '/substitutivo/' + str(materia_apresentada.cod_substitutivo) + '_substitutivo.pdf' + '">' + 'SUBSTITUTIVO Nº ' + str(substitutivo.num_substitutivo) + " - " +  materia.sgl_tipo_materia + ' ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica) + '</link>'
             dic_materia_apresentada["nom_autor"] = ""
             autores = context.zsql.autoria_substitutivo_obter_zsql(cod_substitutivo=substitutivo.cod_substitutivo)
             fields = autores.data_dictionary().keys()
             lista_autor = []
             for autor in autores:
                 for field in fields:
                     nome_autor = autor['nom_autor_join']
                 lista_autor.append(nome_autor)
         dic_materia_apresentada["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         lst_materia_apresentada.append(dic_materia_apresentada)

      elif materia_apresentada.cod_parecer != None:
         for parecer in context.zsql.relatoria_obter_zsql(cod_relatoria=materia_apresentada.cod_parecer):
             materia = context.zsql.materia_obter_zsql(cod_materia=parecer.cod_materia)[0]
             dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
             dic_materia_apresentada["txt_ementa"] = materia_apresentada.txt_observacao
             for comissao in context.zsql.comissao_obter_zsql(cod_comissao=parecer.cod_comissao):
                 sgl_comissao = comissao.sgl_comissao
                 nom_comissao = comissao.nom_comissao
             dic_materia_apresentada["link_materia"] = '<link href="' + context.sapl_documentos.absolute_url() + '/parecer_comissao/' + str(materia_apresentada.cod_parecer) + '_parecer.pdf' + '">' + 'PARECER ' + sgl_comissao+ ' Nº ' + str(parecer.num_parecer) + '/' + str(parecer.ano_parecer) + " - " +  materia.sgl_tipo_materia +' ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica) + '</link>'
             dic_materia_apresentada["nom_autor"] = nom_comissao.decode('utf-8').upper()
             lst_materia_apresentada.append(dic_materia_apresentada)

      elif materia_apresentada.cod_documento != None:
         materia = context.zsql.documento_administrativo_obter_zsql(cod_documento=materia_apresentada.cod_documento)[0]
         dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
         dic_materia_apresentada["txt_ementa"] = materia.txt_assunto
         dic_materia_apresentada["id_materia"] = materia.des_tipo_documento+" "+str(materia.num_documento)+"/"+str(materia.ano_documento)
         dic_materia_apresentada["link_materia"] = '<link href="'+context.sapl_documentos.absolute_url()+'/administrativo/'+ str(materia_apresentada.cod_documento) + '_texto_integral.pdf' +'">'+materia.des_tipo_documento.decode('utf-8').upper()+' Nº '+str(materia.num_documento)+'/'+str(materia.ano_documento)+'</link>'
         dic_materia_apresentada["nom_autor"] = materia.txt_interessado
         lst_materia_apresentada.append(dic_materia_apresentada)

  casa={}
  aux=context.sapl_documentos.props_sagl.propertyItems()
  for item in aux:
      casa[item[0]]=item[1]
  localidade=context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
  estado = context.zsql.localidade_obter_zsql(tip_localidade="U")
  for uf in estado:
      if localidade[0].sgl_uf == uf.sgl_uf:
          nom_estado = uf.nom_localidade
          break
  inf_basicas_dic['nom_camara']= casa['nom_casa']
  inf_basicas_dic["nom_estado"] = nom_estado
  for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
      inf_basicas_dic['nom_localidade']= local.nom_localidade
      inf_basicas_dic['sgl_uf']= local.sgl_uf

return st.materia_apresentada_gerar_odt(inf_basicas_dic, lst_materia_apresentada)
