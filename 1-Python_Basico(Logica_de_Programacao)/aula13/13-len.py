usuario = input('Digite seu usuário: ')
qtd_caractere = len(usuario)

# print(usuario, qtd_caractere, type(qtd_caractere))

if qtd_caractere < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')

