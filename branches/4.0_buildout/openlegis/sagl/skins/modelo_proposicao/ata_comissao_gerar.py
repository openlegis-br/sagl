## Script (Python) "ata_comissao_gerar"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_reuniao
##title=
##

from Products.CMFCore.utils import getToolByName
st = getToolByName(context, 'portal_sagl')

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE

# seleciona dados da reunião
for rc in context.zsql.reuniao_comissao_obter_zsql(cod_reuniao=cod_reuniao,ind_excluido=0):
    ata_dic = {}
    nom_arquivo = str(rc.cod_reuniao)+'_ata.odt'
    data = context.pysc.data_converter_pysc(rc.dat_inicio_reuniao)
    dat_reuniao = context.pysc.data_converter_pysc(rc.dat_inicio_reuniao)
    for comissao in context.zsql.comissao_obter_zsql(cod_comissao=rc.cod_comissao, ind_excluido=0):     
        ata_dic["nom_comissao"] = comissao.nom_comissao
    ata_dic["reuniao"] = str(rc.num_reuniao)+"ª Reunião " + str(rc.des_tipo_reuniao)
    ata_dic["tema"] =  rc.txt_tema
    dia = context.pysc.data_converter_por_extenso_pysc(data=rc.dat_inicio_reuniao)
    ata_dic["horareuniao"] = context.pysc.hora_formatar_pysc(hora=rc.hr_inicio_reuniao)
    ata_dic["horafimreuniao"] = ''
    if rc.hr_fim_reuniao != '' and  rc.hr_fim_reuniao != None:
       ata_dic["horafimreuniao"] = context.pysc.hora_formatar_pysc(hora=rc.hr_fim_reuniao)
    ata_dic["data"]= rc.dat_inicio_reuniao
    ata_dic["datareuniao"] = str(dia).decode('utf-8')

    # obtém os membros da Comissão
    ata_dic["presidente"] = ''
    lst_membros = []
    lst_presenca = []
    lst_ausencia = []
    for periodo in context.zsql.periodo_comp_comissao_obter_zsql(data=DateTime(rc.dat_inicio_reuniao_ord), ind_excluido=0):
        for membro in context.zsql.composicao_comissao_obter_zsql(cod_comissao=rc.cod_comissao, cod_periodo_comp=periodo.cod_periodo_comp, ind_excluido=0):
            dic_composicao = {}
            dic_composicao["nome"] = membro.nom_completo
            dic_composicao["cargo"] = membro.des_cargo
            if membro.des_cargo == 'Presidente':
               ata_dic["presidente"] = membro.nom_completo
            lst_membros.append(dic_composicao)
            if context.zsql.reuniao_comissao_presenca_obter_zsql(cod_reuniao=rc.cod_reuniao, cod_parlamentar=membro.cod_parlamentar, ind_excluido=0):
               for presenca in context.zsql.reuniao_comissao_presenca_obter_zsql(cod_reuniao=rc.cod_reuniao, cod_parlamentar=membro.cod_parlamentar, ind_excluido=0):
                   lst_presenca.append(presenca.nom_completo)
            else:
               lst_ausencia.append(membro.nom_completo)

    ata_dic["membros"] = lst_membros
    ata_dic["qtde_presenca"] = len(lst_presenca)
    ata_dic["presenca"] = ', '.join(['%s' % (value) for (value) in lst_presenca])
    ata_dic["qtde_ausencia"] = len(lst_ausencia)
    ata_dic["ausencia"] = ', '.join(['%s' % (value) for (value) in lst_ausencia])

    # seleciona as matérias que compõem a pauta da reuniao
    lst_pauta = []
    lst_votacao = []
    for item in context.zsql.reuniao_comissao_pauta_obter_zsql(cod_reuniao=rc.cod_reuniao, ind_excluido=0):
        # seleciona os detalhes dos itens da pauta
        dic_votacao = {} 
        dic_votacao["num_ordem"] = item.num_ordem
        dic_votacao["txt_ementa"] = item.txt_observacao
        dic_votacao["nom_relator"] = ''
        
        if item.cod_parecer != None: 
           parecer = context.zsql.relatoria_obter_zsql(cod_relatoria=item.cod_parecer)[0]
           dic_votacao["cod_materia"] = item.cod_parecer
           for materia in context.zsql.materia_obter_zsql(cod_materia=parecer.cod_materia, ind_excluido=0):     
               sgl_tipo_materia = materia.sgl_tipo_materia
               num_ident_basica = materia.num_ident_basica
               ano_ident_basica = materia.ano_ident_basica
               ementa_materia = materia.txt_ementa               
           for comissao in context.zsql.comissao_obter_zsql(cod_comissao=parecer.cod_comissao, ind_excluido=0):
               sgl_comissao = comissao.sgl_comissao
           for relator in context.zsql.parlamentar_obter_zsql(cod_parlamentar=parecer.cod_parlamentar):
               dic_votacao["nom_relator"] = 'Relatoria: ' + relator.nom_parlamentar
           if parecer.tip_conclusao == 'F':
              dic_votacao['conclusao'] = 'Favorável'
           elif parecer.tip_conclusao == 'C':
              dic_votacao['conclusao'] = 'Contrário'
           dic_votacao["materia"] = '<span><b>' + str(item.num_ordem) + '</b>) <a href="' +context.consultas.absolute_url() + '/parecer_comissao/' + str(item.cod_parecer) + '_parecer.pdf"><b>Parecer ' +  sgl_comissao + ' nº ' + str(parecer.num_parecer)+ '/' +str(parecer.ano_parecer) + '</b></a> - ' + dic_votacao['conclusao'] + ' ao ' + sgl_tipo_materia + ' nº ' + str(num_ident_basica) + '/' + str(ano_ident_basica) + ' - ' + ementa_materia + '</span>'
           dic_votacao["resultado"] = ''
           if item.tip_resultado_votacao != None:
              for resultado in context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=item.tip_resultado_votacao, ind_excluido=0):
                  dic_votacao["resultado"] = 'Resultado: ' + resultado.nom_resultado
           materia = dic_votacao["materia"] + dic_votacao["nom_relator"] + '. ' + dic_votacao["resultado"]
           dic_votacao["nom_autor"] = ""
           dic_votacao["substitutivo"] = ''
           dic_votacao["substitutivos"] = ''           
           dic_votacao["emenda"] = ''
           dic_votacao["emendas"] = ''
           
        if item.cod_materia != None:        
           materia = context.zsql.materia_obter_zsql(cod_materia=item.cod_materia)[0]        
           dic_votacao["cod_materia"] = item.cod_materia
           dic_votacao["nom_relator"] = ''          
           dic_votacao["nom_autor"] = ''
           autores = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
           fields = autores.data_dictionary().keys()
           lista_autor = []
           for autor in autores:
               for field in fields:
                   nome_autor = autor['nom_autor_join']
               lista_autor.append(nome_autor)
           dic_votacao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
           dic_votacao["materia"] = '<span><b>' + str(item.num_ordem) + '</b>) <a href="'+context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+str(item.cod_materia)+'"><b>'+materia.des_tipo_materia+' nº '+str(materia.num_ident_basica)+'/'+str(materia.ano_ident_basica)+'</b></a> - Autoria: ' + dic_votacao["nom_autor"] + ' - ' + item.txt_observacao + '</span>'
           if item.cod_relator != '' and item.cod_relator != None:
              for relator in context.zsql.parlamentar_obter_zsql(cod_parlamentar=item.cod_relator):
                  dic_votacao["nom_relator"] = 'Relatoria: ' + relator.nom_parlamentar
           dic_votacao["resultado"] = ''
           if item.tip_resultado_votacao != None:
              for resultado in context.zsql.tipo_resultado_votacao_obter_zsql(tip_resultado_votacao=item.tip_resultado_votacao, ind_excluido=0):
                  dic_votacao["resultado"] = 'Resultado: ' + resultado.nom_resultado          

           materia = dic_votacao["materia"] + dic_votacao["nom_relator"] + '. ' + dic_votacao["resultado"]

           dic_votacao["substitutivo"] = ''
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
               dic_substitutivo["materia"] = 'Substitutivo nº ' + str(substitutivo.num_substitutivo) + autoria
               dic_substitutivo["txt_ementa"] = substitutivo.txt_ementa
               dic_substitutivo["autoria"] = autoria
               lst_substitutivos.append(dic_substitutivo)
               cod_substitutivo = substitutivo.cod_substitutivo
               lst_qtde_substitutivos.append(cod_substitutivo)
           dic_votacao["substitutivos"] = lst_substitutivos
           dic_votacao["substitutivo"] = len(lst_qtde_substitutivos)

           dic_votacao["emenda"] = ''
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
               dic_emenda["materia"] =  'Emenda ' + emenda.des_tipo_emenda + ' nº ' + str(emenda.num_emenda) + ' - ' + autoria + ' - ' + emenda.txt_ementa
               dic_emenda["txt_ementa"] = emenda.txt_ementa
               dic_emenda["autoria"] = autoria
               lst_emendas.append(dic_emenda)
               cod_emenda = emenda.cod_emenda
               lst_qtde_emendas.append(cod_emenda)
           dic_votacao["emendas"] = lst_emendas
           dic_votacao["emenda"] = len(lst_qtde_emendas)

        # adiciona o dicionário na lista de votações
        lst_pauta.append(materia)
        lst_votacao.append(dic_votacao)

    ata_dic["lst_pauta"] = '; '.join(['%s' % (value) for (value) in lst_pauta])
    ata_dic["lst_votacao"] = lst_votacao

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
    ata_dic['nom_camara'] = casa['nom_casa']
    ata_dic['end_camara'] = casa['end_casa']
    ata_dic["nom_estado"] = nom_estado
    for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
        ata_dic['nom_localidade']= local.nom_localidade
        ata_dic['sgl_uf']= local.sgl_uf

return st.ata_comissao_gerar_odt(ata_dic, nom_arquivo)
