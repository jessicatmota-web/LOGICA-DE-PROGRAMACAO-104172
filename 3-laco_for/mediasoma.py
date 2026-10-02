import os
os.system('cls')

print('SOLICITANDO NOTAS =')
soma = 0

for i in range(4):
    nota = float(input('Digite uma nota: '))
    soma = soma + nota

media = soma / 4

print('\n= Exibindo resultados =')
print(f'Média: {media}')