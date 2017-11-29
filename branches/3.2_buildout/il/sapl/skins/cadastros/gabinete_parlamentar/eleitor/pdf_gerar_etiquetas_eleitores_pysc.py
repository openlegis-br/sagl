## Script (Python) "pdf_gerar_etiquetas_pessoas_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= cod_parlamentar_corrente, txt_nom_eleitor, txt_dat_atendimento, txt_dat_atendimento2, lst_mes_aniversario, rad_sex_eleitor, txt_des_estado_civil, rad_filhos, txt_des_profissao, txt_des_local_trabalho, txt_end_residencial, txt_nom_bairro, txt_num_cep, txt_nom_localidade, lst_txt_classe
##title=
##

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

results =  context.zsql.gabinete_eleitor_pesquisar_zsql(
                                               cod_parlamentar=REQUEST['cod_parlamentar_corrente'],
                                               nom_eleitor=REQUEST['txt_nom_eleitor'],
                                               dat_atendimento=REQUEST['txt_dat_atendimento'],
                                               dat_atendimento2=REQUEST['txt_dat_atendimento2'],
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
                                               )
dados = []
for row in results:
    r=[]
    # Label, Data
    if row[3]!=None:
     r.append(row[3])
    if row[13]!=None:
     r.append(row[13])
    if row[14]!=None:
     r.append(row[14])
    if row[15]!=None and row[16]!=None:
     r.append(' CEP '+row[15]+' '+row[16]+ ' ' + row[17])
    dados.append(r)
return context.pdflabels(dados)

