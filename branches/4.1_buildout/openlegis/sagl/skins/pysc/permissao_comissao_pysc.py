## encoding: utf-8 
## Script (Python) "permissao_comissao_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cod_comissao
##title=
##

request=context.REQUEST

# obtém o presidente atual da comissao
presidente = ''
cod_parlamentar_presidente = ''
for periodo in context.zsql.periodo_comp_comissao_obter_zsql(data=DateTime().strftime("%Y/%m/%d"), ind_excluido=0):
    for cargo in context.zsql.composicao_comissao_obter_zsql(cod_comissao=cod_comissao, cod_periodo_comp=periodo.cod_periodo_comp, cod_cargo=1, ind_excluido=0):
        presidente = cargo.nom_completo.decode('utf-8').upper()
        cod_parlamentar_presidente = cargo.cod_parlamentar

temPermissao = 0

if request['AUTHENTICATED_USER'].has_role(['Autor']):
   # verifica se o presidente eh o usuario logado
   for autor in context.zsql.autor_obter_zsql(col_username=request['AUTHENTICATED_USER'].getUserName(), ind_excluido=0):
       if int(autor.cod_parlamentar) == int(cod_parlamentar_presidente):
          temPermissao = 1
       else:
          temPermissao = 0
elif request['AUTHENTICATED_USER'].has_role(['Assessor Parlamentar']):
    # verifica se o usuario logado eh assessor
    for assessor in context.zsql.assessor_parlamentar_obter_zsql(col_username=request['AUTHENTICATED_USER'].getUserName()):
        # verifica se o assessor esta vinculado ao presidente da comissao
        if int(assessor.cod_parlamentar) == int(cod_parlamentar_presidente):
           temPermissao = 1
        else:
           temPermissao = 0
elif request['AUTHENTICATED_USER'].has_role(['Operador', 'Operador Comissao']):
   temPermissao = 1
else:
   temPermissao = 0
           
return str(temPermissao)
