import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION
if context.REQUEST['cod_reuniao']!='':
    cod_reuniao = context.REQUEST['cod_reuniao']
    reuniao = []
    pauta = []
    # seleciona dados da reunião
    for rc in context.zsql.reuniao_comissao_obter_zsql(cod_reuniao=cod_reuniao,ind_excluido=0):
        data = context.pysc.data_converter_pysc(rc.dat_inicio_reuniao)
        dat_reuniao = context.pysc.data_converter_pysc(rc.dat_inicio_reuniao)
        dicrc = {}
        for comissao in context.zsql.comissao_obter_zsql(cod_comissao=rc.cod_comissao, ind_excluido=0):     
            dicrc["nom_comissao"] = comissao.nom_comissao.decode('utf-8').upper()
        dicrc["reuniao"] = 'PAUTA DA ' + str(rc.num_reuniao)+"ª REUNIÃO " + str(rc.des_tipo_reuniao).decode('utf-8').upper()
        dicrc["tema"] =  rc.txt_tema
        dia = context.pysc.data_converter_por_extenso_pysc(data=rc.dat_inicio_reuniao)
        dicrc["horareuniao"] = context.pysc.hora_formatar_pysc(hora=rc.hr_inicio_reuniao)
        dicrc["datareuniao"] = str(dia).decode('utf-8')
        # obtém o nome do Presidente da Comissão
        dicrc["presidente"] = ''
        for periodo in context.zsql.periodo_comp_comissao_obter_zsql(data=DateTime(rc.dat_inicio_reuniao_ord), ind_excluido=0):
            for cargo in context.zsql.composicao_comissao_obter_zsql(cod_comissao=rc.cod_comissao, cod_periodo_comp=periodo.cod_periodo_comp, cod_cargo=1, ind_excluido=0):
                dicrc["presidente"] = cargo.nom_completo.decode('utf-8').upper()                 
        reuniao.append(dicrc) 
        # seleciona as matérias que compõem a pauta da reuniao
    for item in context.zsql.reuniao_comissao_pauta_obter_zsql(cod_reuniao=cod_reuniao, ind_excluido=0):
        # seleciona os detalhes dos itens da pauta
        dic = {} 
        dic["num_ordem"] = item.num_ordem
        dic["txt_ementa"] = item.txt_observacao
        if item.cod_parecer != None: 
           parecer = context.zsql.relatoria_obter_zsql(cod_relatoria=item.cod_parecer)[0]
           dic["cod_materia"] = item.cod_parecer
           for materia in context.zsql.materia_obter_zsql(cod_materia=parecer.cod_materia, ind_excluido=0):     
               sgl_tipo_materia = materia.sgl_tipo_materia
               num_ident_basica = materia.num_ident_basica
               ano_ident_basica = materia.ano_ident_basica               
           for comissao in context.zsql.comissao_obter_zsql(cod_comissao=parecer.cod_comissao, ind_excluido=0):
               sgl_comissao = comissao.sgl_comissao
           for relator in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parecer.cod_parlamentar):
                dic["nom_relator"] = relator.nom_parlamentar
           dic["link_materia"] = '<link href="' + context.sapl_documentos.absolute_url() + '/parecer_comissao/' + str(item.cod_parecer) + '_parecer.pdf' + '">' + 'PARECER ' + sgl_comissao+ ' Nº ' + str(parecer.num_parecer) + '/' + str(parecer.ano_parecer) + '</link>'
           dic["id_materia"] = 'PARECER ' + sgl_comissao+ ' Nº ' + str(parecer.num_parecer) + '/' + str(parecer.ano_parecer) + " - " +  sgl_tipo_materia +' ' + str(num_ident_basica) + '/' + str(ano_ident_basica)
           dic["nom_autor"] = ""
           dic["substitutivo"] = ''
           dic["substitutivos"] = ''           
           dic["emenda"] = ''
           dic["emendas"] = ''
           
        if item.cod_materia != None:        
           materia = context.zsql.materia_obter_zsql(cod_materia=item.cod_materia)[0]        
           dic["cod_materia"] = item.cod_materia
           dic["link_materia"] = '<link href="'+context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+str(item.cod_materia)+'">'+materia.des_tipo_materia.decode('utf-8').upper()+' Nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</link>'
           dic["id_materia"] = materia.des_tipo_materia.decode('utf-8').upper()+" nº "+str(materia.num_ident_basica)+"/"+str(materia.ano_ident_basica)
           dic["nom_relator"] = ''          
           dic["nom_autor"] = ''
           autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
           fields = autores.data_dictionary().keys()
           lista_autor = []
           for autor in autores:
               for field in fields:
                   nome_autor = autor['nom_autor_join']
               lista_autor.append(nome_autor)
           dic["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 

           dic["substitutivo"] = ''
           lst_qtde_substitutivos=[]
           lst_substitutivos=[]
           for substitutivo in context.zsql.substitutivo_obter_zsql(cod_materia=item.cod_materia,ind_excluido=0):
               autores = context.zsql.autoria_substitutivo_obter_zsql(cod_substitutivo=substitutivo.cod_substitutivo, ind_excluido=0)
               dic_substitutivo = {}
               fields = autores.data_dictionary().keys()
               lista_autor = []
               for autor in autores:
                   for field in fields:
                       nome_autor = autor['nom_autor_join']
                   lista_autor.append(nome_autor)
               autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
               dic_substitutivo["id_substitutivo"] = '<link href="' + context.sapl_documentos.absolute_url() + '/substitutivo/' + str(substitutivo.cod_substitutivo) + '_substitutivo.pdf' + '">' + 'Substitutivo nº ' + str(substitutivo.num_substitutivo) + '</link>'
               dic_substitutivo["txt_ementa"] = substitutivo.txt_ementa
               dic_substitutivo["autoria"] = autoria
               lst_substitutivos.append(dic_substitutivo)
               cod_substitutivo = substitutivo.cod_substitutivo
               lst_qtde_substitutivos.append(cod_substitutivo)
           dic["substitutivos"] = lst_substitutivos
           dic["substitutivo"] = len(lst_qtde_substitutivos)

           dic["emenda"] = ''
           lst_qtde_emendas=[]
           lst_emendas=[]
           for emenda in context.zsql.emenda_obter_zsql(cod_materia=item.cod_materia,ind_excluido=0):
               autores = context.zsql.autoria_emenda_obter_zsql(cod_emenda=emenda.cod_emenda,ind_excluido=0)
               dic_emenda = {}
               fields = autores.data_dictionary().keys()
               lista_autor = []
               for autor in autores:
                   for field in fields:
                       nome_autor = autor['nom_autor_join']
                   lista_autor.append(nome_autor)
               autoria = ', '.join(['%s' % (value) for (value) in lista_autor])
               dic_emenda["id_emenda"] = '<link href="' + context.sapl_documentos.absolute_url() + '/emenda/' + str(emenda.cod_emenda) + '_emenda.pdf' + '">' + 'Emenda nº ' + str(emenda.num_emenda) + ' (' + emenda.des_tipo_emenda.decode('utf-8') + ')</link>'
               dic_emenda["txt_ementa"] = emenda.txt_ementa
               dic_emenda["autoria"] = autoria
               lst_emendas.append(dic_emenda)
               cod_emenda = emenda.cod_emenda
               lst_qtde_emendas.append(cod_emenda)
           dic["emendas"] = lst_emendas
           dic["emenda"] = len(lst_qtde_emendas)

        # adiciona o dicionário na pauta
        pauta.append(dic) 

    # obtém as propriedades da casa legislativa para montar o cabeçalho e o rodapé da página
    casa = {} 
    aux=context.sapl_documentos.props_sagl.propertyItems()
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
    if hasattr(context.sapl_documentos.props_sagl,'logo_casa.gif'):
        imagem = context.sapl_documentos.props_sagl['logo_casa.gif'].absolute_url()
    else:
        imagem = context.imagens.absolute_url() + "/brasao.gif"
        
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

#    return imagem, dat_reuniao, cod_reuniao, reuniao, pauta, cabecalho, rodape
    
    caminho = context.pdf_pauta_comissao_gerar(imagem, dat_reuniao, cod_reuniao, reuniao, pauta, cabecalho, rodape)
    if caminho=='aviso':
        return response.redirect('mensagem_emitir_proc')
    else:
        response.redirect(caminho)
