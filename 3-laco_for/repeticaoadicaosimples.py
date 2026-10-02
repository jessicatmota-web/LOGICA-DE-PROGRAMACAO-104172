import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIÁVEL')
soma = 0

for i in range(3):
    numero = int(input('Digite um número para somar: '))
    soma += numero

print(f'\nValor FINAL da variável soma: {soma}')