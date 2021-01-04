## Script (Python) "gerar_itens_painel_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##

itens = []

cod_sessao_plen = int(context.REQUEST['cod_sessao_plen'])

for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=int(context.REQUEST['cod_sessao_plen']), ind_excluido=0):
  tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
  dic_sessao = {}
  dic_sessao["tipo_item"] = 'Mensagem'
  cod_sessao_plen = sessao.cod_sessao_plen
  dic_sessao["cod_sessao_plen"] = sessao.cod_sessao_plen
  dic_sessao["nom_fase"] = 'Abertura'
  dic_sessao["txt_exibicao"] = str(sessao.num_sessao_plen)+'ª' + ' Sessão '+ tipo_sessao.nom_sessao + ' (' + context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao) + ' - ' + sessao.hr_inicio_sessao +'hs)'
  dic_sessao["cod_materia"] = ''
  dic_sessao["txt_autoria"] = ''
  dic_sessao["txt_turno"] = ''
  dic_sessao["txt_quorum"] = ''
  dic_sessao["ind_extrapauta"] = 0
  dic_sessao["ind_exibicao"] = 0
  itens.append(dic_sessao)


dic_presenca = {}
dic_presenca["tipo_item"] = 'Mensagem'
dic_presenca["cod_sessao_plen"] = sessao.cod_sessao_plen
dic_presenca["nom_fase"] = 'Presença'
dic_presenca["txt_exibicao"] = 'Registro de Presença'
dic_presenca["cod_materia"] = ''
dic_presenca["txt_autoria"] = ''
dic_presenca["txt_turno"] = ''
dic_presenca["ind_extrapauta"] = 0
dic_presenca["ind_exibicao"] = 0
itens.append(dic_presenca)

#dic_correspondencias = {}
#dic_correspondencias["tipo_item"] = 'Mensagem'
#dic_correspondencias["nom_fase"] = 'Expediente'
#dic_correspondencias["txt_exibicao"] = '<b>Leitura de correspondências e outros documentos despachados ao Expediente</b><br />' + ' \n ' + dic_sessao["txt_exibicao"]
#dic_correspondencias["cod_materia"] = ''
#dic_correspondencias["txt_autoria"] = ''
#dic_correspondencias["txt_turno"] = ''
#dic_correspondencias["ind_extrapauta"] = 0
#dic_correspondencias["ind_exibicao"] = 0
#itens.append(dic_correspondencias)

lst_indicacoes = []
for indicacoes in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=int(context.REQUEST['cod_sessao_plen']),ind_excluido=0):
  for materia in context.zsql.materia_obter_zsql(cod_materia=indicacoes.cod_materia, des_tipo_materia='Indicação', ind_excluido=0):
    num_ident_basica = materia.num_ident_basica
    lst_indicacoes.append(num_ident_basica)

if len(lst_indicacoes) > 0:
  dic_indicacoes = {}
  dic_indicacoes["tipo_item"] = 'Mensagem'
  dic_indicacoes["cod_sessao_plen"] = sessao.cod_sessao_plen
  dic_indicacoes["nom_fase"] = 'Expediente'
  ano = DateTime().strftime('%Y')
  dic_indicacoes["txt_exibicao"] = '<b>Indicações de números '+str(min(lst_indicacoes))+'/'+ano+ ' a '+str(max(lst_indicacoes))+'/'+ano + '</b><br />' + dic_sessao["txt_exibicao"]
  dic_indicacoes["cod_materia"] = ''
  dic_indicacoes["txt_autoria"] = ''
  dic_indicacoes["txt_turno"] = ''
  dic_indicacoes["ind_extrapauta"] = 0
  dic_indicacoes["ind_exibicao"] = 0
  itens.append(dic_indicacoes)

for requerimentos in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=int(context.REQUEST['cod_sessao_plen']),ind_excluido=0):
  dic_requerimentos = {}
  for materia in context.zsql.materia_obter_zsql(cod_materia=requerimentos.cod_materia, des_tipo_materia='Requerimento', ind_excluido=0):
    dic_requerimentos["tipo_item"] = 'Matéria'
    dic_requerimentos["cod_sessao_plen"] = sessao.cod_sessao_plen
    dic_requerimentos["nom_fase"] = 'Expediente'
    dic_requerimentos["txt_exibicao"] = materia.sgl_tipo_materia.decode('utf-8').upper()+' Nº '+str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa
    dic_requerimentos["cod_materia"] = materia.cod_materia
    dic_requerimentos["txt_autoria"] = ''
    autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
    fields = autores.data_dictionary().keys()
    lista_autor = []
    for autor in autores:
      for field in fields:
        nome_autor = autor['nom_autor_join']
      lista_autor.append(nome_autor)
    dic_requerimentos["txt_autoria"] = ', '.join(['%s' % (value) for (value) in lista_autor])
    dic_requerimentos["txt_turno"] = ''
    dic_requerimentos["ind_extrapauta"] = 0
    dic_requerimentos["ind_exibicao"] = 0
    itens.append(dic_requerimentos)

