#!/usr/bin/python3
"""
  generates a .tgz archive from the contents of the web_static folder
"""


import os
import datetime
from fabric.api import *
from fabric.operations import env, put, run

env.hosts = ['100.25.163.224', '100.25.212.221']
env.user = "ubuntu"


def do_pack():
    """
        generates a .tgz archive from the contents of the web_static folder
    """
    try:
        if os.path.isdir("versions") is False:
            os.mkdir("versions")
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        pack = 'versions/web_static_' + time + '.tgz'
        fabric.api.local("tar -cvzf {} web_static".format(pack))
        return pack
    except Exception as ex:
        return None


def do_deploy(archive_path):
    """
        distributes an archive to web servers
    """
    if os.path.exists(archive_path):
        text = archive_path[9:]
        target = '/data/web_static/releases/' + text[:-4]
        fileName = "/tmp/" + text
        put(archive_path, "/tmp/")
        run('sudo mkdir -p ' + target)
        run('sudo tar -xzf ' + fileName + ' -C' + target + '/')
        run('sudo rm ' + fileName)
        run('sudo mv ' + target + '/web_static/* ' + target)
        run('sudo rm -rf ' + target + '/web_static')
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s ' + target + ' /data/web_static/current')
        print('New version deployed!')
        return True
    return False
