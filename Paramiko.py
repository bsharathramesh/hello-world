# Parmiko Tutorials
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect('192.168.181.129',port = 22, username = 'sharath',password = 'Sharath@123')
stdin,stdout,stderr = client.exec_command('ls -lrt')
output = stdout.readlines()
print(output)

