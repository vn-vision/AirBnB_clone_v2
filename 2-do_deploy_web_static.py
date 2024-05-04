#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['54.174.207.67', '54.210.123.94']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """

    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(
            archive_name.split('.')[0])

        # Upload archive to /tmp/ directory of web servers
        put(archive_path, '/tmp/')

        # Uncompress archive to /data/web_static/releases/<archive filename without extension>
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, folder_name))

        # Delete the archive from the web servers
        run('rm /tmp/{}'.format(archive_name))

        # Delete symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create new symbolic link /data/web_static/current linked to the new version
        run('ln -s {} /data/web_static/current'.format(folder_name))

        return True
    except:
        return False

