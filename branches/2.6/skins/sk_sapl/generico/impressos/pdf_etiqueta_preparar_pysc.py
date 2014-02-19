import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

#Verifica o tamanho da lista das materias selecionadas vindas do form
REQUEST=context.REQUEST

materias=[]
REQUEST=context.REQUEST
for materia in context.zsql.materia_pesquisar_impresso_zsql(npc_inicial=REQUEST.txt_npc_inicial,npc_final=REQUEST.txt_npc_final):
        dic={}
        dic['processo']=materia.num_materia
	dic['tipo_materia']=materia.sgl_tipo_materia
        dic['materia']=str(materia.num_ident_basica) + "/" + str(materia.ano_ident_basica)
        dic['num_externa']=materia.num_origem_externa
        dic['dat_apresentacao']=materia.dat_apresentacao
        dic['txt_ementa']=materia.txt_ementa

        dic['nom_autor'] = " " 
        for autoria in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia, ind_primeiro_autor=1):
            for autor in context.zsql.autor_obter_zsql(cod_autor=autoria.cod_autor):
                if autor.des_tipo_autor=='Parlamentar':
                    for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=autor.cod_parlamentar):
                        dic['nom_autor']=parlamentar.nom_completo
                elif autor.des_tipo_autor=='Comissao':
                    for comissao in context.zsql.comissao_obter_zsql(cod_comissao=autor.cod_comissao):
                        dic['nom_autor']=comissao.nom_comissao
                else:
                    dic['nom_autor']=autor.nom_autor
            
        materias.append(dic)

sessao=session.id
caminho = context.pdf_etiqueta_gerar(sessao,materias)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)
