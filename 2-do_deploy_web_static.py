#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.158.202.47', '52.204.60.176']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp')

        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]

        run('mkdir -p /data/web_static/releases/{}'.format(archive_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_filename, archive_name))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(archive_name, archive_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(archive_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
