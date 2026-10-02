# Lendo a primeira nota
nota1 = float(input("Digite a primeira nota (0 a 10): "))

while nota1 < 0 or nota1 > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota (0 a 10): "))


# Lendo a segunda nota
nota2 = float(input("Digite a segunda nota (0 a 10): "))

while nota2 < 0 or nota2 > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota (0 a 10): "))


# Lendo a terceira nota
nota3 = float(input("Digite a terceira nota (0 a 10): "))

while nota3 < 0 or nota3 > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota3 = float(input("Digite a terceira nota (0 a 10): "))


# Calculando a média
media = (nota1 + nota2 + nota3) / 3

print("Média:", media)


# Verificando a situação do aluno
if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
