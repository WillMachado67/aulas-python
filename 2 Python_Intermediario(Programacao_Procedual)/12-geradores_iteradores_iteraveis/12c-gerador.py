import sys
import time


def gera():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel


g = gera()

# for v in g:
#     print(v)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
