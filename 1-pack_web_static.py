#!/usr/bin/python3
"""
  generates a .tgz archive from the contents of the web_static folder
"""


import os
import datetime
import fabric.api


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
