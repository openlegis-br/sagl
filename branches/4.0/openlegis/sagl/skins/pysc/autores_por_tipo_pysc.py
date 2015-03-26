## Script (Python) "autores_por_tipo_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=tip_autor="1", txt_dat_apresentacao, ind_excluido=0
##title=
##
"""
  Função: verificar se há parlamentar ou comissao disponíveis para terem o papel de autor
  
  Argumentos: tip_autor, cod_comissao, cod_materia e txt_dat_apresentacao  --> retorna 1-verdadeiro ou 0-falso.

""" 
ta=int(tip_autor) 
if ta == 1:           # --- verifica se parlamentares podem ser autores
   lista_parlamentar=context.zsql.parlamentar_obter_zsql(ind_excluido=0)
   parlamentares=[]

   for par in lista_parlamentar:
       codigo = str(par.cod_parlamentar)
       autores = context.zsql.autores_obter_zsql(txt_dat_apresentacao=txt_dat_apresentacao)
       for p in autores:
           s = str(p.cod_parlamentar)
           if s == codigo:
              parlamentares.append(codigo)  # parlamentares que podem ser autores ...
   return parlamentares     
else:
  if  ta == 2:      # --- verifica se comissões podem ser autores
      lista_comissao=context.zsql.comissao_obter_zsql(ind_excluido=0)
      comissoes=[]
      for comissao in lista_comissao:
          codigo = str(comissao.cod_comissao)
          autores = context.zsql_autores_comissao_obter_zsql(txt_dat_apresentacao=txt_dat_apresentacao)
          for c in autores:
              s = str(c.cod_comissao)
              if s == codigo:
                 comissoes.append(codigo)  # comiss�es que podem ser autoras
      return comissoes
   
           



