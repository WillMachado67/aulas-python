def fahrenheit(t):
    return t * 1.8 + 32


def celcius(t):
    return (t - 32) / 1.8


temp = [0, 5, 10, 15, 20, 25, 30, 35, 40]

f_temp = list(map(fahrenheit, temp))
print(f'F {f_temp}')

c_temp = list(map(celcius, f_temp))
print(f'C {c_temp}')

###################################

# f_temp2 = list(map(lambda t: t * 1.8 + 32, temp))
# print(f'F2 {f_temp2}')
#
# c_temp2 = list(map(lambda t: (t - 32) / 1.8, f_temp2))
# print(f'C2 {c_temp2}')
