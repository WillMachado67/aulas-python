# Pilhas e filas
# Pilhas (stack) - LIFO - last in, first out.
#   Exepmplo: Pilhas de livros que sao adicionados um sobre o outro
# Fila (queue) - FIFO -frist in, frist out.
#   Exemplo: Uma fila de banco (ou qualquer outra fila da vida real)
#  Fila podem ter efeito colaterais em desempenho, porque a cada item alterado,
#   todos os índices serão modificados
#  0 1 2 3 4 5 6 7 8
# [1 2 3 4 5 6 7 8 9 ]

# 0093158687
from collections import deque
from time import sleep
fila: deque = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)
print(fila)

# for i in range(100):
#     fila.append(i)
#     sleep(1)
#     print(fila)