#for mocoes in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=int(context.REQUEST['cod_sessao_plen']),ind_excluido=0):
#  dic_mocoes = {}
#  for materia in context.zsql.materia_obter_zsql(cod_materia=mocoes.cod_materia, des_tipo_materia='Moção', ind_excluido=0):
#    dic_mocoes["tipo_item"] = 'Matéria'
#    dic_mocoes["nom_fase"] = 'Expediente'
#    dic_mocoes["txt_exibicao"] = materia.sgl_tipo_materia.decode('utf-8').upper()+' Nº '+str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa
#    dic_mocoes["cod_materia"] = materia.cod_materia
#    dic_mocoes["txt_autoria"] = ''
#    autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
#    fields = autores.data_dictionary().keys()
#    lista_autor = []
#    for autor in autores:
#      for field in fields:
#        nome_autor = autor['nom_autor_join']
#      lista_autor.append(nome_autor)
#    dic_mocoes["txt_autoria"] = ', '.join(['%s' % (value) for (value) in lista_autor])
#    dic_mocoes["txt_turno"] = ''
#    dic_mocoes["ind_extrapauta"] = 0
#    dic_mocoes["ind_exibicao"] = 0
#    itens.append(dic_mocoes)

#dic_peq_expediente = {}
#dic_peq_expediente["tipo_item"] = 'Mensagem'
#dic_peq_expediente["nom_fase"] = 'Expediente'
#dic_peq_expediente["txt_exibicao"] = '<b>Pequeno Expediente' + '</b><br />' + dic_sessao["txt_exibicao"]
#dic_peq_expediente["cod_materia"] = ''
#dic_peq_expediente["txt_autoria"] = ''
#dic_peq_expediente["txt_turno"] = ''
#dic_peq_expediente["ind_extrapauta"] = 0
#dic_peq_expediente["ind_exibicao"] = 0
#itens.append(dic_peq_expediente)

dic_orddia = {}
dic_orddia["tipo_item"] = 'Mensagem'
dic_orddia["cod_sessao_plen"] = cod_sessao_plen
dic_orddia["nom_fase"] = 'Ordem do Dia'
dic_orddia["txt_exibicao"] = '<b>Ordem do Dia' + '</b><br />' + dic_sessao["txt_exibicao"]
dic_orddia["cod_materia"] = ''
dic_orddia["txt_autoria"] = ''
dic_orddia["txt_turno"] = ''
dic_orddia["ind_extrapauta"] = 0
dic_orddia["ind_exibicao"] = 0
itens.append(dic_orddia)

for ordem_dia in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=int(context.REQUEST['cod_sessao_plen']), ind_excluido=0):
    dic_ordem_dia = {}
    materia = context.zsql.materia_obter_zsql(cod_materia=ordem_dia.cod_materia)[0]
    dic_ordem_dia["tipo_item"] = 'Matéria'
    dic_ordem_dia["cod_sessao_plen"] = cod_sessao_plen
    dic_ordem_dia["nom_fase"] = 'Ordem do Dia'
    for turno in context.zsql.turno_discussao_obter_zsql(cod_turno=ordem_dia.tip_turno):
        dic_ordem_dia["txt_turno"] = turno.des_turno
        turno = turno.des_turno
    for quorum in context.zsql.quorum_votacao_obter_zsql(cod_quorum=ordem_dia.tip_quorum):
        dic_ordem_dia["txt_quorum"] = quorum.des_quorum
        quorum = quorum.des_quorum
    dic_ordem_dia["txt_exibicao"] =  materia.sgl_tipo_materia.decode('utf-8').upper()+' Nº '+str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ str(materia.txt_ementa) + ' Turno: ' + str(turno) + ' | Quórum: ' +str(quorum)
    dic_ordem_dia["cod_materia"] = ordem_dia.cod_materia
    dic_ordem_dia["txt_autoria"] = ''
    autores = context.zsql.autoria_obter_zsql(cod_materia=ordem_dia.cod_materia)
    fields = autores.data_dictionary().keys()
    lista_autor = []
    for autor in autores:
        for field in fields:
            nome_autor = autor['nom_autor_join']
        lista_autor.append(nome_autor)
    dic_ordem_dia["txt_autoria"] = ', '.join(['%s' % (value) for (value) in lista_autor])
    dic_ordem_dia["ind_extrapauta"] = 0
    dic_ordem_dia["ind_exibicao"] = 0
    itens.append(dic_ordem_dia)

#dic_exp_pessoais = {}
#dic_exp_pessoais["tipo_item"] = 'Mensagem'
#dic_exp_pessoais["nom_fase"] = 'Explicações Pessoais'
#dic_exp_pessoais["txt_exibicao"] = '<b>Explicações Pessoais' + '</b><br />' + dic_sessao["txt_exibicao"]
#dic_exp_pessoais["cod_materia"] = ''
#dic_exp_pessoais["txt_autoria"] = ''
#dic_exp_pessoais["txt_turno"] = ''
#dic_exp_pessoais["txt_quorum"] = ''
#dic_exp_pessoais["ind_extrapauta"] = 0
#dic_exp_pessoais["ind_exibicao"] = 0
#itens.append(dic_exp_pessoais)

itens = [(i + 1, j) for i, j in enumerate(itens)]

for i, dic in itens:
  context.zsql.sessao_plenaria_painel_incluir_zsql(tip_item=dic.get('tipo_item',dic), cod_sessao_plen=dic.get('cod_sessao_plen',dic), nom_fase=dic.get('nom_fase',dic), num_ordem=i, txt_exibicao=dic.get('txt_exibicao',dic), cod_materia=dic.get('cod_materia',dic), txt_autoria=dic.get('txt_autoria',dic), txt_turno=dic.get('txt_turno',dic), ind_extrapauta=dic.get('ind_extrapauta',dic), ind_exibicao=dic.get('ind_exibicao',dic))
#   return  i, dic.get('tipo_item',dic), dic.get('nom_fase',dic), dic.get('txt_exibicao',dic), dic.get('cod_materia',dic), dic.get('txt_autoria',dic), dic.get('txt_turno',dic), dic.get('ind_extrapauta',dic), dic.get('ind_exibicao',dic)

