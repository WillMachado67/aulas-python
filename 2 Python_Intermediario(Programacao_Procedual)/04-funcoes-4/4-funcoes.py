"""
Escopo global, escopo local
"""

variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)


func()
func2()
print(variavel)
