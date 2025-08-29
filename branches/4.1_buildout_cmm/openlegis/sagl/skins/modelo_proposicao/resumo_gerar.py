## Script (Python) "resumo_gerar"
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

for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
  nom_arquivo = str(cod_sessao_plen)+'_resumo_sessao.odt'
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

  # Presidente
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
  lst_presidente = []
  for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
    for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
      for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
        lst_presidente = presidencia.nom_parlamentar

  # Requerimentos
  lst_requerimentos_pesar = []
  lst_requerimentos_congratulacoes = []
  lst_requerimentos = []

  # Obtem materias da pauta do expediente da sessao
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,ind_excluido=0):
     # Filtra materias do tipo Requerimento
     for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,des_tipo_materia='Requerimento',ind_excluido=0):

       # Requerimentos de Pesar
       if 'pesar' in materia.txt_ementa.split():
         dic_requerimentos_pesar = {}
         dic_requerimentos_pesar['num_ident_basica'] = materia.num_ident_basica
         dic_requerimentos_pesar['ano_ident_basica'] = materia.ano_ident_basica
         dic_requerimentos_pesar['txt_ementa'] = materia.txt_ementa
         dic_requerimentos_pesar["nom_autor"] = ""
         autorias = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
         fields = autorias.data_dictionary().keys()
         nom_autor = []
         lista_autor = []
         for autoria in autorias:
           autores = context.zsql.autor_obter_zsql(cod_autor = autoria.cod_autor)
           for autor in autores:
            for field in fields:
             if autor.cod_parlamentar != None:
                parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
                for parlamentar in parlamentares:
                   if parlamentar.sex_parlamentar =='M':
                      cargo = "Vereador"
                      enunciado = "do Vereador "
                   elif parlamentar.sex_parlamentar =='F':
                      cargo = "Vereadora"
                      enunciado = "da Vereadora "
                nom_autor = enunciado + parlamentar.nom_parlamentar
             else:
                nom_autor = autor.nom_autor_join
            lista_autor.append(nom_autor)
         dic_requerimentos_pesar["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         lst_requerimentos_pesar.append(dic_requerimentos_pesar)

       # Requerimentos de Congratulacoes
       if 'congratulações' in materia.txt_ementa.split():
         dic_requerimentos_congratulacoes = {}
         dic_requerimentos_congratulacoes['num_ident_basica'] = materia.num_ident_basica
         dic_requerimentos_congratulacoes['ano_ident_basica'] = materia.ano_ident_basica         
         dic_requerimentos_congratulacoes['txt_ementa'] = materia.txt_ementa
         dic_requerimentos_congratulacoes["nom_autor"] = ""
         autorias = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
         fields = autorias.data_dictionary().keys()
         nom_autor = []
         lista_autor = []
         for autoria in autorias:
           autores = context.zsql.autor_obter_zsql(cod_autor = autoria.cod_autor)
           for autor in autores:
            for field in fields:
             if autor.cod_parlamentar != None:
                parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
                for parlamentar in parlamentares:
                   if parlamentar.sex_parlamentar =='M':
                      cargo = "Vereador"
                      enunciado = "do Vereador "
                   elif parlamentar.sex_parlamentar =='F':
                      cargo = "Vereadora"
                      enunciado = "da Vereadora "
                nom_autor = enunciado + parlamentar.nom_parlamentar
             else:
                nom_autor = autor.nom_autor_join
            lista_autor.append(nom_autor)
         dic_requerimentos_congratulacoes["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         lst_requerimentos_congratulacoes.append(dic_requerimentos_congratulacoes)

       # Requerimentos Diversos
       if 'congratulações' not in materia.txt_ementa.split() and 'pesar' not in materia.txt_ementa.split():
         dic_requerimentos = {}
         dic_requerimentos['num_ident_basica'] = materia.num_ident_basica
         dic_requerimentos['ano_ident_basica'] = materia.ano_ident_basica
         dic_requerimentos['txt_ementa'] = materia.txt_ementa
         dic_requerimentos["nom_autor"] = ""
         autorias = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
         fields = autorias.data_dictionary().keys()
         nom_autor = []
         lista_autor = []
         for autoria in autorias:
           autores = context.zsql.autor_obter_zsql(cod_autor = autoria.cod_autor)
           for autor in autores:
            for field in fields:
             if autor.cod_parlamentar != None:
                parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
                for parlamentar in parlamentares:
                   if parlamentar.sex_parlamentar =='M':
                      cargo = "Vereador"
                      enunciado = "do Vereador "
                   elif parlamentar.sex_parlamentar =='F':
                      cargo = "Vereadora"
                      enunciado = "da Vereadora "
                nom_autor = enunciado + parlamentar.nom_parlamentar
             else:
                nom_autor = autor.nom_autor_join
            lista_autor.append(nom_autor)
         dic_requerimentos["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         for proposicao in context.zsql.proposicao_obter_zsql(ind_mat_ou_doc='M',cod_mat_ou_doc=materia.cod_materia,ind_excluido=0):
           if proposicao:
             dic_requerimentos['num_proposicao'] = proposicao.cod_proposicao
             dic_requerimentos['txt_consideracoes'] = proposicao.txt_consideracoes
             dic_requerimentos['txt_pedido'] = proposicao.txt_pedido
           else:
             dic_requerimentos['num_proposicao'] = ''
             dic_requerimentos['txt_consideracoes'] = ''
             dic_requerimentos['txt_pedido'] = ''
         lst_requerimentos.append(dic_requerimentos)

  # Indicacoes
  lst_indicacao = [] 
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia,des_tipo_materia='Indicação',ind_excluido=0):
      dic_ind = {}
      dic_ind['txt_ementa'] = materia.txt_ementa.encode('utf-8')
      dic_ind['num_ident_basica'] = materia.num_ident_basica
      dic_ind['ano_ident_basica'] = materia.ano_ident_basica
      dic_ind['dat_apresentacao'] = materia.dat_apresentacao
      dic_ind["nom_autor"] = ""
      autorias = context.zsql.autoria_obter_zsql(cod_materia=item.cod_materia)
      fields = autorias.data_dictionary().keys()
      nom_autor = []
      lista_autor = []
      for autoria in autorias:
        autores = context.zsql.autor_obter_zsql(cod_autor = autoria.cod_autor)
        for autor in autores:
         for field in fields:
          if autor.cod_parlamentar != None:
             parlamentares = context.zsql.parlamentar_obter_zsql(cod_parlamentar = autor.cod_parlamentar)
             for parlamentar in parlamentares:
                if parlamentar.sex_parlamentar =='M':
                   cargo = "Vereador"
                   enunciado = "do Vereador "
                elif parlamentar.sex_parlamentar =='F':
                   cargo = "Vereadora"
                   enunciado = "da Vereadora "
             nom_autor = enunciado + parlamentar.nom_parlamentar
          else:
             nom_autor = autor.nom_autor_join
         lista_autor.append(nom_autor)
      dic_ind["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
      for proposicao in context.zsql.proposicao_obter_zsql(ind_mat_ou_doc='M',cod_mat_ou_doc=materia.cod_materia,ind_excluido=0):
        if proposicao:
          dic_ind['num_proposicao'] = proposicao.cod_proposicao
        else:
          dic_ind['num_proposicao'] = ''
      lst_indicacao.append(dic_ind)

   # Lista das materias objeto de deliberacao
  lst_deliberacao=[]
  for deliberacao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,tip_turno=5,ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=deliberacao.cod_materia)[0]
      dic_deliberacao = {}
      dic_deliberacao["tip_materia"] = materia.des_tipo_materia
      dic_deliberacao["num_ident_basica"] = materia.num_ident_basica
      dic_deliberacao["ano_ident_basica"] = str(materia.ano_ident_basica)
      dic_deliberacao["txt_ementa"] = materia.txt_ementa
      dic_deliberacao["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=deliberacao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	      for field in fields:
                nome_autor = autor['nom_autor_join']
	      lista_autor.append(nome_autor)
      dic_deliberacao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      lst_deliberacao.append(dic_deliberacao)
  lst_deliberacao = [(i + 1, j) for i, j in enumerate(lst_deliberacao)]
  deliberacao = []
  for i, dic in lst_deliberacao:
     dic_delibera = {}
     dic_delibera["num_ordem"] = i
     dic_delibera["tip_materia"] = dic.get('tip_materia',dic)
     dic_delibera["num_ident_basica"] = dic.get('num_ident_basica',dic)
     dic_delibera["ano_ident_basica"] = dic.get('ano_ident_basica',dic)
     dic_delibera["nom_autor"] = dic.get('nom_autor',dic)
     dic_delibera["txt_ementa"] = dic.get('txt_ementa',dic)
     deliberacao.append(dic_delibera)
  lst_deliberacao = deliberacao

   # Lista das materias em 1a discussao
  lst_pdiscussao=[]
  for pdiscussao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,tip_turno=1,ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=pdiscussao.cod_materia)[0]
      dic_pdiscussao = {}
      dic_pdiscussao["tip_materia"] = materia.des_tipo_materia
      dic_pdiscussao["num_ident_basica"] = materia.num_ident_basica
      dic_pdiscussao["ano_ident_basica"] = str(materia.ano_ident_basica)
      dic_pdiscussao["link_materia"] = context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+pdiscussao.cod_materia
      dic_pdiscussao["txt_ementa"] = materia.txt_ementa
      dic_pdiscussao["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=pdiscussao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	      for field in fields:
                nome_autor = autor['nom_autor_join']
	      lista_autor.append(nome_autor)
      dic_pdiscussao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      lst_pdiscussao.append(dic_pdiscussao)
  lst_pdiscussao = [(i + 1, j) for i, j in enumerate(lst_pdiscussao)]
  pdisc = []
  for i, dic in lst_pdiscussao:
     dic_pdisc = {}
     dic_pdisc["num_ordem"] = i
     dic_pdisc["tip_materia"] = dic.get('tip_materia',dic)
     dic_pdisc["num_ident_basica"] = dic.get('num_ident_basica',dic)
     dic_pdisc["ano_ident_basica"] = dic.get('ano_ident_basica',dic)
     dic_pdisc["nom_autor"] = dic.get('nom_autor',dic)
     dic_pdisc["txt_ementa"] = dic.get('txt_ementa',dic)
     pdisc.append(dic_pdisc)
  lst_pdiscussao = pdisc

   # Lista das materias em 2a discussao
  lst_sdiscussao=[]
  for sdiscussao in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,tip_turno=2,ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=sdiscussao.cod_materia)[0]
      dic_sdiscussao = {}
      dic_sdiscussao["tip_materia"] = materia.des_tipo_materia
      dic_sdiscussao["num_ident_basica"] = materia.num_ident_basica
      dic_sdiscussao["ano_ident_basica"] = str(materia.ano_ident_basica)
      dic_sdiscussao["link_materia"] = context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+sdiscussao.cod_materia
      dic_sdiscussao["txt_ementa"] = materia.txt_ementa
      dic_sdiscussao["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=sdiscussao.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	      for field in fields:
                nome_autor = autor['nom_autor_join']
	      lista_autor.append(nome_autor)
      dic_sdiscussao["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      lst_sdiscussao.append(dic_sdiscussao)
  lst_sdiscussao = [(i + 1, j) for i, j in enumerate(lst_sdiscussao)]
  sdisc = []
  for i, dic in lst_sdiscussao:
     dic_sdisc = {}
     dic_sdisc["num_ordem"] = i
     dic_sdisc["tip_materia"] = dic.get('tip_materia',dic)
     dic_sdisc["num_ident_basica"] = dic.get('num_ident_basica',dic)
     dic_sdisc["ano_ident_basica"] = dic.get('ano_ident_basica',dic)
     dic_sdisc["nom_autor"] = dic.get('nom_autor',dic)
     dic_sdisc["txt_ementa"] = dic.get('txt_ementa',dic)
     sdisc.append(dic_sdisc)
  lst_sdiscussao = sdisc

   # Lista das materias em discussao unica
  lst_discussao_unica=[]
  for discussao_unica in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=sessao.cod_sessao_plen,tip_turno=3,ind_excluido=0):
      materia = context.zsql.materia_obter_zsql(cod_materia=discussao_unica.cod_materia)[0]
      dic_discussao_unica = {}
      dic_discussao_unica["tip_materia"] = materia.des_tipo_materia
      dic_discussao_unica["num_ident_basica"] = materia.num_ident_basica
      dic_discussao_unica["ano_ident_basica"] = str(materia.ano_ident_basica)
      dic_discussao_unica["link_materia"] = context.consultas.absolute_url()+'/materia/materia_mostrar_proc?cod_materia='+discussao_unica.cod_materia
      dic_discussao_unica["txt_ementa"] = materia.txt_ementa
      dic_discussao_unica["nom_autor"] = ""
      autores = context.zsql.autoria_obter_zsql(cod_materia=discussao_unica.cod_materia)
      fields = autores.data_dictionary().keys()
      lista_autor = []
      for autor in autores:
	      for field in fields:
                nome_autor = autor['nom_autor_join']
	      lista_autor.append(nome_autor)
      dic_discussao_unica["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor]) 
      lst_discussao_unica.append(dic_discussao_unica)
  lst_discussao_unica = [(i + 1, j) for i, j in enumerate(lst_discussao_unica)]
  disc = []
  for i, dic in lst_discussao_unica:
     dic_disc = {}
     dic_disc["num_ordem"] = i
     dic_disc["tip_materia"] = dic.get('tip_materia',dic)
     dic_disc["num_ident_basica"] = dic.get('num_ident_basica',dic)
     dic_disc["ano_ident_basica"] = dic.get('ano_ident_basica',dic)
     dic_disc["nom_autor"] = dic.get('nom_autor',dic)
     dic_disc["txt_ementa"] = dic.get('txt_ementa',dic)
     disc.append(dic_disc)
  lst_discussao_unica = disc

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
  for local in context.zsql.localidade_obter_zsql(cod_localidade = casa['cod_localidade']):
      inf_basicas_dic['nom_localidade']= local.nom_localidade.encode('utf-8')
      inf_basicas_dic['sgl_uf']= local.sgl_uf

return st.resumo_gerar_odt(cod_sessao_plen, inf_basicas_dic, lst_requerimentos_pesar, lst_requerimentos_congratulacoes, lst_requerimentos, lst_indicacao, lst_deliberacao, lst_pdiscussao, lst_sdiscussao, lst_discussao_unica, lst_presidente, nom_arquivo)
