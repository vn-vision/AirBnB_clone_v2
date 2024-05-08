#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir, join, abspath


def do_pack():
    """generates a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    versions_folder = "versions"
    archive_name = f"web_static_{date}.tgz"
    archive_path = join(versions_folder, archive_name)

    if isdir("versions_folder") is False:
        local("mkdir -p{}". versions)
    file_name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file_name))
    return file_name
