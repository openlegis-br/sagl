## Script (Python) "ementa_carregar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= lst_tip_proposicao, lst_tip_id_basica, txt_num_ident_basica, txt_ano_ident_basica
##title=
##
import simplejson as json

context.REQUEST.RESPONSE.setHeader("Access-Control-Allow-Origin", "*")

materiaArray = [] 
   
for materia in context.zsql.materia_obter_zsql(tip_id_basica = lst_tip_id_basica, num_ident_basica = txt_num_ident_basica, ano_ident_basica = txt_ano_ident_basica, ind_excluido = 0 ):
   dic = {}
   dic["nom_autor"] = ''
   autores = context.zsql.autoria_obter_zsql(cod_materia=materia.cod_materia)
   fields = autores.data_dictionary().keys()
   lista_autor = []
   for autor in autores:
       for field in fields:
           nome_autor = autor['nom_autor_join']
       lista_autor.append(nome_autor)
   autor = ', '.join(['%s' % (value) for (value) in lista_autor])

   if lst_tip_proposicao == 'Parecer' and lst_tip_proposicao == 'Parecer de Comissão' and lst_tip_proposicao == 'Parecer Jurídico':
      dic['ementa'] = str(lst_tip_proposicao) + ' sobre o ' + str(materia.des_tipo_materia) + ' nº ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica) + ' - ' + str(autor) + ' - ' + str(materia.txt_ementa)
   else:
      dic['ementa'] = str(lst_tip_proposicao) + ' ao ' + str(materia.des_tipo_materia) + ' nº ' + str(materia.num_ident_basica) + '/' + str(materia.ano_ident_basica) + ' - ' + str(autor) + ' - ' + str(materia.txt_ementa)
   materiaArray.append(dic)   

    
return json.dumps(materiaArray)
