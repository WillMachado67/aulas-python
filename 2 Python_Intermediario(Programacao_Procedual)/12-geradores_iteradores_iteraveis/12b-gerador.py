import sys
import time


# lista = list(range(100000))
# print(sys.getsizeof(lista))

#####################################


# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         # time.sleep(0.1)
#     return r
#
#
# g = gera()
#
# for v in g:
#     print(v)
#
# print(sys.getsizeof(gera()))
######################################


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

print(g)
for v in g:
    print(v)

print(sys.getsizeof(gera()))