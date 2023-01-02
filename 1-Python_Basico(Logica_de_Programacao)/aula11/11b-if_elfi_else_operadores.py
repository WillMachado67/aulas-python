"""
== igual a
> maior que
>= maior ou igua que
< menor que
<= menor ou igual que
!= diferente de
"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)
"""
# limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} NÃO pode pegar empréstimo.')
"""
# limite para pegar empréstimo
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} NÃO pode pegar empréstimo.')
