"""
Utilizado para realizar ações enquanto
uma condição for verdadeiro
"""
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')


    if not num_1.isdigit() or not num_2.isdigit():
        print('O valor digitado não é um numero.')
        continue
    else:
        num_1 = int(num_1)
        num_2 = int(num_2)
    # + - / *
        if operador == '+':
            print(num_1 + num_2)
        if operador == '-':
            print(num_1 - num_2)
        if operador == '/':
            print(num_1 / num_2)
        if operador == '*':
            print(num_1 * num_2)
        else:
            print('Operador invalido')

    sair = input('Deseja sair? [S]im ou [N]ão: ')

    if sair == 's' or sair == 'S':
        break
