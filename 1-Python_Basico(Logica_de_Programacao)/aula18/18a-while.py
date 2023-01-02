"""
Utilizado para realizar ações enquanto
uma condição for verdadeiro
"""

while True:
    nome = input('Qual seu nome: ')
    print(f'Ola {nome}')

print('Não será executado!')

'''
x = 0
while x < 10:
    # continue
    print(x)

    x = x + 1

print('Programa finalizado!')
'''
'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Programa finalizado!')
'''
'''
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print('Programa finalizado!')
'''