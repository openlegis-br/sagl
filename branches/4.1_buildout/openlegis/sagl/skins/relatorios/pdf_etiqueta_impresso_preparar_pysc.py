import os

request=context.REQUEST
response=request.RESPONSE
session= request.SESSION

data=DateTime().strftime('%d/%m/%Y')

# PythonScript para pesquisar os destinatarios e gerar os dados

destinatarios=[]
REQUEST=context.REQUEST
for destinatario in context.zsql.destinatario_oficio_obter_zsql(cod_documento=REQUEST['cod_documento']):
        dic={}
        dic['codigo']=str(destinatario.cod_documento)
        dic['forma_tratamento']=str(destinatario.txt_forma_tratamento)
        dic['nome_responsavel']=destinatario.nom_responsavel
        dic['cargo']=destinatario.des_cargo
        dic['nome_instituicao']=destinatario.nom_instituicao
        dic['endereco']=destinatario.end_instituicao
        dic['bairro']=destinatario.nom_bairro
        dic['cep']=destinatario.num_cep
        dic['localidade']=''
        for localidade in context.zsql.localidade_obter_zsql(cod_localidade=destinatario.cod_localidade):
               dic['localidade']=localidade.nom_localidade_pesq+' '+localidade.sgl_uf
        destinatarios.append(dic)

#sessao=session.id
caminho = context.pdf_etiqueta_impresso_gerar_pysc(destinatarios)
if caminho=='aviso':
 return response.redirect('mensagem_emitir_proc')
else:
 response.redirect(caminho)

