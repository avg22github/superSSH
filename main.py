import paramiko
from scp import SCPClient

user = "frodo"
remotehost = "192.168.1.17"
defaultpassword = "bolson"
ssh = paramiko.SSHClient()

ssh.connect(remotehost, user, defaultpassword)

    scp = SCPClient(ssh.get_transport())
    scp.close()

ssh.close()