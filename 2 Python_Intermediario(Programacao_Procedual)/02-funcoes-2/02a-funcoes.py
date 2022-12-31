def funcao(var):
    #print(var)
    print('Isso não será executado.')
    return var


variavel = funcao('')

# print(variavel)


if variavel:
    print(variavel)
else:
    print('Nenhum valor.')
