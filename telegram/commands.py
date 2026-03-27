from dotenv import load_dotenv
import os
import paramiko

load_dotenv()

HOST = os.getenv('host')
USERNAME = os.getenv('username')
PASSWORD = os.getenv('passwd')
PORT = os.getenv('ext_port')

def run_command(command):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(HOST, PORT, USERNAME, PASSWORD)
        stdin, stdout, stderr = ssh_client.exec_command(command)
        stdout_str = stdout.read().decode()
        stderr_str = stderr.read().decode()
        return (stdout_str, stderr_str)
    except:
        raise
    finally:
        ssh_client.close()


