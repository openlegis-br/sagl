## Script (Python) "username_pysc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=username='', role='', cod_parlamentar='', adicionar=False, excluir=False, consultar=False
##title=
##

passwd = context.sagl_documentos.props_sagl.txt_senha_inicial

ok = 1

roles = []

if role == 'parlamentar':
    if adicionar:
        roles.append('Parlamentar')
        if username in context.acl_users.getUserNames():
            user = context.acl_users.getUser(username)
            user_roles = list(user.getRoles())
            user_roles.append('Parlamentar')
            context.acl_users.userFolderEditUser(username, passwd, user_roles, '')
            ok = 0
        else:
            context.acl_users.userFolderAddUser(username, passwd, roles, '')
    if excluir:
        context.acl_users.userFolderDelUsers([username,])

    if consultar:
        try:
            txt_login = context.zsql.parlamentar_obter_zsql(cod_parlamentar = cod_parlamentar)[0].txt_login
        except:
            txt_login = ''
        return txt_login


if role == 'autor':
    roles.append('Autor')
    if adicionar:
        if username in context.acl_users.getUserNames() and len(context.zsql.parlamentar_obter_zsql(txt_login = username)) > 0:
            user = context.acl_users.getUser(username)
            user_roles = list(user.getRoles())
            if 'Autor' in user_roles:
                ok = 0
            else:
                user_roles.append('Autor')
                passwd = None
                context.acl_users.userFolderEditUser(username, passwd, user_roles, '')

        elif username not in context.acl_users.getUserNames() and len(context.zsql.parlamentar_obter_zsql(txt_login = username)) > 0:
            user = context.acl_users.getUser(username)
            user_roles = list(user.getRoles())
            user_roles.append('Autor')
            passwd = None
            context.acl_users.userFolderEditUser(username, passwd, user_roles, '')

        else:
            context.acl_users.userFolderAddUser(username, passwd, roles, '')
    if excluir:
        if len(context.zsql.parlamentar_obter_zsql(txt_login = username)) > 0:
            user = context.acl_users.getUser(username)
            user_roles = list(user.getRoles())
            user_roles.remove('Autor')
            passwd = None
            context.acl_users.userFolderEditUser(username, passwd, user_roles, '')
        else:
            context.acl_users.userFolderDelUsers([username,])


return ok
