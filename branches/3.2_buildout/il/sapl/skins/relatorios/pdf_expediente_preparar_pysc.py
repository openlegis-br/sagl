import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

if context.REQUEST['data']!='':
    dat_inicio_sessao = context.REQUEST['data']
    data = context.pysc.data_converter_pysc(dat_inicio_sessao) # converte data para formato yyyy/mm/dd
    codigo = context.REQUEST['cod_sessao_plen']

    for sessao in context.zsql.sessao_plenaria_obter_zsql(dat_inicio_sessao=data, cod_sessao_plen=codigo, ind_excluido=0):
        inf_basicas_dic = {} # dicionário que armazenará as informacoes basicas da sessao plenaria 
        # seleciona o tipo da sessao plenaria
        tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
        inf_basicas_dic["num_sessao_plen"] = sessao.num_sessao_plen
        inf_basicas_dic["nom_sessao"] = tipo_sessao.nom_sessao.upper()
        inf_basicas_dic["num_legislatura"] = sessao.num_legislatura
        inf_basicas_dic["num_sessao_leg"] = sessao.num_sessao_leg
        inf_basicas_dic["dat_inicio_sessao"] = sessao.dat_inicio_sessao
        inf_basicas_dic["dia_sessao"] = context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao).upper()
        inf_basicas_dic["hr_inicio_sessao"] = sessao.hr_inicio_sessao
        inf_basicas_dic["dat_fim_sessao"] = sessao.dat_fim_sessao
        inf_basicas_dic["hr_fim_sessao"] = sessao.hr_fim_sessao

        # obtém o nome do Presidente da Câmara titular
        lst_presidente = []
        for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
          for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
            for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
              lst_presidente = presidencia.nom_parlamentar

        # Lista das matérias apresentadas
        lst_materia_apresentada=[]
        dic_materia_apresentada = None
        for materia_apresentada in context.zsql.materia_apresentada_sessao_obter_zsql(dat_ordem=data,cod_sessao_plen=codigo,ind_excluido=0):
            dic_materia_apresentada = {}
            # seleciona os detalhes de uma matéria
            if materia_apresentada.cod_materia != None:
               materia = context.zsql.materia_obter_zsql(cod_materia=materia_apresentada.cod_materia)[0]
               dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
               dic_materia_apresentada["txt_ementa"] = materia.txt_ementa
               dic_materia_apresentada["id_materia"] = materia.des_tipo_materia+" "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
               dic_materia_apresentada["link_materia"] = '<link href="'+context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+materia.cod_materia+'">'+materia.des_tipo_materia.upper()+' Nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</link>'
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
            elif materia_apresentada.cod_documento != None:
               materia = context.zsql.documento_administrativo_obter_zsql(cod_documento=materia_apresentada.cod_documento)[0]
               dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
               dic_materia_apresentada["txt_ementa"] = materia.txt_assunto
               dic_materia_apresentada["id_materia"] = materia.des_tipo_documento+" "+str(materia.num_documento)+"/"+str(materia.ano_documento)
               dic_materia_apresentada["link_materia"] = '<link href="'+context.consultas.absolute_url()+'/documento_administrativo/documento_administrativo_mostrar_proc?cod_documento='+materia.cod_documento+'">'+materia.des_tipo_documento.upper()+' Nº '+str(materia.num_documento)+'/'+str(materia.ano_documento)+'</link>'
               dic_materia_apresentada["nom_autor"] = materia.txt_interessado
               lst_materia_apresentada.append(dic_materia_apresentada)

        # Mocoes
        lst_mocoes = [] 
        for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=codigo,ind_excluido=0):
          for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,des_tipo_materia='Moção',ind_excluido=0):
            dic_mocoes = {}
            dic_mocoes["num_ordem"] = item.num_ordem
            dic_mocoes['txt_ementa'] = materia.txt_ementa
            dic_mocoes["link_materia"] = '<link href="'+context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+item.cod_materia+'">'+materia.des_tipo_materia.upper()+' Nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</link>'
            dic_mocoes["nom_autor"] = ""
            autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
            fields = autores.data_dictionary().keys()
            lista_autor = []
            for autor in autores:
              for field in fields:
                 nome_autor = autor['nom_autor_join']
   	      lista_autor.append(nome_autor)
            dic_mocoes["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
            lst_mocoes.append(dic_mocoes)

        # Indicacoes
        vereadoresind=[]
        lst_indicacoes = [] 
        for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=codigo,ind_excluido=0):
          # Filtra materias do tipo Indicacao
          for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,des_tipo_materia='Indicação',ind_excluido=0):
            # Obtem autores das indicacoes
            dic_autores = {}
            autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
            fields = autores.data_dictionary().keys()
            lista_autor = []
            for autor in autores:
              for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor[1]):
                dic_autores["nome_completo"] = parlamentar['nom_completo']
                dic_autores["txt_autoria"] = parlamentar['nom_parlamentar']
            vereadoresind.append(dic_autores)
            # Indicacoes
            dic_indicacoes = {}
            dic_indicacoes["num_ordem"] = item.num_ordem
            dic_indicacoes['txt_ementa'] = materia.txt_ementa
            dic_indicacoes["link_materia"] = '<link href="'+context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+item.cod_materia+'">'+materia.des_tipo_materia.upper()+' Nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</link>'
            dic_indicacoes["nom_autor"] = ""
            autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
            fields = autores.data_dictionary().keys()
            lista_autor = []
            for autor in autores:
              for field in fields:
                 nome_autor = autor['nom_autor_join']
   	      lista_autor.append(nome_autor)
            dic_indicacoes["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
            lst_indicacoes.append(dic_indicacoes)


        # Requerimentos
        vereadores=[]
        lst_requerimentos = []
        # Obtem materias da pauta do expediente da sessao
        for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=codigo,ind_excluido=0):
          # Filtra materias do tipo Requerimento
          for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,des_tipo_materia='Requerimento',ind_excluido=0):
            # Obtem autores das materias
            dic_autores = {}
            autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
            fields = autores.data_dictionary().keys()
            lista_autor = []
            for autor in autores:
              for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor[1]):
                dic_autores["nome_completo"] = parlamentar['nom_completo']
                dic_autores["txt_autoria"] = parlamentar['nom_parlamentar']
            vereadores.append(dic_autores)
            # Requerimentos
            dic_requerimentos = {}
            dic_requerimentos["num_ordem"] = item.num_ordem
            dic_requerimentos['txt_ementa'] = materia.txt_ementa
            dic_requerimentos["link_materia"] = '<link href="'+context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+item.cod_materia+'">'+materia.des_tipo_materia.upper()+' Nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</link>'
            dic_requerimentos["nom_autor"] = ""
            autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
            fields = autores.data_dictionary().keys()
            lista_autor = []
            for autor in autores:
              for field in fields:
                 nome_autor = autor['nom_autor_join']
              lista_autor.append(nome_autor)
            dic_requerimentos["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
            lst_requerimentos.append(dic_requerimentos)


    # Selecione apenas uma ocorrencia do nome do vereador - requerimentos
    vereadores = [
        e
        for i, e in enumerate(vereadores)
        if vereadores.index(e) == i
        ]

    # Ordem alfabetica
    vereadores.sort()

    # Ordena requerimentos por autor
    demais=[]
    for autor in vereadores:
     for materia in lst_requerimentos:
       if autor.get('txt_autoria',autor) == materia.get('nom_autor',materia):
         demais.append(materia)

#    lst_requerimentos = demais

    # Selecione apenas uma ocorrencia do nome do vereador - requerimentos
    vereadoresind = [
        e
        for i, e in enumerate(vereadoresind)
        if vereadoresind.index(e) == i
        ]

    # Ordem alfabetica
    vereadoresind.sort()

    # Ordena indicacoes por autor
    indicacoes = []
    for autor in vereadoresind:
     for materia in lst_indicacoes:
       if autor.get('txt_autoria',autor) == materia.get('nom_autor',materia):
         indicacoes.append(materia)

#    lst_indicacoes = indicacoes

    # obtém as propriedades da casa legislativa para montar o cabeçalho e o rodapé da página
    cabecalho={}

    # tenta buscar o logotipo da casa LOGO_CASA
    if hasattr(context.sapl_documentos.props_sapl,'logo_casa.gif'):
        imagem = context.sapl_documentos.props_sapl['logo_casa.gif'].absolute_url()
    else:
        imagem = context.imagens.absolute_url() + "/brasao_transp.gif"
    
    #Abaixo é gerado o dic do rodapé da página (linha 7)
    casa={}
    aux=context.sapl_documentos.props_sapl.propertyItems()
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

    data_emissao= DateTime().strftime("%d/%m/%Y")
    rodape= casa
    rodape['data_emissao']= data_emissao

    REQUEST=context.REQUEST
    for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
        rodape['nom_localidade']= local.nom_localidade
        rodape['sgl_uf']= local.sgl_uf

    sessao=session.id
    caminho = context.pdf_expediente_gerar(rodape, imagem, inf_basicas_dic, lst_materia_apresentada, lst_indicacoes, lst_requerimentos, lst_mocoes, lst_presidente, sessao)
    if caminho=='aviso':
        return response.redirect('mensagem_emitir_proc')
    else:
       response.redirect(caminho)

