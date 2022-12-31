nome = 'Willian Machado'
gerador = iter(nome)
# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)


try:
    print(next(gerador))  # w
    print(next(gerador))  # i
    print(next(gerador))  # l
    print(next(gerador))  # l
    print(next(gerador))  # i
    print(next(gerador))  # a
    print(next(gerador))  # n
    print(next(gerador))  #
    print(next(gerador))  # M
    print(next(gerador))  # a
    print(next(gerador))  # c
    print(next(gerador))  # h
    print(next(gerador))  # a
    print(next(gerador))  # d
    print(next(gerador))  # o
    print(next(gerador))
    print(next(gerador))
except:
    pass
print('Algo mais?')
for v in gerador:
    print(v)
