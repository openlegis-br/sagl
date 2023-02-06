## Script (Python) "gera_pauta_cmm_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, cod_status
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE

itens = []

lst_adiadas = []
for sessao_anterior in context.zsql.sessao_plenaria_penultima_obter_zsql():
  cod_sessao_anterior = sessao_anterior.cod_sessao_plen
  for item in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_anterior, ind_excluido=0):
      for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia):
          dic_adiadas = {}
          dic_adiadas['cod_materia'] = item.cod_materia
          dic_adiadas['txt_observacao'] = item.txt_observacao
          for resultado in context.zsql.votacao_materia_expediente_pesquisar_zsql(cod_sessao_plen=cod_sessao_anterior, cod_materia=item.cod_materia):
              if int(materia.ind_tramitacao) == 1 and (int(resultado.cod_sessao_plen) == int(cod_sessao_anterior) and int(resultado.tip_resultado_votacao) == 3):
                 lst_adiadas.append(dic_adiadas)

for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
  cod_sessao_leg = sessao.cod_sessao_leg
  num_legislatura = sessao.num_legislatura
  tip_sessao = sessao.tip_sessao
  dat_ordem = context.pysc.data_converter_pysc(sessao.dat_inicio_sessao)
  lst_tip_quorum = 1
  rad_tip_votacao = 1

 # Presidente
  for dat_sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    data = context.pysc.data_converter_pysc(dat_sessao.dat_inicio_sessao)
  lst_presidente = []
  for sleg in context.zsql.periodo_comp_mesa_obter_zsql(num_legislatura=sessao.num_legislatura,data=data):
    for cod_presidente in context.zsql.composicao_mesa_obter_zsql(cod_periodo_comp=sleg.cod_periodo_comp,cod_cargo=1):
      for presidencia in context.zsql.parlamentar_obter_zsql(cod_parlamentar=cod_presidente.cod_parlamentar):
        lst_presidente = presidencia.nom_parlamentar

  # Veredores para ordenacao alfabetica
  vereadores=[]

  # Listas
  lst_indicacao = []
  lst_requerimentos_pesar = []
  lst_requerimentos_congratulacoes = []
  lst_requerimentos = []

  # Obtem materias com status de tramitacao selecionado no formulario
  for materia in context.zsql.tramitacao_pesquisar_status_zsql(cod_status=cod_status):
     # Indicacoes
     if materia.des_tipo_materia == 'Indicação':
       dic_ind = {}
       dic_ind['cod_materia'] = materia.cod_materia
       dic_ind['txt_observacao'] = materia.txt_exibicao
       dic_ind["nom_autor"] = ""
       autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
       fields = autores.data_dictionary().keys()
       lista_autor = []
       for autor in autores:
           for field in fields:
                 nome_autor = autor['nom_autor_join']
           lista_autor.append(nome_autor)
       dic_ind["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
       lst_indicacao.append(dic_ind)

     # Autoria de Requerimentos 
     if materia.des_tipo_materia == 'Requerimento':
         autoria = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)[0]
         for autor in context.zsql.autor_obter_zsql(cod_autor=autoria.cod_autor):
             dic_autores = {}
             for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar):
                 dic_autores["nome_completo"] = parlamentar['nom_completo']
                 dic_autores["txt_autoria"] = parlamentar['nom_parlamentar']
                 vereadores.append(dic_autores)

     # Requerimentos de Pesar
     if materia.des_tipo_materia == 'Requerimento' and 'pesar' in materia.txt_exibicao.split():
         dic_requerimentos_pesar = {}
         dic_requerimentos_pesar['cod_materia'] = materia.cod_materia
         dic_requerimentos_pesar['txt_observacao'] = materia.txt_exibicao
         dic_requerimentos_pesar["nom_autor"] = ""
         autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
         fields = autores.data_dictionary().keys()
         lista_autor = []
         for autor in autores:
           for field in fields:
              nome_autor = autor['nom_autor_join']
           lista_autor.append(nome_autor)
         dic_requerimentos_pesar["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         if int(materia.ind_tram) == 1 and not context.zsql.votacao_materia_expediente_pesquisar_zsql(cod_materia=materia.cod_materia):
            lst_requerimentos_pesar.append(dic_requerimentos_pesar)

     # Requerimentos de Congratulacoes
     if materia.des_tipo_materia == 'Requerimento' and 'congratulações' in materia.txt_exibicao.split():
         dic_requerimentos_congratulacoes = {}
         dic_requerimentos_congratulacoes['cod_materia'] = materia.cod_materia
         dic_requerimentos_congratulacoes['txt_observacao'] = materia.txt_exibicao
         dic_requerimentos_congratulacoes["nom_autor"] = ""
         autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
         fields = autores.data_dictionary().keys()
         lista_autor = []
         for autor in autores:
           for field in fields:
              nome_autor = autor['nom_autor_join']
           lista_autor.append(nome_autor)
         dic_requerimentos_congratulacoes["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         if int(materia.ind_tram) == 1 and not context.zsql.votacao_materia_expediente_pesquisar_zsql(cod_materia=materia.cod_materia):
            lst_requerimentos_congratulacoes.append(dic_requerimentos_congratulacoes)

       # Requerimentos de Solicitacao
     if materia.des_tipo_materia == 'Requerimento' and 'congratulações' not in materia.txt_exibicao.split() and 'pesar' not in materia.txt_exibicao.split():
         dic_requerimentos = {}
         dic_requerimentos['cod_materia'] = materia.cod_materia
         dic_requerimentos['txt_observacao'] = materia.txt_exibicao
         dic_requerimentos["nom_autor"] = ""
         autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
         fields = autores.data_dictionary().keys()
         lista_autor = []
         for autor in autores:
           for field in fields:
              nome_autor = autor['nom_autor_join']
           lista_autor.append(nome_autor)
         dic_requerimentos["nom_autor"] = ', '.join(['%s' % (value) for (value) in lista_autor])
         if int(materia.ind_tram) == 1 and not context.zsql.votacao_materia_expediente_pesquisar_zsql(cod_materia=materia.cod_materia):
            lst_requerimentos.append(dic_requerimentos)

  # Selecione apenas uma ocorrencia por nome do vereador
  vereadores = [
      e
      for i, e in enumerate(vereadores)
      if vereadores.index(e) == i
      ]

  # Ordem vereadores alfabeticamente
  vereadores.sort()

  # Ordena requerimentos por autor
  pesar = []
  congrat = []
  demais=[]
  for autor in vereadores:
   for materia in lst_requerimentos_pesar:
     if autor.get('txt_autoria',autor) == materia.get('nom_autor',materia):
       pesar.append(materia)
   for materia in lst_requerimentos_congratulacoes:
     if autor.get('txt_autoria',autor) == materia.get('nom_autor',materia):
       congrat.append(materia)
   for materia in lst_requerimentos:
     if autor.get('txt_autoria',autor) == materia.get('nom_autor',materia):
       demais.append(materia)

  # Alterna requerimentos de pesar - ate 10 ciclos
  listap1 = []
  listap2 = []
  listap3 = []
  listap4 = []
  listap5 = []
  listap6 = []
  listap7 = []
  listap8 = []
  listap9 = []
  listap10 = []
  listap11 = []
  listap12 = []
  listap13 = []
  listap14 = []
  listap15 = []

  for autor in vereadores:
    materias = filter(lambda nome: nome['nom_autor'] == autor.get('txt_autoria',autor), pesar)
    for materia in materias[0:1]:
      listap1.append(materia)
    for materia in materias[1:2]:
      listap2.append(materia)
    for materia in materias[2:3]:
      listap3.append(materia)
    for materia in materias[3:4]:
      listap4.append(materia)
    for materia in materias[4:5]:
      listap5.append(materia)
    for materia in materias[5:6]:
      listap6.append(materia)
    for materia in materias[6:7]:
      listap7.append(materia)
    for materia in materias[7:8]:
      listap8.append(materia)
    for materia in materias[8:9]:
      listap9.append(materia)
    for materia in materias[9:10]:
      listap10.append(materia)
    for materia in materias[10:11]:
      listap11.append(materia)
    for materia in materias[11:12]:
      listap12.append(materia)
    for materia in materias[12:13]:
      listap13.append(materia)
    for materia in materias[13:14]:
      listap14.append(materia)
    for materia in materias[14:15]:
      listap15.append(materia)

  lst_requerimentos_pesar = listap1 + listap2 + listap3 + listap4 + listap5 + listap6 + listap7 + listap8 + listap9 + listap10 + listap11 + listap12 + listap13 + listap14 + listap15

  # Alterna requerimentos de congratulacoes
  listac1 = []
  listac2 = []
  for autor in vereadores:
    materias = filter(lambda nome: nome['nom_autor'] == autor.get('txt_autoria',autor), congrat)
    for materia in materias[0:1]:
      listac1.append(materia)
    for materia in materias[1:2]:
      listac2.append(materia)
  lst_requerimentos_congratulacoes = listac1 + listac2

  # Alterna requerimentos diversos
  listar1 = []
  listar2 = []
  listar3 = []

  for autor in vereadores:
   materias = filter(lambda nome: nome['nom_autor'] == autor.get('txt_autoria',autor), demais)
   for materia in materias[0:1]:
     if materia['nom_autor'] != str(lst_presidente):
       listar1.append(materia)
   for materia in materias:
     if materia['nom_autor'] == str(lst_presidente):
       listar1.append(materia)
   for materia in materias[1:2]:
     if materia['nom_autor'] != str(lst_presidente):
       listar2.append(materia)
   for materia in materias[2:3]:
     if materia['nom_autor'] != str(lst_presidente):
       listar3.append(materia)
  lst_requerimentos = listar1 + listar2 + listar3

for item in lst_indicacao:
  itens.append(item)

for item in lst_requerimentos_pesar:
  itens.append(item)

for item in lst_requerimentos_congratulacoes:
  itens.append(item)

for item in lst_adiadas:
  itens.append(item)

for item in lst_requerimentos:
  itens.append(item)

itens = [(i + 1, j) for i, j in enumerate(itens)]

for i, dic in itens:
  context.zsql.expediente_materia_incluir_zsql(cod_sessao_plen = cod_sessao_plen, cod_materia=dic.get('cod_materia',dic), dat_ordem=dat_ordem, txt_observacao=str(dic.get('txt_observacao',dic)), num_ordem=i, tip_quorum=lst_tip_quorum, tip_votacao=rad_tip_votacao)

mensagem = 'Pauta gerada com sucesso!'
mensagem_obs = ''   
redirect_url=context.portal_url()+'/mensagem_emitir?modal=1&tipo_mensagem=success&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs
RESPONSE.redirect(redirect_url)

