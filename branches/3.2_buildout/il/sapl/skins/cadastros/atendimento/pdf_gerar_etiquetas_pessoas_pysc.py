## Script (Python) "pdf_gerar_etiquetas_pessoas_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= cod_funcionario_corrente, txt_dat_visita, txt_dat_visita2, lst_mes_aniversario, rad_sex_pessoa, txt_des_estado_civil, rad_filhos, txt_des_profissao, txt_des_local_trabalho, txt_end_residencial, txt_nom_bairro, txt_num_cep, txt_nom_cidade
##title=
##

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

results =  context.zsql.pessoa_pesquisar_zsql(
                                               cod_funcionario=REQUEST['cod_funcionario_corrente'],
                                               dat_visita=REQUEST['txt_dat_visita'],
                                               dat_visita2=REQUEST['txt_dat_visita2'],
                                               mes_aniversario=REQUEST['lst_mes_aniversario'],
                                               sex_pessoa=REQUEST['rad_sex_pessoa'],
                                               des_estado_civil=REQUEST['txt_des_estado_civil'],
                                               rad_filhos=REQUEST['rad_filhos'],
                                               des_profissao=REQUEST['txt_des_profissao'],
                                               des_local_trabalho=REQUEST['txt_des_local_trabalho'],
                                               end_residencial=REQUEST['txt_end_residencial'],
                                               nom_bairro=REQUEST['txt_nom_bairro'],
                                               num_cep=REQUEST['txt_num_cep'],
                                               nom_cidade=REQUEST['txt_nom_cidade']
                                               )
dados = []
for row in results:
    r=[]
    # Label, Data
    if row[1]!=None:
     r.append(row[1].encode( "utf-8" ))
    if row[10]!=None:
     r.append(row[10].encode( "utf-8" )+', '+row[11].encode( "utf-8" )+' '+row[12].encode( "utf-8" ))
    if row[13]!=None:
     r.append(row[13].encode( "utf-8" )+' - CEP  '+row[14].encode( "utf-8" ))
    if row[15]!=None:
     r.append(row[15].encode( "utf-8" )+' - '+row[16].encode( "utf-8" ))
    dados.append(r)
return context.pdflabels(dados)

