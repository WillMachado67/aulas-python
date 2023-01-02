"""
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

secreto = 'caminhada'
digitadas = []
chance = 3

while True:
    if chance <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')
    letra = letra.lower()
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHHHULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreta.')

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOUUUU!!!. A palavra era "{secreto}"')
        break
    else:
        print(f'A palavra secreta esta sim: {secreto_temporario}\n')

    if letra not in secreto:
        chance -= 1
    print(f'Você ainda tem {chance} chances.')
    