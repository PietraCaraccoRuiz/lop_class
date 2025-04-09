import random
        
opcao = int(input("Escolha o exercicio: "))

while opcao != 0:
    # 1) Peça 10 números e conte quantos são múltiplos de 3. Use for.
    if opcao ==1:
        mult = 0
        i = 0
        for i in range(10):
            numero = int(input("\nDigite um número: "))
            if numero % 3 == 0:
                mult += 1
        print("São multiplos de 3: ", mult, " numeros")
    # 2) Crie um programa que simule o uso de senha com tentativas infinitas
    # até digitar a senha correta (use while True).
    elif opcao == 2:
        while True:
            tentativa = input("\nDigite um número: ")
            senha = "123"
            if  tentativa == senha:
                print("Acertou!!")
                break
            else:
                print("errou tente denovo!")
        break
    elif opcao == 3:
        # MENU

        while opcao != "Sair":
            print(" - Continuar")
            print(" - Sair")
            opcao = input()

    #    4) Crie um programa que peça dois números
    #    inteiros e exiba todos os números entre eles que são primos. Use for.
    elif opcao == 4:

        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite outro numero: "))
        j = 0

        for i in range(numero1, numero2+ 1):
            cont = 0
            for j in range(1,numero2 + 1):
                if i % j == 0:
                    cont += 1
            if cont == 2:
                print("número primo: ", i)

    elif opcao == 7:
        a = 0
        e = 0
        ii = 0
        o = 0
        u = 0

        frase = input("digite uma frase: ")
        fraseformatada = str.lower(frase)
        for i in fraseformatada:
            if i == "a":
                a += 1
            elif i == "e":
                e += 1
            elif i == "i":
                ii += 1
            elif i == "o":
                o += 1
            elif i == "u":
                u += 1
        print("Quantidade de vogais", a + e + ii + o + u)
        print("A: ", a, "\nE: ", e, "\nI: ", ii, "\nO: ", o, "\nU: ", u )

    elif opcao == 8:
        cara = 0
        lista = ["cara", "coroa"]

        while cara < 3:
            moeda = random.choice(["cara", "coroa"])
            print(moeda)
            if moeda == "cara":
                cara += 1
        break

    elif opcao == 9:
        soma = 0
        quant_menores = 0
        quantidade = int(input("Digite a quantidade de números: "))
        lista = []

        for i in range(quantidade):
            numero = int(input("Digite um número: "))
            lista.insert(0,numero)
            soma += numero

        media = soma / quantidade
        print("Media: ", media)

        for item in lista:
            if item < media:
                print(item)
                quant_menores += 1
        print("Quantidade de números menores que a média: ", quant_menores)
        break



