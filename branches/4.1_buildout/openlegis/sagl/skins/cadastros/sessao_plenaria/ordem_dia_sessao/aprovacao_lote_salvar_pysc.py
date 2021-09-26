## Script (Python) "pauta_expediente_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen, dat_sessao, num_legislatura, cod_sessao_leg, tip_sessao
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

votadas=[]
nao_votadas=[]
anuladas = []

for item in context.zsql.ordem_dia_obter_zsql(cod_sessao_plen = cod_sessao_plen, ind_excluido=0):
    for materia in context.zsql.materia_obter_zsql(cod_materia=item.cod_materia, des_tipo_materia='Requerimento', ind_excluido=0):
       dic_materias = {}
       for votacao in context.zsql.votacao_ordem_dia_obter_zsql(cod_ordem=item.cod_ordem, cod_materia=item.cod_materia):
           votadas.append(int(item.cod_materia))
           if votacao.tip_resultado_votacao == 0:
              dic_materias['cod_materia'] = int(item.cod_materia)
              dic_materias['cod_ordem'] = int(item.cod_ordem)
              dic_materias['cod_votacao'] = int(votacao.cod_votacao)              
              anuladas.append(dic_materias)           
       if int(item.cod_materia) not in votadas:
          dic_materias['cod_materia'] = int(item.cod_materia)
          dic_materias['cod_ordem'] = int(item.cod_ordem)
          nao_votadas.append(dic_materias)

presentes = context.pysc.quantidade_presentes_ordem_dia_pysc(cod_sessao_plen=cod_sessao_plen, dat_ordem=dat_sessao)

if int(presentes) != 0:
   votos_sim = int(presentes) - 1
else:
   votos_sim = 0

for resultado in context.zsql.tipo_resultado_votacao_obter_zsql(nom_resultado='Aprovado'):
    lst_tip_resultado = resultado.tip_resultado_votacao
    nom_resultado = resultado.nom_resultado

for dic in nao_votadas:
    context.zsql.votacao_incluir_zsql(num_votos_sim=votos_sim, num_votos_nao='0', num_abstencao='0', cod_ordem=dic.get('cod_ordem',dic), cod_materia=dic.get('cod_materia',dic), tip_resultado_votacao=lst_tip_resultado)
    context.modelo_proposicao.requerimento_aprovar(cod_sessao_plen=cod_sessao_plen, nom_resultado=nom_resultado, cod_materia=dic.get('cod_materia',dic))
    
for dic in anuladas:
    context.zsql.votacao_atualizar_zsql(cod_votacao=dic.get('cod_votacao',dic), num_votos_sim=votos_sim, num_votos_nao='0', num_abstencao='0', cod_ordem=dic.get('cod_ordem',dic), cod_materia=dic.get('cod_materia',dic), tip_resultado_votacao=lst_tip_resultado)
    context.modelo_proposicao.requerimento_aprovar(cod_sessao_plen=cod_sessao_plen, nom_resultado=nom_resultado, cod_materia=dic.get('cod_materia',dic))

redirect_url = 'index_html?cod_sessao_plen=' + cod_sessao_plen + '&cod_sessao_leg=' + cod_sessao_leg + '&num_legislatura=' + num_legislatura + '&dat_sessao=' + dat_sessao + '&tip_sessao=' + tip_sessao

RESPONSE.redirect(redirect_url)
