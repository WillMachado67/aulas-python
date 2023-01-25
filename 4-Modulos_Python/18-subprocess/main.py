import subprocess
# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
    )

print()

# print('Erro:', proc.stderr)  # saida de erro
print('Padrao:', proc.stdout)  # saida padrao do comando
# print('Retorno:', proc.returncode)  # codigo de retorno do comando
# print('Argumentos:', proc.args)  # lista de argumentos passados
