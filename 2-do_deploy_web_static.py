#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers \
        using the function do_deploy.
"""


from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.86.79.118', '54.237.97.11']
env.user = 'ubuntu'
env.key_filename = '.ssh/authorized_keys'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        filename = os.path.basename(archive_path)
        folder_name = '/data/web_static/releases/' + filename.split('.')[0]
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))
        run('rm /tmp/{}'.format(filename))
        run('mv {}/web_static/* {}'.format(folder_name, folder_name))
        run('rm -rf {}/web_static'.format(folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
