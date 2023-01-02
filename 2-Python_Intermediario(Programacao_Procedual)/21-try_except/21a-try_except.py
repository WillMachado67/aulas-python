# print(a)

# try:
#     print(a)
# except:
#     print('Erro')

#############################

# try:
#     print(a)
# except NameError as erro:
#     print('Erro: ', erro)
#     print('Algo esta errado.')
# except Exception as erro:
#     print('Outro erro inesperado')
# print('Bora continuar...')

##############################

try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro: ', erro)
    print('Algo esta errado.')
except IndexError as erro:
    print('Erro de index - ', erro)
except Exception as erro:
    print('Outro erro inesperado.')
print('Bora continuar...')


######################################

# try:
#     a = {}
#     print(a[1])
# except NameError as erro:
#     print('Erro: ', erro)
#     print('Algo esta errado.')
# except (IndexError, KeyError) as erro:
#     print('Erro de índice ou chave - ', erro)
# except Exception as erro:
#     print('Outro erro inesperado.', erro)
# print('Bora continuar...')
