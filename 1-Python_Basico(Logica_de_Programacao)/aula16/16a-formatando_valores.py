"""
Formatando valore com modificadores

:s - Textos (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

'''
nome = 'Willian'
idade = 29
peso = 73.2
print(f'{nome:s}')
print(f'{idade:d}')
print(f'{peso:f}')
'''

num_1 = 1
print(f'{num_1:0>10}')
print(f'{num_1:0<10}')
print(f'{num_1:0^10}')


# nome = 'Willian'
# nome_formatado = '{:#^15}'.format(nome)
# print(nome_formatado)
