import os
os.system('cls')


print('ACUMULANDO VALORES EM UMA VARIÁVEL. ')
soma = 0

print(f'Valor INICIAL da variável soma: {soma}')


for i in range(3):
    numero = int(input('Digite um número para somar: '))
    soma = soma + numero
    print(f'Valor TEMPÓRARIO da variável soma: {soma}')

print(f'Valor FINAL da variável soma: {soma}')
