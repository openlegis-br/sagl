## Script (Python) "exportar_normas_ods_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tipo_norma, txt_numero, txt_ano, txt_assunto, lst_assunto_norma, lst_tip_situacao_norma, dt_norma, dt_norma2, dt_public, dt_public2, rd_ordenacao
##title=
##
REQUEST  = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session  = REQUEST.SESSION

from Products.CMFCore.utils import getToolByName

normas = []
for item in context.zsql.norma_juridica_obter_zsql(
                                               tip_norma=REQUEST['tipo_norma'],
                                               num_norma=REQUEST['txt_numero'],
                                               ano_norma=REQUEST['txt_ano'],
                                               des_assunto=REQUEST['txt_assunto'],
                                               cod_assunto=REQUEST['lst_assunto_norma'],
                                               cod_situacao=REQUEST['lst_tip_situacao_norma'],
                                               dat_norma=REQUEST['dt_norma'],
                                               dat_norma2=REQUEST['dt_norma2'],
                                               dat_publicacao=REQUEST['dt_public'],
                                               dat_publicacao2=REQUEST['dt_public2'],
                                               rd_ordem=REQUEST['rd_ordenacao']
                                               ):

    norma = {}
    norma['tipo_norma'] = item.des_tipo_norma
    norma['numero_norma'] = item.num_norma
    norma['ano_norma'] = item.ano_norma
    norma['ementa_norma'] = item.txt_ementa
    norma['data_norma'] = item.dat_norma
    norma['des_status']= ""
    if item.cod_situacao!=None:
       for situacao_norma in context.zsql.tipo_situacao_norma_obter_zsql(ind_excluido=0, tip_situacao_norma=item.cod_situacao):
           norma['des_status']= situacao_norma.des_tipo_situacao

    normas.append(norma)

st = getToolByName(context, 'portal_sapl')
return st.normas_exportar(normas)
