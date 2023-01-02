import sys
import time

# lista = list(range(1000))
l1 = [x for x in range(100000)]
print(type(l1))
l2 = (x for x in range(100000))
print(type(l2))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

# print(next(l2))
# print(next(l2))
# print(next(l2))
# print(next(l2))

# for v in l2:
#     print(v)
