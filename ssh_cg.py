__author__ = 'unicomcat'
import os
import paramiko

host = ''
port =
username = ''
password = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command('ls .')
print stdout.read()
ssh.close()