#!/usr/bin/python3
"""
  generates a .tgz archive from the contents of the web_static folder
"""


import os
import datetime
from fabric.api import *

env.hosts = ['100.25.163.224', '100.25.212.221']


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
        text = os.path.split(archive_path)[1]
        fileName = os.path.splitext(text)[0]
        target = '/data/web_static/releases/' + fileName
        path = archive_path.split('/')[1]
        put(archive_path, "/tmp/")
        run('sudo mkdir -p ' + target)
        run('sudo tar -xzf /tmp/' + path + ' -C' + target + '/')
        run('sudo rm /tmp/' + path)
        run('sudo mv ' + target + '/web_static/* ' + target + '/')
        run('sudo rm -rf ' + target + '/web_static')
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s ' + target + '/' + ' /data/web_static/current')
        print('New version deployed!')
        return True
    return False
