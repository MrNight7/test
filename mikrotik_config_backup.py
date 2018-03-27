#!/usr/bin/env python
# -*- coding: utf-8 -*-

from paramiko import SSHClient
from paramiko import AutoAddPolicy
import datetime

version = str(datetime.date.today())
hosts = ["you host list"]
username = "you_user"
password = "you_password"
port = "you_ssh_port"
path = "/you_backup_path/"
def connect(host, path, port):
    """Connect on host and backup export config, and write to path."""
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = ssh.exec_command("export")
    file = open(path + host[:-8] + " " + version + ".rsc", "w")

    for line in stdout:
        file.write(line.strip('\n'))
    file.close()


for i in hosts:
    connect(i, path, port)

