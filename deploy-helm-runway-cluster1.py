  
import re
import os
import time
os.system('pip3 install paramiko')
import paramiko
import sys
import json

#Opening config file....

with open('./resource-sandboxInfo/inputs/sandbox1_info.json') as f:
  data = json.load(f)


host = data["ip"]
port = data["port"]
username = data["username"]
password = data["password"]



command = "export KUBECONFIG=/home/vmware/kubeconfig.yaml; helm --kubeconfig=/home/vmware/kubeconfig.yaml delete wp; sleep 30; helm repo update;helm --kubeconfig=/home/vmware/kubeconfig.yaml install wp isv1/wordpress-mysql-stateless"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password,banner_timeout=200)
stdin, stdout, stderr = ssh.exec_command(command)
#print (stdout.read())
for line in stdout.readlines():
  print (line)
time.sleep(10)

stdout.close()
stdin.close() 
ssh.close()
