import paramiko

def ssh_execute_command(host, user, password, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=password)

        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        client.close()

        return output if output else error
    except Exception as e:
        return f"Erro de conexão ou execução: {str(e)}"
