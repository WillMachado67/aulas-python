"""
count - Itertoools
"""
from itertools import count

# contador = count()
# contador = count(start=5)
contador = count(start=5)

# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))

####################################

# for valor in contador:
#     print(valor)
#
#     if valor >= 10:
#         break

####################################

for valor in contador:
    print(round(valor, 5))

    if valor >= 10:
        break
