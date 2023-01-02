
# try:
#     a = {}
# except NameError as erro:
#     print('Erro: ', erro)
#     print('Algo esta errado.')
# except (IndexError, KeyError) as erro:
#     print('Erro de índice ou chave - ', erro)
# except Exception as erro:
#     print('Outro erro inesperado.', erro)
# else:
#     print('Seu codigo foi executado com sucesso!')
#     print(a)
#
# print('Bora continuar...')

#########################################

try:
    a = 1/0
except NameError as erro:
    print('Erro: ', erro)
    print('Algo esta errado.')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave - ', erro)
except Exception as erro:
    print('Outro erro inesperado.', erro)
else:
    print('Seu codigo foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente')

print('Bora continuar...')

#####################################

# try:
#     a = 1/0
# except NameError as erro:
#     print('Erro: ', erro)
#     print('Algo esta errado.')
# except (IndexError, KeyError) as erro:
#     print('Erro de índice ou chave - ', erro)
# except Exception as erro:
#     print('Outro erro inesperado.', erro)
# else:
#     pass
# finally:
#     # pass
#     a = None
# print(a)
