## Script (Python) "recebimento_normas_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

lst_peticao = []
for peticao in context.zsql.peticao_obter_zsql(ind_norma=1, ind_enviado='1', ind_recebido='0', ind_excluido=0):
    cod_peticao = peticao.cod_peticao
    dic_peticao = {}
    dic_peticao['cod_peticao'] = peticao.cod_peticao
    dic_peticao['titulo'] = peticao.des_tipo_peticionamento + ' nº ' + str(peticao.num_norma) + '/' + str(peticao.ano_norma)
    dic_peticao['descricao'] = peticao.txt_descricao.encode('utf-8')
    dic_peticao['data'] = peticao.dat_envio
    for usuario in context.zsql.usuario_obter_zsql(cod_usuario=peticao.cod_usuario):
        dic_peticao['nom_usuario'] = usuario.nom_completo.encode('utf-8')
    storage_path = context.sapl_documentos.peticao
    nom_arquivo = str(peticao.cod_peticao)+'.pdf'
    for codigo in context.zsql.assinatura_documento_obter_zsql(tipo_doc='peticao', codigo=int(peticao.cod_peticao), ind_assinado='1'):
        if codigo.ind_assinado == 1:
           storage_path = context.sapl_documentos.documentos_assinados
           nom_arquivo = str(codigo.cod_assinatura_doc)+'.pdf'
        break
    arq = getattr(storage_path, nom_arquivo)
    url = arq.absolute_url()
    dic_peticao['link'] = url
    lst_peticao.append(dic_peticao)

return lst_peticao

