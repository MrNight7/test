import getpass

import paramiko

open_file = open("ip.txt")
data_file = open_file.read()
open_file.close()
ip = data_file.split("\n")
username = str(input("Логин: "))
password = getpass.getpass("Пароль: ")

command_list = {'1': ["sudo apt-get update", "sudo yum update -y"], '2': "uptime", '3': "sudo service --status-all",
                "4": None}
command_custom = None
print("1) - Обновление системы\n"
      "2) - Uptime системы\n"
      "3) - Статус сервисов\n"
      "4) - Своя команда")
command_set = None
command_while = 0

while True:
    command_set = str(input("Введите номер команды: "))
    if command_set in command_list:
        break
    else:
        command_while += 1
        print("Нет такой команды!")
        if command_while == 3:
            print("""Вы ввели неизвестную команду более трех раз!
После пяти попыток, завершение программы.""")
        if command_while == 5:
            print("""Вы ввели неизвестную команду пять раз!
Завершение программы!""")
            break
if command_set == "4":
    command_custom = str(input("Ваша команда: "))


def command_run(host, command):
    if command == "1":
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(
            "sudo apt-get update -y && sudo apt-get dist-upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean")

        for line in stdout:
            print('... ' + line.strip('\n'))
        stdin, stdout, stderr = ssh.exec_command(
            "sudo yum update -y && sudo yum dist-upgrade -y && sudo yum autoremove -y && sudo yum autoclean -y")

        for line in stdout:
            print('... ' + line.strip('\n'))

        stdin.close()
        print(" ")

    elif command == "4":
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command_custom)

        for line in stdout:
            print('... ' + line.strip('\n'))

        for line in stderr:
            if (line.strip('\n')) != "command not found":
                print("...  " + line.strip('\n'))

        stdin.close()
        print(" ")

    elif command == "2":
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command("uptime")

        for line in stdout:
            print('... ' + line.strip('\n'))

        stdin.close()
        print(" ")

    elif command == "3":
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command("sudo service --status-all")

        for line in stdout:
            print('... ' + line.strip('\n'))
        stdin.close()

for i in ip:
    print(i)
    print(" ")
    command_run(i, command_set)
