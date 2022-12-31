nome = 'Willian'
idade = 28
altura = 1.83
e_maior = idade > 18
peso = 73
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
# f string
# print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
#print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {0} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))
