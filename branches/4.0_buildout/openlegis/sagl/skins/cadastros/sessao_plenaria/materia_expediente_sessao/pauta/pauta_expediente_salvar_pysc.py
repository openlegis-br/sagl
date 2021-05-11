## Script (Python) "pauta_expediente_salvar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=txt_cod_materia, cod_sessao_plen, txt_dat_ordem, lst_tip_quorum, rad_tip_votacao
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

v=str(txt_cod_materia)
if v.isdigit():
   cod_materia = [txt_cod_materia]
else:
   cod_materia = txt_cod_materia

cod_materia = [
   e
   for i, e in enumerate(cod_materia)
   if cod_materia.index(e) == i
]

lst_materias=[]
for item in cod_materia:
    dic_materias = {}
    for materia in context.zsql.materia_obter_zsql(cod_materia = item, ind_excluido=0):
        dic_materias['cod_materia'] = materia.cod_materia
        dic_materias['txt_observacao'] = materia.txt_ementa.encode('utf-8') 
        lst_materias.append(dic_materias)

lst_materias = [(i + 1, j) for i, j in enumerate(lst_materias)]
      
for i, dic in lst_materias:
    context.zsql.expediente_materia_incluir_zsql(cod_sessao_plen=cod_sessao_plen, cod_materia=dic.get('cod_materia',dic), dat_ordem=txt_dat_ordem, txt_observacao=dic.get('txt_observacao',dic), num_ordem=i, tip_quorum=lst_tip_quorum, tip_votacao=rad_tip_votacao)

mensagem = 'Pauta de matérias do expediente gerada com sucesso!'
mensagem_obs = ''   
redirect_url=context.portal_url()+'/mensagem_emitir?modal=1&tipo_mensagem=success&mensagem=' + mensagem + '&mensagem_obs=' + mensagem_obs
RESPONSE.redirect(redirect_url)

