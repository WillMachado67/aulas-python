# Pilhas e filas
# Pilhas (stack) - LIFO - last in, first out.
#   Exepmplo: Pilhas de livros que sao adicionados um sobre o outro
# Fila (queue) - FIFO -frist in, frist out.
#   Exemplo: Uma fila de banco (ou qualquer outra fila da vida real)
#  Fila podem ter efeito colaterais em desempenho, porque a cada item alterado,
#   todos os índices serão modificados
#  0 1 2 3 4 5 6 7 8
# [1 2 3 4 5 6 7 8 9 ]
from collections import deque
fila: deque = deque()
# print(fila)
fila.append('Suelen')
fila.append('Willian')
fila.append('Jefferson')
fila.append('Rafael')
fila.append('Pedro')
print(fila)
fila.popleft()
print(fila)
