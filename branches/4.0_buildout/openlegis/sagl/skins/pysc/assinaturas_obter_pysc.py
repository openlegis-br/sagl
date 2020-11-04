## Script (Python) "assinaturas_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=codigo_origem, tipo_doc_origem, codigo_destino, tipo_doc_destino
##title=
##

itens = []

for item in context.zsql.assinatura_documento_obter_zsql(codigo=codigo_origem,tipo_doc=tipo_doc_origem,ind_assinado=1):
    dic_assinaturas = {}
    dic_assinaturas["cod_assinatura_doc"] = item.cod_assinatura_doc
    dic_assinaturas["codigo"] = codigo_destino
    dic_assinaturas["tipo_doc"] = tipo_doc_destino
    dic_assinaturas["dat_solicitacao"] = item.data_solicitacao
    dic_assinaturas["cod_usuario"] = item.cod_usuario
    dic_assinaturas["dat_assinatura"] = item.data_assinatura
    dic_assinaturas["ind_assinado"] = item.ind_assinado
    dic_assinaturas["ind_prim_assinatura"] = item.ind_prim_assinatura
    itens.append(dic_assinaturas)

itens = [(i + 1, j) for i, j in enumerate(itens)]

for i, dic in itens:
    context.zsql.assinatura_documento_copiar_zsql(cod_assinatura_doc=dic.get('cod_assinatura_doc',dic), codigo=dic.get('codigo',dic), tipo_doc=dic.get('tipo_doc',dic), dat_solicitacao=dic.get('dat_solicitacao',dic),cod_usuario=dic.get('cod_usuario',dic),dat_assinatura=dic.get('dat_assinatura',dic),ind_assinado=dic.get('ind_assinado',dic),ind_prim_assinatura=dic.get('ind_prim_assinatura',dic))

