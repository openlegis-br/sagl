## Script (Python) "pesquisa_textual_pysc"

##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=lst_tipo,txt_texto, norma_or_materia
##title=
##

#ATENCAO: Parametro norma_or_materia: 1-materia legislativa, 2-norma juridica


'''Este script realiza a busca textual de materias legislativas e normas juridicas'''


lista_result = []

#Verifica se a palavra informada para pesquisa possui somente espacos
if txt_texto.isspace() == False:

	lista_catalog = []
	lista_DB = []
	
	#Teste para saber se pesquisara norma ou materia
	if norma_or_materia == 1:

		#Chama o Catalog do Zope para realizar a busca textual no ZODB
		lista_catalog = context.sapl.sapl_documentos.materia.Catalog(PrincipiaSearchSource=txt_texto)

		#Utiliza este script para realizar a busca no DB de todos os registros do tipo de materia
		lista_DB = context.zsql.materia_obter_zsql(tip_id_basica=lst_tipo)
	
	else:
		#Chama o Catalog do Zope para realizar a busca textual no ZODB
		lista_catalog = context.sapl.sapl_documentos.norma_juridica.Catalog(PrincipiaSearchSource=txt_texto)

		#Utiliza este script para realizar a busca no DB de todos os registros do tipo de materia
		lista_DB = context.zsql.norma_juridica_obter_zsql(tip_norma=lst_tipo)

	#Verifica se lista_catalog e lista_DB estao vazia
	if ((lista_catalog != None) and (lista_DB != None)):

		#Percorre a lista obtida do Banco de Dados
		for elem_DB in lista_DB:

			#Percorre a lista obtida do zcatalog
			for elem_catalog in lista_catalog:

                #cria o id para comparar com os registros obtidos do zcatalog
				id_pesq = str(elem_DB[0]) + '_texto_integral' 
				
				#Verifica se existe o registro com o id obtido do zcatalog
				if id_pesq == elem_catalog.id:
					lista_result.append(elem_DB)


return lista_result
