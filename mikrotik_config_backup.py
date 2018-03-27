#!/usr/bin/env python
# Формат UTF-8
# После заполнения всех полей, ставим скрипт в шедулер для регулярного бекапа.

from paramiko import SSHClient
from paramiko import AutoAddPolicy
import datetime

version = str(datetime.date.today())
hosts = []          # Твой список хостов. ["host1", "host2", "host3"]
username = ""       # Учетная запись от оборудования. Достаточно режима доступа read only.
password = ""       # Пароль от уч.записи read only.
port = ""           # Порт SSH на микротике.
path = ""           # Путь куда будет записывться конфиг от оборудования.
execute = ""        # Команда экспорта конфига. Например для Mikrotik: export или export compact
format_file = ""    # Формат файла сохранения (.rsc .txt .backup)

def connect(host, port, execute, path, format_file):
    """Функция: Подключение к оборудованию по SSH и вывод stdout в файл по указанному пути.
     Файл именуется по имени хоста + дата дня. Например: "hostname.com 25-05-2025\""""
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = ssh.exec_command(execute)
    file = open(path + host[:-8] + " " + version + format_file, "w")

    for line in stdout:
        file.write(line.strip('\n'))
    file.close()


for i in hosts:
    connect(i, port, execute, path, format_file)
