## Script (Python) "pareceres"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=listar, cod_comissao, ano_parecer=""
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

pareceres = []
anos = []

if listar == 'pareceres':
   for relatoria in context.zsql.relatoria_obter_zsql(cod_comissao=cod_comissao, ano_parecer=ano_parecer):
       dic_parecer = {}
       for parlamentar in context.zsql.parlamentar_obter_zsql(cod_parlamentar=relatoria.cod_parlamentar):
           dic_parecer['relator'] = parlamentar.nom_parlamentar
       dic_parecer['dat_desig_relator'] = relatoria.dat_desig_relator
       dic_parecer['dat_parecer'] = relatoria.dat_destit_relator
       dic_parecer['num_parecer'] = relatoria.num_parecer
       dic_parecer['ano_parecer'] = relatoria.ano_parecer
       dic_parecer['cod_relatoria'] = int(relatoria.cod_relatoria)
       dic_parecer['tip_conclusao'] = relatoria.tip_conclusao
       for materia in context.zsql.materia_obter_zsql(cod_materia=relatoria.cod_materia,ind_excluido=0):
           dic_parecer['cod_materia'] = int(materia.cod_materia)
           dic_parecer['tipo_materia'] = materia.des_tipo_materia
           dic_parecer['numero_materia'] = materia.num_ident_basica
           dic_parecer['ano_materia'] = materia.ano_ident_basica
           dic_parecer['ementa_materia'] = materia.txt_ementa
           for autoria in context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia):
               dic_parecer['autoria_materia'] = autoria.nom_autor_join
       pareceres.append(dic_parecer)

   return pareceres

if listar == 'anos':
   for relatoria in context.zsql.relatoria_obter_zsql(cod_comissao=cod_comissao, ind_excluido=0):
      if relatoria.ano_parecer != None and relatoria.ano_parecer != '':
         anos.append(relatoria.ano_parecer)
      
   anos = [
      e
      for i, e in enumerate(anos)
      if anos.index(e) == i
   ]
 
   anos.sort(reverse=True)
 
   return anos

