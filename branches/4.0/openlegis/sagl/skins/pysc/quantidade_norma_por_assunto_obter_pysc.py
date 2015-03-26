## Script (Python) "quantidade_norma_por_assunto_obter_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_assunto=0
##title=
##
cod=cod_assunto
cont=0
assuntos=context.zsql.norma_juridica_quantidade_assunto_obter_zsql()
for reg in assuntos:
       cod_assuntolst=reg.cod_assunto.split(',')
       for i in cod_assuntolst:
           if i==str(cod):
              cont=cont+int(reg.qtd)
           else:
              pass
return str(cont)  # retorna dicionário contendo as chaves dos assuntos e respectivas quantidades de normas jurídicas relacionadas 
