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
        return fabric.api.local("tar -cvzf versions/web_static_{}.tgz web_static".format(time))
    except:
        return None
