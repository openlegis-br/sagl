## Script (Python) "gerar_itens_painel"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen
##title=
##
REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

itens = []

cod_sessao_plen = int(context.REQUEST['cod_sessao_plen'])

for sessao in context.zsql.sessao_plenaria_obter_zsql(cod_sessao_plen=cod_sessao_plen, ind_excluido=0):
  tipo_sessao = context.zsql.tipo_sessao_plenaria_obter_zsql(tip_sessao=sessao.tip_sessao,ind_excluido=0)[0]
  dic_sessao = {}
  dic_sessao["tipo_item"] = 'Mensagem'
  dic_sessao["nom_fase"] = 'Abertura'
  dic_sessao["txt_exibicao"] = 'Sessão '+ tipo_sessao.nom_sessao + ' de ' + context.pysc.data_converter_por_extenso_pysc(data=sessao.dat_inicio_sessao)
  dic_sessao["cod_materia"] = ''
  dic_sessao["txt_autoria"] = ''
  dic_sessao["txt_turno"] = ''
  dic_sessao["ind_extrapauta"] = 0
  dic_sessao["ind_exibicao"] = 0
  itens.append(dic_sessao)

dic_correspondencias = {}
dic_correspondencias["tipo_item"] = 'Mensagem'
dic_correspondencias["nom_fase"] = 'Expediente'
dic_correspondencias["txt_exibicao"] = 'Leitura de correspondências e outros documentos despachados ao Expediente' + ' - ' + dic_sessao["txt_exibicao"]
dic_correspondencias["cod_materia"] = ''
dic_correspondencias["txt_autoria"] = ''
dic_correspondencias["txt_turno"] = ''
dic_correspondencias["ind_extrapauta"] = 0
dic_correspondencias["ind_exibicao"] = 0
itens.append(dic_correspondencias)

lst_indicacoes = [] 
for indicacoes in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=int(context.REQUEST['cod_sessao_plen']),ind_excluido=0):
  dic_indicacoes = {}
  for materia in context.zsql.materia_obter_zsql(cod_materia=indicacoes.cod_materia, des_tipo_materia='Indicação', ind_excluido=0):
    num_ident_basica = materia.num_ident_basica
    lst_indicacoes.append(num_ident_basica)
  dic_indicacoes["tipo_item"] = 'Mensagem'
  dic_indicacoes["nom_fase"] = 'Expediente'
  ano = DateTime().strftime('%Y')
  dic_indicacoes["txt_exibicao"] = 'Indicações de números '+str(min(lst_indicacoes))+'/'+ano+ ' a '+str(max(lst_indicacoes))+'/'+ano + ' - ' + dic_sessao["txt_exibicao"]
  dic_indicacoes["cod_materia"] = ''
  dic_indicacoes["txt_autoria"] = ''
  dic_indicacoes["txt_turno"] = ''
  dic_indicacoes["ind_extrapauta"] = 0
  dic_indicacoes["ind_exibicao"] = 0
  itens.append(dic_indicacoes)

for requerimentos in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
  dic_requerimentos = {}
  for materia in context.zsql.materia_obter_zsql(cod_materia=requerimentos.cod_materia, des_tipo_materia='Requerimento', ind_excluido=0):
    dic_requerimentos["tipo_item"] = 'Matéria'
    dic_requerimentos["nom_fase"] = 'Expediente'
    dic_requerimentos["txt_exibicao"] = materia.des_tipo_materia+' '+str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa
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

dic_peq_expediente = {}
dic_peq_expediente["tipo_item"] = 'Mensagem'
dic_peq_expediente["nom_fase"] = 'Expediente'
dic_peq_expediente["txt_exibicao"] = 'Pequeno Expediente' + ' - ' + dic_sessao["txt_exibicao"]
dic_peq_expediente["cod_materia"] = ''
dic_peq_expediente["txt_autoria"] = ''
dic_peq_expediente["txt_turno"] = ''
dic_peq_expediente["ind_extrapauta"] = 0
dic_peq_expediente["ind_exibicao"] = 0
itens.append(dic_peq_expediente)

for ordem_dia in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
  dic_ordem_dia = {}
  materia = context.zsql.materia_obter_zsql(cod_materia=ordem_dia.cod_materia)[0]
  turno = context.zsql.turno_discussao_obter_zsql(cod_turno=ordem_dia.tip_turno)[0]
  dic_ordem_dia["tipo_item"] = 'Matéria'
  dic_ordem_dia["nom_fase"] = 'Ordem do Dia'
  dic_ordem_dia["txt_exibicao"] =  materia.des_tipo_materia+' '+str(materia.num_ident_basica)+"/"+str(context.pysc.ano_abrevia_pysc(ano=str(materia.ano_ident_basica)))+" - "+ materia.txt_ementa
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
  dic_ordem_dia["txt_turno"] = turno.des_turno
  dic_ordem_dia["ind_extrapauta"] = 0
  dic_ordem_dia["ind_exibicao"] = 0
  itens.append(dic_ordem_dia)

dic_exp_pessoais = {}
dic_exp_pessoais["tipo_item"] = 'Mensagem'
dic_exp_pessoais["nom_fase"] = 'Explicações Pessoais'
dic_exp_pessoais["txt_exibicao"] = 'Explicações Pessoais' + ' - ' + dic_sessao["txt_exibicao"]
dic_exp_pessoais["cod_materia"] = ''
dic_exp_pessoais["txt_autoria"] = ''
dic_exp_pessoais["txt_turno"] = ''
dic_exp_pessoais["ind_extrapauta"] = 0
dic_exp_pessoais["ind_exibicao"] = 0
itens.append(dic_exp_pessoais)

itens = [(i + 1, j) for i, j in enumerate(itens)]

for i, dic in itens:
  context.zsql.sessao_plenaria_painel_incluir_zsql(tip_item=dic.get('tipo_item',dic), nom_fase=dic.get('nom_fase',dic), num_ordem=i, txt_exibicao=dic.get('txt_exibicao',dic), cod_materia=dic.get('cod_materia',dic), txt_autoria=dic.get('txt_autoria',dic), txt_turno=dic.get('txt_turno',dic), ind_extrapauta=dic.get('ind_extrapauta',dic), ind_exibicao=dic.get('ind_exibicao',dic))
#   return  i, dic.get('tipo_item',dic), dic.get('nom_fase',dic), dic.get('txt_exibicao',dic), dic.get('cod_materia',dic), dic.get('txt_autoria',dic), dic.get('txt_turno',dic), dic.get('ind_extrapauta',dic), dic.get('ind_exibicao',dic)
