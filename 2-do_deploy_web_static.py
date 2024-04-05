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
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp')

        # Extract archive filename without extension
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]

        # Create directory to uncompress archive
        run('mkdir -p /data/web_static/releases/{}'.format(archive_name))

        # Uncompress the archive to the folder /data/web_static/releases/
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_filename, archive_name))

        # Remove archive from web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move contents of archive to the correct location
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(archive_name, archive_name))

        # Remove empty web_static directory
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_name))

        # Remove the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(archive_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False

