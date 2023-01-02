def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise
        # return False


# print(divide(2, 0))

try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print('Erro.', error)
