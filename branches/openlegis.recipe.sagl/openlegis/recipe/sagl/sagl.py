# -*- coding: utf-8 -*-
import logging
from datetime import datetime

import MySQLdb

import zc.buildout
import transaction

from zope.site.hooks import setSite

from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManagement import noSecurityManager
from Testing import makerequest
from optparse import OptionParser
import pkg_resources

from subprocess import Popen, PIPE

logger = logging.getLogger('openlegis.recipe.sagl')


def create(container, sagl_id):
    oids = container.objectIds()
    if sagl_id in oids:
        logger.warning("SAGL já existe e não será substituído")
        sagl = getattr(container, sagl_id)
        created = False
        return (sagl, created)
    if sagl_id not in oids:
        created = True
        factory = container.manage_addProduct['openlegis.sagl']
        factory.manage_addSAGL(sagl_id, title='OpenLegis - Processo Legislativo Eletrônico', database="MySQL")
        transaction.commit()
        logger.info("Added SAGL")
        sagl = getattr(container, sagl_id)
        setSite(sagl)
        return (sagl, created)


def main(app, parser):
    (options, args) = parser.parse_args()
    sagl_id = options.sagl_id
    admin_user = options.admin_user
    mysql_user = options.mysql_user
    mysql_pass = options.mysql_pass
    mysql_host = options.mysql_host
    mysql_db = options.mysql_db
    add_mountpoint = options.add_mountpoint
    add_mountpoint = add_mountpoint == 'True'
    container_path = options.container_path
    log_level = options.log_level

    # set up logging
    try:
        log_level = int(log_level)
    except ValueError:
        msg = 'O log-level configurado não é válido: %s' % log_level
        raise zc.buildout.UserError(msg)
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    logger.setLevel(logging.getLevelName(log_level))
    for handler in root_logger.handlers:
        handler.setLevel(log_level)

    app = makerequest.makerequest(app)
    try:
        db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass)
    except:
        msg = "Falha ao conectar no servidor MySQL"
        raise zc.buildout.UserError(msg)
    if db:
        cursor = db.cursor()

        sagl_create = "CREATE SCHEMA IF NOT EXISTS %s DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" % mysql_db

        try:
            db.select_db(mysql_db)
            created = True
        except:
            cursor.execute(sagl_create)
            db.select_db(mysql_db)
            created = False
        logger.info("Banco de dados criado com sucesso")

        if not created:
            # create SAGL user
            sagl_dbuser = "CREATE USER 'sagl'@'localhost' IDENTIFIED BY 'sagl';"
            sagl_dbperms = "GRANT ALL ON openlegis.* TO 'sagl'@'localhost' WITH GRANT OPTION;"
            
            sagl_dbuser = "GRANT ALL PRIVILEGES ON interlegis.* TO 'sagl'@'localhost' IDENTIFIED BY 'sagl';"
            cursor.execute(sagl_dbuser)
            cursor.execute(sagl_dbperms)
            logger.info("Concluída a criação do usuário MySQL")

            sagl_sql = pkg_resources.resource_filename('il.sagl', 'instalacao/sagl.sql')
            process = Popen("mysql %s -u%s -p%s -h %s" % (mysql_db, mysql_user, mysql_pass, mysql_host), stdout=PIPE, stdin=PIPE, shell=True)
            process.communicate('source ' + sagl_sql)[0]
            logger.info("Estrutura de tabelas criada com sucesso")
        else:
            logger.info("As tabelas já existem no banco de dados")

    # set up security manager
    acl_users = app.acl_users
    user = acl_users.getUser(admin_user)
    if user:
        user = user.__of__(acl_users)
        newSecurityManager(None, user)
        logger.info("Recupera usuário admin")
    else:
        raise zc.buildout.UserError('O usuário administrador não existe')

    # create sagl if it doesn't exist
    sagl, created = create(app, sagl_id)

    # Verify if the mount-point exists
    try:
        app.unrestrictedTraverse(container_path)
    except KeyError:
        if add_mountpoint:
            try:
                app.manage_addProduct['ZODBMountPoint'].manage_addMounts(
                    paths=[container_path], create_mount_points=1
                )
            except Exception as e:
                msg = 'Ocorreu um erro ao tentar adicionar o ZODB Mount Point %s: %s'
                raise zc.buildout.UserError(msg % (container_path, str(e)))
        else:
            msg = 'Nenhum ZODB Mount Point encontrado no container %s e add-mountpoint não especificado.'
            raise zc.buildout.UserError(msg % container_path)

    if sagl and created:
        setup_tool = getattr(sagl, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile('profile-il.sagl:default')
        logger.info("Finalizado")

    # commit the transaction
    transaction.commit()
    noSecurityManager()


if __name__ == '__main__':
    now_str = datetime.now().strftime('%Y-%m-%d-%H%M%S')
    parser = OptionParser()
    parser.add_option("-s", "--sagl-id", dest="sagl_id", default="SAGL-%s" % now_str)
    parser.add_option("-c", "--container-path", dest="container_path", default="/")
    parser.add_option("-u", "--admin-user", dest="admin_user", default="admin")
    parser.add_option("-U", "--mysql-user", dest="mysql_user", default="root")
    parser.add_option("-P", "--mysql-pass", dest="mysql_pass", default="root")
    parser.add_option("-H", "--mysql-host", dest="mysql_host", default="localhost")
    parser.add_option("-D", "--mysql-db", dest="mysql_db", default="interlegis_teste")
    parser.add_option("-M", "--add-mountpoint", dest="add_mountpoint", default="/sagl/sagl_documentos")

    parser.add_option("--log-level", dest="log_level", default='20')
    main(app, parser)
