## Script (Python) "proposicoes_contar_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=caixa
##title=
##

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
session = REQUEST.SESSION

revisao = []
assinatura = []
protocolo = []
incorporado = []
devolvido = []
qtde = ''

if caixa == 'revisao' or caixa == 'assinatura' or caixa == 'protocolo':
   for proposicao in context.zsql.proposicao_obter_zsql(ind_excluido=0, ind_pendente=1, ind_devolvido=0):
       id_odt = str(proposicao.cod_proposicao) +'.odt'
       id_documento = str(proposicao.cod_proposicao) +'.pdf'
       id_documento_assinado = str(proposicao.cod_proposicao) +'_signed.pdf'

       if proposicao.dat_recebimento==None and hasattr(context.sapl_documentos.proposicao,id_odt) and not hasattr(context.sapl_documentos.proposicao,id_documento_assinado):
          revisao.append(proposicao.cod_proposicao)

       if proposicao.dat_recebimento==None and hasattr(context.sapl_documentos.proposicao,id_documento) and not hasattr(context.sapl_documentos.proposicao,id_documento_assinado):
          assinatura.append(proposicao.cod_proposicao)

       if hasattr(context.sapl_documentos.proposicao,id_documento_assinado):
          protocolo.append(proposicao.cod_proposicao)

   if caixa == 'revisao':
      if len(revisao) > 0:
         qtde = '[' + str(len(revisao)) + ']'
      else: qtde = ''
   if caixa == 'assinatura':
      if len(assinatura) > 0:
         qtde = '[' + str(len(assinatura)) + ']'
      else: qtde = ''
   if caixa == 'protocolo':
      if len(protocolo) > 0:
         qtde = '[' + str(len(protocolo)) + ']'
      else: qtde = ''   

if caixa == 'incorporado':
   for proposicao in context.zsql.proposicao_obter_zsql(ind_excluido=0, ind_incorporado=1):
          incorporado.append(proposicao.cod_proposicao)
          
   if len(incorporado) > 0:
      qtde = '[' + str(len(incorporado)) + ']'
   else: qtde = '' 


if caixa == 'devolvido':
   for proposicao in context.zsql.proposicao_obter_zsql(ind_excluido=0, ind_devolvido=1):
          devolvido.append(proposicao.cod_proposicao)

   if len(devolvido) > 0:
      qtde = '[' + str(len(devolvido)) + ']'
   else: qtde = '' 

return qtde


