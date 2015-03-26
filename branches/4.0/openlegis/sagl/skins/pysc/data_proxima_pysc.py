## Script (Python) "data_proxima"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lista_de_datas
##title=
##
"""
  Funcao: a partir de uma lista de strings representando datas,
          retornar a primeira data da lista que for maior ou igual a
          data de hoje. NÃ£o havendo, retorna a primeira data da lista

  Argumento: lista de datas.

  Retorno: a primeira data da lista_de_datas que for maior ou igual a
           data de hoje ou a primeira data da lista
"""


#---- retorna a data da Ãºltima sessÃ£o se esta for menor ou igual a data de hoje ---

data = context.zsql.ultima_sessao_plenaria_obter_zsql()[0].dat_inicio_sessao
hoje = DateTime(DateTime().Date())
if hoje >= data:
   tmp = str(data).split('/')
   tmp.reverse()
   return '/'.join(tmp)

# ---------------------------------------------------------------------------------
   
if not lista_de_datas:
    return None

# transforma ['DD/MM/YYYY', ] em [DateTime('YYYY/MM/DD'), ]
lista = []
for d in lista_de_datas:
    tmp = d.split('/')
    tmp.reverse()
    lista.append(DateTime('/'.join(tmp)))
lista.sort()

# retorna a proxima data maior ou igual a hoje
hoje = DateTime(DateTime().Date())
for d in lista:
    if d.greaterThanEqualTo(hoje):
        tmp = str(d).split('/')
        tmp.reverse()
        return '/'.join(tmp)

# retorna a primeira data caso nao encontre outra
return lista_de_datas[0]
