import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION
if context.REQUEST['cod_sessao_plen']!='':
    cod_sessao_plen = context.REQUEST['cod_sessao_plen']
    splen = []
    pauta = []
    data = ""
    for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
     data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
     dat_ordem = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
    # seleciona dados da sessão plenária
    for sp in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
        dicsp = {}
        ts = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sp.tip_sessao)[0]
        dicsp["sessao"] = str(sp.num_sessao_plen)+"ª SESSÃO "+ts.nom_sessao.decode('utf-8').upper()+" DA "+str(sp.num_legislatura)+"ª LEGISLATURA"
        dia = context.pysc.data_converter_por_extenso_pysc(data=sp.dat_inicio_sessao)
        hora = context.pysc.hora_formatar_pysc(hora=sp.hr_inicio_sessao)
        dicsp["datasessao"] = str(dia).decode('utf-8').upper()
        splen.append(dicsp) 
        # seleciona as matérias que compõem a pauta na data escolhida
    for ordem in context.zsql.ordem_dia_obter_zsql(dat_ordem=data, cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
        # seleciona os detalhes de uma matéria 
        materia = context.zsql.materia_obter_zsql(cod_materia=ordem.cod_materia)[0]
        dic = {} 
        dic["num_ordem"] = ordem.num_ordem
        dic["cod_materia"] = ordem.cod_materia
        dic["link_materia"] = '<link href="'+context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+ordem.cod_materia+'">'+materia.des_tipo_materia.decode('utf-8').upper()+' Nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</link>'
        dic["id_materia"] = materia.des_tipo_materia.decode('utf-8').upper()+" nº "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica) 
        dic["txt_ementa"] = ordem.txt_observacao
        dic["des_numeracao"]=""
        numeracao = context.zsql.numeracao_obter_zsql(cod_materia=ordem.cod_materia)
        if len(numeracao):
           numeracao = numeracao[0]
           dic["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia) 
        dic["des_turno"]=""
        for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=ordem.tip_turno):
           dic["des_turno"] = turno.des_turno
        dic["des_quorum"]=""
        for quorum in context.zsql.quorum_votacao_obter_zsql(cod_quorum=ordem.tip_quorum):
           dic["des_quorum"] = quorum.des_quorum
        dic["tip_votacao"]=""
        for tip_votacao in context.zsql.tipo_votacao_obter_zsql(tip_votacao=ordem.tip_votacao):
           dic["tip_votacao"] = tip_votacao.des_tipo_votacao
        dic["des_situacao"] = ""
        dic["nom_autor"] = ""
        autores = context.zsql.autoria_obter_zsql(cod_materia=ordem.cod_materia)
        fields = autores.data_dictionary().keys()
        lista_autor = []
        for autor in autores:
	  for field in fields:
                  nome_autor = autor['nom_autor_join']
  	  lista_autor.append(nome_autor)
        dic["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 

        lst_relator = [] # lista contendo os relatores da matéria
        for relatoria in context.zsql.relatoria_obter_zsql(cod_materia=ordem.cod_materia):
            parlamentar = context.zsql.parlamentar_obter_zsql(cod_parlamentar=relatoria.cod_parlamentar)[0]
            comissao = context.zsql.comissao_obter_zsql(cod_comissao=relatoria.cod_comissao)[0]
            lst_relator.append(parlamentar.nom_parlamentar+" - "+comissao.nom_comissao)
        if not len(lst_relator):
            lst_relator = ['']            
        dic["lst_relator"] = lst_relator

        # adiciona o dicionário na pauta
        pauta.append(dic) 

    # obtém o nome do Presidente da Câmara titular
    lst_presidente = []
    for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sp.num_legislatura,data=data):
      for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
        for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
          lst_presidente = presidencia.nom_parlamentar

    # obtém as propriedades da casa legislativa para montar o cabeçalho e o rodapé da página
    casa = {} 
    aux=context.sapl_documentos.props_sapl.propertyItems()
    for item in aux:
        casa[item[0]] = item[1]

    # obtém a localidade
    localidade = context.zsql.localidade_obter_zsql(cod_localidade=casa["cod_localidade"])
        
    # monta o cabeçalho da página
    cabecalho = {}        
    estado = context.zsql.localidade_obter_zsql(tip_localidade="U")
    for uf in estado:
        if localidade[0].sgl_uf == uf.sgl_uf:
            nom_estado = uf.nom_localidade.encode('utf-8')
            break

    cabecalho["nom_casa"] = casa["nom_casa"]
    cabecalho["nom_estado"] = nom_estado

    # tenta buscar o logotipo da casa LOGO_CASA
    if hasattr(context.sapl_documentos.props_sapl,'logo_casa.gif'):
        imagem = context.sapl_documentos.props_sapl['logo_casa.gif'].absolute_url()
    else:
        imagem = context.imagens.absolute_url() + "/brasao_transp.gif"
        
    # monta o rodapé da página        
    num_cep = casa["num_cep"]
    if len(casa["num_cep"]) == 8:
        num_cep=casa["num_cep"][:4]+"-"+casa["num_cep"][5:]
            
    linha1 = casa["end_casa"] 
    if num_cep!=None and num_cep!="":
        if casa["end_casa"]!="" and casa["end_casa"]!=None:
            linha1 = linha1 +"  "
        linha1 = linha1 +" CEP: "+num_cep
    if localidade[0].nom_localidade!=None and localidade[0].nom_localidade!="":
        linha1 = linha1 +"   "+localidade[0].nom_localidade +" - "+localidade[0].sgl_uf
    if casa["num_tel"]!=None and casa["num_tel"]!="":
        linha1 = linha1 +"   Tel.: "+casa["num_tel"]

    linha2 = casa["end_web_casa"]
    if casa["end_email_casa"]!=None and casa["end_email_casa"]!="": 
        if casa["end_web_casa"]!="" and casa["end_web_casa"]!=None:
            linha2= linha2 + " - "
        linha2 = linha2 +"E-mail: "+casa["end_email_casa"]
    dat_emissao = DateTime().strftime("%d/%m/%Y")
    rodape = [linha1, linha2, dat_emissao]
    
    sessao=session.id
    caminho = context.pdf_ordem_dia_gerar(sessao, imagem, dat_ordem, cod_sessao_plen, splen, pauta, cabecalho, rodape, lst_presidente)
    if caminho=='aviso':
        return response.redirect('mensagem_emitir_proc')
    else:
        response.redirect(caminho)
