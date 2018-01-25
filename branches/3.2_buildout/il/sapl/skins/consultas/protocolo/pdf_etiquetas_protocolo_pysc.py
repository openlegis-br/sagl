## Script (Python) "pdf_etiquetas_protocolo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= rad_tip_protocolo, txt_num_protocolo, txt_ano_protocolo, lst_tip_documento, rad_tip_processo, lst_tip_materia, txt_assunto, hdn_cod_autor, txa_txt_interessado, dt_apres, dt_apres2
##title=
##

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
session = REQUEST.SESSION

protocolos=[]
for protocolo in context.zsql.protocolo_pesquisar_zsql(tip_protocolo=REQUEST['rad_tip_protocolo'], 
                              num_protocolo=REQUEST['txt_num_protocolo'], ano_protocolo=REQUEST['txt_ano_protocolo'],
                              tip_documento=REQUEST['lst_tip_documento'], tip_processo=REQUEST['rad_tip_processo'], 
                              tip_materia=REQUEST['lst_tip_materia'], des_assunto=REQUEST['txt_assunto'], 
                              cod_autor=REQUEST['hdn_cod_autor'], des_interessado=REQUEST['txa_txt_interessado'], 
                              dat_apres=REQUEST['dt_apres'], dat_apres2=REQUEST['dt_apres2']):
        dic={}
        dic['codigo']=str(protocolo.cod_protocolo)
        dic['titulo']=str(protocolo.num_protocolo)
        dic['ano']=str(protocolo.ano_protocolo)
        dic['ano']=str(protocolo.ano_protocolo)
        dic['data']='Data: '+context.pysc.iso_to_port_pysc(protocolo.dat_protocolo)+' - Horário: '+protocolo.hor_protocolo[0:2]+':'+protocolo.hor_protocolo[3:5]
        dic['txt_assunto']=protocolo.txt_assunto_ementa
        dic['txt_interessado']=protocolo.txt_interessado
        dic['nom_autor'] = " " 
        if protocolo.cod_autor!=None:
           for autor in context.zsql.autor_obter_zsql(cod_autor=protocolo.cod_autor):
                if autor.des_tipo_autor=='Parlamentar':
                    for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar):
                        dic['nom_autor']=parlamentar.nom_parlamentar
                elif autor.des_tipo_autor=='Comissao':
                    for comissao in context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao):
                        dic['nom_autor']=comissao.nom_comissao
                elif autor.des_tipo_autor=='Bancada':
                    for bancada in context.zsql.bancada_obter_zsql(cod_bancada=autor.cod_bancada):
                        dic['nom_autor']=bancada.nom_bancada
                else:
                    dic['nom_autor']=autor.nom_autor
        else:
            dic['nom_autor']=protocolo.txt_interessado

        dic['tipo_autor'] = " "
        if protocolo.tip_processo==0:
           dic['tipo_autor']='Interessado'
        elif protocolo.tip_processo==1:
           dic['tipo_autor']='Autor'

        if protocolo.tip_processo==0:
           dic['tipo_enunciado']='Assunto'
        elif protocolo.tip_processo==1:
           dic['tipo_enunciado']='Ementa'

        if protocolo.tip_processo==0:
           dic['natureza']='Administrativo'
        elif protocolo.tip_processo==1:
           dic['natureza']='Legislativo'

        if protocolo.tip_processo==0:
           dic['ident_processo']=protocolo.des_tipo_documento
        elif protocolo.tip_processo==1:
           dic['ident_processo']=protocolo.des_tipo_materia

        dic['sgl_processo']=protocolo.des_tipo_materia or protocolo.des_tipo_documento

        dic['num_materia']=''
        for materia in context.zsql.materia_obter_zsql(num_protocolo=protocolo.num_protocolo,ano_ident_basica=protocolo.ano_protocolo):
               dic['num_materia']=str(materia.num_ident_basica)+'/'+ str(materia.ano_ident_basica)

        dic['num_documento']=''
        for documento in context.zsql.documento_administrativo_obter_zsql(num_protocolo=protocolo.num_protocolo,ano_documento=protocolo.ano_protocolo):
               dic['num_documento']=str(documento.num_documento)+'/'+ str(documento.ano_documento)

        dic['num_processo']=dic['num_materia'] or dic['num_documento']

        dic['anulado']=''
        if protocolo.ind_anulado==1:
           dic['anulado']='Nulo'
        protocolos.append(dic)

dados = []
for dic in protocolos:
    r=[]
    # Label, Data
    r.append('Protocolo nº '+dic['titulo']+'/'+dic['ano']+ ' - '+dic['sgl_processo'].upper() +' ' + dic['num_processo'] )
    r.append( dic['tipo_autor']+': ' + dic['nom_autor'])
    r.append( dic['tipo_enunciado']+': '+dic['txt_assunto'])
    dados.append(r)
return context.pdflabels(dados)

