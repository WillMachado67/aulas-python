num1 = input('Digite um número: ')
num2 = input('Digite outro numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter os numeros para realizar contas.')
