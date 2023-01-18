import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('você não passou argumentos suficientes.')
else:
    print(f'Você passou os argumentos {argumentos[1:]}.')
    for palavra in argumentos:
        if palavra.lower() == 'comer':
            print('AI QUE FOME!')
