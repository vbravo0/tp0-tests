from . import shell_cmd

def generate_docker_compose(client_amount):
	shell_cmd.silent(f'sh generar-compose.sh docker-compose-dev.yaml {client_amount}')
 
def validate_echo_server():
	return shell_cmd.pipe(f'sh validar-echo-server.sh')