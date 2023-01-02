# https://docs.python.org/3/library/functions.html#open

# try:
#     file = open("abc.txt", 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()


##################################
#  Gerenciador de contexto

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())
