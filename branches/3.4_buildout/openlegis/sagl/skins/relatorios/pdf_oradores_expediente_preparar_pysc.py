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
        data_emissao= DateTime().strftime("%d/%m/%Y")
        inf_basicas_dic['data_emissao']= data_emissao
 
        # Lista e exibe os Expedientes Diversos da Sessão
        lst_expedientes = []
        dic_expedientes = None
        for expediente in context.zsql.expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,cod_expediente=3, ind_excluido=0):
            dic_expedientes = {}
            dic_expedientes["txt_expediente"] = expediente.txt_expediente

            if dic_expedientes:
                lst_expedientes.append(dic_expedientes)

        # Lista dos oradores do Pequeno Expediente
        lst_oradores_expediente = []
        for orador_expediente in context.zsql.oradores_expediente_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen, ind_excluido=0):
            for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=orador_expediente.cod_parlamentar,ind_excluido=0):
                dic_oradores_expediente = {}
                dic_oradores_expediente["num_ordem"] = orador_expediente.num_ordem
                dic_oradores_expediente["nom_completo"] = parlamentar.nom_parlamentar
                dic_oradores_expediente['sgl_partido'] = parlamentar.sgl_partido
                lst_oradores_expediente.append(dic_oradores_expediente)

    # obtém o nome do Presidente da Câmara titular
    lst_presidente = []
    for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
      for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
        for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
          lst_presidente = presidencia.nom_parlamentar

    # obtém as propriedades da casa legislativa para montar o cabeçalho e o rodapé da página
    cabecalho={}

    # tenta buscar o logotipo da casa LOGO_CASA
    if hasattr(context.sapl_documentos.props_sagl,'logo_casa.gif'):
        imagem = context.sapl_documentos.props_sagl['logo_casa.gif'].absolute_url()
    else:
        imagem = context.imagens.absolute_url() + "/brasao_transp.gif"
    
    #Abaixo é gerado o dic do rodapé da página (linha 7)
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

    inf_basicas_dic['nom_camara']= casa['nom_casa']
    inf_basicas_dic["nom_estado"] = nom_estado

    data_emissao= DateTime().strftime("%d/%m/%Y")
    rodape= casa
    rodape['data_emissao']= data_emissao

    REQUEST=context.REQUEST
    for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
        rodape['nom_localidade']= local.nom_localidade.encode('utf-8')
        rodape['sgl_uf']= local.sgl_uf

#   return lst_votacao
    sessao=session.id
    caminho = context.pdf_oradores_expediente_gerar(rodape, sessao, imagem, inf_basicas_dic, lst_expedientes, lst_oradores_expediente,  lst_presidente)
    if caminho=='aviso':
        return response.redirect('mensagem_emitir_proc')
    else:
       response.redirect(caminho)
