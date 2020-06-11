## Script (Python) "exportar_eleitores_ods_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= cod_parlamentar_corrente, txt_nom_eleitor, txt_dat_atendimento, txt_dat_atendimento2, txt_dia_aniversario, lst_mes_aniversario, rad_sex_eleitor, txt_des_estado_civil, rad_filhos, txt_des_profissao, txt_des_local_trabalho, txt_end_residencial, txt_nom_bairro, txt_num_cep, txt_nom_localidade, lst_txt_classe
##title=
##

REQUEST  = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session  = REQUEST.SESSION

from Products.CMFCore.utils import getToolByName

eleitores = []
for item in context.zsql.gabinete_eleitor_pesquisar_zsql(
                                               cod_parlamentar=REQUEST['cod_parlamentar_corrente'],
                                               dat_atendimento=REQUEST['txt_dat_atendimento'],
                                               dat_atendimento2=REQUEST['txt_dat_atendimento2'],
                                               dia_aniversario=REQUEST['txt_dia_aniversario'],
                                               dia_aniversario2=REQUEST['txt_dia_aniversario2'],
                                               mes_aniversario=REQUEST['lst_mes_aniversario'],
                                               sex_eleitor=REQUEST['rad_sex_eleitor'],
                                               des_estado_civil=REQUEST['txt_des_estado_civil'],
                                               rad_filhos=REQUEST['rad_filhos'],
                                               des_profissao=REQUEST['txt_des_profissao'],
                                               des_local_trabalho=REQUEST['txt_des_local_trabalho'],
                                               end_residencial=REQUEST['txt_end_residencial'],
                                               nom_bairro=REQUEST['txt_nom_bairro'],
                                               num_cep=REQUEST['txt_num_cep'],
                                               nom_localidade=REQUEST['txt_nom_localidade'],
                                               txt_classe=REQUEST['lst_txt_classe']
                                               ):

    eleitor = {}
    eleitor['nom_eleitor'] = item.nom_eleitor
    eleitor['doc_identidade'] = item.doc_identidade
    eleitor['num_tit_eleitor'] = item.num_tit_eleitor
    eleitor['dat_nascimento'] = item.dat_nascimento
    eleitor['sex_eleitor'] = item.sex_eleitor
    eleitor['des_estado_civil'] = item.des_estado_civil
    eleitor['nom_conjuge'] = item.nom_conjuge
    eleitor['end_residencial'] = item.end_residencial
    eleitor['nom_bairro'] = item.nom_bairro
    eleitor['num_cep'] = item.num_cep
    eleitor['nom_localidade'] = item.nom_localidade
    eleitor['sgl_uf'] = item.sgl_uf
    eleitor['num_telefone'] = item.num_telefone
    eleitor['num_celular'] = item.num_celular
    eleitor['end_email'] = item.end_email
    eleitor['des_profissao'] = item.des_profissao
    eleitor['des_local_trabalho'] = item.des_local_trabalho
    eleitor['txt_observacao'] = item.txt_observacao
    eleitores.append(eleitor)

st = getToolByName(context, 'portal_sapl')
return st.eleitores_exportar(eleitores)

