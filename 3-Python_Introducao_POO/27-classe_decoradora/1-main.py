class Multiplicar:
    def __init__(self, args):
        print('INIT', args)
    
    def __call__(self, *args, **kwargs):
        print(args, kwargs)

@Multiplicar
def soma(x, y):
    return x + y


dois_mais_dois = soma(2,2)

print(dois_mais_dois)