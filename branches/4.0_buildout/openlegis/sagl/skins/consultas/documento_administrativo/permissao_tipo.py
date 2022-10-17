## Script (Python) "permissao_tipo"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request=context.REQUEST

response=request.RESPONSE

if request['AUTHENTICATED_USER'].has_role(['Authenticated']):
   for usuario in context.zsql.usuario_obter_zsql(col_username=request['AUTHENTICATED_USER'].getUserName()):
       if usuario.cod_usuario:
          cod_usuario_corrente = int(usuario.cod_usuario)
       else:
          cod_usuario_corrente = 0

lst_tipo=[]

for tipo in context.zsql.tipo_documento_administrativo_obter_zsql(ind_escluido=0):
    if request['AUTHENTICATED_USER'].has_role(['Manager', 'Operador', 'Operador Modulo Administrativo', 'Consulta Modulo Administrativo']):
       dic_tipo= {}
       dic_tipo['tip_documento']= tipo.tip_documento
       dic_tipo['sgl_tipo_documento']= tipo.sgl_tipo_documento
       dic_tipo['des_tipo_documento']= tipo.des_tipo_documento
       dic_tipo['ind_publico']= tipo.ind_publico 
       dic_tipo['ind_incluir']= 1 
       lst_tipo.append(dic_tipo)
    elif request['AUTHENTICATED_USER'].has_role([ 'Operador Materia']):
       if str(tipo.ind_publico) == '1':
          dic_tipo= {}
          dic_tipo['tip_documento']= tipo.tip_documento
          dic_tipo['sgl_tipo_documento']= tipo.sgl_tipo_documento
          dic_tipo['des_tipo_documento']= tipo.des_tipo_documento 
          dic_tipo['ind_publico']= tipo.ind_publico 
          dic_tipo['ind_incluir']= 1 
          lst_tipo.append(dic_tipo) 
    elif request['AUTHENTICATED_USER'].has_role(['Authenticated']):
       if str(tipo.ind_publico) == '1' or context.zsql.usuario_tipo_documento_obter_zsql(tip_documento=tipo.tip_documento, cod_usuario=cod_usuario_corrente, ind_excluido=0):
          dic_tipo= {}
          dic_tipo['tip_documento']= tipo.tip_documento
          dic_tipo['sgl_tipo_documento']= tipo.sgl_tipo_documento
          dic_tipo['des_tipo_documento']= tipo.des_tipo_documento 
          dic_tipo['ind_publico']= tipo.ind_publico
          dic_tipo['ind_incluir']= 0 
          if context.zsql.usuario_tipo_documento_obter_zsql(tip_documento=tipo.tip_documento, cod_usuario=cod_usuario_corrente, ind_excluido=0):
             dic_tipo['ind_incluir']= 1 
          lst_tipo.append(dic_tipo) 
    elif tipo.ind_publico == 1:
       dic_tipo= {}
       dic_tipo['tip_documento']= tipo.tip_documento
       dic_tipo['sgl_tipo_documento']= tipo.sgl_tipo_documento
       dic_tipo['des_tipo_documento']= tipo.des_tipo_documento 
       dic_tipo['ind_publico']= tipo.ind_publico 
       lst_tipo.append(dic_tipo)  

lst_tipo = [
    e
    for i, e in enumerate(lst_tipo)
    if lst_tipo.index(e) == i
    ]

return lst_tipo



