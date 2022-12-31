def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name!r}({class_dict!r})'
        return class_repr


def adicionar_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        # resultado = self.falar_nome()
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você esta em casa'

        return resultado
    return interno


@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Prtugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())