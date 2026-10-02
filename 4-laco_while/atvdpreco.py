import os
os.system('cls')

while True:
    print("===== MENU DE FRUTAS =====")
    print("1 - Maçã - R$ 2,00")
    print("2 - Banana - R$ 1,50")
    print("3 - Laranja - R$ 2,50")
    print("4 - Uva - R$ 5,00")
    print("5 - Melancia - R$ 8,00")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        fruta = "Maçã"
        preco = 2.00
    elif opcao == 2:
        fruta = "Banana"
        preco = 1.50
    elif opcao == 3:
        fruta = "Laranja"
        preco = 2.50
    elif opcao == 4:
        fruta = "Uva"
        preco = 5.00
    elif opcao == 5:
        fruta = "Melancia"
        preco = 8.00
    else:
        print("Opção inválida! Tente novamente.")
        continue

    print("Fruta escolhida:", fruta)
    print("Preço: R$", preco)
    break
