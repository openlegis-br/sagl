## Script (Python) "rede_sagl_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

from Products.CMFCore.utils import getToolByName

sagl_tool = getToolByName(context, 'portal_sagl')

enderecos = context.zsql.presenca_endereco_obter_zsql()

endereco_ip = context.REQUEST.get('endereco_ip', None)

endereco_mac = context.REQUEST.get('endereco_mac', None)

if endereco_ip and endereco_mac:
    endereco_completo = [endereco_mac.upper(), endereco_ip]

    lista_enderecos = [[end.txt_mac_address.upper(), end.txt_ip_address] for end in enderecos]

    if endereco_completo in lista_enderecos:
        return True
    else:
        return False
else:
    return False