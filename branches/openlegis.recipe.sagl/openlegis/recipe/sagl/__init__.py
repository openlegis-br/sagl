# -*- coding: utf-8 -*-
"""Recipe sagl"""

import os
import subprocess
import pkg_resources
import logging

TRUISMS = ['yes', 'y', 'on', 'true', 'sure', 'ok', '1']


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.logger = logging.getLogger(name)

        options['location'] = os.path.join(
            buildout['buildout']['parts-directory'],
            self.name,
        )
        # suppress script generation.
        self.options['scripts'] = ''
        options['bin-directory'] = buildout['buildout']['bin-directory']

        # all the options that will be passed on to the 'run' script
        self.sagl_id = options.get('sagl-id', 'sagl')
        self.container_path = options.get('container-path', '/sagl/sapl_documentos')
        self.admin_user = options.get('admin-user', 'admin')
        self.mysql_user = options.get('mysql-user', 'root')
        self.mysql_pass = options.get('mysql-pass', 'root')
        self.mysql_host = options.get('mysql-host', 'localhost')
        self.mysql_db = options.get('mysql-db', 'openlegis')
        self.add_mountpoint = options.get('add-mountpoint', '').lower() in TRUISMS
        self.log_level = buildout._log_level
        options['args'] = self.createArgs()
        instance = buildout[options.get('instance', 'instance')]
        instance_home = instance['location']
        instance_script = os.path.basename(instance_home)
        options['instance-script'] = instance_script
        self.enabled = options.get('enabled', 'true').lower() in TRUISMS

    def install(self):
        """Installer"""
        options = self.options
        location = options['location']

        if self.enabled:
            options['script'] = pkg_resources.resource_filename(
                __name__, 'sagl.py')
            # run the script
            cmd = ("%(bin-directory)s/%(instance-script)s run "
                   "%(script)s %(args)s") % options

            subprocess.call(cmd.split())
        return location

    def update(self):
        """Updater"""
        self.install()

    def createArgs(self):
        """Helper method to create an argument list
        """
        args = []
        args.append("--sagl-id=%s" % self.sagl_id)
        args.append("--admin-user=%s" % self.admin_user)
        args.append("--container-path=%s" % self.container_path)
        args.append("--mysql-user=%s" % self.mysql_user)
        args.append("--mysql-pass=%s" % self.mysql_pass)
        args.append("--mysql-host=%s" % self.mysql_host)
        args.append("--mysql-db=%s" % self.mysql_db)
        args.append("--add-mountpoint=%s" % self.add_mountpoint)

        return " ".join(args)
