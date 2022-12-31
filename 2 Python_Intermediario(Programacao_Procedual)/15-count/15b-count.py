"""
count - Itertoools
"""
from itertools import count


contador = count(start=10, step=-1)


for valor in contador:
    print(valor)

    # if valor >= 11 or valor <= -10:
    #     break
