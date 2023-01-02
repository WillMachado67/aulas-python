# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6
#
#
# var = func(1, 2, 3, 4, 5, nome='will', a6='oi')
#
# print(var, type(var))
#
#
# lista = [1, 2, 3, 4, 5]
#
# print(*lista, sep='*')


# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
#
# func('a', 2, 3, 4, 5, 'oi')

# def func(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#
#
# func(1, 2, 3, 4, 5)

# def func(*args):
#     for v in args:
#         print(v)
#
#
# func(1, 2, 3, 4, 5)

# def func(*args):
#     print(args)
#
#
# lista = [1, 2, 3, 4, 5]
# func(*lista, 20, 21)
# func(*lista)

def func(*args, **kwargs):
    print(args)
    print(kwargs)


lista = [1, 2, 3, 4, 5]

func(*lista, nome='Willian', sobrenome='Machado')

# def func(**kwargs):
#     print(kwargs)
#     nome = kwargs['nome']
#     sobrenome = kwargs['sobrenome']
#     idade = kwargs['idade']
#
#     print(nome)
#     print(sobrenome)
#     print(idade)
#
#
# func(nome='Willian', sobrenome='Machado')

# def func(**kwargs):
#     print(kwargs)
#     idade = kwargs.get('idade')
#
#     if idade is not None:
#         print(idade)
#
#
# func(nome='Willian', sobrenome='Machado')
