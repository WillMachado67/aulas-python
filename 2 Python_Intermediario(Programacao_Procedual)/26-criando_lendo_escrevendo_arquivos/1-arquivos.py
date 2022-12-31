# https://docs.python.org/3/library/functions.html#open

file = open("abc.txt", 'w+')  # cria arquivo
file.write('Linha 1\n')  # escrever no arquivo
file.write('Linha 2\n')
file.write('Linha 3\n')

# file.close()  # Fecha o arquivo

#########################################

# file.seek(0, 0)    # muda a posição do  "cursor"
# print('Lendo linhas: ')
# print(file.read())  # Lê o arquivo inteiro


#################################################

# file.seek(0, 0)
# print(file.readline(), end='')  # lê linha por linha
# print(file.readline(), end='')
# print(file.readline(), end='')


######################################

file.seek(0, 0)
# print(file.readlines())
#
# file.close()

for linha in file.readlines():
    print(linha)

file.close()
