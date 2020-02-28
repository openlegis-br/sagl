import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

if context.REQUEST['data']!='':
    dat_inicio_sessao = context.REQUEST['data']
    pauta = [] # lista contendo a pauta da ordem do dia a ser impressa    
    data = context.pysc.data_converter_pysc(dat_inicio_sessao) # converte data para formato yyyy/mm/dd
    codigo = context.REQUEST['cod_sessao_plen']

    # seleciona as matérias que compõem a pauta na data escolhida
    for sessao in context.zsql.sessao_plenaria_obter_zsql(dat_inicio_sessao=data, cod_sessao_plen=codigo, ind_excluido=0):
        inf_basicas_dic = {} # dicionário que armazenará as informacoes basicas da sessao plenaria 
        # seleciona o tipo da sessao plenaria
        tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
        inf_basicas_dic["num_sessao_plen"] = sessao.num_sessao_plen
        inf_basicas_dic["nom_sessao"] = tipo_sessao.nom_sessao.decode('utf-8').upper()
        inf_basicas_dic["num_legislatura"] = sessao.num_legislatura
        inf_basicas_dic["num_sessao_leg"] = sessao.num_sessao_leg
        inf_basicas_dic["dat_inicio_sessao"] = sessao.dat_inicio_sessao
        inf_basicas_dic["dia_sessao"] = context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao)
        inf_basicas_dic["hr_inicio_sessao"] = sessao.hr_inicio_sessao
        inf_basicas_dic["dat_fim_sessao"] = sessao.dat_fim_sessao
        inf_basicas_dic["hr_fim_sessao"] = sessao.hr_fim_sessao
 
        # Lista da composicao da mesa diretora da Sessão
        lst_mesa = []
        for composicao in context.zsql.composicao_mesa_sessao_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=composicao.cod_parlamentar,ind_excluido=0):
                for cargo in context.zsql.cargo_mesa_obter_zsql(cod_cargo=composicao.cod_cargo, ind_excluido=0):
                    dic_mesa = {}
                    dic_mesa['nom_completo'] = parlamentar.nom_parlamentar
                    dic_mesa['sgl_partido'] = parlamentar.sgl_partido
                    dic_mesa['des_cargo'] = cargo.des_cargo
                    lst_mesa.append(dic_mesa)

        # Lista de presença na sessão
        lst_presenca_sessao = []
        for presenca in context.zsql.presenca_sessao_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca.cod_parlamentar,ind_excluido=0):
                dic_presenca = {}
                nom_completo = parlamentar.nom_parlamentar
                lst_presenca_sessao.append(nom_completo)
        lst_presenca_sessao = ', '.join(['%s' % (value) for (value) in lst_presenca_sessao])

        # Lista e exibe os Expedientes Diversos da Sessão
        lst_expedientes = []
        dic_expedientes = None
        for tip_expediente in context.zsql.tipo_expediente_obter_zsql():
            for expediente in context.zsql.expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,cod_expediente=tip_expediente.cod_expediente, ind_excluido=0):
                dic_expedientes = {}
                dic_expedientes["nom_expediente"] = tip_expediente.nom_expediente
                dic_expedientes["txt_expediente"] = context.modelo_proposicao.xhtml2rml(expediente.txt_expediente,'P2')

            if dic_expedientes:
                lst_expedientes.append(dic_expedientes)

        # Lista das matérias apresentadas
        lst_materia_apresentada=[]
        dic_materia_apresentada = None
        for materia_apresentada in context.zsql.materia_apresentada_sessao_obter_zsql(dat_ordem=data,cod_sessao_plen=codigo,ind_excluido=0):
        
            # seleciona os detalhes de uma matéria
            materia = context.zsql.materia_obter_zsql(cod_materia=materia_apresentada.cod_materia)[0]
            dic_materia_apresentada = {}
            dic_materia_apresentada["num_ordem"] = materia_apresentada.num_ordem
            dic_materia_apresentada["id_materia"] = materia.des_tipo_materia+" "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
            dic_materia_apresentada["txt_ementa"] = materia.txt_ementa

       	    dic_materia_apresentada["des_numeracao"]=""
            numeracao = context.zsql.numeracao_obter_zsql(cod_materia=materia_apresentada.cod_materia)
            if len(numeracao):
               numeracao = numeracao[0]
               dic_materia_apresentada["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)

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
      
        # Lista das matérias do Expediente, incluindo o resultado das votacoes
        lst_expediente_materia=[]
        for expediente_materia in context.zsql.votacao_expediente_materia_obter_zsql(dat_ordem = data, cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
        
            # seleciona os detalhes de uma matéria
            dic_expediente_materia = {}
            for materia in context.zsql.materia_obter_zsql(cod_materia=expediente_materia.cod_materia):
              dic_expediente_materia["num_ordem"] = expediente_materia.num_ordem
              dic_expediente_materia["id_materia"] = materia.des_tipo_materia+" "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
       	      dic_expediente_materia["des_numeracao"]=""
              numeracao = context.zsql.numeracao_obter_zsql(cod_materia=expediente_materia.cod_materia)
              if len(numeracao):
                 numeracao = numeracao[0]
                 dic_expediente_materia["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
              tram = context.zsql.tramitacao_turno_obter_zsql(cod_materia=materia.cod_materia)
              if len(tram):
                 tram_turno = tram[0]
                 if tram_turno.sgl_turno != "":           
                    for turno in [("P","Primeiro"), ("S","Segundo"), ("U","Unico"), ("L","Suplementar"), ("A","Votacao Unica em Regime de Urgencia"), ("B","1ª Votacao"), ("C","2ª e 3ª Votacoes")]:
                      if tram_turno.sgl_turno == turno[0]:
                          dic_expediente_materia["des_turno"] = turno[1]
              dic_expediente_materia["txt_ementa"] = materia.txt_ementa
              dic_expediente_materia["ordem_observacao"] = expediente_materia.ordem_observacao

              dic_expediente_materia["nom_autor"] = ""
              autores = context.zsql.autoria_obter_zsql(cod_materia=expediente_materia.cod_materia)
              fields = autores.data_dictionary().keys()
              lista_autor = []
              for autor in autores:
  	        for field in fields:
                        nome_autor = autor['nom_autor_join']
	        lista_autor.append(nome_autor)
              dic_expediente_materia["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
            
              if expediente_materia.tip_resultado_votacao:
                  resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=expediente_materia.tip_resultado_votacao, ind_excluido=0)
                  for i in resultado:
                      dic_expediente_materia["nom_resultado"] = i.nom_resultado
                      if expediente_materia.votacao_observacao:
                          dic_expediente_materia["votacao_observacao"] = expediente_materia.votacao_observacao
              else:
                  dic_expediente_materia["nom_resultado"] = "Materia nao votada"
                  dic_expediente_materia["votacao_observacao"] = ""
              lst_expediente_materia.append(dic_expediente_materia)

        # Lista dos oradores do Pequeno Expediente
        lst_oradores_expediente = []
        for orador_expediente in context.zsql.oradores_expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador_expediente.cod_parlamentar,ind_excluido=0):
                dic_oradores_expediente = {}
                dic_oradores_expediente["num_ordem"] = orador_expediente.num_ordem
                dic_oradores_expediente["nom_completo"] = parlamentar.nom_parlamentar
                dic_oradores_expediente['sgl_partido'] = parlamentar.sgl_partido
                lst_oradores_expediente.append(dic_oradores_expediente)

        # Lista presença na ordem do dia
        lst_presenca_ordem_dia = []
        for presenca_ordem_dia in context.zsql.presenca_ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, tip_frequencia='P', ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_ordem_dia.cod_parlamentar,ind_excluido=0):
                nom_completo = parlamentar.nom_parlamentar
                lst_presenca_ordem_dia.append(nom_completo)
        lst_presenca_ordem_dia = ', '.join(['%s' % (value) for (value) in lst_presenca_ordem_dia])
       
        # Lista das matérias da Ordem do Dia, incluindo o resultado das votacoes
        lst_votacao=[]
        for votacao in context.zsql.votacao_ordem_dia_obter_zsql(dat_ordem = data, cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
        
            # Seleciona os detalhes de uma matéria
            materia = context.zsql.materia_obter_zsql(cod_materia=votacao.cod_materia)[0]

            dic_votacao = {}
            dic_votacao["num_ordem"] = votacao.num_ordem
            dic_votacao["id_materia"] = materia.des_tipo_materia+"  "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
       	    dic_votacao["des_numeracao"]=""
            numeracao = context.zsql.numeracao_obter_zsql(cod_materia=votacao.cod_materia)
            if len(numeracao):
               numeracao = numeracao[0]
               dic_votacao["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
            dic_votacao["des_turno"]=""
            tramitacao = context.zsql.tramitacao_obter_zsql(cod_materia=materia.cod_materia, ind_ult_tramitacao=1)
            if len(tramitacao):
               tramitacao = tramitacao[0]
            tram = context.zsql.tramitacao_turno_obter_zsql(cod_materia=materia.cod_materia)
            if len(tram):
               tram_turno = tram[0]
               if tram_turno.sgl_turno != "":           
                  for turno in [("P","Primeiro"), ("S","Segundo"), ("U","Unico"), ("L","Suplementar"), ("A","Votacao Unica em Regime de Urgencia"), ("B","1ª Votacao"), ("C","2ª e 3ª Votacoes")]:
                    if tram_turno.sgl_turno == turno[0]:
                        dic_votacao["des_turno"] = turno[1]
            dic_votacao["txt_ementa"] = materia.txt_ementa
            dic_votacao["ordem_observacao"] = votacao.ordem_observacao

            dic_votacao["nom_autor"] = ""
            autores = context.zsql.autoria_obter_zsql(cod_materia=votacao.cod_materia)
            fields = autores.data_dictionary().keys()
            lista_autor = []
            for autor in autores:
	      for field in fields:
                      nome_autor = autor['nom_autor_join']
	      lista_autor.append(nome_autor)
            dic_votacao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
            
            if votacao.tip_resultado_votacao:
                resultado = context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=votacao.tip_resultado_votacao, ind_excluido=0)
                for i in resultado:
                    dic_votacao["nom_resultado"] = i.nom_resultado
                    if votacao.votacao_observacao:
                        dic_votacao["votacao_observacao"] = votacao.votacao_observacao
            else:
                dic_votacao["nom_resultado"] = "Materia nao votada"
                dic_votacao["votacao_observacao"] = ""
            lst_votacao.append(dic_votacao)

        # Lista presença no Grande Expediente
        lst_presenca_expediente = []
        for presenca_expediente in context.zsql.presenca_expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_expediente.cod_parlamentar,ind_excluido=0):
                nom_completo = parlamentar.nom_parlamentar
                lst_presenca_expediente.append(nom_completo)
        lst_presenca_expediente = ', '.join(['%s' % (value) for (value) in lst_presenca_expediente])

        # Lista dos oradores nas Explicações Pessoais (Grande Expediente)
        lst_oradores = []
        for orador in context.zsql.oradores_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador.cod_parlamentar,ind_excluido=0):
                dic_oradores = {}
                dic_oradores["num_ordem"] = int(orador.num_ordem)
                dic_oradores["nom_completo"] = parlamentar.nom_parlamentar
                dic_oradores['sgl_partido'] = parlamentar.sgl_partido
                lst_oradores.append(dic_oradores)

        # Lista presença no encerramento da Sessão
        lst_presenca_encerramento = []
        for presenca_encerramento in context.zsql.presenca_encerramento_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=presenca_encerramento.cod_parlamentar,ind_excluido=0):
                nom_completo = parlamentar.nom_parlamentar
                lst_presenca_encerramento.append(nom_completo)
        lst_presenca_encerramento = ', '.join(['%s' % (value) for (value) in lst_presenca_encerramento])

    # obtém o nome do Presidente da Câmara titular
    lst_presidente = []
    for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
      for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
        for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
          lst_presidente = presidencia.nom_parlamentar

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

#   return lst_votacao
    sessao=session.id
    caminho = context.pdf_sessao_plenaria_gerar(rodape, imagem, inf_basicas_dic, lst_mesa, lst_presenca_sessao, lst_materia_apresentada, lst_expedientes, lst_expediente_materia, lst_oradores_expediente, lst_presenca_ordem_dia, lst_votacao, lst_presenca_expediente, lst_oradores, lst_presenca_encerramento, lst_presidente, sessao)
    if caminho=='aviso':
        return response.redirect('mensagem_emitir_proc')
    else:
       response.redirect(caminho)
