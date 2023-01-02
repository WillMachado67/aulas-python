def f(var):
    print(var)


def dumb():
    return f

var = dumb()
print(type(var))
print(id(var), id(f))
