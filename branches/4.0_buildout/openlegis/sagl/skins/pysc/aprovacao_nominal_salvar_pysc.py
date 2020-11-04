## encoding: utf-8 
## Script (Python) "aprovacao_nominal_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_sessao_plen,cod_parlamentar,tip_resultado_votacao,txt_observacao="",vot_parlamentar=""
##title=
##

dic={}
votos_sim=[]
votos_nao=[]
votos_abstencao=[]

for voto in vot_parlamentar:
    if voto=='Sim':
        votos_sim.append(voto)

for voto in vot_parlamentar:
    if voto=='Nao':
        votos_nao.append(voto)

for voto in vot_parlamentar:
    if voto=='Abstencao':
        votos_abstencao.append(voto)

for n in range(len(cod_parlamentar)):
    dic = dict(zip(cod_parlamentar, vot_parlamentar))

lst_materias = []       
for materia in context.zsql.expediente_materia_obter_zsql(cod_sessao_plen=cod_sessao_plen,ind_excluido=0):
    dic_materias = {}
    if materia.tip_votacao == 2:
       dic_materias["cod_ordem"] = materia.cod_ordem
       dic_materias["cod_materia"] = materia.cod_materia
       lst_materias.append(dic_materias)

for materia in lst_materias:
    votacao=context.zsql.votacao_obter_zsql(cod_ordem=materia.get('cod_ordem',materia),cod_materia=materia.get('cod_materia',materia),ind_excluido=0)
    try:
        cod_votacao = votacao[0].cod_votacao
    except:
        cod_votacao = None
    if cod_votacao is None:
        context.zsql.votacao_incluir_zsql(num_votos_sim=len(votos_sim),num_votos_nao=len(votos_nao),num_abstencao=len(votos_abstencao),txt_observacao=txt_observacao,cod_ordem=materia.get('cod_ordem',materia),cod_materia=materia.get('cod_materia',materia), tip_resultado_votacao=tip_resultado_votacao)
    else:
        context.zsql.votacao_atualizar_zsql(cod_votacao=cod_votacao,num_votos_sim=len(votos_sim),num_votos_nao=len(votos_nao),num_abstencao=len(votos_abstencao),txt_observacao=txt_observacao,cod_ordem=materia.get('cod_ordem',materia),cod_materia=materia.get('cod_materia',materia),tip_resultado_votacao=tip_resultado_votacao)

    parlamentares=[]
    if cod_votacao is not None:
       votacao_parlamentares=context.zsql.votacao_parlamentar_obter_zsql(cod_votacao=cod_votacao,ind_excluido=0)
       for parlamentar in votacao_parlamentares:
           parlamentares.append(str(parlamentar.cod_parlamentar))
    else:
        votacao_incluida=context.zsql.votacao_incluida_obter_zsql()
        cod_votacao = votacao_incluida[0].cod_votacao

    for p in cod_parlamentar:
        if p not in parlamentares:
            context.zsql.votacao_parlamentar_incluir_zsql(cod_votacao=cod_votacao,cod_parlamentar=p,vot_parlamentar=dic.get(p))
        else:
            context.zsql.votacao_parlamentar_atualizar_zsql(cod_votacao=cod_votacao,cod_parlamentar=p,vot_parlamentar=dic.get(p),ind_excluido=0)

return 1
