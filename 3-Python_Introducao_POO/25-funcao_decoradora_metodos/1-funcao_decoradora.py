def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name!r}({class_dict!r})'
    return class_repr

    
def adicionar_repr(cls):
    cls.__repr__ = meu_repr
    return cls

@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

# Time = adicionar_repr(Time)
# Planeta = adicionar_repr(Planeta)

brasil = Time('Brasil')
portugal = Time('Prtugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print(terra)
print(marte)