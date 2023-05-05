## Script (Python) "ordem_dia"
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

request = context.REQUEST
response =  request.RESPONSE

if request.has_key('ind_audiencia'):
  for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_audiencia=1, ind_excluido=0):
    inf_basicas_dic = {}
    tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_audiencia='1',ind_excluido=0)[0]
    inf_basicas_dic["cod_sessao_plen"] = sessao.cod_sessao_plen
    # CM Jaboticabal
    #inf_basicas_dic["num_tip_sessao"] = sessao.num_tip_sessao  
    inf_basicas_dic["num_sessao_plen"] = sessao.num_sessao_plen
    inf_basicas_dic["nom_sessao"] = tipo_sessao.nom_sessao
    inf_basicas_dic["num_legislatura"] = sessao.num_legislatura
    inf_basicas_dic["num_sessao_leg"] = sessao.num_sessao_leg
    inf_basicas_dic["dat_inicio_sessao"] = sessao.dat_inicio_sessao
    inf_basicas_dic["dia_sessao"] = context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao)
    inf_basicas_dic["hr_inicio_sessao"] = sessao.hr_inicio_sessao
    inf_basicas_dic["dat_fim_sessao"] = sessao.dat_fim_sessao
    inf_basicas_dic["hr_fim_sessao"] = sessao.hr_fim_sessao
    data = context.pysc.data_converter_pysc(sessao.dat_inicio_sessao)
    nom_arquivo = str(cod_sessao_plen)+'_pauta_sessao.odt'
        # Presidente
    lst_presidente = []
    for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_audiencia=1, ind_excluido=0):
      data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
    for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
      for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
        for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
          lst_presidente = presidencia.nom_completo
    lst_pdiscussao=[]
    for pdiscussao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=inf_basicas_dic["cod_sessao_plen"], ind_excluido=0):
        materia = context.zsql.materia_obter_zsql(cod_materia=pdiscussao.cod_materia)[0]
        dic_pdiscussao = {}
        dic_pdiscussao["num_ordem"] = pdiscussao.num_ordem
        dic_pdiscussao["tip_materia"] = materia.des_tipo_materia.decode('utf-8').upper()
        dic_pdiscussao["num_ident_basica"] = materia.num_ident_basica
        dic_pdiscussao["ano_ident_basica"] = context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))
        dic_pdiscussao["link_materia"] = context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+pdiscussao.cod_materia
        dic_pdiscussao["txt_ementa"] = materia.txt_ementa
        dic_pdiscussao["des_numeracao"]=""
        numeracao = context.zsql.numeracao_obter_zsql(cod_materia=pdiscussao.cod_materia)
        if len(numeracao):
           numeracao = numeracao[0]
           dic_pdiscussao["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
        dic_pdiscussao["nom_autor"] = ""
        autores = context.zsql.autoria_obter_zsql(cod_materia=pdiscussao.cod_materia)
        fields = autores.data_dictionary().keys()
        lista_autor = []
        for autor in autores:
            for field in fields:
                nome_autor = autor['nom_autor_join']
            lista_autor.append(nome_autor)
        dic_pdiscussao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
        dic_pdiscussao["des_turno"]=""
        dic_pdiscussao["des_quorum"]=""
        dic_pdiscussao["tip_votacao"]=""
        lst_pdiscussao.append(dic_pdiscussao)
    lst_sdiscussao=[]
    lst_discussao_unica=[]
else:
  for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
    inf_basicas_dic = {}
    tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
    inf_basicas_dic["cod_sessao_plen"] = sessao.cod_sessao_plen
    # CM Jaboticabal
    #inf_basicas_dic["num_tip_sessao"] = sessao.num_tip_sessao  
    inf_basicas_dic["num_sessao_plen"] = sessao.num_sessao_plen
    inf_basicas_dic["nom_sessao"] = tipo_sessao.nom_sessao
    inf_basicas_dic["num_legislatura"] = sessao.num_legislatura
    inf_basicas_dic["num_sessao_leg"] = sessao.num_sessao_leg
    inf_basicas_dic["dat_inicio_sessao"] = sessao.dat_inicio_sessao
    inf_basicas_dic["dia_sessao"] = context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao)
    inf_basicas_dic["hr_inicio_sessao"] = sessao.hr_inicio_sessao
    inf_basicas_dic["dat_fim_sessao"] = sessao.dat_fim_sessao
    inf_basicas_dic["hr_fim_sessao"] = sessao.hr_fim_sessao
    data = context.pysc.data_converter_pysc(sessao.dat_inicio_sessao)

    nom_arquivo = str(cod_sessao_plen)+'_pauta_sessao.odt'

    # Presidente
    lst_presidente = []
    for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
      data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
    for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
      for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
        for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
          lst_presidente = presidencia.nom_completo

     # Lista das materias em 1a discussao
    lst_pdiscussao=[]
    for pdiscussao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=inf_basicas_dic["cod_sessao_plen"],tip_turno=1,ind_excluido=0):
        materia = context.zsql.materia_obter_zsql(cod_materia=pdiscussao.cod_materia)[0]
        dic_pdiscussao = {}
        dic_pdiscussao["num_ordem"] = pdiscussao.num_ordem
        dic_pdiscussao["tip_materia"] = materia.des_tipo_materia.decode('utf-8').upper()
        dic_pdiscussao["num_ident_basica"] = materia.num_ident_basica
        dic_pdiscussao["ano_ident_basica"] = context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))
        dic_pdiscussao["link_materia"] = context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+pdiscussao.cod_materia
        dic_pdiscussao["txt_ementa"] = materia.txt_ementa
        dic_pdiscussao["des_numeracao"]=""
        numeracao = context.zsql.numeracao_obter_zsql(cod_materia=pdiscussao.cod_materia)
        if len(numeracao):
           numeracao = numeracao[0]
           dic_pdiscussao["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
        dic_pdiscussao["nom_autor"] = ""
        autores = context.zsql.autoria_obter_zsql(cod_materia=pdiscussao.cod_materia)
        fields = autores.data_dictionary().keys()
        lista_autor = []
        for autor in autores:
            for field in fields:
                nome_autor = autor['nom_autor_join']
            lista_autor.append(nome_autor)
        dic_pdiscussao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
        dic_pdiscussao["des_turno"]=""
        for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=pdiscussao.tip_turno):
           dic_pdiscussao["des_turno"] = turno.des_turno
        dic_pdiscussao["des_quorum"]=""
        for quorum in context.zsql.quorum_votacao_obter_zsql(cod_quorum=pdiscussao.tip_quorum):
           dic_pdiscussao["des_quorum"] = quorum.des_quorum
        dic_pdiscussao["tip_votacao"]=""
        for tip_votacao in context.zsql.tipo_votacao_obter_zsql(tip_votacao=pdiscussao.tip_votacao):
           dic_pdiscussao["tip_votacao"] = tip_votacao.des_tipo_votacao
      
        lst_pdiscussao.append(dic_pdiscussao)

    # Lista das materias em 2a discussao
    lst_sdiscussao=[]
    for sdiscussao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=inf_basicas_dic["cod_sessao_plen"], tip_turno=2,ind_excluido=0):
        materia = context.zsql.materia_obter_zsql(cod_materia=sdiscussao.cod_materia)[0]
        dic_sdiscussao = {}
        dic_sdiscussao["num_ordem"] = sdiscussao.num_ordem
        dic_sdiscussao["tip_materia"] = materia.des_tipo_materia.decode('utf-8').upper()
        dic_sdiscussao["num_ident_basica"] = materia.num_ident_basica
        dic_sdiscussao["ano_ident_basica"] = context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))
        dic_sdiscussao["link_materia"] = context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+sdiscussao.cod_materia
        dic_sdiscussao["txt_ementa"] = materia.txt_ementa
        dic_sdiscussao["des_numeracao"]=""
        numeracao = context.zsql.numeracao_obter_zsql(cod_materia=sdiscussao.cod_materia)
        if len(numeracao):
           numeracao = numeracao[0]
           dic_sdiscussao["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
        dic_sdiscussao["nom_autor"] = ""
        autores = context.zsql.autoria_obter_zsql(cod_materia=sdiscussao.cod_materia)
        fields = autores.data_dictionary().keys()
        lista_autor = []
        for autor in autores:
            for field in fields:
                nome_autor = autor['nom_autor_join']
            lista_autor.append(nome_autor)
        dic_sdiscussao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
        dic_sdiscussao["des_turno"]=""
        for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=sdiscussao.tip_turno):
           dic_sdiscussao["des_turno"] = turno.des_turno
        dic_sdiscussao["des_quorum"]=""
        for quorum in context.zsql.quorum_votacao_obter_zsql(cod_quorum=sdiscussao.tip_quorum):
           dic_sdiscussao["des_quorum"] = quorum.des_quorum
        dic_sdiscussao["tip_votacao"]=""
        for tip_votacao in context.zsql.tipo_votacao_obter_zsql(tip_votacao=sdiscussao.tip_votacao):
           dic_sdiscussao["tip_votacao"] = tip_votacao.des_tipo_votacao      
      
        lst_sdiscussao.append(dic_sdiscussao)

    # Lista das materias em discussao unica
    lst_discussao_unica=[]
    for discussao_unica in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=inf_basicas_dic["cod_sessao_plen"], tip_turno=3,ind_excluido=0):
        materia = context.zsql.materia_obter_zsql(cod_materia=discussao_unica.cod_materia)[0]
        dic_discussao_unica = {}
        dic_discussao_unica["num_ordem"] = discussao_unica.num_ordem
        dic_discussao_unica["tip_materia"] = materia.des_tipo_materia.decode('utf-8').upper()
        dic_discussao_unica["num_ident_basica"] = materia.num_ident_basica
        dic_discussao_unica["ano_ident_basica"] = context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica))
        dic_discussao_unica["link_materia"] = context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+discussao_unica.cod_materia
        dic_discussao_unica["txt_ementa"] = materia.txt_ementa
        dic_discussao_unica["des_numeracao"]=""
        numeracao = context.zsql.numeracao_obter_zsql(cod_materia=discussao_unica.cod_materia)
        if len(numeracao):
           numeracao = numeracao[0]
           dic_discussao_unica["des_numeracao"] = str(numeracao.num_materia)+"/"+str(numeracao.ano_materia)
        dic_discussao_unica["nom_autor"] = ""
        autores = context.zsql.autoria_obter_zsql(cod_materia=discussao_unica.cod_materia)
        fields = autores.data_dictionary().keys()
        lista_autor = []
        for autor in autores:
	    for field in fields:
                nome_autor = autor['nom_autor_join']
	    lista_autor.append(nome_autor)
        dic_discussao_unica["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
        dic_discussao_unica["des_turno"]=""
        for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=discussao_unica.tip_turno):
           dic_discussao_unica["des_turno"] = turno.des_turno
        dic_discussao_unica["des_quorum"]=""
        for quorum in context.zsql.quorum_votacao_obter_zsql(cod_quorum=discussao_unica.tip_quorum):
           dic_discussao_unica["des_quorum"] = quorum.des_quorum
        dic_discussao_unica["tip_votacao"]=""
        for tip_votacao in context.zsql.tipo_votacao_obter_zsql(tip_votacao=discussao_unica.tip_votacao):
           dic_discussao_unica["tip_votacao"] = tip_votacao.des_tipo_votacao
      
        lst_discussao_unica.append(dic_discussao_unica)

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

return st.ordem_dia_gerar_odt(inf_basicas_dic, lst_pdiscussao, lst_sdiscussao, lst_discussao_unica, lst_presidente, nom_arquivo)
