## Script (Python) "exportar_contatos_ods_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= cod_funcionario_corrente, txt_dat_visita, txt_dat_visita2, lst_mes_aniversario, rad_sex_pessoa, txt_des_estado_civil, rad_filhos, txt_des_profissao, txt_des_local_trabalho, txt_end_residencial, txt_nom_bairro, txt_num_cep, txt_nom_cidade
##title=
##

REQUEST  = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session  = REQUEST.SESSION

from Products.CMFCore.utils import getToolByName

pessoas = []
for item in context.zsql.pessoa_pesquisar_zsql(cod_funcionario=REQUEST['cod_funcionario_corrente'], dat_visita=REQUEST['txt_dat_visita'], dat_visita2=REQUEST['txt_dat_visita2'], mes_aniversario=REQUEST['lst_mes_aniversario'], sex_pessoa=REQUEST['rad_sex_pessoa'], des_estado_civil=REQUEST['txt_des_estado_civil'], rad_filhos=REQUEST['rad_filhos'], des_profissao=REQUEST['txt_des_profissao'], des_local_trabalho=REQUEST['txt_des_local_trabalho'], end_residencial=REQUEST['txt_end_residencial'], nom_bairro=REQUEST['txt_nom_bairro'], num_cep=REQUEST['txt_num_cep'], nom_cidade=REQUEST['txt_nom_cidade']):
    pessoa = {}
    pessoa['nom_pessoa'] = item.nom_pessoa
    pessoa['doc_identidade'] = item.doc_identidade
    pessoa['num_tit_eleitor'] = item.num_tit_eleitor
    pessoa['dat_nascimento'] = item.dat_nascimento
    pessoa['sex_pessoa'] = item.sex_pessoa
    pessoa['des_estado_civil'] = item.des_estado_civil
    pessoa['nom_conjuge'] = item.nom_conjuge
    pessoa['num_dependentes'] = item.num_dependentes
    pessoa['end_residencial'] = item.end_residencial
    pessoa['num_imovel'] = item.num_imovel
    pessoa['txt_complemento'] = item.txt_complemento
    pessoa['nom_bairro'] = item.nom_bairro
    pessoa['num_cep'] = item.num_cep
    pessoa['nom_cidade'] = item.nom_cidade
    pessoa['sgl_uf'] = item.sgl_uf
    pessoa['des_tempo_residencia'] = item.des_tempo_residencia
    pessoa['num_telefone'] = item.num_telefone
    pessoa['num_celular'] = item.num_celular
    pessoa['end_email'] = item.end_email
    pessoa['des_profissao'] = item.des_profissao
    pessoa['des_local_trabalho'] = item.des_local_trabalho
    pessoa['txt_observacao'] = item.txt_observacao
    pessoas.append(pessoa)

st = getToolByName(context, 'portal_sapl')
return st.pessoas_exportar(pessoas)

