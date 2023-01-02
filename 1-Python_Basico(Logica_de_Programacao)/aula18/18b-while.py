"""
Utilizado para realizar ações enquanto
uma condição for verdadeiro
"""

x = 0  # Linha
y = 0  # Coluna

while x < 10:
    y = 0
    while y < 5:
        print(f'Linha {x} e Coluna {y}', end=' | ')
        y += 1
    print('\n')
    x += 1
print('Programa finalizado!')
