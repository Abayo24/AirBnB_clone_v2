#!/usr/bin/python3
"""
Fabric script which creates and distributes an archive to your web servers using the function do_deploy.
"""

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['54.86.79.118', '54.237.97.11']


def do_pack():
    """
    Create a compressed archive of web_static folder
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(file_name))
    if result.failed:
        return None
    return file_name


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}".format(
            file_name.replace(".tgz", ""))
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, folder_name))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}/web_static/* {}/".format(folder_name, folder_name))
        run("sudo rm -rf {}/web_static".format(folder_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder_name))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
    Deploy web static
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
