import os
os.system('cls')

print('SOLICITANDO NOTAS =')
soma = 0

for i in range(3):
    nota = float(input('Digite uma nota: '))
    soma = soma + nota

media = soma / 3

if media >= 7:
    print("Aprovado")
elif media <4:
    print("Reprovado")
else:
    print("Recuperação")